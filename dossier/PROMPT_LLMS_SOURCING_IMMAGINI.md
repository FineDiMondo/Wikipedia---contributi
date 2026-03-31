# 🎯 PROMPT PER LLM: SOURCING IMMAGINI SORGIVA FONTANIN DA FONTI PUBBLICHE

**Scopo**: Trovare/identificare fonti di immagini ad alta risoluzione (CC0, CC-BY-SA, dominio pubblico) da caricare su Wikimedia Commons per l'articolo Wikipedia "Sorgiva Fontanin".

**Nota importante**: Ogni immagine deve avere:
- ✅ Licenza verificabile (CC0, CC-BY-SA, dominio pubblico, o autorizzazione explicit)
- ✅ Risoluzione minima 1200×800 px (preferibilmente 2000+×1500+ px)
- ✅ Tracciabilità della fonte (URL, archivio, autore)
- ✅ Metadati EXIF conservati (se disponibili)

---

## **PROMPT GENERALE (Da lanciare come introduzione)**

```
Sei un esperto di ricerca di contenuti visual da archivi pubblici e banche dati open access.

Il tuo compito è trovare immagini di alta qualità (licenza CC0, CC-BY-SA, dominio pubblico, o su cui autore ha dato autorizzazione esplicita) per 7 posizioni diverse in un articolo Wikipedia sulla "Sorgiva Fontanin" in provincia di Verona, Italia.

Ogni immagine deve essere:
1. Effettivamente disponibile online da una fonte verificabile
2. In dominio pubblico O con licenza open che permette riuso su Wikimedia Commons
3. Tracciabile (fornire URL diretto, metadati autore, archivio)
4. Ad alta risoluzione possibile (minimo 1200×800 px)

Per ogni immagine che troverai, fornisci:
- URL della fonte
- Autore (se noto)
- Licenza esatta (es. "CC0", "CC-BY-SA 3.0", "dominio pubblico USA")
- Risoluzione
- Breve descrizione di come sarà usata su Wikipedia
- Link al file originale scaricabile

Procederò una immagine alla volta. Pronto?
```

---

## **IMMAGINE #1: VISTA AEREA DEL FONTANIN (CRITICA)**

**Nome file da caricare**: `File:Fontanile_Villafranca_Verona_risorgiva.jpg`

**Posizione nel testo**: Infobox (campo immagine principale)

**Descrizione richiesta**: Vista aerea del Fontanin che mostra il cratere circolare profondo 6 m circondato da campi coltivati e boschi di ripa

**Prompt specifico**:

```
Cerca una vista aerea/satellitare di alta qualità (CC0, CC-BY-SA, o dominio pubblico) della zona di Sant'Andrea presso Villafranca di Verona, che mostri:
- Una depressione circolare (fontanile/cratere di escavazione)
- Circondata da campi agricoli (risaie o seminativi)
- Vegetazione riparia (boschi)
- Coordinate approssimative: 45.34004°N, 10.86285°E (provincia di Verona, Bassa Veronese)

Fonti da cercare (in ordine di priorità):
1. **Google Earth Pro** (immagini storiche CC-BY-SA) — cerca Villafranca di Verona, zoom level satellite
2. **Sentinel-2 ESA** (immagini satellitari europee, libere CC0) — https://scihub.copernicus.eu/
3. **USGS Earth Explorer** (immagini Landsat, dominio pubblico USA) — https://earthexplorer.usgs.gov/
4. **Kartaview** (photo crowdsourced, CC-BY-SA) — https://kartaview.org/
5. **Drone imagery OpenData** — cercare in banche dati regionali Veneto open data
6. **Giugno-settembre** è stagione migliore (meno nuvolosità)

Se non trovi vista aerea specifica del Fontanin, accetta:
- Vista aerea generica della zona (Sant'Andrea, Villafranca) con visibilità del fontanile
- Screenshot da Google Maps (verificare se CC-BY-SA)
- Immagine da Bing Maps (verificare licenza)

Alternative ammesse:
- Foto da drone privato ad altissima risoluzione (se autore dà autorizzazione esplicita a rilasciare CC0 o CC-BY-SA)
- Fotografia terrestre ad altissima risoluzione che mostri il cratere caratteristico

Risultato atteso: URL diretto a immagine scaricabile, formato JPEG/PNG, risoluzione 2000×1500+ px
```

