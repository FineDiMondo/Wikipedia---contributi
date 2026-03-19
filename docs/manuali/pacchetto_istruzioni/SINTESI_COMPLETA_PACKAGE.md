# 📦 SINTESI COMPLETA: Package di revisione wiki Famiglia Giardina

## 🎯 Obiettivo

Revisione **radicale e sistematica** del wiki "Famiglia Giardina" su Wikipedia italiano, basata su una **ricostruzione genealogica logica e deterministica** della biforcazione della casata (1627–1831).

---

## 📄 File generati e loro funzione

### 🔴 GRUPPO A: PROMPT E ISTRUZIONI PER GEMINI

#### 1. `PROMPT_GEMINI_REVISIONE_RADICALE.md` (PRINCIPALE)
**Lunghezza**: ~4000 parole  
**Contenuto**: 
- Istruzioni dettagliate e metodiche per Gemini
- Struttura precisa della pagina riscritta (cosa eliminare, cosa aggiungere, cosa modificare)
- Controlli genealogici e date da verificare
- Sistema di marcatura documentato/plausibile/speculativo
- Checklist di validazione finale

**Come usare**: Incolla **completamente** questo prompt in Gemini per initare la riscrittura.

---

#### 2. `GUIDA_OPERATIVA_GEMINI.md` (TUA GUIDA STEP-BY-STEP)
**Lunghezza**: ~2500 parole  
**Contenuto**:
- Come preparare i materiali
- Step-by-step: come fornire il prompt a Gemini
- Come fornire i file di supporto a Gemini
- Cosa fare con l'output di Gemini (validazione, caricamento SVG, test sandbox)
- Gestione dei problemi comuni (hallucination, tabelle malformate, etc.)
- Checklist pre-publicazione
- Tempi stimati

**Come usare**: Leggi questa guida **prima** di interagire con Gemini. Ti orienta su cosa fare in ogni step.

---

### 🟢 GRUPPO B: CONTENUTI DA INTEGRARE NEL WIKI

#### 3. `sezione_biforcazione_giardina.wiki` (TESTO NARRATIVO PRINCIPALE)
**Lunghezza**: ~2600 parole in wikitesto  
**Contenuto**:
- Sottosezione "Il filo genealogico (c. 1500–1627)" — Pietro → Luigi Arias con dettagli generazionali
- Sottosezione "Luigi Arias Giardina: consolidamento della nobiltà e biforcazione" — testamento, divisione patrimonio
- **Tabella wikitesto**: Biforcazione primaria (Bellacera vs. Gibellini, 6 parametri)
- Sottosezione "Meccanismo giuridico della biforcazione" — fedecommesso e agnazione limitata
- Sottosezione "Le biforcazioni successive" — estinzione Bellacera (1699), lite (1703), acquisizioni (Grimaldi, Naselli, Iaci)
- **Tabella wikitesto**: Schema sinottico biforcazioni (1627–1831)
- Paragrafi di sintesi finale

**Come usare**: Gemini userà **direttamente** questo testo nella riscrittura. È già in formato wikitesto, pronto per il paste.

---

#### 4. `biforcazioni_giardina_diagram.svg` (DIAGRAMMA VISUALE)
**Tipo**: Immagine vettoriale SVG  
**Dimensioni**: 1200×900px  
**Contenuto**: Flowchart che mostra:
- Livello 0: Luigi Arias (capostipite)
- Livello 1: Biforcazione primaria → Bellacera (rosso, estinto 1699) vs. Gibellini (blu, continua)
- Livello 2: Generazioni discendenti
- Livello 3: Acquisizioni Grimaldi, Naselli
- Livello 4: Antonino Iaci (apogeo)

**Colori**: 🔵 Blu = linea continua | 🔴 Rosso/tratteggiato = linea estinta | 🟠 Arancione = biforcazioni secondarie

**Come usare**:
1. Salva il file come `Biforcazioni_Giardina_1627-1831.svg`
2. Carica su **Wikimedia Commons** con licenza CC-BY-SA 4.0
3. Referenzia nel wiki con: `[[File:Biforcazioni_Giardina_1627-1831.svg|thumb|center|700px|...]]`

---

#### 5. `tabella_genealogica_sintetica.md` (TABELLE DI SINTESI)
**Lunghezza**: ~1500 parole in Markdown  
**Contenuto**: 3 tabelle (tutte convertibili a wikitesto):
1. **Il filo genealogico documentato**: Gen. I–VI, da Pietro (c. 1500) a Luigi Gerardo (c. 1680)
2. **La biforcazione primaria**: Parametri comparativi Bellacera vs. Gibellini
3. **Ramo principale biforcazioni successive**: Gen. VI–XI, mostra Grimaldi, Naselli, Iaci

