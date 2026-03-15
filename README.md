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

- `docs/`: regole operative e riferimenti ufficiali
- `templates/`: modelli riusabili per dossier e bozze
- `dossier/`: un dossier per ogni soggetto valutato
- `scripts/`: automazioni PowerShell

## Avvio rapido

Per il caso che hai citato e' gia' presente il dossier:
- `dossier/famiglia-giardina/`

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

## Workflow consigliato

1. Compila `scheda.md` con dati minimi e rischi.
2. Compila `fonti.md` inserendo solo fonti verificabili.
3. Usa `valutazione.md` per decidere `GO` o `NO-GO`.
4. Scrivi o aggiorna `bozza.wiki` solo se hai abbastanza fonti indipendenti.

## Regola pratica per il tuo caso

- `famiglia-giardina`: ha senso provarci solo se esistono libri, studi storici, repertori o fonti giornalistiche affidabili che trattano la famiglia come soggetto autonomo.
- `parenti maschi diretti`: va valutato un dossier separato per ogni persona. In assenza di notorieta' pubblica e copertura indipendente sostanziale, la voce quasi certamente non passera'.

## Riferimenti

Vedi:
- `docs/riferimenti-wikipedia.md`
- `docs/checklist-ammissibilita.md`