---

## **IMMAGINE #2: MAPPA GEOGRAFICA RISORGIVE VERONESE (CRITICA)**

**Nome file da caricare**: `File:Villafranca_Verona_location_map.svg`

**Posizione nel testo**: Sezione "Localizzazione e geografia"

**Descrizione richiesta**: Mappa vettoriale (SVG o rasterizzata) che mostra la fascia delle risorgive venete in rosso tra Valeggio e San Giovanni Lupatoto, con marcatore del Fontanin

**Prompt specifico**:

```
Cerca O crea una mappa geografica (CC0, CC-BY-SA) che mostri:
- Territorio della provincia di Verona
- Fascia delle risorgive lungo il confine tra alta e bassa pianura (evidenziata in rosso)
- Comuni interessati: Valeggio, Villafranca, Mozzecane, Povegliano, Vigasio, San Giovanni Lupatoto
- Marcatore del Fontanin presso Sant'Andrea (45°20′24″N 10°51′46″E)
- Corsi d'acqua principali: Tione dei Monti, Canale Raccoglitore

Fonti per mappe vettoriali (SVG):
1. **Wikimedia Commons** — cercare "Verona map" o "risorgive Veneto" formato SVG
2. **OpenStreetMap** — esportare come SVG (completamente CC0)
3. **Natural Earth Data** — mappe vettoriali CC0 (https://www.naturalearthdata.com/)
4. **QGIS + Open Data Regione Veneto** — scaricare shapefile dati geografici regionali e renderizzare come SVG/PNG

Se mappa già esistente in Wikimedia Commons:
- Usa quella (risparmia tempo)
- Ricerca: "Comune Villafranca di Verona"

Se non esiste:
- Puoi creare una mappa vettoriale semplificata usando:
  - QGIS (gratuito, open source)
  - Inkscape (per SVG vettoriale)
  - Python con folium/geopandas (genera mappe automaticamente)

Risultato atteso: File SVG (vettoriale) OPPURE PNG ad alta risoluzione (2000×1500+ px)
Licenza: CC0 oppure CC-BY-SA 3.0
Formato da caricare: SVG preferibilmente (scalabile)
```

---

## **IMMAGINE #3: RANA DI LATASTE (SPECIE ENDEMICA)**

**Nome file da caricare**: `File:Rana_latastei_habitat_risorgiva.jpg`

**Posizione nel testo**: Sezione "Flora e fauna" → "Condizioni attuali"

**Descrizione richiesta**: Fotografia della rana di Lataste (Rana latastei) nel suo habitat naturale di risorgiva

**Prompt specifico**:

```
Cerca una fotografia ad alta qualità di **Rana latastei** (rana di Lataste) che mostri:
- Il rospo/rana intero visibile
- Preferibilmente in habitat naturale (risorgiva, fontanile, zona umida)
- Specie caratteristica della pianura padana

Fonti da cercare:
1. **Wikimedia Commons** — cerca "Rana latastei" (potrebbe già esistere in CC0/CC-BY-SA)
2. **iNaturalist** (https://www.inaturalist.org/) — foto di osservatori da licenza CC, filtro per "CC0" o "CC-BY-SA"
3. **GBIF** (https://www.gbif.org/) — foto da archivi naturalistici globali, spesso CC-BY-SA
4. **Flickr Creative Commons** — cerca "Rana latastei" con licenza CC-BY-SA
5. **Museo Civico di Storia Naturale Milano** — archivi fotografici naturalistici (contattare per permesso)
6. **Università di Padova - Dipartimento di Biologia** — ricerche su rana di Lataste (contattare autori per autorizzazione)

Criteri di accettabilità:
- Se foto è da naturalista/ricercatore pubblico, contatta per chiedere autorizzazione esplicita a rilasciare CC0 o CC-BY-SA
- Qualità fotografica: nitida, colori accurati, ambiente visibile
- Risoluzione: minimo 1200×800 px

Se non trovi Rana latastei specifica:
- Accetta Rana dalmatina (altra rana padana vulnerabile)
- Accetta foto di risorgiva con rospi/rane generiche (purché in habitat appropriato)

Risultato atteso: URL diretto a JPEG/PNG ad alta risoluzione, licenza verificata
```

