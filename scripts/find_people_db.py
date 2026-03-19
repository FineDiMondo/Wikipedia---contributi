from scripts.db_utils import get_db_connection

def find_people():
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor(dictionary=True)
    
    names = ['Simone%', 'Gaetano%']
    print("--- RICERCA PERSONE ---")
    for name in names:
        cursor.execute("SELECT person_id, given_name, full_name, birth_date FROM PERSON WHERE given_name LIKE %s", (name,))
        for r in cursor.fetchall():
            print(f"ID: {r['person_id']} | Nome: {r['full_name']} | Nascita: {r['birth_date']}")
    
    conn.close()

if __name__ == "__main__":
    find_people()
