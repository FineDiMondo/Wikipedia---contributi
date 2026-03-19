from scripts.db_utils import get_db_connection

def db_delta_audit():
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor(dictionary=True)
    
    print("--- 1. ULTIME MODIFICHE PERSON (BY CREATED_AT) ---")
    cursor.execute("SELECT person_id, full_name, created_at FROM PERSON ORDER BY created_at DESC LIMIT 15")
    for r in cursor.fetchall():
        print(f"ID: {r['person_id']} | Nome: {r['full_name']} | Data: {r['created_at']}")

    print("\n--- 2. ULTIME MODIFICHE PERSON (BY UPDATED_AT) ---")
    cursor.execute("SELECT person_id, full_name, updated_at FROM PERSON ORDER BY updated_at DESC LIMIT 15")
    for r in cursor.fetchall():
        print(f"ID: {r['person_id']} | Nome: {r['full_name']} | Data: {r['updated_at']}")

    print("\n--- 3. NUOVI EVENTI (OFFICES/TITLES) ---")
    cursor.execute("SELECT event_id, event_type, description, created_at FROM EVENT ORDER BY created_at DESC LIMIT 10")
    for r in cursor.fetchall():
        print(f"EV_ID: {r['event_id']} | Tipo: {r['event_type']} | Desc: {r['description']} | Data: {r['created_at']}")

    conn.close()

if __name__ == "__main__":
    db_delta_audit()
