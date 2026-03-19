# 🔄 DIAGRAMMA DI FLUSSO: FILE E WORKFLOW COMPLETO

## STRUTTURA LOGICA DEL PACKAGE

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TU (Utente che esegue la revisione)                      │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               │
                ┌──────────────┴──────────────┐
                ↓                             ↓
        ┌──────────────┐            ┌──────────────────┐
        │   LEGGI      │            │  PREPARA FILE    │
        └──────────────┘            └──────────────────┘
              │                           │
              ↓                           ↓
    ┌─────────────────────────────────────────────────┐
    │  1. CHECKLIST_CARTOGRAFIA_FILE.md              │
    │     (Carta geografica, dove siamo?)             │
    ├─────────────────────────────────────────────────┤
    │  2. GUIDA_OPERATIVA_GEMINI.md                  │
    │     (Step-by-step per te)                       │
    ├─────────────────────────────────────────────────┤
    │  3. SINTESI_COMPLETA_PACKAGE.md                │
    │     (Riepilogo progetto)                        │
    └─────────────────────────────────────────────────┘
              │
              ├─ Cartella locale:
              │  ├── PROMPT_GEMINI_REVISIONE_RADICALE.md    ← DA INCOLLARE
              │  ├── PROMPT_GEMINI_COMPATTO.md              ← BACKUP
              │  ├── sezione_biforcazione_giardina.wiki      ← DA FORNIRE
              │  ├── biforcazioni_giardina_diagram.svg       ← DA FORNIRE
              │  ├── tabella_genealogica_sintetica.md        ← DA FORNIRE
              │  └── Famiglia_Giardina.wiki                  ← DA FORNIRE
              │
              ↓
        ┌──────────────────┐
        │ APRI GEMINI      │
        └────────┬─────────┘
                 │
    ┌────────────┴────────────┐
    ↓                         ↓
┌──────────────┐      ┌──────────────┐
│ INCOLLA:     │      │ FORNISCI A   │
│ PROMPT       │      │ GEMINI:      │
└──────┬───────┘      └──────┬───────┘
       │                     │
       ↓                     ↓
   ┌─────────────────────────────────────┐
   │ PROMPT_GEMINI_REVISIONE_RADICALE    │
   │ (4000 parole, specifiche e logiche) │
   ├─────────────────────────────────────┤
   │ ↓ Gemini legge e comprende          │
   │ "Ho capito, sono pronto"             │
   └────────────┬────────────────────────┘
                │
    ┌───────────┴───────────┬────────────┬────────────┐
    ↓                       ↓            ↓            ↓
 ┌─────────────────────────────────────────────────────────────┐
 │ FILE DA FORNIRE A GEMINI (UNO PER UNO):                    │
 ├─────────────────────────────────────────────────────────────┤
 │ 1. sezione_biforcazione_giardina.wiki                       │
 │    (2600 parole, testo narrativo + tabelle wikitesto)       │
 │ 2. biforcazioni_giardina_diagram.svg                        │
 │    (Diagramma SVG, flowchart biforcazioni)                  │
 │ 3. tabella_genealogica_sintetica.md                         │
 │    (Tabelle Markdown, riferimento dati)                     │
 │ 4. Famiglia_Giardina.wiki                                   │
 │    (Versione attuale con errori da riscrivere)              │
 └─────────────────────────────────────────────────────────────┘
                │
                ↓
    ┌─────────────────────────────┐
    │ COMANDO FINALE PER GEMINI   │
    │ "Procedi ADESSO con la      │
    │ riscrittura radicale"       │
    └────────────┬────────────────┘
                 │
              (ATTESA: 15–20 minuti)
                 │
                 ↓
    ┌────────────────────────────┐
    │ GEMINI RISCRIVE            │
    │ (produce testo wikitesto)  │
    └────────────┬───────────────┘
                 │
                 ↓
    ┌──────────────────────────────┐
    │ OUTPUT GEMINI:               │
    │ Famiglia_Giardina_RISCRITTO  │
    │ (intero testo wikitesto)     │
    └────────────┬─────────────────┘
                 │
         ┌───────┴────────┬────────────┐
         ↓                ↓            ↓
    ┌──────────┐   ┌────────────┐  ┌─────────┐
    │ VALIDA   │   │ CARICA SVG │  │  TEST   │
    │ MANUALE  │   │  COMMONS   │  │ SANDBOX │
    └────┬─────┘   └─────┬──────┘  └────┬────┘
         │               │              │
         ↓               ↓              ↓
    ┌─────────────────────────────────────────┐
    │ STEP DI VALIDAZIONE E CARICAMENTO:      │
    ├─────────────────────────────────────────┤
    │ 1. Checklist genealogia                 │
    │    (date, nomi, biforcazioni)           │
    │ 2. Valida wikitesto (no errori sintassi)│
    │ 3. Carica SVG su Commons (CC-BY-SA 4.0)│
    │ 4. Testa testo in sandbox Wikipedia     │
    │ 5. Verifica render tabelle e diagrammi  │
    └──────────────────┬──────────────────────┘
                       │
              (OK? ↓ SÌ / NO ↗ Gemini)
                       │
                       ↓
    ┌──────────────────────────────┐
    │ REVISIONE COMUNITÀ           │
    │ (Progetto Sicilia, Nobiltà)  │
    └──────────────┬───────────────┘
                   │
            (Attesa 1–7 giorni)
                   │
         ┌─────────┴─────────┐
         ↓                   ↓
    ┌──────────┐        ┌──────────┐
    │ APPROVATO│        │ CORREZIONI│
    │          │        │ RICHIESTE │
    └────┬─────┘        └────┬──────┘
         │                   │
         ↓                   ↓ (Modifica e ricertifica)
    ┌──────────────────────────┐
    │ PUBBLICAZIONE FINALE      │
    │ (Spazio principale Wiki)  │
    └──────────────┬───────────┘
                   │
                   ↓
         ┌──────────────────┐
         │ ✅ PROGETTO      │
         │    COMPLETATO    │
         └──────────────────┘
