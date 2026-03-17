#!/usr/bin/env python3
"""
check_blp.py - Verifica conformita BLP (Biografie di persone viventi).

Uso:
    python scripts/check_blp.py wiki/Famiglia_Giardina.wiki
    python scripts/check_blp.py wiki/Famiglia_Giardina.wiki wiki/Marco_Aurelio_Pasquale_Giardina.wiki
"""

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Set, Tuple


MONTHS_IT = (
    r"gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|"
    r"settembre|ottobre|novembre|dicembre"
)

LIVING_THRESHOLD = 1925

BIRTH_PATTERNS = [
    re.compile(
        r"\bnat[oa]\s+il\s+\d{1,2}\s+(?:%s)\s+((?:19|20)\d{2})\b" % MONTHS_IT,
        re.IGNORECASE,
    ),
    re.compile(r"\(\s*n\.\s*((?:19|20)\d{2})\s*\)", re.IGNORECASE),
    re.compile(r"\bn\.\s*((?:19|20)\d{2})\b", re.IGNORECASE),
    re.compile(r"\bnat[oa]\s+nel\s+((?:19|20)\d{2})\b", re.IGNORECASE),
]

PRIVATE_PATTERNS = {
    "indirizzo di residenza": re.compile(
        r"\b(via|viale|piazza|corso|vicolo|largo)\s+[A-Z][\w\s'.-]{2,50}\s+\d+\b",
        re.IGNORECASE,
    ),
    "numero di telefono": re.compile(
        r"\b(?:\+\d{1,3}[\s-]?)?(?:\(?\d{2,4}\)?[\s-]?)\d{3,4}[\s-]?\d{3,5}\b"
    ),
    "dettagli medici": re.compile(
        r"\b(malattia|diagnosi|patologia|sintomi|terapia|ricovero|ospedale|"
        r"operazione chirurgica|tumore|cancro|depressione|psichiatric[oa])\b",
        re.IGNORECASE,
    ),
    "informazioni finanziarie personali": re.compile(
        r"\b(conto corrente|iban|codice fiscale|reddito personale|"
        r"dichiarazione dei redditi|patrimonio personale)\b",
        re.IGNORECASE,
    ),
    "dettagli familiari non pubblici": re.compile(
        r"\b(figlio(?:/a)? illegittim[oa]|figlio(?:/a)? non riconosciut[oa]|"
        r"adottato|affidamento|separazione personale)\b",
        re.IGNORECASE,
    ),
}

SENSITIVE_KEYWORDS = [
    "arrestato",
    "condannato",
    "accusato",
    "processo",
    "indagato",
    "controversia",
    "scandalo",
    "divorzio",
    "malattia",
]

BLP_MARKER_RE = re.compile(
    r"\{\{\s*blp\s*\}\}|WP:BLP|Wikipedia:Biografie\s+di\s+persone\s+viventi",
    re.IGNORECASE,
)
REF_RE = re.compile(r"<ref\b[^>]*?(?:/>|>.*?</ref>)", re.IGNORECASE | re.DOTALL)
SENSITIVE_RE = re.compile(
    r"\b(" + "|".join(re.escape(keyword) for keyword in SENSITIVE_KEYWORDS) + r")\b",
    re.IGNORECASE,
)


@dataclass
class Issue(object):
    severity: str
    line: int
    message: str
    context: str = ""

    def render(self) -> str:
        prefix = "[%s]" % self.severity
        if self.line > 0:
            location = " riga %d" % self.line
        else:
            location = ""
        if self.context:
            return "%s%s: %s\n    -> %s" % (prefix, location, self.message, self.context.strip())
        return "%s%s: %s" % (prefix, location, self.message)


@dataclass
class LivingMention(object):
    line: int
    year: int
    name: str
    start: int
    context: str


def extract_name(line: str) -> str:
    bold_match = re.search(r"'''([^']+)'''", line)
    if bold_match:
        return bold_match.group(1).strip()

    name_match = re.search(
        r"([A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’-]+(?:\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’-]+){1,4})",
        line,
    )
    if name_match:
        return name_match.group(1).strip()
    return "persona non identificata"


def find_living_mentions(text: str, lines: List[str]) -> List[LivingMention]:
    mentions = []  # type: List[LivingMention]
    seen = set()  # type: Set[Tuple[int, int]]
    for pattern in BIRTH_PATTERNS:
        for match in pattern.finditer(text):
            year = int(match.group(1))
            if year <= LIVING_THRESHOLD:
                continue
            line_number = text.count("\n", 0, match.start()) + 1
            key = (line_number, year)
            if key in seen:
                continue
            seen.add(key)
            line = lines[line_number - 1] if line_number - 1 < len(lines) else ""
            mentions.append(
                LivingMention(
                    line=line_number,
                    year=year,
                    name=extract_name(line),
                    start=match.start(),
                    context=line[:160],
                )
            )
    mentions.sort(key=lambda item: (item.line, item.start))
    return mentions


