# Handoff Implementativo - Famiglia Giardina

Documento operativo per il team Accenture incaricato di correggere e riallineare la voce [Famiglia_Giardina.wiki](D:/Progetti%20GITHUB/Wikipedia%20-%20contributi/wiki/Famiglia_Giardina.wiki) e la relativa sandbox Wikipedia.

## Obiettivo

Correggere la sequenza genealogica del ramo Bellacera e del passaggio al ramo di Ficarazzi, eliminare le contraddizioni interne oggi presenti nella voce e ridurre i collegamenti non ancora dimostrati verso il ramo moderno.

## Perimetro

- File locale target: `wiki/Famiglia_Giardina.wiki`
- Sandbox target: `Utente:Daniel Giardina/Sandbox/Famiglia Giardina`
- Sezioni coinvolte:
  - incipit tecnico della sandbox
  - `La linea di Bellacera (XVII-XVIII secolo)`
  - `Discendenza nel XVIII-XIX secolo`
  - `Linea patrilineare`
  - eventuali riferimenti al ramo moderno non ancora sostenuti da fonti solide

## Difetti gia' accertati

- Nella sandbox e' presente un loop del template dovuto alla auto-inclusione iniziale della pagina stessa.
- Il testo narrativo afferma che Simone II Giardina Bellacera mori' senza prole maschile e che nel 1703 prevalse la linea di Luigi Gerardo Giardina e Lucchese.
- La `Linea patrilineare` locale rappresenta invece una continuita' diretta `Simone II -> Diego -> Luigi Gerardo`, che e' internamente incoerente.
- Il ramo `Antonino Giardina-Iaci -> Antonino Giardina -> Rosa Lipari -> Giuseppe Giardina` non e' ancora sufficientemente dimostrato da fonti web robuste e non deve essere trattato come catena chiusa.

## Fonti da usare

Usare in priorita' le fonti sotto. Le fonti interne di progetto servono solo come supporto di lavoro, non come prova finale.

- Archivio di Stato di Palermo, inventario `Archivio SPADAFORA`:
  - URL: `https://saassipa.cultura.gov.it/wp-content/uploads/2020/05/166-Archivio-SPADAFORA.pdf`
  - Elementi utili:
    - presenza di `Stato di S. Ninfa - Eredita' di Simone Giardina`
    - presenza di `Successione di Giuseppe Giardina Bellacera`
    - presenza di atti fra il principe di Resuttano e il marchese di S. Ninfa
    - presenza di `Eleonora Di Napoli e Bellacera`
- Rassegna Siciliana di Storia e Cultura, articolo su Ficarazzi:
  - URL: `https://isspe.it/wp-content/uploads/2024/11/Rassegna-Siciliana-0-finale_compressed.pdf`
  - Elementi utili:
    - Luigi Giardina De Guevara Lucchese e Alagona come principe di Ficarazzi
    - successione `Luigi -> Diego -> Giulio Antonio -> Diego Giardina Naselli`
- Virtual Sicily, pagina storica su Ficarazzi:
  - URL: `https://www.virtualsicily.it/Storia-ficarazzi-PA-348`
  - Utile come fonte derivata di controllo per la sequenza `Simone II -> Pietro -> Giuseppe -> Eleonora -> lite -> Luigi Gerardo`
- Fonti a stampa gia' citate nel file:
  - Mango di Casalgerardo
  - Palizzolo Gravina
  - San Martino De Spucches

## Fonti da non usare come prova finale

- FamilySearch
- Geneanet
- alberi genealogici pubblici
- sintesi familiari prive di edizione o segnatura

## Alberatura target da implementare

La voce deve essere riallineata a questa struttura minima.

