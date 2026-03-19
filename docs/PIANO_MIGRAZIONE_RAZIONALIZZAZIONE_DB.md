# Strategic Database Consolidation Plan (SDCP) - Baseline 2026

## 1. Executive Summary
L'attuale infrastruttura MariaDB presenta una frammentazione in 5 database indipendenti con significative sovrapposizioni funzionali. Il presente piano definisce la strategia per consolidare i dati in due soli pilastri logici, migliorando la manutenibilità e la coerenza del Knowledge Graph.

## 2. Stato AS-IS (Frammentato)
- `db_gedcom`: Dati genealogici (366 record, molte tabelle vuote).
- `db_heraldry`: Metadati araldici (vuoto).
- `db_wikipedia`: Governance operativa (attiva).
- `gn370_giardina_negrini`: Governance ridondante (ripopolata da JSON).
- `pmf_master`: Framework di gestione (3 record).

## 3. Target Architecture (Consolidata)

### A. Dominio "CORE" (`db_giardina_core`)
Schema unificato per la conoscenza storica.
- **Tabelle:** `PERSON`, `FAMILY`, `EVENT`, `TITLE`, `SOURCE`, `CITATION`, `HERALDRY`.
- **Origine:** `db_gedcom` + `db_heraldry`.

### B. Dominio "MGMT" (`db_wikipedia_mgmt`)
Schema unificato per la gestione di progetto.
- **Tabelle:** `MGMT_PROJECT`, `MGMT_SUBJECT`, `MGMT_TASK`, `MGMT_LOG`.
- **Origine:** `db_wikipedia` + `gn370_giardina_negrini` + `pmf_master`.

## 4. Matrice di Migrazione

| Vecchia Tabella | Vecchio DB | Nuova Tabella | Nuovo DB |
| :--- | :--- | :--- | :--- |
| `PERSON`, `FAMILY` | `db_gedcom` | `PERSON`, `FAMILY` | `db_giardina_core` |
| `subjects` | `db_wikipedia` | `MGMT_SUBJECT` | `db_wikipedia_mgmt` |
| `project_config` | `db_wikipedia` | `MGMT_PROJECT` | `db_wikipedia_mgmt` |
| `active_batch` | `db_wikipedia` | `MGMT_TASK` | `db_wikipedia_mgmt` |
| `project_manifest`| `pmf_master` | `MGMT_LOG` | `db_wikipedia_mgmt` |

## 5. Roadmap Operativa

### Step 1: Preparazione (Pre-migration)
- Eseguire `mysqldump` di tutti i database.
- Validare l'integrità dei dati JSON (backup primario).

### Step 2: Consolidamento Governance
- Creare il DB `db_wikipedia_mgmt`.
- Importare i dati da `subjects` e `project_config`.
- Mappare i task attivi da `BACKLOG_OPERATIVO.md` nella tabella `MGMT_TASK`.

### Step 3: Consolidamento Core
- Rinominare `db_gedcom` in `db_giardina_core`.
- Integrare le tabelle araldiche da `db_heraldry`.
- Rieseguire gli script di arricchimento fonti (S1-S4) per popolare le tabelle vuote.

### Step 4: Finalizzazione
- Aggiornare `scripts/db_utils.py`.
- Effettuare il `DROP` dei database obsoleti: `db_heraldry`, `db_wikipedia`, `gn370_giardina_negrini`, `pmf_master`.

---
*Documento redatto secondo metodologia Accenture Strategy - 19 marzo 2026*
