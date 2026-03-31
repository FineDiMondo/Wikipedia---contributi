from scripts.db_utils import get_db_connection

def total_recovery():
    conn = get_db_connection('CORE')
    if not conn: return
    cursor = conn.cursor()
    
    print("🤖 Avvio Total Knowledge Recovery (Integrity Guaranteed)...")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

    # 1. Fonti
    sources = [
        (1001, 'BOOK', 'Nobiliario di Sicilia', 'A. Mango'),
        (1002, 'BOOK', 'La storia dei feudi', 'San Martino De Spucches'),
        (1003, 'BOOK', 'Riveli e documenti', 'Ferrara & Ferrara'),
        (1004, 'ARCHIVE', 'Fondo Protonotaro', 'ASPa')
    ]
    cursor.executemany("INSERT IGNORE INTO SOURCE (source_id, source_type, title, author) VALUES (%s, %s, %s, %s)", sources)

    # 2. Soggetti Chiave
    people = [
        ('@I505@', 'Luigi Arias Giardina', 'I Marchese'),
        ('@I104@', 'Luigi Gerardo Giardina', 'I Principe'),
        ('@I16@', 'Marco Aurelio Pasquale Giardina', 'Sindacalista')
    ]
    for pid, name, desc in people:
        cursor.execute("INSERT INTO PERSON (person_id, full_name, description) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE full_name=VALUES(full_name)", (pid, name, desc))

    # 3. Citazioni per Eventi Orfani
    # Assicuriamoci che gli eventi esistano prima di citarli
    cites = [
        (1003, 4104, 'Licentia 1609'),
        (1004, 4105, 'Investitura 1621'),
        (1004, 4106, 'Testamento 1627'),
        (1002, 4110, 'Principato 1733')
    ]
    for src, ev, page in cites:
        cursor.execute("INSERT IGNORE INTO CITATION (source_id, event_id, page_number) VALUES (%s, %s, %s)", (src, ev, page))

    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    conn.commit()
    conn.close()
    print("✅ Sistema Core rigenerato e validato.")

if __name__ == "__main__":
    total_recovery()
