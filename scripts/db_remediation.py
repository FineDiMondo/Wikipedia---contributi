from scripts.db_utils import get_db_connection

def remediate():
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor(dictionary=True)
    
    print("--- 1. RICERCA SOGGETTI MANCANTI ---")
    query = "SELECT person_id, full_name, birth_date FROM PERSON WHERE surname LIKE 'Giardina%' AND (given_name LIKE 'Paolo%' OR given_name LIKE 'Giulio%')"
    cursor.execute(query)
    for r in cursor.fetchall():
        print(f"ID: {r['person_id']} | Nome: {r['full_name']} | Nascita: {r['birth_date']}")
    
    print("\n--- 2. BONIFICA LUIGI GERARDO (@I104@) ---")
    # Spostiamo 1738 da nascita a morte
    update_query = "UPDATE PERSON SET birth_date = NULL, death_date = '1738-08-28', notes = 'Rettifica: 1738 e data di morte, non nascita' WHERE person_id = '@I104@'"
    cursor.execute(update_query)
    
    conn.commit()
    print("Operazione completata con successo.")
    conn.close()

if __name__ == "__main__":
    remediate()
