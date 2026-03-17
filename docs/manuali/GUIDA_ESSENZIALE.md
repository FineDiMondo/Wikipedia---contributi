# Guida Essenziale Wikipedia - Progetto Giardina

Questa guida compatta i criteri, la procedura e i riferimenti operativi per la gestione delle bozze locali.

---

## 1. Test di Ammissibilità (Checklist Rapida)
Prima di lavorare a una bozza, verifica se:
- [ ] Esistono almeno **2 fonti secondarie affidabili e indipendenti** (libri, studi storici, dizionari).
- [ ] Il soggetto ha un **ruolo storico, politico o culturale** documentato (non solo familiare).
- [ ] Le informazioni sono **verificabili senza documenti privati** o memoria personale.
- [ ] Il tono è **neutrale** (privo di aggettivi celebrativi).

**STOP IMMEDIATO SE:**
- La voce è basata solo su alberi genealogici o fonti come Facebook, Geneanet, blog.
- Il soggetto è noto solo in ambito locale/familiare senza copertura indipendente.

---

## 2. Flusso di Lavoro (Workflow)
1. **Validazione Locale**:
   ```powershell
   python scripts/validate_wikitesto.py wiki/Nome_Pagina.wiki
   ```
   *Controlla: note mancanti, citazioni librarie senza pagina, toni non neutrali.*

2. **Verifica BLP (Soggetti Viventi)**:
   ```powershell
   python scripts/check_blp.py wiki/Nome_Pagina.wiki
   ```
   *Se compaiono persone nate dopo il 1925, è obbligatorio il template `{{BLP}}`.*

3. **Pubblicazione in Sandbox**:
   - Copia il wikitesto validato.
   - Incolla nella tua Sandbox personale su Wikipedia.
   - **Verifica in Anteprima**: Note (Reflist), tabelle, assenza di link rossi.
   - **Salvataggio**: Usa un oggetto della modifica descrittivo e neutrale.

---

## 3. Standard di Qualità
- **Fonti**: Per i libri, indica sempre il numero di pagina o usa `{{pagina necessaria}}`.
- **Neutralità**: Evita "illustre", "insigne", "straordinario".
- **Ricerca Originale**: Vietata. Ogni affermazione deve derivare da fonti pubblicate.
- **Conflitto di Interessi (COI)**: Se scrivi della tua famiglia, dichiaralo in cima alla bozza.

---

## 4. Riferimenti Rapidi
- [Criteri Biografie](https://it.wikipedia.org/wiki/Wikipedia:Criteri_di_enciclopedicita/Biografie)
- [Voci su Persone Viventi](https://it.wikipedia.org/wiki/Wikipedia:Voci_su_persone_viventi)
- [Conflitto di Interessi](https://it.wikipedia.org/wiki/Wikipedia:Conflitto_di_interessi)

---
*Ultimo aggiornamento: 17 marzo 2026*
