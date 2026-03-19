# Workflow Operativo: Recupero Asset da Gallica (BnF)

Questo documento definisce la procedura per la ricerca, l'estrazione e il caricamento su Wikimedia Commons di materiali in Pubblico Dominio (PD) relativi alla Famiglia Giardina, conservati presso la Bibliothèque nationale de France (Gallica).

## 🎯 Obiettivi
- Arricchire le voci Wikipedia con iconografia originale (manoscritti, armoriali, mappe).
- Garantire la massima qualità documentale attingendo a fonti primarie internazionali.
- Assicurare la conformità legale (Copyright/Public Domain).

## 🛠️ Procedura End-to-End

### 1. Ricerca e Identificazione (Filtering)
Utilizzare il motore di ricerca di [Gallica](https://gallica.bnf.fr) con le seguenti chiavi di ricerca:
- `Giardina Sicile`
- `Santa Ninfa Sicile`
- `Ficarazzi Sicile`
- `Noblesse Sicilienne armorial`

### 2. Validazione Legale (Compliance)
Prima dello scarico, verificare che l'asset sia:
- **Pubblico Dominio**: Verificare la data di pubblicazione o il decesso dell'autore (+70 anni).
- **Licenza Gallica**: Identificare la dicitura "Utilisation commerciale non commerciale" o "Domaine Public".

### 3. Estrazione e Raffinamento (Processing)
- Scaricare l'immagine nel formato massimo disponibile (TIFF o JPG alta qualità).
- Rinominare il file secondo la nomenclatura del progetto: `Gallica_Giardina_[Descrizione]_[Anno].jpg`.
- Eseguire eventuale ritaglio (crop) se l'immagine fa parte di una pagina di testo più ampia.

### 4. Caricamento su Wikimedia Commons (Upload)
Utilizzare lo script `scripts/commons_upload.py` con i seguenti parametri:
- **Source**: `Gallica.bnf.fr / Bibliothèque nationale de France`.
- **License**: `{{PD-old-70}}` o `{{PD-Italy}}`.
- **Category**: `Heraldry of the Giardina family` o `Maps of Sicily`.

## 📊 Registro Tracking Asset (Gallica Stream)

| ID Gallica (ark) | Descrizione Asset | Stato | Target Wiki | Note |
| :--- | :--- | :--- | :--- | :--- |
| `ark:/12148/btv1b53011566x` | **Carta del Regno di Sicilia (Magini, 1620)** | **IN ATTESA DOWNLOAD** | Famiglia Giardina (Incipit) | Mappa coeva alla fondazione di Santa Ninfa (1609). |
| `ark:/12148/bpt6k111461z` | **Dizionario Storico-Araldico (Sicile)** | **ANALIZZATO** | Araldica | Contiene descrizione variante messinese (leone d'oro). |
| `ark:/12148/bpt6k6521142j` | **L'Italie (Ettore Janni, 1915)** | **ANALIZZATO** | Geografia | Citazione Monte Castrone e Santa Ninfa. |
| `ark:/12148/bpt6k64562424` | **Guida per Palermo (Gaspare Palermo)** | **IN RICERCA** | Patrimonio | Descrizione originale Palazzo Castrone-Santa Ninfa. |
| `ark:/12148/btv1b100249410` | **Armorial manuscrit (BnF)** | **IN RICERCA** | Araldica | Cercare miniatura stemma Giardina (XV-XVI sec). |

---
*Riferimento Documento Compass: artifact_wf-c022c709-3be6-4d94-b5aa-5d9abf7cb377*
