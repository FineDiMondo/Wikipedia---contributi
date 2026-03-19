import json
from scripts.db_utils import get_db_connection

def alignment_audit():
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor(dictionary=True)
    
    # 1. Caricamento Dati JSON
    with open("ricerca/stato_progetto.json", "r", encoding="utf-8") as f:
        stato_json = json.load(f)
    with open("ricerca/registro_soggetti.json", "r", encoding="utf-8") as f:
        registro_json = json.load(f)
    
    # 2. Caricamento Dati DB
    cursor.execute("SELECT * FROM project_config")
    db_config = cursor.fetchone()
    
    cursor.execute("SELECT * FROM subjects")
    db_subjects = {s['subject_id']: s for s in cursor.fetchall()}
    
    print("═══ REPORT ALLINEAMENTO DB vs JSON ═══\n")
    
    # --- PROGETTO ---
    print("--- CONFIGURAZIONE PROGETTO ---")
    json_proj = stato_json['progetto']
    db_proj = db_config['progetto_nome']
    if json_proj == db_proj:
        print(f"✅ Nome Progetto: {json_proj}")
    else:
        print(f"❌ Discrepanza Nome: JSON='{json_proj}' vs DB='{db_proj}'")
    
    # --- SOGGETTI ---
    print("\n--- STATO SOGGETTI ---")
    # Prendiamo i soggetti dal registro JSON
    for js in registro_json['subjects']:
        sid = js['id']
        print(f"Soggetto: {sid}")
        if sid in db_subjects:
            ds = db_subjects[sid]
            # Confronto stato
            if js['status'] == ds['stato']:
                print(f"  ✅ Stato: {js['status']}")
            else:
                print(f"  ❌ Discrepanza Stato: JSON='{js['status']}' vs DB='{ds['stato']}'")
            
            # Confronto evidenze
            if js['evidence_strength'] == ds['forza_evidenze']:
                print(f"  ✅ Evidenze: {js['evidence_strength']}")
            else:
                print(f"  ❌ Discrepanza Evidenze: JSON='{js['evidence_strength']}' vs DB='{ds['forza_evidenze']}'")
        else:
            print(f"  ❌ Soggetto '{sid}' non trovato nel Database.")

    conn.close()

if __name__ == "__main__":
    alignment_audit()
