from scripts.db_utils import get_db_connection

def detailed_audit():
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor(dictionary=True)
    
    ids = ['@I35@', '@I104@', '@I116@', '@I30@', '@I39@'] # Antonino, Luigi Gerardo, Diego, Paolo, Giulio Antonio
    query = "SELECT person_id, given_name, surname, full_name, birth_date, death_date, notes FROM PERSON WHERE person_id IN (%s)" % ",".join(["%s"]*len(ids))
    
    cursor.execute(query, ids)
    rows = cursor.fetchall()
    
    print("--- DETTAGLIO SOGGETTI CRITICI ---")
    for r in rows:
        print(f"ID: {r['person_id']} | Nome: {r['full_name']}")
        print(f"  Nascita: {r['birth_date']} | Morte: {r['death_date']}")
        print(f"  Note: {r['notes'][:150] if r['notes'] else 'Nessuna nota'}")
        print("-" * 50)

    conn.close()

if __name__ == "__main__":
    detailed_audit()
