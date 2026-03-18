# Ambiente di lavoro per bozze Wikipedia

Questo repository serve a preparare bozze locali e raccolte fonti prima di tentare la pubblicazione su Wikipedia.

Obiettivo pratico:
- verificare se un soggetto e' davvero enciclopedico;
- separare fonti, valutazione e testo in bozza;
- evitare pagine che verrebbero respinte per conflitto di interessi, ricerca originale o mancanza di fonti indipendenti.

## Punto critico

Una pagina sulla propria famiglia o sui propri parenti non e' automaticamente ammissibile. Per Wikipedia servono fonti secondarie, affidabili e indipendenti che trattino il soggetto in modo significativo. Un albero genealogico, ricordi familiari, social network, siti personali o atti sparsi non bastano.

Per questo il flusso corretto e':
1. aprire un dossier per ogni soggetto;
2. raccogliere fonti indipendenti;
3. decidere se il soggetto supera la checklist di ammissibilita;
4. solo dopo scrivere la bozza in wikitesto.

## Struttura

- `wiki/`: pagine wiki finali da sincronizzare con Wikipedia
- `docs/`: regole operative e riferimenti ufficiali
- `templates/`: modelli riusabili per dossier e bozze
- `ricerca/`: materiali di supporto, fonti, valutazioni e appunti di lavoro
- `ricerca/registro_soggetti.json`: registro centrale dei soggetti, con stato, priorita' e gate di pubblicazione
- `ricerca/stato_progetto.json`: snapshot operativo sintetico allineato al registro centrale
- `dossier/`: materiali tecnici e lavorazioni specialistiche
- `assets/`: risorse locali, immagini e sorgenti di lavoro
- `scripts/`: automazioni e utility

## Avvio rapido

Per il caso che hai citato sono presenti:
- `wiki/Famiglia_Giardina.wiki`
- `wiki/Marco_Aurelio_Pasquale_Giardina.wiki`
- `wiki/index.wiki`
- `ricerca/famiglia-giardina/` come supporto documentale

Per creare un nuovo dossier da terminale PowerShell:

```powershell
.\scripts\nuovo-soggetto.ps1 -Nome "Nome Cognome" -Tipo biografia
```

Oppure per una famiglia/casato:

```powershell
.\scripts\nuovo-soggetto.ps1 -Nome "Famiglia Giardina" -Tipo famiglia
```

Se il soggetto e' una persona vivente:

```powershell
.\scripts\nuovo-soggetto.ps1 -Nome "Nome Cognome" -Tipo biografia -Vivente
```

## Setup tecnico

Installa le dipendenze Python una sola volta:

```powershell
python -m pip install -r requirements.txt
```

Per le operazioni verso Wikipedia e Wikimedia Commons puoi usare variabili
d'ambiente di shell oppure un file locale `.env` in radice repo. E' disponibile
un modello in `.env.example`.

Controllo completo del setup:

```powershell
python scripts/repo_doctor.py
```

Controllo locale senza rete:

```powershell
python scripts/repo_doctor.py --no-network
```

Validazione del registro centrale dei soggetti:

```powershell
python scripts/validate_registry.py
```

Estrazione del prossimo batch di lavoro dal registro:

```powershell
python scripts/next_subjects.py
```

## Modello operativo

Il repository segue un modello a doppio binario:

- `knowledge_graph`: soggetti e relazioni interne lavorabili nel tempo, anche se non ancora pubblicabili
- `publishing_track`: soli soggetti che stanno superando i gate di verificabilita', neutralita' e ammissibilita' Wikipedia

Regola pratica:

- i segnaposti sono ammessi nel repository e nei dossier di ricerca;
- non vanno trattati come pronti per lo spazio principale Wikipedia;
- ogni agente deve partire da `ricerca/registro_soggetti.json` e lavorare prima sull'accrescimento verificabile delle evidenze, poi sulla superficie pubblicabile.
- lo snapshot `ricerca/stato_progetto.json` serve solo come vista sintetica del momento, non come fonte primaria di governance.

## Workflow consigliato

1. Compila `scheda.md` con dati minimi e rischi.
2. Compila `fonti.md` inserendo solo fonti verificabili.
3. Usa `valutazione.md` per decidere `GO` o `NO-GO`.
4. Scrivi o aggiorna `bozza.wiki` solo se hai abbastanza fonti indipendenti.
5. Aggiorna `ricerca/registro_soggetti.json` con stato, priorita' e prossime azioni.

## Regola pratica per il tuo caso

- `famiglia-giardina`: ha senso provarci solo se esistono libri, studi storici, repertori o fonti giornalistiche affidabili che trattano la famiglia come soggetto autonomo.
- `parenti maschi diretti`: va valutato un dossier separato per ogni persona. In assenza di notorieta' pubblica e copertura indipendente sostanziale, la voce quasi certamente non passera'.

## Riferimenti

Vedi:
- `docs/riferimenti/riferimenti-wikipedia.md`
- `docs/checklists/checklist-ammissibilita.md`
- `docs/manuali/GUIDA_PUBBLICAZIONE_SANDBOX.md`
