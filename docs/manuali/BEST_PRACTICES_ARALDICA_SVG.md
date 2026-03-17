# Best Practices: Composizione Araldica in SVG

Questo documento definisce gli standard tecnici e metodologici per la creazione, normalizzazione e manutenzione degli asset araldici vettoriali (SVG) all'interno del progetto.

## 1. Struttura della Tela (Canvas)
*   **ViewBox Standard**: Tutti i master SVG e i derivati finali devono utilizzare una `viewBox` quadrata standardizzata, preferibilmente `0 0 1000 1000`. Questo garantisce una base di riferimento assoluta per calcolare le traslazioni e i centri di simmetria.
*   **Sfondo**: Il `background` deve essere mantenuto trasparente. I riempimenti a tutto campo (es. campo dello scudo) devono essere definiti tramite tracciati espliciti (`<path>`).

## 2. Architettura XML e Nomenclatura
La struttura dell'XML deve riflettere la gerarchia semantica degli elementi araldici.
*   **Gruppi Nominati**: Ogni elemento araldico distinto (scudo, corona, albero, leone) deve essere racchiuso in un tag `<g>` con un attributo `id` esplicito e descrittivo (es. `id="lion-left"`, `id="shield"`).
*   **Livelli**: Mantenere separati i livelli di sfondo, figure (carichi) e decorazioni esterne (timbri, sostegni). Evitare l'eccessivo annidamento di tag `<g>` inutilizzati derivanti da esportazioni automatiche (es. Inkscape o Illustrator).

## 3. Simmetria e Allineamento
L'araldica richiede una precisione geometrica rigorosa:
*   **Asse Centrale**: Per una `viewBox="0 0 1000 1000"`, l'asse di simmetria verticale si trova esattamente a `x = 500`. Gli elementi centrali (scudo, corona, figure in palo come l'albero) devono avere il proprio centro di massa allineato su questo asse.
*   **Mirroring**: Per i sostegni o le figure controrampanti (es. leoni), utilizzare cloni esatti o istanze (`<use>`) scalati sull'asse X con fattore negativo (es. `transform="matrix(-scaleX 0 0 scaleY translateX translateY)"`). Le distanze dall'asse centrale devono essere matematicamente equivalenti.

## 4. Palette e Stile Araldico
*   **Colori Piatti**: Utilizzare esadecimali solidi. Evitare rigorosamente gradienti, sfumature (blur) o raster incorporati (base64 PNG/JPG). L'araldica vettoriale Wikipedia privilegia le tinte piatte e il contrasto netto.
*   **Contorni (Stroke)**: Mantenere uno spessore del contorno coerente tra i vari elementi (es. scudo e corona non dovrebbero avere spessori radicalmente diversi, a meno di effetti stilistici voluti).

## 5. Licenze e Derivazioni
*   **Tracciamento dei Sorgenti**: Se si utilizzano asset preesistenti da Wikimedia Commons, mantenere i metadati originari (autore, licenza CC, URL) nei manifesti di progetto (es. `manifest.json` o `sources.json`).
*   **Normalizzazione**: Durante l'importazione di asset esterni, pulire il codice SVG eliminando namespace proprietari (`sodipodi:`, `inkscape:`), metadati inutili e tag `<defs>` non referenziati.
