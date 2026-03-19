from scripts.db_utils import get_db_connection

def insert_offices():
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor()
    
    # 1. Inserimento Nuove Fonti
    sources = [
        (1005, 'BOOK', 'Il blasone in Sicilia ossia raccolta araldica', 'Vincenzo Palizzolo Gravina', 'Palermo', '1871-1875'),
        (1006, 'BOOK', 'Servizio, lealta, onore. I cavalieri "italiani" degli Ordini militari spagnoli', 'Davide Balestra', 'Roma', '2024'),
        (1007, 'BOOK', 'Ordine con cui intervennero li tre bracci nel Parlamento celebrato in Messina nel mese di marzo 1639', 'Alberico Lo Faso di Serradifalco', 'Palermo', '2023'),
        (1008, 'BOOK', 'Sicilia 1812. Laboratorio costituzionale', 'Pierfrancesco Palazzotto', 'Palermo', '2012'),
        (1009, 'WEB', 'Dizionario Biografico degli Italiani (voce Antonino Mongitore)', 'Nicoletta Bazzano', 'Treccani', '2011')
    ]
    
    source_query = "INSERT IGNORE INTO SOURCE (source_id, source_type, title, author, repository, publication_date) VALUES (%s, %s, %s, %s, %s, %s)"
    for s in sources:
        cursor.execute(source_query, s)
    
    # 2. Inserimento Nuove Persone
    people = [
        ('@I506@', 'Simone', 'Giardina', 'Simone /Giardina/', 'M', 'Figlio di Luigi Arias, linea Bellacera'),
        ('@I507@', 'Simone', 'Giardina Bellacera', 'Simone /Giardina Bellacera/', 'M', 'Capitano giustiziere e Cavaliere di Santiago'),
        ('@I508@', 'Gaetano', 'Giardina', 'Gaetano /Giardina/', 'M', 'Cofondatore Accademia dei Geniali (1719)')
    ]
    
    person_query = "INSERT IGNORE INTO PERSON (person_id, given_name, surname, full_name, sex, description) VALUES (%s, %s, %s, %s, %s, %s)"
    for p in people:
        cursor.execute(person_query, p)
        
    # 3. Inserimento Cariche (come EVENT + PERSON_EVENT)
    # person_id, event_type, date, description, source_id
    events = [
        ('@I505@', 'OFFICE', '1627-01-01', 'Governatore del Monte di Pieta di Palermo', 1005),
        ('@I506@', 'OFFICE', '1632-01-01', 'Governatore della Compagnia della Carita di Palermo', 1005),
        ('@I507@', 'OFFICE', '1667-01-01', 'Governatore della Compagnia della Pace di Palermo', 1005),
        ('@I507@', 'OFFICE', '1670-01-01', 'Capitano giustiziere di Palermo', 1005),
        ('@I507@', 'OFFICE', '1671-01-01', 'Cavaliere dell\'Ordine di Santiago', 1006),
        ('@I104@', 'OFFICE', '1733-01-01', 'Governatore della Compagnia della Pace di Palermo', 1005),
        ('@I116@', 'OFFICE', '1748-01-01', 'Capitano giustiziere di Palermo', 1005),
        ('@I508@', 'CULTURAL', '1719-01-01', 'Cofondatore Accademia dei Geniali', 1009)
    ]
    
    event_query = "INSERT IGNORE INTO EVENT (event_id, event_type, event_date, description) VALUES (%s, %s, %s, %s)"
    pe_query = "INSERT IGNORE INTO PERSON_EVENT (person_id, event_id, role) VALUES (%s, %s, %s)"
    cite_query = "INSERT IGNORE INTO CITATION (citation_id, source_id, event_id) VALUES (%s, %s, %s)"
    
    for i, e in enumerate(events):
        ev_id = 4001 + i
        cursor.execute(event_query, (ev_id, e[1], e[2], e[3]))
        cursor.execute(pe_query, (e[0], ev_id, 'PRINCIPAL'))
        cursor.execute(cite_query, (5001 + i, e[4], ev_id))

    conn.commit()
    print("Aggiornamento cariche e ruoli istituzionali completato correttamente.")
    conn.close()

if __name__ == "__main__":
    insert_offices()
