# Audit tecnico SVG

## Problemi trovati nei sorgenti

- `scudo_base.svg`: nessun `viewBox`; geometria minima ma non pronta al riuso modulare.
- `corona_principesca.svg`: niente `viewBox`, molti gruppi e trasformazioni annidate, stili inline rumorosi.
- `stemma_giardina_source.svg`: nessun `viewBox`, 20 `clipPath`, molte trasformazioni Inkscape; non adatto al riuso diretto.
- `lion_rampant_element.svg`: semplice ma senza `viewBox` e con palette non coerente con il progetto.
- `lion_rampant.svg`: 2 gradienti, 12 gruppi, 80 path; troppo illustrativo per uso diretto.
- `lion_rampant_heraldry.svg`: 2 gradienti, 40 gruppi, 233 path; stilisticamente forte ma tecnicamente denso.

## Correzioni minime applicate alle derivate

- Tutti i derivati sono stati portati a `viewBox="0 0 1000 1000"` con wrapper trasformativo, senza alterare i sorgenti.
- Rimossi metadati Inkscape, gradienti, `defs`, `clipPath`, elementi nascosti e attributi rumorosi non necessari.
- Convertiti gli stili inline nei soli attributi SVG utili (`fill`, `stroke`, `stroke-width`, `transform`, opacita`).
- Palette ridotta a campiture piatte araldiche: oro, argento, verde albero, rosso leoni, contorni scuri.
- Estratto il solo gruppo arboreo `g43358` dallo stemma Giardina in un asset separato e riusabile.

## Sintesi numerica

| File | viewBox | gruppi | path | clipPath | gradienti | transform | style |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sources/scudo_base.svg` | False | 0 | 1 | 0 | 0 | 0 | 0 |
| `sources/corona_principesca.svg` | False | 22 | 52 | 0 | 0 | 37 | 70 |
| `sources/stemma_giardina_source.svg` | False | 12 | 128 | 20 | 0 | 110 | 129 |
| `candidates/lions/lion_rampant_element.svg` | False | 1 | 13 | 0 | 0 | 0 | 13 |
| `candidates/lions/lion_rampant.svg` | False | 12 | 80 | 0 | 2 | 12 | 90 |
| `candidates/lions/lion_rampant_heraldry.svg` | False | 40 | 233 | 0 | 2 | 39 | 273 |

## Derivati chiave

| File | viewBox | gruppi | path | clipPath | gradienti | transform | style |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `normalized/scudo_base.normalized.svg` | True | 1 | 2 | 0 | 0 | 1 | 0 |
| `normalized/corona_principesca.normalized.svg` | True | 21 | 52 | 0 | 0 | 36 | 0 |
| `normalized/lion_rampant_element.normalized.svg` | True | 2 | 13 | 0 | 0 | 1 | 0 |
| `normalized/lion_rampant.normalized.svg` | True | 13 | 80 | 0 | 0 | 13 | 0 |
| `normalized/lion_rampant_heraldry.normalized.svg` | True | 41 | 233 | 0 | 0 | 40 | 0 |
| `extracted/albero_sradicato.svg` | True | 13 | 107 | 0 | 0 | 110 | 0 |