```text
Luigi Arias Giardina
I marchese di Santa Ninfa
|
|-- ramo Bellacera
|   |
|   |-- Orsola Giardina
|   |   sposò Mario Bellacera
|   |
|   |-- Simone Giardina Bellacera
|   |   II marchese
|   |
|   `-- Giuseppe Giardina Bellacera
|       |
|       |-- Simone II Giardina Bellacera
|       |   principe di Monteleone
|       |   morto senza figli maschi
|       |
|       `-- Pietro Giardina Bellacera
|           investito nel 1685
|           |
|           `-- Giuseppe Giardina Bellacera
|               morto senza eredi maschi
|               |
|               `-- Eleonora Bellacera
|                   diritti contestati
|                   sposò Federico Di Napoli e La Grua
|
`-- ramo collaterale di Gibellini / Lucchesi
    |
    `-- Diego Giardina
        |
        `-- Luigi Gerardo Giardina e Lucchese
            investito nel 1703
            principe di Ficarazzi nel 1733
            |
            `-- Diego Giardina Massa
                investito nel 1739
                |
                `-- Giulio Antonio Giardina Grimaldi
                    investito nel 1787
                    |
                    |-- Diego Giardina Naselli
                    |   investito nel 1812
                    |
                    `-- Paolo Giardina Naselli
                        sposò Maria Antonia Teresa Maddalena Iaci
                        |
                        `-- Antonino Giardina-Iaci
```

## Alberatura da non implementare come certa

Questa catena non deve essere presentata come dimostrata finche' non viene sostenuta da fonti migliori:

```text
Antonino Giardina-Iaci
-> Antonino Giardina
-> Rosa Lipari
-> Giuseppe Giardina (1863)
-> Franco / Marco Aurelio
```

Se necessario, il ramo puo' rimanere menzionato come pista di ricerca separata, ma non come prosecuzione lineare certa del ramo principesco.

## Attivita' richieste

1. Rimuovere dalla sandbox la auto-inclusione iniziale che genera il loop del template.
2. Riscrivere il paragrafo sulla linea Bellacera in forma coerente con la successione `Simone II -> Pietro -> Giuseppe -> Eleonora`.
3. Riscrivere il passaggio del 1703 come esito di lite successoria e non come continuita' padre-figlio.
4. Correggere la `Linea patrilineare` separando visivamente il ramo Bellacera dal ramo collaterale di Gibellini / Lucchesi.
5. Mantenere la linea `Luigi Gerardo -> Diego -> Giulio Antonio -> Diego Giardina Naselli` come successione di Ficarazzi.
6. Limitare `Paolo Giardina Naselli -> Antonino Giardina-Iaci` al massimo livello oggi sostenibile.
7. Rimuovere o declassare ogni raccordo moderno non ancora dimostrato con fonti solide.
8. Uniformare il linguaggio: evitare formule come `anello di congiunzione`, `continuita' storica sancita`, `ha mantenuto il proprio prestigio` se non direttamente supportate.

## Riscritture dei capitoli

Le sezioni sotto sono gia' formulate in modo da poter essere adattate direttamente nel file `wiki/Famiglia_Giardina.wiki`. Il team deve privilegiare la tenuta storica e la sobrieta' del testo rispetto alla completezza genealogica.

### 1. Incipit

Testo proposto:

```wikitext
'''I Giardina''' sono una famiglia della [[Nobiltà siciliana|nobilta' siciliana]] attestata nei repertori storici e feudali tra [[Palermo]], [[Santa Ninfa]] e [[Ficarazzi]] tra la fine del [[XVI secolo]] e il [[XIX secolo]]. Dalla linea marchionale di Santa Ninfa derivarono il ramo dei Giardina Bellacera e, per successione collaterale maturata all'inizio del Settecento, la linea dei principi di Ficarazzi.<ref>A. Mango di Casalgerardo, ''Nobiliario di Sicilia'', vol. I, pp. 433-434; F. San Martino De Spucches, ''La storia dei feudi e dei titoli nobiliari di Sicilia'', vol. VII, pp. 310-318; F. Ferrara, P. Ferrara, ''Riveli, platee e documenti feudali del Marchesato di Santa Ninfa'', Palermo, 1990.</ref>
```