---

## **IMMAGINE #4: GAMBERO DI FIUME (AUSTROPOTAMOBIUS PALLIPES)**

**Nome file da caricare**: `File:Austropotamobius_pallipes_fontanile.jpg`

**Posizione nel testo**: Sezione "Flora e fauna" → "Condizioni attuali"

**Descrizione richiesta**: Fotografia del gambero di fiume (Austropotamobius pallipes), specie minacciata EN

**Prompt specifico**:

```
Cerca una fotografia di **Austropotamobius pallipes** (gambero di fiume europeo, pallido) che mostri:
- Il gambero intero visibile da angolo superiore o laterale
- Specie vulnerabile, colorazione pallida caratteristica
- Preferibilmente in ambiente acquatico/roccia

Fonti:
1. **Wikimedia Commons** — "Austropotamobius pallipes" (potrebbe già esistere CC-BY-SA)
2. **iNaturalist** — filtro "Austropotamobius pallipes" + CC-BY-SA license
3. **GBIF** — foto da naturalistiche pubbliche
4. **Università di Verona - Biologia Acquatica** — ricerche locali su gamberi fontanili (contattare)
5. **IUCN Red List** — spesso include foto degli autori in CC

Criteri:
- Immagine nitida, dettagli morfologici visibili
- Minimo 1200×800 px
- Licenza CC0 o CC-BY-SA

Alternativa:
- Se non trovi Austropotamobius pallipes: accetta Austropotamobius torrentium (gambero di torrente)
- Accetta anche video screenshot se qualità suffciente

Risultato atteso: URL JPEG/PNG, licenza verificata
```

---

## **IMMAGINE #5: RICOSTRUZIONE PAESAGGIO MEDIEVALE BASSA VERONESE**

**Nome file da caricare**: `File:Palude_pianura_padana_ricostruzione_medievale.jpg`

**Posizione nel testo**: Sezione "Storia e memoria del paesaggio" → "Il castrum longobardo"

**Descrizione richiesta**: Ricostruzione artistica/paesaggistica della Bassa Veronese nel Medioevo (VIII-XII sec.) prima della bonifica: vaste paludi, foreste fluviali di ontani-pioppi-salici

**Prompt specifico**:

```
Cerca una ricostruzione storica/artistica (CC0, CC-BY-SA, o dominio pubblico) che mostri:
- Paesaggio palustrese medievale della pianura padana
- Foreste riparie con ontani, pioppi, salici
- Corsi d'acqua sinuosi, aree acquitrinose
- Stile: disegno, acquarello, illustrazione, pittura scientifica
- Periodo: VIII-XVI secolo (prima della bonifica moderna)

Fonti da cercare:
1. **Wikimedia Commons** — "Po river medieval" o "Padane wetlands reconstruction"
2. **Museo del Territorio di Verona** — archivi storico-artistici (contattare)
3. **Università di Verona - Storia Medievale** — ricostruzioni per pubblicazioni storiche (contattare Giostra)
4. **Musei regionali veneti** — disegni/dipinti paesaggistici storici
5. **Biblioteca Civica di Verona** — archivi cartografici e illustrazioni antiche (dominio pubblico)
6. **Atlas Coelestis di Coronelli** — mappe storiche di Verona/Padania (XVII sec., spesso dominio pubblico)
7. **OpenAI DALL-E / Midjourney** — se necessario, generare ricostruzione con prompt: "Medieval Bassa Veronese wetlands, Longobard period, 8th century, swamps and riparian forests, paludi e foreste fluviali"

Se trova immagine storica (XVI-XVII sec.):
- Accetta disegni/incisioni/mappe antiche che mostrano "paludi" veronesi
- Verifica se dominio pubblico (dipende da anno pubblicazione + copyright)

Risultato atteso: JPEG/PNG ad alta risoluzione (minimo 1500×1200 px), licenza verificata
```

