from scripts.db_utils import get_db_connection

def audit():
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor(dictionary=True)
    
    # 1. Carichiamo tutte le persone
    cursor.execute("SELECT person_id, full_name, birth_date FROM PERSON")
    persons = {p['person_id']: p for p in cursor.fetchall()}
    
    # 2. Carichiamo le famiglie (chi è il padre di ogni famiglia)
    cursor.execute("SELECT family_id, husband_id FROM FAMILY")
    families = {f['family_id']: f['husband_id'] for f in cursor.fetchall()}
    
    # 3. Carichiamo i link figli-famiglia
    cursor.execute("SELECT family_id, child_id FROM FAMILY_LINK")
    child_to_family = {l['child_id']: l['family_id'] for l in cursor.fetchall()}
    
    print("--- ANALISI LINEA PATRILINEARE (VIA FAMILY LINKS) ---")
    
    # Cerchiamo i Giardina
    giardina_ids = [pid for pid, p in persons.items() if "Giardina" in p['full_name']]
    
    for pid in giardina_ids:
        line = []
        curr_id = pid
        while curr_id in persons:
            line.append(persons[curr_id])
            # Troviamo la famiglia di origine del soggetto
            fam_id = child_to_family.get(curr_id)
            if fam_id and fam_id in families:
                # Il padre del soggetto è il marito della sua famiglia di origine
                curr_id = families[fam_id]
            else:
                break
        
        if len(line) >= 3:
            path = " -> ".join([f"{x['full_name']} ({x['birth_date'] or '?'})" for x in reversed(line)])
            print(f"LINEA: {path}")

    conn.close()

if __name__ == "__main__":
    audit()
