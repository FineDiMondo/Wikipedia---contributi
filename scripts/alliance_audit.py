from scripts.db_utils import get_db_connection

def alliance_audit():
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor(dictionary=True)
    
    # IDs dei soggetti chiave
    ids = ('@I35@', '@I57@', '@I73@', '@I104@', '@I116@')
    
    query = """
    SELECT p.full_name as figlio, m.full_name as madre 
    FROM PERSON p 
    JOIN FAMILY_LINK fl ON p.person_id = fl.child_id
    JOIN FAMILY f ON fl.family_id = f.family_id
    JOIN PERSON m ON f.wife_id = m.person_id
    WHERE p.person_id IN (%s)
    """ % ",".join(["%s"]*len(ids))
    
    cursor.execute(query, ids)
    rows = cursor.fetchall()
    
    print("--- VERIFICA ALLEANZE MATRIMONIALI (DB vs WIKI) ---")
    for r in rows:
        print(f"Figlio: {r['figlio']:<35} | Madre: {r['madre']}")

    conn.close()

if __name__ == "__main__":
    alliance_audit()
