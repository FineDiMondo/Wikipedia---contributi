# Istruzioni per Gemini v2 — Sistemazione Stemma Giardina (FEEDBACK REALE DAL SVG)

## 0. PROBLEMI CONCRETI IDENTIFICATI NELL'SVG GENERATO

Analizzando il file `v05_giardina_albero_dominante_newsystem.svg` effettivamente prodotto:

### ⚠️ PROBLEMA 1: Colore oro sbagliato
```xml
<!-- Generato -->
<path id="shield-field" ... fill="#D4A017" />  ❌ WRONG

<!-- Atteso -->
fill="#D4AF37"  ✓ CORRECT
```
**Causa**: Il valore nel JSON non è stato rispettato dal motore di composizione.
**Azione**: Verificare che la mutation `fill_shield_field` passi correttamente il valore `#D4AF37` e non sia sovrascritto.

### ⚠️ PROBLEMA 2: Stroke bordo scudo troppo spesso
```xml
<!-- Generato -->
<path id="shield-outline" ... stroke-width="8" />  ❌ THICK

<!-- Target -->
stroke-width="0.5"  ✓ THIN (heraldico standard)
```
**Causa**: Il motore applica uno stroke-width hardcoded anziché dalla recipe.
**Azione**: Rimuovere o parametrizzare lo stroke-width nella recipe (deve essere ≤0.5px).

### ⚠️ PROBLEMA 3: Trasformazioni annidate complesse
```xml
<!-- Generato (tree layer) -->
<g id="v05-tree" transform="matrix(0.69 0 0 0.69 159.54 180)">
  <g id="tree-root" transform="matrix(2.077098 0 0 2.077098 211.806829 85.000000)">
    <g id="layer1" transform="matrix(-1,0,0,1,445.38489,-64.395254)">
      <!-- TREE PATHS HERE -->
```
**Causa**: Transform compositi (matrix anziché translate/scale) → difficile debuggare, impossibile misurare.
**Azione**: Semplificare alla sola struttura: `<g id="v05-tree" transform="translate(159.54 180) scale(0.69)">` — BASTA.

### ⚠️ PROBLEMA 4: ViewBox eccessivamente grande
```xml
<!-- Generato -->
<svg viewBox="0 0 1000 1000" ... >  ❌ TOO LARGE

<!-- Target -->
<svg viewBox="0 0 400 480" ... >  ✓ PROPORTIONAL
```
**Causa**: Il motore non usa il canvas dichiarato nella recipe.
**Azione**: Force nel JSON: `"canvas": {"width": 400, "height": 480, "viewBox": "0 0 400 480"}`.

### ✓ PROBLEMA 5: Colore albero CORRETTO
```xml
<path ... fill="#2E7D32" />  ✓ Colore verde corretto
<path ... stroke="#1B5E20" />  ✓ Stroke verde scuro corretto
```
Il verde è stato applicato correttamente → la pipeline dei colori funziona per il tree.

---

## 1. CAUSE IDENTIFICATE NEL MOTORE DI COMPOSIZIONE

Basandosi sul SVG generato, il motore `compose_heraldic_svg.py`:

1. **Non rispetta correttamente i colori dalla recipe** — Il colore oro (#D4A017) suggerisce:
   - O una hardcoded palette nel motore
   - O una trasformazione di colore in fase di composizione
   - O un default nel template SVG sorgente che non viene sovrascritto

2. **Applica stroke-width hardcoded** — Non viene parametrizzato dalla recipe.

3. **Usa matrix() anziché translate/scale** — Rende il debugging geometrico quasi impossibile.

4. **ViewBox generato non corrisponde al target** — 1000×1000 invece di 400×480.

---

## 2. RECIPE JSON RIVISTA — CON CORREZIONI PER IL MOTORE

```json
{
  "metadata": {
    "variant": "v05_giardina_albero_dominante_newsystem_v2",
    "description": "Stemma famiglia Giardina: campo oro, albero verde centrale, leoni rossi laterali, corona principesca",
    "created": "2026-03-18",
    "sources": [
      "normalized/scudo_base.normalized.svg",
      "extracted/albero_sradicato.svg",
      "normalized/lion_rampant_element.normalized.svg",
      "normalized/corona_principesca.normalized.svg"
    ]
  },

  "canvas": {
    "width": 400,
    "height": 480,
    "viewBox": "0 0 400 480",
    "background_color": "transparent"
  },

  "layers": [
    {
      "id": "shield_base",
      "asset": "normalized/scudo_base.normalized.svg",
      "z_order": 1,
      "transform": {
        "translate": [0, 0],
        "scale": [1.0, 1.0],
        "rotate": 0
      },
      "mutations": {
        "fill_shield_field": "#D4AF37",
        "stroke_shield_outline": "#1A1A1A",
        "stroke_width_outline": 0.5
      },
      "notes": "FIX: Aggiunto stroke_width_outline=0.5 per heraldica"
    },

    {
      "id": "albero_sradicato",
      "asset": "extracted/albero_sradicato.svg",
      "z_order": 3,
      "transform": {
        "translate": [200, 180],
        "scale": [1.0, 1.0],
        "rotate": 0
      },
      "mutations": {
        "fill_color": "#228B22",
        "stroke_color": "#1B5E20",
        "stroke_width": 0.5,
        "opacity": 1.0
      },
      "constraints": {
        "centering": "both",
        "max_width_percent": 40,
        "max_height_percent": 45,
        "enforce_xy_centering": true
      },
      "notes": "FIX: translate=[200, 180] deve essere ESATTO (non scalato)"
    },

    {
      "id": "leone_sinistro",
      "asset": "normalized/lion_rampant_element.normalized.svg",
      "z_order": 2,
      "transform": {
        "translate": [100, 220],
        "scale": [0.85, 0.85],
        "rotate": 0
      },
      "mutations": {
        "fill_color": "#C41E3A",
        "stroke_width": 0.5
      },
      "constraints": {
        "symmetry_partner": "leone_destro",
        "mirror_x": false
      }
    },

    {
      "id": "leone_destro",
      "asset": "normalized/lion_rampant_element.normalized.svg",
      "z_order": 2,
      "transform": {
        "translate": [300, 220],
        "scale": [0.85, 0.85],
        "rotate": 0
      },
      "mutations": {
        "fill_color": "#C41E3A",
        "stroke_width": 0.5,
        "flip_x": true
      },
      "constraints": {
        "symmetry_partner": "leone_sinistro",
        "mirror_x": true
      }
    },

    {
      "id": "corona_principesca",
      "asset": "normalized/corona_principesca.normalized.svg",
      "z_order": 4,
      "transform": {
        "translate": [200, 60],
        "scale": [0.95, 0.95],
        "rotate": 0
      },
      "mutations": {
        "fill_color": "#D4AF37",
        "gemma_centrale_color": "#FF0000",
        "gemma_centrale_brightness": 1.15,
        "stroke_width": 0.5
      },
      "constraints": {
        "centering": "x_only",
        "min_clearance_from_tree_px": 20
      }
    }
  ],

  "output": {
    "path": "varianti/v05_giardina_albero_dominante_newsystem_v2.svg",
    "format": "svg",
    "embed_metadata": true,
    "simplify_transforms": true,
    "notes": "FIX: simplify_transforms=true forza translate/scale, NON matrix()"
  },

  "validation": {
    "target_metrics": {
      "canvas_viewBox": "0 0 400 480",
      "albero_area_percent": [38, 42],
      "leoni_combined_area_percent": [23, 27],
      "corona_area_percent": [16, 20],
      "albero_x_offset_px": [-5, 5],
      "albero_y_offset_px": [-3, 3],
      "symmetry_leoni_ratio": [0.95, 1.05],
      "color_shield_field_hex": "#D4AF37",
      "color_tree_hex": "#228B22",
      "color_lions_hex": "#C41E3A"
    },
    "baseline_comparison": "varianti/v05_giardina_albero_dominante.svg"
  }
}
```

---

## 3. ISSUE DA SEGNALARE AL MOTORE

### Issue 3.1: Colore oro hardcoded
**Manifestazione**: Output SVG contiene `#D4A017` anziché `#D4AF37`.
**Sospetta causa**: 
- O il template SVG di `scudo_base.normalized.svg` ha un valore hardcoded
- O il motore ignora la mutation `fill_shield_field`

**Fix**: 
1. Ispezionare `assets/araldica/giardina/normalized/scudo_base.normalized.svg` e verificare che `fill="#D4AF37"` (non #D4A017)
2. Nel motore, assicurare che `mutations.fill_shield_field` modifichi effettivamente il `fill` del path #shield-field

### Issue 3.2: ViewBox non rispettato
**Manifestazione**: Output ViewBox è `0 0 1000 1000` anziché `0 0 400 480`.
**Causa**: Il canvas dichiarato nella recipe non viene usato; il motore estrae il viewBox dai sorgenti SVG.

**Fix**: 
Nel motore, DOPO il merge di tutti i layer, rewrite il viewBox del root `<svg>` in base a `canvas.viewBox`.

### Issue 3.3: Transform compositi anziché semplici
**Manifestazione**: Output contiene `matrix(0.69 0 0 0.69 159.54 180)` anziché `translate(159.54 180) scale(0.69)`.
**Causa**: Il motore usa la funzione SVG `matrix()` per applicare le trasformazioni composte.

**Fix**: 
Aggiungere flag `"simplify_transforms": true` nel JSON; il motore deve decomposare matrix() in translate/scale/rotate separati.

### Issue 3.4: Stroke-width hardcoded nel template
**Manifestazione**: `stroke-width="8"` nel bordo scudo; non è controllato dalla recipe.

**Fix**:
Nel template `scudo_base.normalized.svg`, usare un attributo placeholder come `stroke-width="__STROKE_WIDTH__"` che il motore rimpiazza durante il caricamento asset.

---

## 4. CHECKLIST PER GEMINI

Prima di procedere, conferma:

- [ ] **Comprendi il problema colore**: Il #D4A017 generato è diverso dal #D4AF37 atteso. Sai dove controllare?
- [ ] **Comprendi viewBox**: Il motore genera 1000×1000; target è 400×480. È una constraints del motore o un bug?
- [ ] **Comprendi transform**: matrix() vs translate/scale. Sai come leggere `matrix(0.69 0 0 0.69 159.54 180)` e convertirti in coordinate cartesiane?
- [ ] **Puoi modificare la recipe JSON** per passare le correzioni al motore?
- [ ] **Conosci il file sorgente asset** `scudo_base.normalized.svg`? Dovrebbe contenere il colore esatto?

---

## 5. PROSSIMI STEP CONCRETI

### Passo 1: Ispezionare il template scudo
```bash
cat ./assets/araldica/giardina/normalized/scudo_base.normalized.svg | head -50
# Cercare: <path fill="#..." stroke-width="..." >
# Verificare che fill SIA #D4AF37, non #D4A017
```

### Passo 2: Verificare il motore compie le mutazioni
Nel codice di `compose_heraldic_svg.py`:
```python
# Dove viene applicata la mutation fill_shield_field?
# Dovrebbe contenere:
# if "fill_shield_field" in mutations:
#     shield_field_element.set("fill", mutations["fill_shield_field"])
```

### Passo 3: Rigenerare con recipe aggiornata
```bash
python .\scripts\compose_heraldic_svg.py \
  --recipe .\assets\araldica\giardina\recipes\v05_giardina_albero_dominante_newsystem.json
```

### Passo 4: Controllare il nuovo SVG generato
```bash
# Cercare il colore oro:
grep 'fill="#D4AF37"' ./assets/araldica/giardina/varianti/v05_giardina_albero_dominante_newsystem_v2.svg

# Cercare il viewBox:
grep 'viewBox=' ./assets/araldica/giardina/varianti/v05_giardina_albero_dominante_newsystem_v2.svg

# Dovrebbe essere:
# viewBox="0 0 400 480"

# Cercare i transform (dovrebbe essere translate/scale, non matrix):
grep 'transform=' ./assets/araldica/giardina/varianti/v05_giardina_albero_dominante_newsystem_v2.svg | head -5
```

### Passo 5: Analizzare metriche
```bash
python .\scripts\analyze_heraldic_composition.py \
  --svg .\assets\araldica\giardina\varianti\v05_giardina_albero_dominante_newsystem_v2.svg \
  --baseline .\assets\araldica\giardina\varianti\v05_giardina_albero_dominante.svg
```

Attese (da validare):
```
albero_area_percent: 40 ± 2 ✓
leoni_combined_area_percent: 25 ± 2 ✓
corona_area_percent: 18 ± 2 ✓
symmetry_leoni_ratio: 0.98–1.02 ✓
color_shield_field: #D4AF37 (verifica HEX nel SVG)
baseline_delta_percent: < 3% ✓
```

---

## 6. DOMANDE PER GEMINI

Se contatti Gemini, poni questi quesiti concreti:

1. **Su colore oro**: "Confronta #D4A017 vs #D4AF37. Qual è la differenza percettiva in heraldica? Come assicurare che il motore componga il colore corretto?"

2. **Su viewBox**: "Il motore genera viewBox 1000×1000 anziché 400×480 dichiarato. È un vincolo del canvas SVG sorgente o del motore?"

3. **Su transform**: "Come convertirti matrix(0.69 0 0 0.69 159.54 180) in translate/scale semplici? Qual è il valore scale reale dell'albero?"

4. **Su stroke**: "Nel bordo scudo stroke-width="8" è troppo. Dovrebbe essere ≤ 0.5px. Come parametrizzare nel motore?"

5. **Su recipe**: "La recipe JSON v2 che ho preparato affronta questi problemi. Puoi verificare che il motore la supporti?"

---

## 7. ALLEGATI ALLA RECIPE

Quando invii a Gemini, allega anche:

1. **Lo SVG generato** (v05_giardina_albero_dominante_newsystem.svg) — Così vede i problemi reali
2. **Il file sorgente scudo** (scudo_base.normalized.svg) — Per verificare il colore hardcoded
3. **Il codice del motore** (compose_heraldic_svg.py, prime 100 righe) — Per capire come applica le mutazioni
4. **Output atteso** (immagine dello stemma corretto da Wikipedia o riferimento) — Benchmark visivo