Nota operativa:

- Ridurre nell'incipit le forme onomastiche lunghe se non strettamente necessarie.
- Non anticipare in apertura il raccordo con i rami moderni.
- La menzione all'`Elenco Ufficiale Nobiliare Italiano` puo' restare, ma non deve sostituire la ricostruzione storica seicentesca e settecentesca.

### 2. Origini attestate nei repertori

Testo proposto:

```wikitext
== Origini attestate nei repertori (XVI-XVII secolo) ==
La fase iniziale della storia familiare e' ricostruibile soprattutto attraverso repertori nobiliari e feudali, che attestano la presenza dei Giardina a [[Palermo]] tra tardo Cinquecento e primo Seicento e ne seguono l'ascesa nell'amministrazione del [[Regno di Sicilia]].<ref>A. Mango di Casalgerardo, ''Nobiliario di Sicilia'', vol. I, pp. 433-434; F. San Martino De Spucches, ''La storia dei feudi e dei titoli nobiliari di Sicilia'', vol. VII, pp. 310-312.</ref>

Il primo esponente per il quale le fonti consentono una successione continua e' '''Luigi Arias Giardina''' (c. 1555-1630), al quale i repertori riconducono l'acquisto del feudo di Rampinzeri nel 1605 e l'elevazione di [[Santa Ninfa]] a marchesato nel 1621. Gli studi dedicati al marchesato richiamano inoltre il suo testamento del 1627 come snodo utile per documentare il consolidamento patrimoniale del casato.<ref>F. Ferrara, P. Ferrara, ''Riveli, platee e documenti feudali del Marchesato di Santa Ninfa'', Palermo, 1990, p. 12; F. San Martino De Spucches, ''La storia dei feudi e dei titoli nobiliari di Sicilia'', vol. VII, p. 310.</ref>
```

Nota operativa:

- Tenere il focus su Palermo, Rampinzeri e Santa Ninfa.
- Non riaprire origini medievali, normanne o Val Demone.

### 3. La linea di Bellacera e la lite del 1703

Testo proposto:

```wikitext
== La linea di Bellacera (XVII-XVIII secolo) ==
Il ramo primogenito dei marchesi di Santa Ninfa si intreccio' con la famiglia Bellacera, dalla quale derivo' la linea dei '''Giardina Bellacera'''.<ref>V. Palizzolo Gravina, ''Il blasone in Sicilia'', pp. 195-196; F. San Martino De Spucches, ''La storia dei feudi e dei titoli nobiliari di Sicilia'', vol. VII, pp. 314-318.</ref>

'''Simone Giardina''', figlio di Luigi Arias, sposo' '''Anna Bellacera'''. Dal loro ramo discesero '''Giuseppe Giardina Bellacera''' e quindi '''Simone II Giardina Bellacera''', il quale fu Capitano Giustiziere di Palermo nel 1670 e Principe di Monteleone nel 1671.<ref>V. Palizzolo Gravina, ''Il blasone in Sicilia'', pp. 195-196; F. San Martino De Spucches, ''La storia dei feudi e dei titoli nobiliari di Sicilia'', vol. V, voce "Monteleone", p. 245.</ref>

Alla morte di Simone II la linea non prosegui' in forma lineare verso il ramo di Ficarazzi. La successione passo' infatti a '''Pietro Giardina Bellacera''', investito nel 1685, e successivamente a '''Giuseppe Giardina Bellacera''', morto senza eredi maschi. La figlia di quest'ultimo, '''Eleonora Bellacera''', sposo' '''Federico Di Napoli e La Grua''', aprendo una complessa lite ereditaria sullo Stato di Santa Ninfa e sui diritti della casata. Il contenzioso si concluse nel 1703 con il riconoscimento dei diritti del ramo collaterale rappresentato da '''Luigi Gerardo Giardina e Lucchese'''.<ref>F. San Martino De Spucches, ''La storia dei feudi e dei titoli nobiliari di Sicilia'', vol. VII, p. 318; Archivio di Stato di Palermo, inventario ''Archivio Spadafora'', sezioni sulla successione di Giuseppe Giardina Bellacera e su Eleonora Di Napoli e Bellacera; ''Rassegna Siciliana di Storia e Cultura'', n. 0.</ref>
```

