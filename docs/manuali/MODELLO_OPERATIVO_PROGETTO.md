# Modello Operativo del Progetto

Questo progetto non deve crescere come accumulo di pagine pubblicate, ma come rete documentale verificabile.

## Obiettivo

Consentire a un agent o a un contributore umano di:

- capire subito quali soggetti esistono gia';
- sapere quali nodi sono solo ricerca interna e quali sono candidabili a Wikipedia;
- lavorare in parallelo senza trasformare bozze deboli in pubblicazioni premature.

## Doppio binario

### 1. Knowledge graph interno

Qui rientrano:

- soggetti incompleti ma promettenti;
- nodi genealogici utili a collegare persone, famiglie, luoghi e istituzioni;
- dossier che servono a far emergere nuove piste di ricerca;
- pagine che oggi non hanno ancora base sufficiente per Wikipedia.

Regola: questi nodi possono esistere e crescere nel repository anche se non sono pubblicabili.

### 2. Publishing track

Qui rientrano solo i soggetti che stanno superando i gate editoriali:

- fonti secondarie indipendenti presenti;
- tono neutrale sostenibile;
- assenza di dipendenza da memoria familiare o sintesi originale;
- rischio COI dichiarato e gestito;
- bozza abbastanza matura da essere sottoposta a revisione esterna.

Regola: un soggetto entra in questo binario solo quando il valore documentale e' gia' distinguibile dal semplice interesse genealogico.

## Stati standard dei soggetti

Ogni soggetto nel registro centrale deve avere uno stato tra questi:

- `candidate`: nodo appena identificato, da esplorare
- `researching`: raccolta fonti e verifica identita' in corso
- `sourced`: esiste una base documentale minima, ma non ancora sufficiente per pubblicazione
- `publishable`: bozza localmente sostenibile e pronta per revisione
- `sandboxed`: bozza destinata o presente in sandbox, in attesa di revisione terza
- `published`: soggetto gia' pubblicato
- `parked`: nodo sospeso, da non spingere attivamente

## Gate di pubblicazione

Ogni soggetto deve avere anche un gate esplicito:

- `do_not_publish`: non deve essere spinto verso Wikipedia
- `sandbox_only`: puo' restare come bozza o sandbox, ma non va promosso oltre
- `candidate_for_review`: puo' essere sottoposto a revisione esterna
- `published`: gia' pubblicato

Il gate conta piu' dell'esistenza di un file `.wiki`.

## Regole hard

- Nessun placeholder va trattato come voce pronta per lo spazio principale.
- Una bozza familiare non diventa ammissibile solo perche' completa sul piano genealogico.
- Le relazioni tra soggetti devono derivare da fonti tracciabili, non da memoria personale.
- Le fonti familiari, private o solo indiziarie possono orientare la ricerca, non chiudere il gate editoriale.
- Se un soggetto dipende ancora da sintesi genealogica, resta nel knowledge graph.

## Flusso per agent e contributor

1. Leggere `ricerca/registro_soggetti.json`.
2. Estrarre il batch corrente con `python scripts/next_subjects.py`.
3. Selezionare i soggetti `high` o `medium` non `parked`.
4. Lavorare prima su identita', fonti secondarie, date, attribuzioni, segnature archivistiche.
5. Ridurre o rimuovere materiale che crea ricerca originale.
6. Aggiornare dossier, bozze e registro centrale.
7. Aggiornare lo snapshot `ricerca/stato_progetto.json` se cambia il quadro operativo.
8. Eseguire i validator:
   - `python scripts/validate_registry.py`
   - `python scripts/next_subjects.py`
   - `python scripts/validate_wikitesto.py ...`
   - `python scripts/check_blp.py ...`

## Ordine di priorita' raccomandato

- Prima: soggetti in `publishing_track` con gate `sandbox_only` o `candidate_for_review`
- Poi: nodi `knowledge_graph` che possono sbloccare soggetti gia' promettenti
- Infine: nuovi candidati ancora molto deboli o solo ipotetici

## Definizione di avanzamento sano

Un soggetto avanza davvero quando migliora almeno uno di questi elementi:

- qualita' delle fonti indipendenti;
- precisione delle segnature e dei riferimenti;
- neutralita' del testo;
- riduzione della dipendenza da materiale familiare;
- chiarezza del motivo per cui il soggetto esiste nel progetto.

Non e' avanzamento sano:

- aumentare il numero di pagine senza aumentare le evidenze;
- aggiungere dettagli genealogici non ancora attribuiti;
- dichiarare `100%` o `blindata` una voce con verifiche ancora aperte.
