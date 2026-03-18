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
