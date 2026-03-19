# Come usare il Prompt Gemini per la revisione radicale del wiki Famiglia Giardina

## 📋 Panoramica

Hai un **prompt deterministico e sistematico** (`PROMPT_GEMINI_REVISIONE_RADICALE.md`) che istruisce Gemini a riscrivere il wiki della Famiglia Giardina secondo la nuova impostazione con le **biforcazioni genealogiche** come asse centrale.

Il prompt è accompagnato da **3 file di supporto** che Gemini userà per la riscrittura:

1. **Sezione narrativa** (`sezione_biforcazione_giardina.wiki`) — testo wikitesto pronto all'uso
2. **Diagramma SVG** (`biforcazioni_giardina_diagram.svg`) — visualizzazione flowchart
3. **Tabelle genealogiche** (`tabella_genealogica_sintetica.md`) — riferimento dati

---

## 🚀 Step-by-step: Come procedere

### Step 1: Preparare i materiali

Raccogli i seguenti file in una cartella locale o cloud:

```
/materiali_revisione_gemini/
├── PROMPT_GEMINI_REVISIONE_RADICALE.md          [il prompt principale]
├── sezione_biforcazione_giardina.wiki           [testo narrativo da integrare]
├── biforcazioni_giardina_diagram.svg            [diagramma SVG]
├── tabella_genealogica_sintetica.md             [tabelle di riferimento]
├── Famiglia_Giardina.wiki                       [versione attuale da riscrivere]
└── INTEGRAZIONE_SEZIONE_BIFORCAZIONE.md         [note metodologiche, opzionale]
```

---

### Step 2: Aprire Gemini e configurare la sessione

1. Accedi a **Gemini** (gemini.google.com)
2. Avvia una **nuova conversazione**
3. **Incolla il prompt completo** dal file `PROMPT_GEMINI_REVISIONE_RADICALE.md`

**Nota**: Il prompt è **lungo** (~4000 parole). Gemini può gestirlo, ma potrebbe rispondere dicendo "Ho capito le istruzioni, sono pronto a procedere. Cosa devo fare?" — questo è normale.

---

### Step 3: Fornire a Gemini i file di supporto

Dopo che Gemini ha confermato di aver letto il prompt, **incolla in sequenza** i contenuti dei file:

#### 3a. Incolla il contenuto della sezione narrativa
```
Ecco il contenuto di "sezione_biforcazione_giardina.wiki" che devi integrare 
direttamente nella riscrittura:

[INCOLLA INTERO CONTENUTO DI sezione_biforcazione_giardina.wiki]
```

#### 3b. Fornisci il riferimento al diagramma SVG
```
Il seguente diagramma SVG deve essere caricato su Wikimedia Commons 
con il nome "File:Biforcazioni_Giardina_1627-1831.svg":

[INCOLLA INTERO CONTENUTO DI biforcazioni_giardina_diagram.svg]
```

#### 3c. Fornisci le tabelle genealogiche come riferimento
```
Ecco le tabelle genealogiche di sintesi (formato Markdown) 
che servono da riferimento per la validazione dei dati:

[INCOLLA INTERO CONTENUTO DI tabella_genealogica_sintetica.md]
```

#### 3d. Fornisci la versione attuale del wiki
```
Ecco la versione ATTUALE del wiki da riscrivere. 
La riscrittura deve:
- MANTENERE la struttura infobox (righe 1–21)
- ELIMINARE le sezioni confuse (vedi istruzioni nel prompt)
- INSERIRE le nuove sezioni sulla biforcazione
- AGGIORNARE date e nomi secondo le corrette genealogie

[INCOLLA INTERO CONTENUTO DI Famiglia_Giardina.wiki ATTUALE]
```

---

### Step 4: Dare a Gemini il comando finale

Una volta forniti tutti i materiali, dai un comando finale esplicito:

```
COMANDO FINALE per Gemini:

Sulla base del prompt ricevuto e dei materiali forniti, 
procedi ADESSO con la riscrittura radicale del wiki "Famiglia Giardina" secondo 
le istruzioni. 

OUTPUT ATTESO:
1. Una versione completamente riscritta del wiki (intero testo wikitesto, pronto per il paste nel sandbox Wikipedia)
2. Una sezione di VALIDAZIONE che verifica:
   - ✅ Coerenza genealogica (date, parentele, titoli)
   - ✅ Assenza di hallucination (ogni affermazione ha fonte?)
   - ✅ Integrazione diagramma SVG (il file è referenziato correttamente?)
   - ✅ Marcatura documentato/plausibile/speculativo (è presente e coerente?)
   - ✅ Rimozione errori precedenti (nomi, date, genealogie corretti?)
3. Una lista di PROSSIMI STEP (caricamento SVG, verifica sandbox, revisione comunità)

Procedere.
```

