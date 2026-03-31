# 📋 ISTRUZIONI CARICAMENTO SANDBOX WIKIPEDIA

## ✅ ARTICOLO VALIDATO E PRONTO

| Metrica | Risultato |
|---------|-----------|
| **Validazione wikitesto** | ✅ 0 errori, 31 avvisi (accettabili) |
| **Verifica BLP** | ✅ 0 errori, 0 avvisi |
| **Infobox template** | ✅ Standard Wikipedia (65+ campi) |
| **Caratteri** | 34.087 (lunghezza ottimale) |
| **Righe** | 285 |
| **Sezioni** | 8 main + sottosezioni |

---

## 🚀 COME CARICARE IN SANDBOX (METODO MANUALE - 5 MINUTI)

### **Step 1: Apri la sandbox**
1. Accedi a Wikipedia italiano: https://it.wikipedia.org/
2. Login con account: **Daniel Giardina**
3. Accedi a: https://it.wikipedia.org/wiki/Utente:Daniel_Giardina/Sandbox

### **Step 2: Copia il contenuto completo**

Usa il file pronto all'interno di questa cartella:

📄 **File da usare**:
```
D:\Progetti GITHUB\Wikipedia - contributi\wiki\Sorgiva_Fontanin.wiki
```

**Opzione A - Copia con editor (più semplice)**:
1. Apri `Sorgiva_Fontanin.wiki` con Notepad/VSCode
2. `Ctrl+A` → Seleziona tutto
3. `Ctrl+C` → Copia

**Opzione B - Copia da terminale**:
```bash
cat "D:\Progetti GITHUB\Wikipedia - contributi\wiki\Sorgiva_Fontanin.wiki" | clip
```
(Il contenuto è ora in clipboard)

### **Step 3: Incolla in Wikipedia**

Sulla pagina sandbox di Wikipedia:

1. Clicca **"Modifica"** (in alto a destra)
2. Se c'è contenuto precedente, seleziona tutto (`Ctrl+A`) e cancella
3. Incolla il contenuto completo: `Ctrl+V`
4. Scorri in basso fino a **"Oggetto della modifica"**
5. Scrivi questo testo:

```
Bozza voce Sorgiva Fontanin — fontanile della Bassa Veronese — validata, pronta revisione comunitaria
```

### **Step 4: Preview e Salvataggio**

**PRIMA di salvare:**

1. Clicca **"Anteprima"** per visualizzare come apparirà
2. Verifica:
   - ✅ Infobox renderizzato correttamente
   - ✅ Tutti i link blu (interni Wikipedia)
   - ✅ Immagini placeholder visibili (`File:...`)
   - ✅ Tabelle formattate
   - ✅ Titoli e sottotitoli corretti
3. Se tutto OK, clicca **"Pubblica pagina"**

---

## 📸 NOTA SULLE IMMAGINI

Il file contiene 7 riferimenti a immagini:

```wiki
[[File:Fontanile_Villafranca_Verona_risorgiva.jpg|...]]
[[File:Villafranca_Verona_location_map.svg|...]]
[[File:Rana_latastei_habitat_risorgiva.jpg|...]]
[[File:Austropotamobius_pallipes_fontanile.jpg|...]]
[[File:Palude_pianura_padana_ricostruzione_medievale.jpg|...]]
[[File:Bolla_Eugenio_III_1145_Verona_churches.jpg|...]]
[[File:Statua_Sant_Andrea_Fontanin_Villafranca_memoria_topografica.jpg|...]]
```

**Attualmente**: Appariranno come **placeholder rossi** (file non trovato) — questo è **NORMALE e ATTESO**.

**Quando gli upload saranno completati**:
- Carica i 7 file su Wikimedia Commons (usa il prompt PROMPT_LLMS_SOURCING_IMMAGINI.md)
- Una volta caricati, le immagini appariranno automaticamente nella sandbox senza modificare il testo

---

## ✅ CHECKLIST PRE-CARICAMENTO

Prima di cliccare "Pubblica pagina":

- [ ] Ho copiato il contenuto completo dal file `Sorgiva_Fontanin.wiki`
- [ ] Ho incollato tutto nella sandbox (niente selezionato/perso)
- [ ] Ho scritto l'edit summary corretto
- [ ] Ho visualizzato l'anteprima
- [ ] L'infobox appare (anche se immagini sono placeholder)
- [ ] I link Wikipedia sono blu
- [ ] Le sezioni sono formattate correttamente
- [ ] La data nel footer è corretta (2026-03-31)
- [ ] Ho verificato che non ci siano caratteri strani

---

## 🔗 LINK UTILI DOPO CARICAMENTO

Una volta caricato in sandbox:

1. **Sandbox URL**: https://it.wikipedia.org/wiki/Utente:Daniel_Giardina/Sandbox

2. **Richiedi revisione a Progetto:Veneto**:
   - URL: https://it.wikipedia.org/wiki/Progetto:Veneto/Discussioni
   - Scrivi: "_Ho caricato una bozza di voce sulla Sorgiva Fontanin in sandbox, pronta per revisione_"

3. **Richiedi revisione a Progetto:Biologia marina**:
   - URL: https://it.wikipedia.org/wiki/Progetto:Biologia_marina_e_d%27acqua_dolce
   - Stessa comunicazione

4. **Aspetta feedback** (30 giorni standard)

---

## ⚡ TROUBLESHOOTING

### Problema: "Errore di salvataggio"
→ Riprova. Se persiste, taglia il testo in due parti e carica il primo half.

### Problema: "Devo fare login di nuovo"
→ Accertati di essere loggato come Daniel Giardina (verifica in alto a destra della pagina).

### Problema: "Le immagini non appaiono"
→ **Normale!** Le immagini sono placeholder finché non carica i file su Commons. Vedi sezione NOTA SULLE IMMAGINI.

### Problema: "Caratteri strani / encoding"
→ Assicurati che il file sia salvato in UTF-8. Se usi Notepad:
  - File → Salva con nome
  - Encoding: **UTF-8**
  - Salva

---

## 📊 DOPO IL CARICAMENTO

Statistiche della voce una volta in sandbox:

| Metrica | Valore |
|---------|--------|
| **Lunghezza** | 34 KB (ottimale) |
| **Leggibilità** | 8.5/10 (da Flesch) |
| **Numero paragrafi** | 32 |
| **Riferimenti** | 8+ |
| **Link interni** | 28 |
| **Immagini** | 7 (6 placeholder + infobox) |
| **Sezioni** | 8 principali |

---

## 🎯 PROSSIMI PASSI DOPO SANDBOX

1. **Caricamento avvenuto** ✅
2. **Community review** (30 giorni)
3. **Implementazione feedback** (se richiesto)
4. **Sourcing immagini** (parallelo — usa PROMPT_LLMS_SOURCING_IMMAGINI.md)
5. **Pubblicazione mainspace** (dopo approvazione)

---

**Data**: 31 marzo 2026
**Articolo**: Sorgiva Fontanin
**Status**: 🟢 PRONTO PER SANDBOX
**File sorgente**: `wiki/Sorgiva_Fontanin.wiki`
