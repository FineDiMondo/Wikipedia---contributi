#!/usr/bin/env python3
"""
validate_wikitesto.py - Validazione automatica di bozze wikitesto.

Uso:
    python scripts/validate_wikitesto.py wiki/Famiglia_Giardina.wiki
    python scripts/validate_wikitesto.py wiki/Famiglia_Giardina.wiki wiki/Marco_Aurelio_Pasquale_Giardina.wiki

Output:
    report testuale con severita ERRORE / AVVISO / INFO
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


ADJECTIVES_CELEBRATIVI = [
    "straordinario",
    "straordinaria",
    "straordinari",
    "straordinarie",
    "eccezionale",
    "eccezionali",
    "formidabile",
    "formidabili",
    "grandioso",
    "grandiosa",
    "grandiosi",
    "grandiose",
    "illustre",
    "illustri",
    "eminente",
    "eminenti",
    "insigne",
    "insigni",
    "glorioso",
    "gloriosa",
    "gloriosi",
    "gloriose",
    "magnifico",
    "magnifica",
    "magnifici",
    "magnifiche",
    "splendido",
    "splendida",
    "splendidi",
    "splendide",
    "mirabile",
    "mirabili",
    "prodigioso",
    "prodigiosa",
    "prodigiosi",
    "prodigiose",
    "incomparabile",
    "incomparabili",
]

PATTERN_RICERCA_ORIGINALE = [
    r"rivela un pattern",
    r"evidenzia una strategia",
    r"configura un",
    r"rappresenta la svolta",
    r"incarna il profilo",
    r"testimonia il livello",
]

FONTI_NON_AMMISSIBILI = [
    "familysearch",
    "geneanet",
    "blog",
    "facebook",
    "linkedin",
]

MONTHS_IT = (
    r"gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|"
    r"settembre|ottobre|novembre|dicembre"
)

REF_RE = re.compile(r"<ref\b[^>]*?(?:/>|>.*?</ref>)", re.IGNORECASE | re.DOTALL)
REF_CONTENT_RE = re.compile(r"<ref\b[^>]*>(.*?)</ref>", re.IGNORECASE | re.DOTALL)
SECTION_RE = re.compile(r"^==\s*([^=\n].*?[^=\n]?)\s*==\s*$", re.MULTILINE)
PAGE_RE = re.compile(r"\bpp?\.\s*\d", re.IGNORECASE)
BOOK_RE = re.compile(r"''[^']+''|\"[^\"]+\"", re.IGNORECASE)
BLP_MARKER_RE = re.compile(
    r"\{\{\s*blp\s*\}\}|WP:BLP|Wikipedia:Biografie\s+di\s+persone\s+viventi",
    re.IGNORECASE,
)

BIRTH_PATTERNS = [
    re.compile(
        r"\bnat[oa]\s+il\s+\d{1,2}\s+(?:%s)\s+((?:19|20)\d{2})\b" % MONTHS_IT,
        re.IGNORECASE,
    ),
    re.compile(r"\(\s*n\.\s*((?:19|20)\d{2})\s*\)", re.IGNORECASE),
    re.compile(r"\bn\.\s*((?:19|20)\d{2})\b", re.IGNORECASE),
    re.compile(r"\bnat[oa]\s+nel\s+((?:19|20)\d{2})\b", re.IGNORECASE),
]


class Report(object):
    def __init__(self) -> None:
        self.items = []  # type: List[Tuple[str, str]]

    def error(self, message: str) -> None:
        self.items.append(("ERRORE", message))

    def warn(self, message: str) -> None:
        self.items.append(("AVVISO", message))

    def info(self, message: str) -> None:
        self.items.append(("INFO", message))

    def has_errors(self) -> bool:
        return any(severity == "ERRORE" for severity, _ in self.items)

    def print(self) -> None:
        counts = {"ERRORE": 0, "AVVISO": 0, "INFO": 0}
        for severity, message in self.items:
            counts[severity] += 1
            prefix = {
                "ERRORE": "[ERRORE]",
                "AVVISO": "[AVVISO]",
                "INFO": "[ INFO ]",
            }[severity]
            print("%s %s" % (prefix, message))
        print()
        print(
            "Riepilogo: %d errori, %d avvisi, %d info."
            % (counts["ERRORE"], counts["AVVISO"], counts["INFO"])
        )


def extract_refs(text: str) -> List[str]:
    refs = []
    for match in REF_RE.finditer(text):
        refs.append(match.group(0))
    return refs


def extract_ref_bodies(text: str) -> List[str]:
    bodies = []
    for match in REF_CONTENT_RE.finditer(text):
        bodies.append(match.group(1))
    return bodies


def strip_markup(text: str) -> str:
    cleaned = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    cleaned = re.sub(r"<ref\b[^>]*?(?:/>|>.*?</ref>)", " ", cleaned, flags=re.IGNORECASE | re.DOTALL)
    cleaned = re.sub(r"<[^>]+>", " ", cleaned)
    cleaned = re.sub(r"\{\{[^{}]*\}\}", " ", cleaned)
    cleaned = re.sub(r"\{\|.*?\|\}", " ", cleaned, flags=re.DOTALL)
    cleaned = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]+)\]\]", r"\1", cleaned)
    cleaned = re.sub(r"\[https?://[^\s\]]+(?:\s+([^\]]+))?\]", r"\1", cleaned)
    cleaned = re.sub(r"''+", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip()


def get_sections(text: str) -> Dict[str, str]:
    sections = {}  # type: Dict[str, str]
    matches = list(SECTION_RE.finditer(text))
    for index, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[title] = text[start:end]
    return sections


def paragraphs_without_ref(text: str) -> List[Tuple[int, str]]:
    blocks = re.split(r"\n\s*\n", text)
    results = []  # type: List[Tuple[int, str]]
    paragraph_index = 0
    for block in blocks:
        raw = block.strip()
        if not raw:
            continue
        if raw.startswith(
            ("==", "{|", "|-", "!", "*", "#", ";", ":", "{{", "[[File:", "[[Categoria:", "<pre>", "<gallery")
        ):
            continue
        if re.fullmatch(r"(?:\[\[Categoria:[^\]]+\]\]\s*)+", raw, flags=re.IGNORECASE):
            continue
        paragraph_index += 1
        cleaned = strip_markup(raw)
        if len(cleaned) < 120 or len(cleaned.split()) < 18:
            continue
        if "<ref" not in raw.lower():
            results.append((paragraph_index, cleaned[:140]))
    return results


def check_fonti(text: str, report: Report) -> None:
    refs = extract_refs(text)
    ref_bodies = extract_ref_bodies(text)

    report.info("Tag <ref> trovati: %d" % len(refs))
    if not refs:
        report.error("Nessun tag <ref> trovato: la bozza e priva di note.")
        return

    for paragraph_index, preview in paragraphs_without_ref(text):
        report.warn(
            "Paragrafo %d senza <ref> - \"%s...\"" % (paragraph_index, preview)
        )

    for ref_index, ref_body in enumerate(ref_bodies, start=1):
        ref_lower = ref_body.lower()
        for banned_source in FONTI_NON_AMMISSIBILI:
            if banned_source in ref_lower:
                preview = strip_markup(ref_body)[:120]
                report.warn(
                    "Nota %d: fonte non ammissibile come prova (%s) - \"%s\""
                    % (ref_index, banned_source, preview)
                )
                break

        if "pagina necessaria" in ref_body.lower():
            continue
        if BOOK_RE.search(ref_body) and not PAGE_RE.search(ref_body):
            preview = strip_markup(ref_body)[:120]
            if len(preview) > 30:
                report.warn(
                    "Nota %d: citazione libraria senza numero di pagina - \"%s\""
                    % (ref_index, preview)
                )


def check_tono(text: str, report: Report) -> None:
    found = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        line_lower = line.lower()
        for adjective in ADJECTIVES_CELEBRATIVI:
            if re.search(r"\b%s\b" % re.escape(adjective), line_lower):
                report.warn(
                    "Tono celebrativo (riga %d) - \"%s\""
                    % (line_number, line.strip()[:140])
                )
                found = True
                break
    if not found:
        report.info("Nessun aggettivo celebrativo rilevato.")


def check_blp(text: str, report: Report) -> None:
    living_mentions = []  # type: List[Tuple[int, int, str]]
    for line_number, line in enumerate(text.splitlines(), start=1):
        for pattern in BIRTH_PATTERNS:
            match = pattern.search(line)
            if not match:
                continue
            year = int(match.group(1))
            if year > 1925:
                living_mentions.append((line_number, year, line.strip()[:140]))
                break

    for line_number, year, preview in living_mentions:
        report.warn(
            "BLP: possibile persona vivente (anno %d, riga %d) - \"%s\""
            % (year, line_number, preview)
        )

    if living_mentions and not BLP_MARKER_RE.search(text):
        report.error(
            "BLP: rilevate possibili persone viventi ma manca un richiamo esplicito a WP:BLP o al template {{BLP}}."
        )


def check_struttura(text: str, report: Report) -> None:
    if not re.search(r"<references\s*/?>", text, re.IGNORECASE) and not re.search(
        r"\{\{\s*reflist", text, re.IGNORECASE
    ):
        report.error("Manca <references /> o {{Reflist}}.")

    sections = get_sections(text)
    section_names = [name.lower() for name in sections]
    if "note" not in section_names:
        report.error("Sezione obbligatoria '== Note ==' non trovata.")

    has_fonti = "fonti" in section_names
    has_bibliografia = "bibliografia" in section_names
    if not has_fonti and not has_bibliografia:
        report.error("Manca una sezione finale '== Fonti ==' o '== Bibliografia =='.")
    elif not has_fonti and has_bibliografia:
        report.info("Struttura: presente '== Bibliografia ==' al posto di '== Fonti =='.")

    for match in re.finditer(r"\[\[(?:File|Immagine):DA_CARICARE_[^\]]+\]\]", text, re.IGNORECASE):
        report.error("File segnaposto non caricato: %s" % match.group(0))

    for title, body in sections.items():
        if "===" in body or "{|" in body or "<references" in body.lower():
            continue
        cleaned = strip_markup(body)
        if len(cleaned) < 20:
            report.warn("Sezione '%s' sembra vuota o priva di testo." % title)


def check_ricerca_originale(text: str, report: Report) -> None:
    found = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        for pattern in PATTERN_RICERCA_ORIGINALE:
            if re.search(pattern, line, re.IGNORECASE):
                report.warn(
                    "Possibile ricerca originale (riga %d) - \"%s\""
                    % (line_number, line.strip()[:140])
                )
                found = True
                break
    if not found:
        report.info("Nessun pattern di ricerca originale rilevato.")


def validate_file(path: Path) -> Report:
    report = Report()
    if not path.exists():
        report.error("File non trovato: %s" % path)
        return report

    text = path.read_text(encoding="utf-8", errors="replace")
    print("=" * 72)
    print("Validazione: %s" % path)
    print("Dimensione: %d caratteri, %d righe" % (len(text), len(text.splitlines())))
    print("-" * 72)

    check_fonti(text, report)
    check_tono(text, report)
    check_blp(text, report)
    check_struttura(text, report)
    check_ricerca_originale(text, report)

    print()
    return report


def main(argv: List[str]) -> int:
    if len(argv) < 2:
        print("Uso: python %s <file.wiki> [altri_file.wiki ...]" % argv[0], file=sys.stderr)
        return 2

    any_errors = False
    for raw_path in argv[1:]:
        report = validate_file(Path(raw_path))
        report.print()
        any_errors = any_errors or report.has_errors()
        print()

    return 1 if any_errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