Nota operativa:

- Qui il team deve esplicitare il carattere collaterale e litigioso della successione.
- Non va ripristinata nessuna catena `Simone II -> Diego -> Luigi Gerardo`.

### 4. Il Principato di Ficarazzi

Testo proposto:

```wikitext
== Il Principato di Ficarazzi (XVIII secolo) ==
All'inizio del Settecento il baricentro feudale della famiglia si sposto' verso la costa palermitana con la linea di '''Luigi Gerardo Giardina e Lucchese''', subentrata nel patrimonio del casato dopo la lite successoria del 1703.<ref>F. San Martino De Spucches, ''La storia dei feudi e dei titoli nobiliari di Sicilia'', vol. III, pp. 308-310 e vol. VII, p. 318.</ref>

Il 9 novembre 1733 l'imperatore [[Carlo VI d'Asburgo]] investi' Luigi Gerardo del titolo di '''I Principe di Ficarazzi'''. La tradizione storica locale e gli studi sul marchesato di Santa Ninfa collegano a questa fase opere di sistemazione territoriale, la trasformazione del castello di Ficarazzi in residenza principesca e la committenza legata alla [[Chiesa di Sant'Atanasio (Ficarazzi)|Chiesa di Sant'Atanasio]].<ref>F. San Martino De Spucches, ''La storia dei feudi e dei titoli nobiliari di Sicilia'', vol. III, p. 310; F. Ferrara, P. Ferrara, ''Riveli, platee e documenti feudali del Marchesato di Santa Ninfa'', Palermo, 1990, p. 45.</ref>
```

Nota operativa:

- Mantenere il verbo `collegano` o equivalenti, evitando toni troppo assertivi.
- Se la pagina resta priva di immagine corretta della Chiesa di Sant'Atanasio di Ficarazzi, non sostituire con la chiesa romana omonima.

### 5. Discendenza nel XVIII-XIX secolo

Testo proposto:

```wikitext
== Discendenza nel XVIII-XIX secolo ==
La linea principesca di Ficarazzi prosegui' con '''Diego Giardina Massa''', investito nel 1739, e con suo figlio '''Giulio Antonio Giardina Grimaldi''', che mantenne la continuita' del ramo nel secondo Settecento.<ref>F. San Martino De Spucches, ''La storia dei feudi e dei titoli nobiliari di Sicilia'', vol. III, pp. 312-315.</ref>

Dal matrimonio di Diego con '''Emilia Grimaldi Del Castrone''' derivo' inoltre, per ''iure uxoris'', il collegamento con il Principato di Santa Caterina. Nel primo Ottocento la linea comprende ancora '''Diego Giardina Naselli''', investito nel 1812, e il ramo di '''Paolo Giardina Naselli''', marito di '''Maria Antonia Teresa Maddalena Iaci'''.<ref>A. Mango di Casalgerardo, ''Nobiliario di Sicilia'', vol. I, pp. 438-440; F. San Martino De Spucches, ''La storia dei feudi e dei titoli nobiliari di Sicilia'', vol. III, p. 315 e vol. IX, pp. 140-145.</ref>

Allo stato attuale delle fonti utilizzate nel progetto, la prosecuzione oltre '''Antonino Giardina-Iaci''' deve essere tenuta distinta dalle linee moderne ancora in corso di verifica e non va presentata come continuita' genealogica certa del ramo principesco.
```

Nota operativa:

- Fermare il racconto genealogico al livello oggi davvero sostenibile.
- Il ramo moderno puo' al massimo essere richiamato in nota metodologica, non come prosecuzione lineare.

