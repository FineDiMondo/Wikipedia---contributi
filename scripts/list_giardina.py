from scripts.db_utils import get_db_connection

def list_giardina():
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor(dictionary=True)
    
    print("--- TUTTI I GIARDINA ---")
    cursor.execute("SELECT person_id, given_name, full_name, birth_date FROM PERSON WHERE surname LIKE '%Giardina%'")
    for r in cursor.fetchall():
        print(f"ID: {r['person_id']} | Nome: {r['full_name']} | Nascita: {r['birth_date']}")
    
    conn.close()

if __name__ == "__main__":
    list_giardina()