---

## 🔧 Cosa fare con l'output di Gemini

### Dopo che Gemini fornisce la riscrittura

#### 1. Copiare il testo wikitesto
Copia l'intero **testo wikitesto riescritto** di Gemini in un file locale:
```
/output_gemini/
└── Famiglia_Giardina_RISCRITTA.wiki     [testo pronto per paste nel sandbox]
```

#### 2. Validare manualmente la riscrittura
**Checklist di controllo**:

- [ ] La sezione "La linea continua: da Pietro Giardina a Luigi Arias" è presente?
- [ ] La biforcazione primaria (Bellacera / Gibellini, 1627) è spiegata chiaramente?
- [ ] Le date sono coerenti: Luigi Arias c. 1580–1627, NON c. 1555–1630?
- [ ] Il ramo Bellacera è marcato come estinto nel 1699 in linea maschile?
- [ ] La lite 1699–1703 è descritta come passaggio di asse a Luigi Gerardo?
- [ ] Le biforcazioni successive (Grimaldi, Naselli, Iaci) sono marcate come matrimoniali, non testamentarie?
- [ ] Il tono è enciclopedico e neutrale (niente "spettacolare", "incredibile", etc.)?
- [ ] Le fonti sono citate correttamente (Mango, Palizzolo Gravina, San Martino De Spucches)?
- [ ] Non ci sono frasi come "non è noto" o "rimane misterioso" — le lacune sono marcate come "da verificare" o omesse?

#### 3. Caricare il diagramma SVG su Wikimedia Commons
Il diagramma SVG deve essere preparato per il caricamento:

1. Salva il file SVG fornito come: `Biforcazioni_Giardina_1627-1831.svg`
2. Accedi a **Wikimedia Commons** (commons.wikimedia.org) con il tuo account Wikimedia
3. **Carica il file** (Special:Upload)
4. **Compila i metadati**:
   - Titolo: "Biforcazioni della casata Giardina (1627–1831)"
   - Descrizione: "Diagramma flowchart che mostra la biforcazione primaria (Bellacera vs. Gibellini, 1627), l'estinzione di Bellacera (1699), la lite successoria (1703), e le acquisizioni successive di Grimaldi, Naselli e Iaci."
   - Licenza: **CC-BY-SA 4.0** (compatibile con Wikipedia)
   - Categoria: [[:Category:Coats of arms of families of Sicily]], [[:Category:Genealogy diagrams]]
5. **Conferma upload** e nota l'URL/nome file per il riferimento nel wiki

#### 4. Testare nel sandbox Wikipedia
1. Accedi al tuo **sandbox Wikipedia italiano**: `it.wikipedia.org/wiki/Utente:TuoNome/Sandbox`
2. **Crea una sottopagina** test: `it.wikipedia.org/wiki/Utente:TuoNome/Sandbox/Famiglia_Giardina_TEST`
3. **Incolla il testo riescritto** di Gemini
4. **Includi il diagramma SVG** con: `[[File:Biforcazioni_Giardina_1627-1831.svg|thumb|center|700px|...]]`
5. **Clicca "Anteprima"** per verificare il render
6. **Controlla**:
   - Il layout è leggibile?
   - Le tabelle sono formattate correttamente?
   - Il diagramma SVG appare?
   - I link interni funzionano?

#### 5. Revisione da parte della comunità
Sottoponi il testo a:

1. **Progetto Sicilia** (si/Progetto_Sicilia) per peer review
2. **Progetto Nobiltà** (si/Progetto_Nobiltà) per verifiche genealogiche
3. Almeno **2 reviewer indipendenti** prima di move nello spazio principale

---

## ⚙️ Gestione dei problemi comuni

### Gemini non integra correttamente le tabelle wikitesto

**Problema**: Gemini converte le tabelle Markdown in testo disordinato invece che in wikitesto.

**Soluzione**:
1. Nel prompt finale, aggiungi: "Le tabelle devono essere in formato wikitesto con `{| class='wikitable'|...|}`, non in Markdown."
2. Se succede comunque, **copia manualmente** le tabelle pre-formattate da `sezione_biforcazione_giardina.wiki` (che sono già in wikitesto).

### Gemini produce hallucination (dati inventati)

**Problema**: Gemini aggiunge nomi, date o relazioni genealogiche non presenti nelle fonti.

**Soluzione**:
1. Chiedi a Gemini: "Cerca nel testo fornito la fonte per questa affermazione. Se non esiste, marcala come 'da verificare' o rimuovila."
2. Valida **manualmente** ogni nuova affermazione contro le fonti (Mango, Palizzolo Gravina, San Martino De Spucches).

