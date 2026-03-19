# Backlog Operativo: Progetto Wikipedia Giardina

Questo documento contiene la lista delle attività pendenti, classificate per priorità e area di intervento. Gli agenti devono consultare questo file all'inizio di ogni sessione e aggiornarlo al completamento di ogni task.

## 🔴 Alta Priorità (Bloccanti per rilascio)

| ID | Task | Area | Stato | Riferimento |
| :--- | :--- | :--- | :--- | :--- |
| T01 | Scarico e Upload Mappa Magini (Gallica) | Media | PENDING | `docs/WORKFLOW_RECUPERO_GALLICA.md` |
| T02 | Popolamento Tabelle `TITLE` e `TITLE_ASSIGNMENT` | DB | COMPLETED | `scripts/db_utils.py` |
| T03 | Rafforzamento fonti biografia Marco Giardina (Atti Senato) | Wiki | IN_PROGRESS | `wiki/Marco_Aurelio_Pasquale_Giardina.wiki` |
| T04 | Creazione Template Navigazione `{{Giardina}}` | Wiki | PENDING | `wiki/index.wiki` |

## 🟡 Media Priorità (Miglioramento Qualitativo)

| ID | Task | Area | Stato | Riferimento |
| :--- | :--- | :--- | :--- | :--- |
| T05 | Audit madri e alleanze per rami Marquet e Iaci | DB/Wiki | IN_PROGRESS | `scripts/alliance_audit.py` |
| T06 | Normalizzazione date morte/nascita XVII sec nel DB | DB | COMPLETED | `scripts/db_remediation.py` |
| T07 | Inserimento incisione Palazzo Castrone da Gallica | Media | PENDING | `docs/ORGANIZZAZIONE_IMMAGINI_SANDBOX.md` |

## 🟢 Bassa Priorità (Ottimizzazione)

| ID | Task | Area | Stato | Riferimento |
| :--- | :--- | :--- | :--- | :--- |
| T08 | Timeline interattiva in `index.wiki` | Wiki | PENDING | Tag `<timeline>` |
| T09 | Backup periodico del Database MariaDB in SQL | Infra | PENDING | `scripts/db_utils.py` |

---

## 🛠️ Note per gli Agenti
- **Metodo:** Ogni modifica al wikitesto deve essere seguita da `scripts/wp_sync.py`.
- **DB:** Utilizzare sempre `scripts/db_utils.py` per le connessioni.
- **Validazione:** Non rimuovere i tag `<ref>` senza aver prima verificato la fonte nel registro `fonti.md`.

---
*Ultimo aggiornamento: 18 marzo 2026 - Allineamento Dossier Cariche e Bonifica Date completati*
