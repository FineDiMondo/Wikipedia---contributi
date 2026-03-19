# Guida di integrazione: Sezione "Biforcazione della linea Giardina"

## Struttura proposta

La sezione sulla **biforcazione** dovrebbe essere inserita nel wiki principale **dopo la sezione "Fondazione della nobiltà (1605–1627)"** e **prima di "La linea Bellacera (1627–1699)"**, oppure in alternativa **sostituire le due sezioni "La linea Bellacera" e "La lite di successione"** con la nuova struttura unificata.

### Opzione A: Inserimento come sezione storica nuova (CONSIGLIATA)

**Posizionamento**: Tra l'attuale "Fondazione della nobiltà" (termine: "Morì nel 1627...") e "La linea Bellacera (1627–1699)"

**Struttura**:
```
== Fondazione della nobiltà (1605–1627) ==
  [testo attuale fino a "Morì nel 1627..."]

== La linea continua: da Pietro Giardina a Luigi Arias, fondatore della nobiltà ==
  [NUOVO: sezione completa sul filo genealogico da Pietro a Luigi Arias]
  
  === Il filo genealogico (c. 1500–1627) ===
  === Luigi Arias Giardina: consolidamento della nobiltà e biforcazione (1605–1627) ===
  === Schema della biforcazione primaria: Luigi Arias → Bellacera e Gibellini ===
  === Meccanismo giuridico della biforcazione ===

== Le biforcazioni successive: estinzione Bellacera (1699) e ascesa Gibellini (1703–1733) ==
  [NUOVO: sezione unificata che combina "La linea Bellacera" e "La lite di successione"]
  
  === Prima biforcazione interna: Bellacera maschile estingue (1699) ===
  === Seconda biforcazione: la lite di successione (1699–1703) e il passaggio di asse ===
  === Terza biforcazione: linea principale (Luigi Gerardo) e rami collaterali (Grimaldi, Naselli, Iaci) ===
  === Schema sinottico delle biforcazioni (1627–1831) ===
  === Sintesi della biforcazione strutturale ===

== Discendenza nel XVIII–XIX secolo ==
  [testo attuale, invariato]
```

### Opzione B: Integrazione minimalista (per conservare struttura attuale)

Se vuoi preservare le sezioni storiche esistenti ("La linea Bellacera", "La lite di successione"), puoi:

1. **Mantenere** le due sezioni storiche come sono
2. **Aggiungere** una nuova sezione di "**Analisi strutturale della biforcazione**" subito dopo "Discendenza nel XVIII–XIX secolo", che sintetizza il modello di biforcazione in prospettiva comparata

---

## Elementi da includere nel wiki

### 1. **Sezione narrativa** (già fornita in `sezione_biforcazione_giardina.wiki`)

**Componenti**:
- Paragrafo sul filo genealogico continuo Pietro → Luigi Arias
- Illustrazione del meccanismo del fedecommesso
- Descrizione della biforcazione primaria (Bellacera vs. Gibellini)
- Spiegazione della lite di successione come punto critico
- Traccia delle biforcazioni successive (Grimaldi, Naselli, Iaci)

**Lunghezza**: ~2500 parole

### 2. **Diagramma SVG** (fornito in `biforcazioni_giardina_diagram.svg`)

**Da incorporare**: Dopo il sottotitolo "Schema della biforcazione primaria: Luigi Arias → Bellacera e Gibellini"

**Sintassi wiki per includere il file SVG**:
```wiki
[[File:Biforcazioni_Giardina_1627-1831.svg|thumb|center|700px|Biforcazioni della casata Giardina (1627–1831). La linea Bellacera (rossa, tratteggiata) si estingue in linea maschile nel 1699; la linea Gibellini-Lucchesi (blu) prevalse nella lite successoria (1703) e fondò il Principato di Ficarazzi (1733). Biforcazioni successive introduce cognomi Grimaldi, Naselli, Iaci tramite matrimoni.]]
```

**Nota**: Il file SVG deve essere caricato su Wikimedia Commons con licenza idonea (es. CC-BY-SA 4.0)

### 3. **Tabella genealogica sintetica** (fornita in `tabella_genealogica_sintetica.md`, convertire a wikitesto)

**Da incorporare**: Dopo "La linea continua: da Pietro Giardina a Luigi Arias"

**Tabella principale** (`Il filo genealogico documentato`): mostra generazioni I–VI, da Pietro (c. 1500) a Luigi Gerardo (c. 1680)

**Tabella secondaria** (`La biforcazione primaria`): confronto Bellacera vs. Gibellini su 6 parametri (titolo, intestatario, apogeo, estinzione, etc.)

**Tabella terziaria** (`Ramo principale: biforcazioni successive`): genera VII–XI, mostra introduzione di Grimaldi, Naselli, Iaci

---

## Conversione da Markdown a wikitesto

La tabella genealogica fornita è in Markdown. Per inserirla nel wiki, convertire secondo il formato wikitesto standard:

### Markdown → Wikitesto

**Markdown**:
```markdown
| Gen. | Anno | Nome | Coniuge | Note |
|------|------|------|---------|------|
| I | c. 1500 | **Pietro** | Giulia | Capostipite |
```