### 6. Nuova sezione sul patrimonio storico-architettonico

Testo proposto:

```wikitext
== Patrimonio storico-architettonico ==
Alla memoria storica del casato sono collegati alcuni beni che documentano il suo radicamento tra Palermo, Santa Ninfa e Ficarazzi. Tra questi figurano il '''Palazzo Castrone-Santa Ninfa''' a Palermo, associato alla presenza cittadina del ramo marchionale, e il '''Castello Giardina di Ficarazzi''', trasformato in residenza principesca nel corso del XVIII secolo.<ref>F. Ferrara, P. Ferrara, ''Riveli, platee e documenti feudali del Marchesato di Santa Ninfa'', Palermo, 1990; F. San Martino De Spucches, ''La storia dei feudi e dei titoli nobiliari di Sicilia'', vol. III, pp. 308-310.</ref>

La committenza attribuita a Luigi Gerardo Giardina e al ramo principesco di Ficarazzi e' inoltre richiamata, nella storiografia locale, in relazione alla [[Chiesa di Sant'Atanasio (Ficarazzi)|Chiesa di Sant'Atanasio]], che costituisce uno dei riferimenti materiali piu' significativi associati alla presenza storica della famiglia nel territorio.<ref>F. Ferrara, P. Ferrara, ''Riveli, platee e documenti feudali del Marchesato di Santa Ninfa'', Palermo, 1990, p. 45.</ref>
```

Nota operativa:

- Questa sezione serve a rafforzare la rilevanza storica della voce senza aprire nuovi rami genealogici.
- Restare su committenza, radicamento territoriale e sopravvivenza dei beni.

### 7. Linea patrilineare in forma pronta

Testo proposto:

```wikitext
== Linea patrilineare ==
La genealogia documentata consente di distinguere il ramo primogenito dei marchesi di Santa Ninfa, estinto in linea maschile all'inizio del XVIII secolo, e il ramo collaterale di Gibellini e Lucchesi, dal quale derivo' la linea dei principi di Ficarazzi.<ref>V. Palizzolo Gravina, ''Il blasone in Sicilia'', pp. 195-196; F. San Martino De Spucches, ''La storia dei feudi e dei titoli nobiliari di Sicilia'', vol. III, pp. 308-315 e vol. VII, pp. 310-318.</ref>

'''Ramo primogenito (Santa Ninfa e Bellacera)'''
* '''Luigi Arias Giardina''' (c. 1555-1630), I Marchese di Santa Ninfa.
** '''Simone Giardina''', II Marchese di Santa Ninfa, sposo' Anna Bellacera.
*** '''Giuseppe Giardina Bellacera''', Marchese di Santa Ninfa.
**** '''Simone II Giardina Bellacera''' (c. 1640-1703), Principe di Monteleone e Capitano Giustiziere di Palermo; morto senza prole maschile.
**** '''Pietro Giardina Bellacera''', investito nel 1685.
***** '''Giuseppe Giardina Bellacera''', morto senza eredi maschi.
****** '''Eleonora Bellacera''', moglie di Federico Di Napoli e La Grua; i relativi diritti furono oggetto di lite successoria.

'''Ramo collaterale (Gibellini, Lucchesi e Ficarazzi)'''
* '''Diego Giardina''', barone di Gibellini.
** '''Luigi Gerardo Giardina e Lucchese''' (c. 1680-1738), subentrato nel 1703 per esito di lite successoria; I Principe di Ficarazzi dal 1733.
*** '''Diego Giardina Massa''' (c. 1720-1786), II Principe di Ficarazzi.
**** '''Giulio Antonio Giardina Grimaldi''' (c. 1750-1811).
***** '''Diego Giardina Naselli''', investito nel 1812.
***** '''Paolo Giardina Naselli''' (1791-1837), sposo' Maria Antonia Teresa Maddalena Iaci.
****** '''Antonino Giardina-Iaci''' (nato nel 1831 a Palermo).
```