```

---

## RELAZIONI TRA FILE

### **LIVELLO 0: LETTURA (iniziale)**
```
Per PRIMA cosa, leggi (in ordine):

1. CHECKLIST_CARTOGRAFIA_FILE.md        ← TU SEI QUI (carta geografica)
2. GUIDA_OPERATIVA_GEMINI.md            ← Come procedere step-by-step
3. SINTESI_COMPLETA_PACKAGE.md          ← Riepilogo completo progetto
```

### **LIVELLO 1: PROMPT PER GEMINI**
```
Scegli UNO di questi due:

├─ PROMPT_GEMINI_REVISIONE_RADICALE.md  ← PRINCIPALE (4000 parole, completo)
│  (Se Gemini supporta prompt lunghi)
│
└─ PROMPT_GEMINI_COMPATTO.md            ← BACKUP (1500 parole, ultra-sintetico)
   (Se il principale è troppo lungo per Gemini)

Entrambi producono lo stesso output; scegli in base alla lunghezza supportata da Gemini.
```

### **LIVELLO 2: MATERIALI DA FORNIRE A GEMINI**
```
Dopo aver incollato il prompt, fornisci a Gemini (UNO PER UNO):

├─ sezione_biforcazione_giardina.wiki      (Testo narrativo + tabelle wikitesto)
├─ biforcazioni_giardina_diagram.svg       (Diagramma SVG)
├─ tabella_genealogica_sintetica.md        (Tabelle Markdown riferimento)
└─ Famiglia_Giardina.wiki                  (Wiki attuale da riscrivere)

Tutti questi file sono usati DIRETTAMENTE da Gemini nella riscrittura.
```

### **LIVELLO 3: SUPPORTI SUPPLEMENTARI**
```
Letture opzionali per approfondire:

├─ INTEGRAZIONE_SEZIONE_BIFORCAZIONE.md   (Approfondimento metodologico)
└─ [Tutti gli altri file di livello 0–2]  (Ripetuto per studio)
```

---

## DIPENDENZE FILE (Chi dipende da chi?)

```
Famiglia_Giardina.wiki (VERSIONE ATTUALE)
    │
    └──→ PROMPT_GEMINI_REVISIONE_RADICALE.md  (contiene istruzioni di riscrittura)
         │
         ├──→ sezione_biforcazione_giardina.wiki (testo da integrare)
         │
         ├──→ biforcazioni_giardina_diagram.svg (diagramma da includere)
         │
         └──→ tabella_genealogica_sintetica.md (tabelle da validare)
                  │
                  └──→ OUTPUT: Famiglia_Giardina_RISCRITTA.wiki
                       │
                       ├──→ VALIDA con CHECKLIST_CARTOGRAFIA_FILE.md
                       │
                       ├──→ CARICA biforcazioni_giardina_diagram.svg su Commons
                       │
                       └──→ TEST in sandbox Wikipedia

CONCLUSIONE: Famiglia_Giardina_RISCRITTA.wiki (pronta per revisione comunità)
```

---

## FLUSSO DI DATI (Cosa entra, cosa esce)

```
                    INGRESSO
                       │
        ┌──────────────┴──────────────┐
        ↓                             ↓
    TU (LETTURE)              GEMINI (PROCESSING)
        │                             │
    CHECKLIST_CARTOGRAFIA... │
    GUIDA_OPERATIVA...       │    PROMPT_GEMINI... ─→ sezione_biforcazione...
    SINTESI_COMPLETA...      │                    ─→ diagram.svg
                             │                    ─→ tabelle_sintetica...
                             │                    ─→ wiki_attuale
                             │
                             ↓ (Riscrittura automatica)
                             
                        USCITA
                             │
                    wiki_RISCRITTA
                             │
             ┌───────────────┼───────────────┐
             ↓               ↓               ↓
          VALIDA        CARICA SVG        TEST
          (manuale)     (Commons)         (Sandbox)
             │               │               │
             └───────────────┴───────────────┘
                             │
                    REVISIONE COMUNITÀ
                             │
                    PUBBLICAZIONE FINALE
