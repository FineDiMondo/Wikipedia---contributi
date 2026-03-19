from scripts.db_utils import get_db_connection

def normalize():
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor(dictionary=True)
    
    # 1. Cerchiamo il record
    query_find = "SELECT person_id, given_name, full_name FROM PERSON WHERE given_name LIKE 'Eumilia%' AND surname LIKE 'Grimaldi%'"
    cursor.execute(query_find)
    results = cursor.fetchall()
    
    if not results:
        print("Nessun record trovato per 'Eumilia Grimaldi'.")
        conn.close()
        return

    for res in results:
        pid = res['person_id']
        old_fn = res['full_name']
        new_gn = res['given_name'].replace('Eumilia', 'Emilia')
        new_fn = res['full_name'].replace('Eumilia', 'Emilia')
        
        # 2. Eseguiamo l'update
        query_update = "UPDATE PERSON SET given_name = %s, full_name = %s WHERE person_id = %s"
        cursor.execute(query_update, (new_gn, new_fn, pid))
        print(f"Normalizzato ID {pid}: {old_fn} -> {new_fn}")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    normalize()
