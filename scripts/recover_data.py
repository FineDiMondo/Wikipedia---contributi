import json
from scripts.db_utils import get_db_connection

def recover_data():
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor()
    
    # 1. Caricamento file JSON
    with open("ricerca/stato_progetto.json", "r", encoding="utf-8") as f:
        stato = json.load(f)
    with open("ricerca/registro_soggetti.json", "r", encoding="utf-8") as f:
        registro = json.load(f)
        
    # 2. Ripopolamento MGMT_PROJECT
    print("Ripristino Progetto...")
    cursor.execute("INSERT INTO MGMT_PROJECT (name, description, status) VALUES (%s, %s, 'ACTIVE')", 
                   (stato['progetto'], "Ripristinato da backup JSON dopo perdita DB"))
    project_id = cursor.lastrowid
    
    # 3. Ripopolamento MGMT_SUBJECT
    print("Ripristino Soggetti...")
    sub_query = """
    INSERT INTO MGMT_SUBJECT (subject_id, project_id, title, track, status, gate, priority, evidence_strength)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    for sub in registro['subjects']:
        cursor.execute(sub_query, (
            sub['id'], project_id, sub['title'], sub['track'], sub['status'], 
            sub['publishability'], sub['priority'], sub['evidence_strength']
        ))
        
    # 4. Log dell'operazione
    print("Logging Recovery...")
    cursor.execute("INSERT INTO MGMT_GOVERNANCE_LOG (subject_id, action, agent_type) VALUES (%s, %s, %s)",
                   ('famiglia_giardina', 'DISASTER_RECOVERY_COMPLETED', 'AI_CONSULTANT'))
    
    conn.commit()
    print(f"Recupero completato. Progetto ID: {project_id}, Soggetti: {len(registro['subjects'])}")
    conn.close()

if __name__ == "__main__":
    recover_data()