### Il diagramma SVG non renderizza correttamente

**Problema**: Il file SVG fornito ha errori di sintassi o conflitti di licensing su Wikimedia Commons.

**Soluzione**:
1. Carica il file comunque su Commons — i template tecnici possono aiutare a ripararlo.
2. Se il rendering fallisce, crea una **versione semplificata** in Mermaid o PlantUML (altamente leggibili su Wikipedia).

### Date o nomi incoerenti dopo la riscrittura

**Problema**: Gemini ha mantenuto date/nomi dalla vecchia versione errata (es. Luigi Arias c. 1555–1630).

**Soluzione**:
1. Usa **Find & Replace** nel testo riescritto:
   - `c. 1555–1630` → `c. 1580–1627`
   - `Anna Bellacera` (spouse di Orsola) → `Mario Bellacera`
   - `Di Napoli e La Grua` → `Napoli di Resuttano`

---

## 📊 Checklist finale pre-publicazione

Prima di spostare nel **spazio principale** di Wikipedia:

- [ ] **Testo wikitesto**: riescritto completo, testato in sandbox, nessun errore di sintassi
- [ ] **Diagramma SVG**: caricato su Commons, licensing CC-BY-SA, referenziato correttamente nel wiki
- [ ] **Tabelle**: tutte in formato wikitesto, dati verificati
- [ ] **Fonti**: ogni fonte citata esiste e è corretta (no "Rassegna Siciliana n. 0", no "Archivio Spadafora" generiche)
- [ ] **Genealogia**: 
  - [ ] Pietro (c. 1500) → Luigi Arias (c. 1580–1627) linea tracciata
  - [ ] Biforcazione 1627: Bellacera vs. Gibellini spiegata
  - [ ] Estinzione Bellacera 1699 documentata
  - [ ] Lite 1703 descritta
  - [ ] Biforcazioni successive (Grimaldi, Naselli, Iaci) marcate come matrimoniali
- [ ] **Marcatura**: documentato/plausibile/speculativo coerente
- [ ] **BLP**: nessun dato personale di viventi (verificare Franco Giardina jr., 1943, e discendenti)
- [ ] **Revisione comunità**: almeno 2 reviewer hanno approvato
- [ ] **Conflitto di interessi**: se sei discendente della famiglia, mantieni l'avviso {{Avviso COI}} fino a review conclusiva

---

## 🎯 Tempi stimati

| Fase | Tempo | Note |
|------|-------|-------|
| Step 1–2: Preparazione materiali | 15 min | Semplice copia/paste |
| Step 3: Incollare materiali a Gemini | 10 min | Gemini legge e elabora |
| Gemini riscrive il testo | 10–20 min | Dipende dalla lunghezza della risposta |
| Step 4: Validazione manuale | 45–60 min | Checklist genealogica, controllo errori |
| Step 5: Upload SVG e test sandbox | 30 min | Caricamento Commons, anteprima Wikipedia |
| Revisione comunità | 1–7 giorni | Dipende dalla disponibilità dei reviewer |

**Tempo totale**: ~2 ore per la riscrittura + test, + 1–7 giorni per revisione comunità.

---

## 📚 Risorse di supporto

Se Gemini ha dubbi, forniscigli questi riferimenti:

1. **Fonti primarie**: 
   - ASPa (Archivio di Stato di Palermo): Fondo Protonotaro del Regno, Conservatoria del Registro
   - Real Cancelleria (investiture 1621, 1703, 1733)

2. **Fonti secondarie validate**:
   - Mango di Casalgerardo (1912–1915) — **sempre accurato**
   - Palizzolo Gravina (1871–1875) — **sempre accurato**
   - San Martino De Spucches (1924–1941) — **sempre accurato**

3. **Fonti da verificare/escludere**:
   - "Archivio Spadafora" — generica, non verificabile
   - "Rassegna Siciliana di Storia e Cultura, n. 0" — n. 0 improbabile, fonte dubbia

---

## 🎓 Nota metodologica finale

Questo flusso di lavoro è **deterministico**: segui gli step nell'ordine specificato. Non improvvisare. Se Gemini fa domande non coperte dal prompt, riportati al prompt stesso o agli allegati forniti.

**Il prompt è stato progettato per:**
- Minimizzare hallucination (ogni affermazione deve avere fonte)
- Massimizzare coerenza (tutte le date/nomi verificati contro fonte primaria)
- Facilitare revisione (marcatura documentato/plausibile/speculativo rende le lacune trasparenti)

Se il flusso produce **un testo wikitesto coerente e validato**, sei pronto per il caricamento in Wikipedia.

Buona riscrittura! 🚀