def check_private_data(lines: List[str], mentions: List[LivingMention]) -> List[Issue]:
    issues = []  # type: List[Issue]
    if not mentions:
        return issues

    living_lines = [mention.line for mention in mentions]
    for line_number, line in enumerate(lines, start=1):
        for label, pattern in PRIVATE_PATTERNS.items():
            if not pattern.search(line):
                continue
            near_living_person = any(abs(line_number - living_line) <= 10 for living_line in living_lines)
            severity = "ERRORE" if near_living_person else "AVVISO"
            issues.append(
                Issue(
                    severity=severity,
                    line=line_number,
                    message="Possibili %s nel testo" % label,
                    context=line[:160],
                )
            )
    return issues


def check_blp_marker(text: str, mentions: List[LivingMention]) -> List[Issue]:
    if mentions and not BLP_MARKER_RE.search(text):
        return [
            Issue(
                severity="ERRORE",
                line=0,
                message=(
                    "Persone viventi rilevate ma manca un richiamo esplicito "
                    "a [[Wikipedia:Biografie di persone viventi|WP:BLP]] o al template {{BLP}}"
                ),
            )
        ]
    return []


def check_sensitive_claims(text: str, lines: List[str], mentions: List[LivingMention]) -> List[Issue]:
    issues = []  # type: List[Issue]
    seen = set()  # type: Set[Tuple[int, str]]
    for mention in mentions:
        window_start = max(0, mention.start - 600)
        window_end = min(len(text), mention.start + 600)
        window_text = text[window_start:window_end]

        for match in SENSITIVE_RE.finditer(window_text):
            absolute_start = window_start + match.start()
            if abs(absolute_start - mention.start) > 250:
                continue

            ref_start = max(0, absolute_start - 200)
            ref_end = min(len(text), absolute_start + 200)
            ref_window = text[ref_start:ref_end]
            if REF_RE.search(ref_window):
                continue

            line_number = text.count("\n", 0, absolute_start) + 1
            keyword = match.group(1).lower()
            key = (line_number, keyword)
            if key in seen:
                continue
            seen.add(key)

            context = lines[line_number - 1][:160] if line_number - 1 < len(lines) else ""
            issues.append(
                Issue(
                    severity="ERRORE",
                    line=line_number,
                    message=(
                        "Affermazione sensibile vicino a %s senza fonte: '%s'"
                        % (mention.name, match.group(1))
                    ),
                    context=context,
                )
            )
    return issues


def check_file(path: Path) -> List[Issue]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    issues = []  # type: List[Issue]

    mentions = find_living_mentions(text, lines)
    for mention in mentions:
        issues.append(
            Issue(
                severity="AVVISO",
                line=mention.line,
                message="Possibile persona vivente (%s, anno nascita %d)" % (mention.name, mention.year),
                context=mention.context,
            )
        )

    issues.extend(check_private_data(lines, mentions))
    issues.extend(check_blp_marker(text, mentions))
    issues.extend(check_sensitive_claims(text, lines, mentions))

    return issues


def run_for_file(path: Path) -> int:
    if not path.exists():
        print("[ERRORE] File non trovato: %s" % path)
        return 1

    issues = check_file(path)
    errors = [issue for issue in issues if issue.severity == "ERRORE"]
    warnings = [issue for issue in issues if issue.severity == "AVVISO"]

    print("=" * 72)
    print("Verifica BLP: %s" % path)
    print("=" * 72)

    if not issues:
        print("[ INFO ] Nessun problema BLP rilevato.")
    else:
        for issue in sorted(issues, key=lambda item: (item.line, item.severity, item.message)):
            print(issue.render())

    print()
    print("Riepilogo: %d errori, %d avvisi." % (len(errors), len(warnings)))
    print()
    return 1 if errors else 0


def main(argv: List[str]) -> int:
    if len(argv) < 2:
        print("Uso: python %s <file.wiki> [altri_file.wiki ...]" % argv[0], file=sys.stderr)
        return 2

    exit_code = 0
    for raw_path in argv[1:]:
        file_exit_code = run_for_file(Path(raw_path))
        exit_code = max(exit_code, file_exit_code)
    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
