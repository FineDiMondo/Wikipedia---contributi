from scripts.db_utils import get_db_connection

def import_data():
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor()
    
    # subjects: id, given, surname, full, sex, birth, birth_q, death, death_q, desc
    # Usiamo 'A' per ABOUT per evitare truncating
    subjects = [
        ('@I501@', 'Pietro', 'Giardina', 'Pietro /Giardina/', 'M', '1500-01-01', 'A', None, None, 'Capostipite ramo palermitano (c. 1500)'),
        ('@I502@', 'Luigi', 'Giardina', 'Luigi /Giardina/', 'M', '1530-01-01', 'A', None, None, 'Figlio di Pietro, sposo Corvino (c. 1530)'),
        ('@I503@', 'Franco', 'Giardina', 'Franco /Giardina senior/', 'M', '1921-01-01', None, '1943-09-12', None, 'Vittima eccidio Arcole, Laurea ad honorem'),
        ('@I504@', 'Giuseppe', 'Giardina', 'Giuseppe /Giardina/', 'M', None, None, None, None, 'Avvocato Ferrovie dello Stato, padre di Franco e Marco'),
        ('@I505@', 'Luigi Arias', 'Giardina', 'Luigi Arias /Giardina/', 'M', '1580-01-01', 'A', '1627-05-02', None, 'I Marchese di Santa Ninfa (c. 1580-1627)')
    ]
    
    query = """
    INSERT INTO PERSON (person_id, given_name, surname, full_name, sex, birth_date, birth_qualifier, death_date, death_qualifier, description) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE 
        birth_date = VALUES(birth_date),
        birth_qualifier = VALUES(birth_qualifier),
        death_date = VALUES(death_date),
        death_qualifier = VALUES(death_qualifier),
        description = VALUES(description)
    """
    
    for s in subjects:
        cursor.execute(query, s)
    
    conn.commit()
    print("Sincronizzazione DB completata con successo (Schema Optimized).")
    conn.close()

if __name__ == "__main__":
    import_data()
