# Provenienza SVG Giardina

## Overview

Originali Wikimedia Commons conservati intatti in `sources/` e `candidates/lions/`.
Tutte le pulizie e composizioni successive sono derivate locali non distruttive.

## Assets

| Nome locale | Titolo Commons | URL usato | Licenza | Autore | Note |
| --- | --- | --- | --- | --- | --- |
| `sources/scudo_base.svg` | Shield plain.svg | https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Shield_plain.svg | Public domain | GeMet | Redirect Commons scaricato correttamente come SVG testuale. |
| `sources/corona_principesca.svg` | Corona heráldica.svg | https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Corona_her%C3%A1ldica.svg | Public domain | Asqueladd | Redirect Commons scaricato correttamente come SVG testuale. |
| `sources/stemma_giardina_source.svg` | Stemma Giardina fam ITA.svg | https://upload.wikimedia.org/wikipedia/commons/0/0d/Stemma_Giardina_fam_ITA.svg | CC BY-SA 4.0 | Sanngreal | Il redirect Commons ha restituito HTML di errore; risolto via file page/API e URL upload diretto. |
| `candidates/lions/lion_rampant_element.svg` | Lion rampant element.svg | https://upload.wikimedia.org/wikipedia/commons/a/ae/Lion_rampant_element.svg | Public domain | Inductiveload (traced from a public domain source) | Il redirect Commons ha restituito HTML di errore; risolto via file page/API e URL upload diretto. |
| `candidates/lions/lion_rampant.svg` | Lion Rampant.svg | https://upload.wikimedia.org/wikipedia/commons/7/75/Lion_Rampant.svg | CC BY-SA 3.0 | Sodacan | Il redirect e il primo URL upload hanno colpito un 429/HTML; recuperato con retry conservativo. |
| `candidates/lions/lion_rampant_heraldry.svg` | Lion rampant - Heraldry.svg | https://upload.wikimedia.org/wikipedia/commons/8/88/Lion_rampant_-_Heraldry.svg | CC BY-SA 2.5 | SajoR | Il redirect e il primo URL upload hanno colpito un 429/HTML; recuperato con retry conservativo. |

## Licenze e attribuzione

- Le licenze restano quelle dichiarate nelle rispettive pagine file di Wikimedia Commons.
- I derivati locali mantengono titolo originale, URL e licenza d'origine.
- I file `CC BY-SA` richiedono attribuzione e condivisione allo stesso modo in eventuale redistribuzione pubblica.

## Validazione download

- Verifica testuale `<svg>` e assenza di HTML di errore.
- Parsing XML con root `svg` e controllo `xmllint`.
- Hash SHA-256 registrato in `sources.json`.

## Download notes

- Quattro asset hanno richiesto fallback via URL upload diretto/API per errore HTML o rate limit 429 sui redirect iniziali.
