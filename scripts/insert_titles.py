from scripts.db_utils import get_db_connection

def insert_titles():
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor()
    
    # 1. Inserimento Titoli
    titles = [
        (1, 'Marchese di Santa Ninfa', 'Marchese', 'Titolo istituito nel 1621'),
        (2, 'Principe di Ficarazzi', 'Principe', 'Titolo istituito nel 1733'),
        (3, 'Barone di Santa Ninfa', 'Barone', 'Acquisito nel 1615')
    ]
    
    title_query = "INSERT IGNORE INTO TITLE (title_id, title_name, rank, description) VALUES (%s, %s, %s, %s)"
    for t in titles:
        cursor.execute(title_query, t)
    
    # 2. Assegnazione Titoli
    # person_id, title_id, date, source_id, notes
    assignments = [
        ('@I505@', 3, '1615-01-01', 1005, 'Primo acquirente'),
        ('@I505@', 1, '1621-01-01', 1005, 'Primo marchese'),
        ('@I104@', 1, '1703-01-01', 1005, 'Investitura dopo lite successoria'),
        ('@I104@', 2, '1733-01-01', 1005, 'Elevazione a principato'),
        ('@I116@', 2, '1739-01-01', 1005, 'Successione principesca')
    ]
    
    assign_query = "INSERT IGNORE INTO TITLE_ASSIGNMENT (assignment_id, person_id, title_id, acquisition_date, source_id, notes) VALUES (%s, %s, %s, %s, %s, %s)"
    for i, a in enumerate(assignments):
        cursor.execute(assign_query, (6001 + i, a[0], a[1], a[2], a[3], a[4]))
        
    # 3. Presenze Parlamentari (come EVENT)
    parl_events = [
        ('@I506@', 'PARLIAMENT', '1639-03-01', 'Intervento nel Parlamento di Messina (Braccio militare)', 1007),
        ('@I35@', 'PARLIAMENT', '1813-01-01', 'Presenza Camera dei Pari (rappresentato per procura)', 1008)
    ]
    
    event_query = "INSERT IGNORE INTO EVENT (event_id, event_type, event_date, description) VALUES (%s, %s, %s, %s)"
    pe_query = "INSERT IGNORE INTO PERSON_EVENT (person_id, event_id, role) VALUES (%s, %s, %s)"
    cite_query = "INSERT IGNORE INTO CITATION (citation_id, source_id, event_id) VALUES (%s, %s, %s)"
    
    for i, e in enumerate(parl_events):
        ev_id = 4101 + i
        cursor.execute(event_query, (ev_id, e[1], e[2], e[3]))
        cursor.execute(pe_query, (e[0], ev_id, 'REPRESENTATIVE'))
        cursor.execute(cite_query, (5101 + i, e[4], ev_id))

    conn.commit()
    print("Aggiornamento titoli e presenze parlamentari completato.")
    conn.close()

if __name__ == "__main__":
    insert_titles()