```

---

## TIMELINE TOTALE (Con tempistiche)

```
TEMPO 0:00      → Sei qui (leggi CHECKLIST_CARTOGRAFIA_FILE.md)
                │
TEMPO 0:20      → Finito letture preliminari
                │
TEMPO 0:35      → Preparati materiali in cartella locale
                │
TEMPO 0:45      → Aperto Gemini
TEMPO 0:50      → Incollato prompt
TEMPO 0:55      → Forniti 4 materiali a Gemini
TEMPO 1:00      → Comando finale "Procedi ADESSO..."
                │
TEMPO 1:00-1:20 → [ATTESA — Gemini riscrive]
TEMPO 1:20      → Ricevuto output Gemini
                │
TEMPO 1:20-2:20 → Validazione manuale (checklist genealogia)
TEMPO 2:20-2:50 → Caricamento SVG su Commons
TEMPO 2:50-3:20 → Test in sandbox Wikipedia
                │
TEMPO 3:20      → Tutto testato e validato
TEMPO 3:20-3:30 → Preparazione per revisione comunità
TEMPO 3:30      → ✅ FASE 1 COMPLETATA
                │
                ├─ [ATTESA 1–7 giorni: revisione comunità]
                │
TEMPO 3:30+1d   → Feedback comunità ricevuto
TEMPO 3:30+1-2d → Correzioni apportate (se richieste)
TEMPO 3:30+2d   → ✅ FASE 2 COMPLETATA, PRONTO PUBBLICAZIONE

TOTALE TEMPO ATTIVO: ~3 ore + 1–7 giorni revisione comunità
```

---

## MAPPA RAPIDA: Dove trovare cosa?

```
❓ Domanda                          ↓ Risposta / File
─────────────────────────────────────────────────────────────
"Come comincio?"                   CHECKLIST_CARTOGRAFIA_FILE.md
"Mi spieghi step-by-step?"         GUIDA_OPERATIVA_GEMINI.md
"Qual è il riepilogo totale?"      SINTESI_COMPLETA_PACKAGE.md
"Qual è il prompt per Gemini?"     PROMPT_GEMINI_REVISIONE_RADICALE.md
"E se il prompt è troppo lungo?"   PROMPT_GEMINI_COMPATTO.md
"Quale testo narrativo incollare?" sezione_biforcazione_giardina.wiki
"Quale diagramma SVG?"             biforcazioni_giardina_diagram.svg
"Quale tabella di riferimento?"    tabella_genealogica_sintetica.md
"Come integro tutto nel wiki?"     INTEGRAZIONE_SEZIONE_BIFORCAZIONE.md
"Come valido l'output?"            CHECKLIST_CARTOGRAFIA_FILE.md (sezione 4)
"Ho tempo solo 2 ore?"             GUIDA_OPERATIVA_GEMINI.md → Opzione B (veloce)
"Ho tempo 4 ore?"                  GUIDA_OPERATIVA_GEMINI.md → Opzione A (completo)
```

---

## ✅ ULTIMA CHECKLIST (Prima di iniziare ADESSO)

Verifica di aver:

- [ ] **Letto questa pagina** (CHECKLIST_CARTOGRAFIA_FILE.md)
- [ ] **Capito il workflow** (quali sono i step?)
- [ ] **Preparato cartella locale** (hai copiat i 6 file necessari?)
- [ ] **Scelto il prompt** (RADICALE o COMPATTO?)
- [ ] **Accesso a Gemini** (sei loggato?)
- [ ] **Accesso a Commons** (account Wikimedia?)
- [ ] **Accesso a Wikipedia** (account Wikipedia italiano?)

**Se TUTTI gli item sono ✅**: SEI PRONTO! Procedi con Opzione A o B della GUIDA_OPERATIVA_GEMINI.md

**Se ALCUNI sono ❌**: Risolvi prima di procedere.

---

## 🎉 CONCLUSIONE

Hai una **cartografia completa** di tutti i file e come usarli. Il workflow è lineare, deterministic, e non è facile sbagliare se segui i step.

**Prossimo passo**: Apri `GUIDA_OPERATIVA_GEMINI.md` e segui il workflow step-by-step.

**Buona riscrittura! 🚀**

---

**Versione**: 1.0  
**Data**: 18 marzo 2026  
**Contesto**: Revisione radicale wiki Famiglia Giardina per Wikipedia italiano