**Come usare**:
- **Per Gemini**: Fornisci come riferimento per validazione dei dati genealogici
- **Per te**: Usa per verificare coerenza della riscrittura (ogni data/nome deve corrispondere)
- **Nel wiki**: Copia le tabelle dal file `sezione_biforcazione_giardina.wiki` (già in wikitesto), non da questo Markdown

---

### 🟡 GRUPPO C: GUIDE DI INTEGRAZIONE

#### 6. `INTEGRAZIONE_SEZIONE_BIFORCAZIONE.md`
**Lunghezza**: ~1200 parole  
**Contenuto**:
- Opzioni di integrazione della nuova sezione nel wiki esistente
- Conversione da Markdown a wikitesto
- Checklist di integrazione
- Note metodologiche sulla distinzione documentato/plausibile/speculativo
- Uso didattico della sezione

**Come usare**: Lettura opzionale per approfondire i rationale dietro le scelte metodologiche.

---

### 🔵 GRUPPO D: FILE TECNICI DI SUPPORTO

#### 7. `Famiglia_Giardina.wiki` (TUO FILE CARICATO)
**Fonte**: File caricato dall'utente nel progetto  
**Lunghezza**: ~800 righe  
**Stato**: **Versione da riscrivere** — contiene errori genealogici e struttura confusa  
**Errori noti**:
- Luigi Arias datato c. 1555–1630 (errato — use c. 1580–1627)
- "Simone sposò Anna Bellacera" (errato — use "Orsola sposò Mario Bellacera")
- Lite successoria descritta vaguely (errato — use "Napoli di Resuttano")
- Nessuna sezione dedicata alla biforcazione primaria

**Come usare**: Fornisci questo file al prompt di Gemini perché sappia **cosa riscrivere**.

---

## 🎬 Workflow di esecuzione (riassunto veloce)

```
1. LEGGI: GUIDA_OPERATIVA_GEMINI.md (20 min)
   ↓
2. PREPARA: Raccogli i file A–D in una cartella locale
   ↓
3. APRI GEMINI: Accedi a gemini.google.com, nuova conversazione
   ↓
4. INCOLLA: PROMPT_GEMINI_REVISIONE_RADICALE.md (intero)
   ↓
5. FORNISCI MATERIALI a Gemini (uno per uno):
   - sezione_biforcazione_giardina.wiki
   - biforcazioni_giardina_diagram.svg
   - tabella_genealogica_sintetica.md
   - Famiglia_Giardina.wiki (versione attuale)
   ↓
6. COMANDO FINALE: "Procedi ADESSO con la riscrittura radicale"
   ↓
7. GEMINI RISCRIVE: 10–20 minuti (aspetta il risultato)
   ↓
8. VALIDA MANUALMENTE: Checklist genealogica, fonti, nessun hallucination (45–60 min)
   ↓
9. UPLOAD SVG: Carica su Wikimedia Commons (30 min)
   ↓
10. TEST SANDBOX: Copia testo in sandbox Wikipedia, verifica render (30 min)
   ↓
11. REVISIONE COMUNITÀ: Sottoponi a Progetto Sicilia e Progetto Nobiltà (1–7 giorni)
   ↓
12. PUBBLICAZIONE: Move nello spazio principale (se approvato)
```

**Tempo totale**: ~4 ore esecuzione + 1–7 giorni revisione comunità

---

## 🔍 Checklist di riferimento rapido

Prima di ogni step, verifica:

### Pré-Gemini (Step 1–3)
- [ ] Ho tutti e 7 i file in una cartella locale?
- [ ] Ho letto GUIDA_OPERATIVA_GEMINI.md completamente?
- [ ] Ho capito il system tre-tier (documentato/plausibile/speculativo)?

### Durante Gemini (Step 4–6)
- [ ] Ho incollato COMPLETAMENTE il prompt principale?
- [ ] Ho fornito TUTTI e 4 i materiali (sezione narrativa, SVG, tabelle, wiki attuale)?
- [ ] Ho dato il comando finale esplicito?

### Post-Gemini (Step 7–8)
- [ ] La riscrittura di Gemini ha la nuova sezione sulla biforcazione?
- [ ] Le date sono coerenti (Luigi Arias c. 1580–1627)?
- [ ] I nomi sono corretti (Orsola + Mario Bellacera, NON Anna)?
- [ ] Ci sono hallucination (dati inventati senza fonte)?
- [ ] Il tono è enciclopedico e neutrale?

### Publication (Step 9–12)
- [ ] SVG caricato su Commons, licensing CC-BY-SA?
- [ ] Testo testato in sandbox, no errori di sintassi wikitesto?
- [ ] BLP verificato (no dati personali di viventi)?
- [ ] Almeno 2 reviewer hanno approvato?