---

## **IMMAGINE #6: BOLLA PONTIFICIA EUGENIO III 1145**

**Nome file da caricare**: `File:Bolla_Eugenio_III_1145_Verona_churches.jpg`

**Posizione nel testo**: Sezione "Storia e memoria del paesaggio" → "Il castrum longobardo"

**Descrizione richiesta**: Documento originale (facsimile fotografico ad alta risoluzione) della Bolla pontificia "Piae postulatio voluntatis" di Papa Eugenio III, 17 maggio 1145

**Prompt specifico**:

```
Cerca facsimile / fotografico di alta qualità (CC0, CC-BY-SA, dominio pubblico) della:
**Bolla pontificia "Piae postulatio voluntatis" di Papa Eugenio III, 17 maggio 1145**

Documento originale cita: "cappella di Santo Andrea, al Fontanile" (chiesa presso Fontanin, Verona)

Fonti:
1. **Archivio Vaticano** (https://asv.vatican.va/) — richiedi accesso digitale, spesso disponibile scannerizzato CC0
2. **Regesta Pontificia** — database online di bolle pontificie con immagini
3. **Biblioteca Apostolica Vaticana** — collezioni digitali (spesso dominio pubblico)
4. **Archivio della Diocesi di Verona** — conserva copia della bolla (contattare per fotografia ad alta risoluzione autorizzata)
5. **BVMC (Biblioteca Virtuale dei Manoscritti Medievali Canonici)** — collezioni pontificali digitali
6. **Google Arts & Culture** — archivi digitali Vaticani spesso CC0

Se originale non trovabile:
- Accetta scansione a buona risoluzione di una copia legittima dal XVI-XVII sec. (dominio pubblico se vecchio enough)
- Accetta disegno/incisione interpretativo (dominio pubblico pre-1923)

Verificare licenza esplicitamente con ente custode (Vaticano, Diocesi, Università).

Risultato atteso: JPEG/TIFF ad altissima risoluzione (3000×2400 px min), formato documento leggibile, licenza verificata
```

---

## **IMMAGINE #7: STATUA SANT'ANDREA AL FONTANIN (MEMORIA TOPOGRAFICA)**

**Nome file da caricare**: `File:Statua_Sant_Andrea_Fontanin_Villafranca_memoria_topografica.jpg`

**Posizione nel testo**: Sezione "Storia e memoria del paesaggio" → "Memoria topografica e patrimonio intangibile"

**Descrizione richiesta**: Fotografia contemporanea della statua in pietra di Sant'Andrea presso il Fontanin di Villafranca, mostrando lo stato attuale di danneggiamento da vandalismo

**Prompt specifico**:

```
Cerca fotografia contemporanea (CC0, CC-BY-SA, o autorizzazione esplicita) della:
**Statua di Sant'Andrea presso il Fontanin di Villafranca di Verona**

Criteri:
- Localizzazione: Sant'Andrea, Villafranca di Verona (45.34004°N, 10.86285°E)
- Soggetto: statua in pietra dell'apostolo Sant'Andrea
- Stato: visibile danneggiamento da vandalismo e incuria
- Foto recente (2020-2026 preferibilmente)
- Qualità: alta risoluzione, illuminazione naturale, monumento ben visibile

Fonti da cercare:
1. **Contatti locali**:
   - Comune di Villafranca di Verona (ufficio patrimonio/ambiente)
   - Compagnia del Fontanin (gruppo di stewardship locale) — hanno documentazione fotografica
   - Associazioni ambientaliste locali (WWF Veronese, Italia Nostra)

2. **Database open**:
   - Wikimedia Commons — "Villafranca Verona" + "Sant'Andrea"
   - iNaturalist — foto di visitatori/naturalisti che hanno documentato il sito
   - Flickr Creative Commons — ricerca "Fontanin Villafranca"

3. **Social media / Repository locali**:
   - Facebook di Villafranca di Verona (ricerca foto pubbliche)
   - Instagram #fontanin #villafranca (con licenza CC opzionalmente)
   - Siti locali di storia/turismo

4. **Contattare direttamente autori**:
   - Se trovi foto interessante non-CC: contatta autore per chiedere autorizzazione a rilasciare CC-BY-SA (spesso accettano)
   - Cavallini, Tosi, Giostra — se hanno documentazione fotografica personale

Alternativa ammessa:
- Se statua non fotografata recentemente: accetta foto non-contemporanea di buona qualità
- Accetta foto che mostri fontanile da diverse angolazioni (fornisce contesto)

Risultato atteso: JPEG ad alta risoluzione (1500×1200+ px), licenza CC0 o CC-BY-SA verificata, oppure autorizzazione esplicita autore
```