Nota operativa:

- Questa forma sostituisce integralmente la vecchia sequenza lineare.
- Non aggiungere sotto `Antonino Giardina-Iaci` il ramo `Lipari` se non intervengono nuove fonti dedicate.

## Bibliografia da integrare

Il team puo' gia' predisporre la struttura della bibliografia storica rafforzata. Dove l'edizione esatta va confermata sul volume effettivamente usato, lasciare il dato editoriale finale solo dopo verifica materiale.

- `Ferrara, Ferruccio; Ferrara, Paolo. Riveli, platee e documenti feudali del Marchesato di Santa Ninfa. Palermo, 1990.`
- `Amico, Vito Maria. Dizionario topografico della Sicilia. 2 voll., Palermo, 1855-1859.`
- `Mugnos, Filadelfo. Teatro genealogico delle famiglie nobili, titolate, feudatarie ed antiche nobili del Regno di Sicilia. Ristampa anastatica, 3 voll., Forni.`
- `Villabianca, Francesco Maria Emanuele e Gaetani. Della Sicilia nobile. Ristampa anastatica, 5 voll., Forni.`

Regola:

- `Mugnos` e `Villabianca` servono come repertori complementari.
- Non usarli da soli per chiudere passaggi genealogici controversi.

## Media e Wikimedia Commons

Il team deve trattare gli asset media come parte dell'impianto storiografico della voce. Sotto e' riportata una selezione gia' verificata o controllata per categoria.

| Sezione | Asset Commons | Stato | Uso consigliato | Note operative |
| --- | --- | --- | --- | --- |
| Apertura / contesto | `File:Regno_di_Sicilia_-_Gio._Antonio_Magini_-_btv1b53011566x.jpg` | gia' in voce | mantenere come immagine di cornice storica | verificare in sandbox che il nome file sia identico a quello locale |
| Investitura del 1733 | `https://commons.wikimedia.org/wiki/File:Johann_Gottfried_Auerbach_004.jpg` | verificato | mantenere accanto al paragrafo su Carlo VI | immagine pertinente e stabile per contestualizzare l'investitura |
| Patrimonio di Ficarazzi | `https://commons.wikimedia.org/wiki/Category:Castello_Giardina_(Ficarazzi)` | verificato | usare come categoria di riferimento per scegliere la migliore immagine del castello | nella categoria risultano almeno `Castello di Ficarazzi - panoramio.jpg` e `Castellodificarazzi.jpg` |
| Castello di Ficarazzi | `https://commons.wikimedia.org/wiki/File:Castello_di_Ficarazzi_-_panoramio.jpg` | verificato | fallback se non si usa il file ad alta risoluzione della categoria | qualita' bassa; preferire il file migliore disponibile nella categoria |
| Contesto urbano di Ficarazzi | `https://commons.wikimedia.org/wiki/Category:Ficarazzi` | verificato | utile per eventuali immagini panoramiche o di localizzazione | contiene anche `Ficarazzi panorama.jpg` e la mappa del comune |
| Patrimonio di Palermo | `https://commons.wikimedia.org/wiki/File:Palazzo_Castrone_Santa_Ninfa.jpg` | verificato | inseribile nella nuova sezione sul patrimonio storico-architettonico | la categoria collegata contiene piu' viste del palazzo |
| Palazzo Castrone-Santa Ninfa | `https://commons.wikimedia.org/wiki/Category:Palazzo_Castrone_di_Santa_Ninfa_(Palermo)` | verificato | riferimento principale per scegliere facciata o cortile | usare una sola immagine, non una galleria |
| Contesto di Santa Ninfa | `https://commons.wikimedia.org/wiki/Category:Santa_Ninfa` | verificato | utile per una immagine di luogo se si vuole rafforzare la parte territoriale | la categoria e' povera, ma `Santa Ninfa.jpg` e' utilizzabile |
| Santa Ninfa | `https://commons.wikimedia.org/wiki/File:Santa_Ninfa.jpg` | verificato | opzionale nella parte sulle origini territoriali | da usare solo se non appesantisce l'apertura |
| Araldica | `https://commons.wikimedia.org/wiki/File:Stemma_Giardina_fam_ITA.svg` | verificato | puo' restare nel template o nella sezione araldica | il file e' recente e auto-pubblicato; mantenerlo solo se il disegno e' coerente con la blasonatura usata in voce |

