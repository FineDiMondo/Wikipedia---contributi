# Guida pubblicazione sandbox

Questa guida descrive una procedura manuale per pubblicare o aggiornare una bozza nella sandbox Wikipedia senza usare bot o automazioni di login.

## Procedura manuale

1. Aprire la sandbox utente su Wikipedia e verificare di operare con l'account corretto.
2. Preparare localmente il wikitesto definitivo e validarlo con:

```bash
python scripts/validate_wikitesto.py wiki/Famiglia_Giardina.wiki
python scripts/check_blp.py wiki/Famiglia_Giardina.wiki
```

3. Copiare il contenuto del file `.wiki` destinato alla sandbox.
4. Aprire la modifica wikitesto della sandbox e incollare il testo manualmente.
5. Usare l'anteprima per controllare:
   - note e reflist;
   - tabelle e template;
   - assenza di link rossi o file segnaposto;
   - resa corretta delle sezioni genealogiche.
6. Salvare con un edit summary descrittivo e non promozionale.

## Checklist pre-pubblicazione

- COI dichiarato in testa alla bozza, se esistente.
- Richiamo a WP:BLP presente se la bozza contiene o menziona persone viventi.
- Fonti secondarie complete e, per i libri, pagine specifiche oppure `{{pagina necessaria}}`.
- Nessuna sezione di ricerca originale o sintesi interpretativa non attribuita.
- Nessun uso di FamilySearch, Geneanet, social network o blog come prova principale.
- Nessun file `DA_CARICARE_*` ancora presente nel wikitesto.

## Richiesta di revisione

Dopo il salvataggio in sandbox, la revisione va richiesta manualmente ai progetti tematici pertinenti, ad esempio:

- Progetto:Sicilia
- Progetto:Biografie
- Progetto:Nobiltà e araldica

Nel messaggio di richiesta indicare:

- che la bozza e in sandbox;
- che il conflitto di interessi e stato dichiarato, se presente;
- quali fonti secondarie principali sostengono la bozza;
- quali punti sono ancora da verificare o da integrare.