---

## **ISTRUZIONI FINALI DI CARICAMENTO A WIKIMEDIA COMMONS**

Una volta trovate tutte le 7 immagini, per ogni file:

### **1. Preparazione del file**

```
- Converti a JPEG (qualità 90-95) se non già JPEG/PNG
- Risoluzione minima: 1200×800 px (consigliato 2000×1500+ px)
- Comprimi senza perdere qualità
- Estrai metadati EXIF se presenti
- Salva in UTF-8 per nomi file Unicode-safe
```

### **2. Template Wiki per Commons (copiare nell'upload form)**

```wiki
== {{int:filedesc}} ==
{{Information
|Description = [DESCRIZIONE ITALIANA BREVE]
|Source = [URL FONTE ORIGINALE]
|Date = [DATA FOTO O DOCUMENTO]
|Author = [AUTORE O "ANONYMOUS" SE SCONOSCIUTO]
|Permission = [LICENZA ORIGINALE]
}}

== {{int:license}} ==
{{CC-BY-SA-3.0}} [O {{CC0}} O {{PD}} A SECONDA DI LICENZA]

== {{int:categories}} ==
[[Category:Sorgiva Fontanin]]
[[Category:Villafranca di Verona]]
[[Category:Risorgive del Veneto]]
[[Category:Hydrography of Italy]]
[AGGIUNGERE CATEGORIE RILEVANTI]
```

### **3. URL per caricamento**

```
Vai a: https://commons.wikimedia.org/wiki/Special:Upload

- Seleziona file locale
- Incolla template Wikipedia sopra
- Inserisci nome file in italiano (es. "Fontanile_Villafranca_Verona_risorgiva.jpg")
- Accetta termini licensing
- Clicca "Upload"
```

### **4. Dopo caricamento**

- File apparirà come `File:Fontanile_Villafranca_Verona_risorgiva.jpg` su Commons
- Puoi usare `[[File:...]]` nel wikitesto di Wikipedia italiano
- Aggiorna i riferimenti in `wiki/Sorgiva_Fontanin.wiki` con URL finale

---

## **CHECKLIST FINALE**

- [ ] Immagine #1 (Vista aerea) trovata e verificata CC/PD
- [ ] Immagine #2 (Mappa risorgive) trovata o creata
- [ ] Immagine #3 (Rana di Lataste) trovata
- [ ] Immagine #4 (Gambero di fiume) trovata
- [ ] Immagine #5 (Paesaggio medievale) trovata o generata
- [ ] Immagine #6 (Bolla Eugenio III) trovata nei Vaticani/Diocesi
- [ ] Immagine #7 (Statua Sant'Andrea) fotografata o trovata
- [ ] Tutte le licenze verificate e documentate
- [ ] Tutti i file caricati a Wikimedia Commons
- [ ] Wikitesto aggiornato con nomi file finali
- [ ] Link alle immagini testati e funzionanti

---

**Data**: 31 marzo 2026
**Creato per**: Articolo Wikipedia "Sorgiva Fontanin"
**Status**: 🟢 Pronto per uso con LLM
