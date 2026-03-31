# 🚀 Setup Gemini per Sorgiva Fontanin

## 📁 File preparati

Ho creato **3 file pronti per l'uso** nella cartella `dossier/`:

| File | Uso | Formato |
|------|-----|---------|
| **Sorgiva_Fontanin_PROMPT_STUDIO.txt** | 🎯 **QUESTO** — Copia-incolla diretto in Google AI Studio | TXT (Plain text) |
| **Sorgiva_Fontanin_PROMPT_GEMINI.md** | Documentazione strutturata per referenza | Markdown |
| **Sorgiva_Fontanin_PAYLOAD_API_GEMINI.json** | Integrazione API Gemini (avanzato) | JSON |

---

## 🎯 ISTRUZIONI VELOCI

### **Opzione A: Google AI Studio (consigliato per principianti)**

1. Apri: https://aistudio.google.com/app/apikey
2. Crea una **nuova chat** (+ New chat)
3. **Copia-incolla integralmente il contenuto di** `Sorgiva_Fontanin_PROMPT_STUDIO.txt`
4. Premi **Send** o **Invio**
5. Aspetta il rapporto di Gemini (2-3 minuti)
6. **Copia il risultato** e salvalo in `dossier/REPORT_GEMINI_FONTANIN.md`

### **Opzione B: API Gemini (avanzato)**

```bash
# Richiede Google Cloud SDK e API key configurata
curl -X POST https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent \
  -H "Content-Type: application/json" \
  -d @dossier/Sorgiva_Fontanin_PAYLOAD_API_GEMINI.json
```

### **Opzione C: Python SDK**

```python
import google.generativeai as genai

# Configura API key
genai.configure(api_key="YOUR_API_KEY")

# Leggi il prompt
with open("dossier/Sorgiva_Fontanin_PROMPT_STUDIO.txt", "r") as f:
    prompt = f.read()

# Chiama Gemini
model = genai.GenerativeModel("gemini-1.5-pro")
response = model.generate_content(prompt)

# Salva il risultato
with open("dossier/REPORT_GEMINI_FONTANIN.md", "w") as f:
    f.write(response.text)

print("✅ Rapporto salvato in dossier/REPORT_GEMINI_FONTANIN.md")
```

---

## 📋 Cosa farà Gemini

Gemini analizzerà la bozza e genererà un **rapporto strutturato** con:

✅ **Verdetto di ammissibilità** (GO / NO-GO / CONDITIONAL GO)
✅ **Valutazione dei 4 criteri Wikipedia** (Notorietà, Verifiabilità, Neutralità, Fonti indipendenti)
✅ **Lacune critiche** (cosa manca)
✅ **Punti di forza** (cosa funziona bene)
✅ **Raccomandazioni di miglioramento** (con priorità)
✅ **Checklist pre-carico** (verifiche finali)
✅ **Istruzioni di carico in sandbox** (URL, metodo, edit summary)
✅ **Prossimi passi** (come procedere dopo)

---

## 📊 Timeline atteso

| Fase | Durata | Azione |
|------|--------|--------|
| 1. Caricamento prompt | 1 min | Copia-incolla in Google AI Studio |
| 2. Elaborazione Gemini | 2-3 min | Gemini analizza la bozza |
| 3. Ricezione rapporto | Istantaneo | Risultato visibile in chat |
| 4. Salvataggio locale | 1 min | Copia → dossier/REPORT_GEMINI_FONTANIN.md |
| 5. Revisione rapporto | 10-15 min | Leggi raccomandazioni |
| 6. Implementazione migliorie (opzionale) | 30-60 min | Aggiorna wikitesto basato su feedback |
| 7. Carico in sandbox Wikipedia | 5 min | Copia wikitesto → Utente:Daniel_Giardina/Sandbox |

**⏱️ Totale (senza migliorie)**: ~7 minuti
**⏱️ Totale (con migliorie)**: ~1-1,5 ore

---

## 🔑 Punti chiave

### Cosa NON deve fare Gemini
- ❌ Modificare il testo wikitesto (solo analizzarlo)
- ❌ Creare una nuova voce da zero (è già pronta)
- ❌ Aggiungere sezioni interne senza essere richiesto
- ❌ Giudicare con tono non-neutrale

### Cosa DEVE fare Gemini
- ✅ Valutare ammissibilità secondo criteri Wikipedia
- ✅ Identificare lacune documentali
- ✅ Suggerire miglioramenti con priorità
- ✅ Fornire istruzioni concrete di carico
- ✅ Mantener tono professionale e supportivo

---

## 📖 Lettura consigliata dopo il rapporto

Dopo aver ricevuto il rapporto da Gemini:

1. **Esamina il verdetto complessivo** → È GO/NO-GO/CONDITIONAL?
2. **Se CONDITIONAL GO**: Esamina le condizioni e se sono facili da soddisfare
3. **Se NO-GO**: Leggi le lacune critiche; potrebbe non essere ancora pronta
4. **Se GO**: Procedi direttamente al carico in sandbox
5. **In tutti i casi**: Leggi le "Raccomandazioni di miglioramento" — sono opzionali ma utili

---

## 🚀 Dopo il rapporto di Gemini

Se il verdetto è **GO** o **CONDITIONAL GO**:

1. **Carica in sandbox**:
   - URL: https://it.wikipedia.org/wiki/Utente:Daniel_Giardina/Sandbox
   - Metodo: Modifica → Cancella → Incolla → Salva

2. **Richiedi revisione comunitaria**:
   - Progetto:Veneto
   - Progetto:Biologia marina
   - Edit summary: "Bozza voce Sorgiva Fontanin — validata, pronta revisione"

3. **Aspetta feedback** (30 giorni standard)

4. **Aggiorna iterativamente** basato su critiche

5. **Pubblica in mainspace** quando comunità approva

---

## 🆘 Troubleshooting

### Gemini risponde in inglese?
→ Ripeti il prompt in modo esplicito: "Rispondi in italiano"

### Gemini chiede di modificare il testo?
→ Rispondi: "No, solo analizzare e generar rapporto, non modificare"

### Gemini non genera un rapporto strutturato?
→ Copia-incolla il prompt **esattamente come è**, inclusa la sezione "OUTPUT RICHIESTO"

### Rapporto troppo lungo?
→ Chiedi: "Fornisci solo il verdetto complessivo e le 5 raccomandazioni principali"

---

## 📞 Supporto

- Domande su **Wikipedia**: Vedi `docs/riferimenti/riferimenti-wikipedia.md`
- Domande su **validazione locale**: Vedi `scripts/validate_wikitesto.py --help`
- Domande su **Gemini API**: Vedi https://ai.google.dev/docs

---

## ✅ Checklist finale

Prima di usare il prompt:

- [ ] Ho letto questo file README
- [ ] So quale opzione scegliere (A, B, o C)
- [ ] Ho accesso a Google AI Studio O API key Gemini
- [ ] Ho il file `Sorgiva_Fontanin_PROMPT_STUDIO.txt` pronto
- [ ] So dove salvare il rapporto (`dossier/REPORT_GEMINI_FONTANIN.md`)
- [ ] Comprendo i 4 criteri di ammissibilità Wikipedia
- [ ] So come interpretare il verdetto (GO/NO-GO/CONDITIONAL)

---

**🎯 Pronto? Vai all'Opzione A o B qui sopra e inizia!**

---

Data: 31 marzo 2026
Autore: Claude Code | Daniel Giardina (user)
Status: 🟢 Operativo