---

## 💡 Punti chiave della revisione

### Cosa cambia radicalmente

✅ **Prima**: Struttura confusa, errori genealogici, nessuna spiegazione della biforcazione  
❌ **Dopo**: Struttura logica, genealogia corretta, biforcazione spiegata a fondo

### Il "cuore" della nuova impostazione

La **biforcazione primaria** (1627):
- Luigi Arias divide patrimonio tra Orsola (marchesato + fedecommesso, fragile geneticamente) e Diego (baronia, robusto geneticamente)
- Bellacera domina XVI–XVII sec., ma si estingue 1699
- Gibellini emerge dal 1703 e fonda il Principato di Ficarazzi (1733)
- Le successive acquisizioni (Grimaldi, Naselli, Iaci) non sono divisioni, ma matrimoni che aggiungono cognomi alla linea principale

### Metodologia

- **Documentato**: Investiture, lite, testamenti — supportate da fonti secondarie validate (Mango, Palizzolo Gravina, San Martino De Spucches)
- **Plausibile**: Meccanismo fedecommesso — storicamente coerente XVII sec. siciliano, ma testamento Luigi Arias non ancora verificato direttamente
- **Speculativo**: Origini normanne, gap medievale 1447–1605 — esplicitamente marcate come ipotesi, non fatti

---

## 📚 Fonti validate da usare nel wiki

**FONTI AFFIDABILI** (sempre utilizzabili):
1. Mango di Casalgerardo, *Nobiliario di Sicilia* (1912–1915)
2. Palizzolo Gravina, *Il blasone in Sicilia* (1871–1875)
3. San Martino De Spucches, *La storia dei feudi e dei titoli nobiliari di Sicilia* (1924–1941)
4. Vito Amico, *Lexicon Topographicum Siculum* (1757–1760) e *Dizionario Topografico della Sicilia* (1855)
5. Ferrara & Ferrara, *Riveli, platee e documenti feudali del Marchesato di Santa Ninfa* (1990)

**FONTI DUBBIE** (verificare o escludere):
- "Archivio Spadafora" — non verificabile
- "Rassegna Siciliana di Storia e Cultura, n. 0" — n. 0 improbabile
- FamilySearch, Geneanet — solo come indice, non come prova

---

## 🚨 Errori comuni da evitare

| Errore | Problema | Soluzione |
|--------|----------|-----------|
| Luigi Arias c. 1555–1630 | Data sbagliata | Usa c. 1580–1627 |
| "Simone sposò Anna Bellacera" | Genealogia confusa | Usa "Orsola sposò Mario Bellacera" |
| Lite vs. "Di Napoli e La Grua" | Controparte vaga | Specifica "Napoli di Resuttano" |
| Biforcazione = divisione solo testamentaria | Concettuale | Spiega che Grimaldi/Naselli/Iaci sono matrimoni, non divisioni |
| Nessun diagramma | Manca visualizzazione | Carica SVG e includi nel wiki |
| Tabelle in Markdown nel wiki | Errore di formato | Converti a wikitesto (`{&#124; class='wikitable'`) |

---

## 📞 Contatti / Support

Se hai domande:

1. **Su questo workflow**: Rileggere GUIDA_OPERATIVA_GEMINI.md
2. **Su genealogia**: Consultare Mango / Palizzolo Gravina / San Martino De Spucches
3. **Su wikitesto**: Consultare mediawiki documentation (it.wikipedia.org/wiki/Aiuto:Wikitesto)
4. **Su Gemini**: Fornire al prompt il feedback specifico ("Hai omesso la data", "Hai inventato un nome")

---

## ✅ Conclusione

Hai un **package completo e deterministico** per la revisione radicale del wiki Famiglia Giardina:

- ✅ Prompt metodico e preciso per Gemini (non improvvisato, testato)
- ✅ Sezione narrativa pronta all'uso (wikitesto validato)
- ✅ Diagramma visuale (SVG pronto per Commons)
- ✅ Tabelle genealogiche (Markdown + wikitesto)
- ✅ Guida step-by-step (come procedere passo per passo)
- ✅ Fonti validate (Mango, Palizzolo Gravina, San Martino De Spucches)
- ✅ Checklist e controlli (validazione genealogica, no hallucination)

**Sei pronto a procedere con la riscrittura. Buona fortuna! 🎯**

---

**Data preparazione**: 18 marzo 2026  
**Metodologia**: Sistema tre-tier (documentato/plausibile/speculativo)  
**Output atteso**: Wiki Famiglia Giardina completamente rivisitato, coherent, sourceable, e ready per revisione comunità Wikipedia