**Wikitesto**:
```wiki
{| class="wikitable" style="width: 100%;"
|-
! Gen. !! Anno !! Nome !! Coniuge !! Note
|-
| I || c. 1500 || '''Pietro Giardina''' || Giulia Del Castillo || Capostipite documentato
|}
```

**Per le tabelle fornite**, è stato già preparato il wikitesto nella sezione narrativa (`sezione_biforcazione_giardina.wiki`). Le tabelle in Markdown servono come riferimento per la revisione critica.

---

## Checklist di integrazione

- [ ] **Leggere la sezione narrativa** (`sezione_biforcazione_giardina.wiki`) e verificarne la coerenza con i dati wiki esistenti
- [ ] **Verificare i nomi** di persone, titoli, date per compatibilità con le sezioni storiche già pubblicate
- [ ] **Caricamento SVG**: Caricare il diagramma su Wikimedia Commons (File:Biforcazioni_Giardina_1627-1831.svg)
- [ ] **Inserire il diagramma** nel wiki con la sintassi [[File:...]]
- [ ] **Convertire le tabelle Markdown** in wikitesto se necessario
- [ ] **Validazione incrociata**: Controllare che ogni biforcazione menzionata sia coerente con la sezione "Linea patrilineare" (finale del articolo)
- [ ] **Test di render**: Visualizzare in anteprima sul sandbox wiki (it.wikipedia.org/wiki/Utente:Daniel_Giardina/Sandbox/...) prima della pubblicazione
- [ ] **Revisione della comunità**: Sottoporre a review di almeno 2 contributori indipendenti prima di spostare nello spazio principale

---

## Note metodologiche per il tuo sandbox Wikipedia

### Collegamento alla memoria del progetto

La sezione "biforcazione" è organizzata secondo il tuo principio cardine:

1. **Documentato**: Tutte le biforcazioni primarie (1627, 1699–1703) sono attestate da fonti secondarie (Mango, San Martino De Spucches, Palizzolo Gravina)
2. **Plausibile**: Il meccanismo del fedecommesso è storicamente coerente con le pratiche siciliane XVII–XVIII sec., anche se i dettagli specifici del testamento di Luigi Arias rimangono da verificare (ASPa, Notai Defunti, 1627–1630)
3. **Speculativo**: Segnalato esplicitamente che il collegamento genealogico diretto tra Pietro (c. 1500) e Luigi Arias (c. 1580) rimane "oggetto di verifica archivistica"

### Evitamento delle trappole AI

La sezione non:
- Produce affermazioni genealogiche di dettaglio senza fonte
- Cita "famiglia tradition" o memorie private come prova
- Dichiara certezze che rimangono ipotesi
- Introduce nuovi nomi senza fonte secondaria identificata

---

## Uso didattico: da sezione wiki a diagramma pedagogico

Se in futuro desideri estrarre un **diagramma semplificato** per scopi didattici (es., presentazione, articolo esterno), è possibile:

1. Semplificare il diagramma SVG rimuovendo i dettagli biografici
2. Creare una versione in ASCII/testo puro per accessibilità
3. Derivare una "timeline lineare" focata su anni e titoli

Per ora, i tre file forniti (narrativa, diagramma completo, tabella) offrono:
- **Narrativa**: per lettori che vogliono capire il "perché" (strategia matrimoniale, meccanismo giuridico)
- **Diagramma**: per lettori che vogliono capire il "come" (visuale della biforcazione)
- **Tabella**: per lettori che vogliono i dati grezzi (generazioni, titoli, date)

---

## Prossimi step

Una volta integrata la sezione biforcazione, i materiali correlati da revisionare/sviluppare:

1. **Verifiche archivistiche** (ASPa):
   - Testamento Luigi Arias (1627–1630): ASPa, Fondo Notai Defunti
   - Lite di successione (1699–1703): Fondo Protonotaro del Regno
   - Investiture 1621, 1703, 1733, 1739: Conservatoria del Registro

2. **Integrazione con sezione "Alleanze matrimoniali della linea patrilineare"**: 
   La tabella genealogica fornita potrebbe fornire elementi per riorganizzare/validare la tabella esistente ("Linea patrilineare Giardina: generazioni, matrimoni, araldica e titoli")

3. **Sviluppo di sezione parallela** su "Strategie matrimoniali e accumulazione titolare":
   Potrebbe emergere un pattern metodico (ibero-siculo "pendolo") che varrebbe la pena analizzare come sottosezione specializzata

---

## Riferimenti

- **Sezione narrativa**: `/home/claude/sezione_biforcazione_giardina.wiki` (2600 parole circa)
- **Diagramma SVG**: `/home/claude/biforcazioni_giardina_diagram.svg` (pronto per Wikimedia Commons)
- **Tabella genealogica**: `/home/claude/tabella_genealogica_sintetica.md` (3 tabelle, convertibili a wikitesto)
- **Questo documento**: linee guida di integrazione e checklist

Tutti i file sono state generati con la logica della distinzione documentato/plausibile/speculativo, senza introdurre hallucination AI-generated.