### Asset da non usare

- `https://commons.wikimedia.org/wiki/File:Chiesa_di_Sant%27Atanasio.jpg`
  - Non pertinente: raffigura la chiesa romana di Sant'Atanasio in via del Babuino, non la chiesa di Ficarazzi.
- Asset generici su `Sant'Atanasio` non geolocalizzati a Ficarazzi.
- Gallerie troppo ampie o immagini prive di relazione diretta con i luoghi del casato.

### Regole media

- Una immagine per sezione e' sufficiente.
- Privilegiare beni o luoghi direttamente collegati alla storia del casato.
- Evitare immagini puramente decorative se non rafforzano un passaggio preciso del testo.
- Se un asset Commons e' auto-pubblicato o recente, segnalarlo nel changelog editoriale e valutarne la coerenza con la letteratura araldica o con il bene rappresentato.

## Regole editoriali

- Non rappresentare come certa una successione solo perche' genealogicamente plausibile.
- Quando il passaggio e' litigioso o collaterale, scriverlo come tale.
- Se una persona entra per via ereditaria femminile o per lite successoria, esplicitarlo.
- Evitare di fondere nello stesso albero una linea storicamente attestata e un ramo familiare moderno ancora da provare.
- Preferire una struttura con due rami separati a una catena lineare ma fragile.

## Deliverable attesi

- Versione corretta di `wiki/Famiglia_Giardina.wiki`
- Sandbox allineata al file locale
- Note bibliografiche aggiornate nelle sezioni corrette
- Changelog sintetico delle modifiche effettuate

## Criteri di accettazione

- Nessun loop del template in sandbox
- Nessuna discendenza diretta `Simone II -> Diego -> Luigi Gerardo`
- Presenza esplicita del nodo `Pietro Giardina Bellacera`
- Presenza esplicita del nodo `Giuseppe Giardina Bellacera`
- Presenza esplicita del nodo `Eleonora Bellacera` con indicazione di successione contestata
- Passaggio al 1703 descritto come lite conclusa a favore di Luigi Gerardo Giardina e Lucchese
- Linea di Ficarazzi resa come `Luigi Gerardo -> Diego -> Giulio Antonio -> Diego Giardina Naselli`
- Ramo moderno non presentato come pienamente provato se non accompagnato da nuove fonti

## Punti aperti da validare in una fase successiva

- Forma esatta dei nomi `Aloisio / Luigi Arias / Aloisio Arias Giardina`
- relazione precisa tra Simone Giardina Bellacera e Giuseppe Giardina Bellacera
- data e formula esatta dell'investitura di Pietro Giardina Bellacera nel 1685
- identificazione certa del passaggio `Paolo Giardina Naselli -> Antonino Giardina-Iaci -> ramo Lipari`

## Sequenza di lavoro consigliata

1. Correggere il loop della sandbox.
2. Correggere la `Linea patrilineare`.
3. Correggere il paragrafo narrativo Bellacera.
4. Ridurre il ramo moderno alla sola parte davvero sostenuta.
5. Rieseguire la revisione editoriale finale su tono, neutralita' e consistenza interna.

## Nota finale

Se durante l'implementazione emergono nuove fonti archivistiche o a stampa che contraddicono l'alberatura target sopra proposta, il team deve aggiornare prima la mappa di successione e solo dopo il testo narrativo. La priorita' e' la coerenza genealogica minima, non la completezza.
