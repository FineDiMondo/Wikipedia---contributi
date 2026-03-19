from scripts.db_utils import get_db_connection

def setup_core_schema():
    conn = get_db_connection('db_giardina_core')
    if not conn: return
    cursor = conn.cursor()
    
    # 1. Tabelle Anagrafiche
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PERSON (
        person_id VARCHAR(50) PRIMARY KEY,
        given_name VARCHAR(255),
        surname VARCHAR(255),
        full_name VARCHAR(255),
        sex ENUM('M', 'F', 'U'),
        birth_date DATE,
        birth_qualifier VARCHAR(10),
        death_date DATE,
        death_qualifier VARCHAR(10),
        description TEXT,
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB;
    """)

    # 2. Tabelle Fonti e Citazioni
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SOURCE (
        source_id INT PRIMARY KEY,
        source_type VARCHAR(50),
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255),
        repository VARCHAR(255),
        publication_date VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB;
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS EVENT (
        event_id INT PRIMARY KEY,
        event_type VARCHAR(50),
        event_date DATE,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB;
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CITATION (
        citation_id INT PRIMARY KEY,
        source_id INT,
        person_id VARCHAR(50),
        event_id INT,
        page_number VARCHAR(100),
        notes TEXT,
        FOREIGN KEY (source_id) REFERENCES SOURCE(source_id),
        FOREIGN KEY (person_id) REFERENCES PERSON(person_id),
        FOREIGN KEY (event_id) REFERENCES EVENT(event_id)
    ) ENGINE=InnoDB;
    """)

    # 3. Tabelle Relazionali (Mancanti nel turno precedente)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PERSON_EVENT (
        person_event_id INT AUTO_INCREMENT PRIMARY KEY,
        person_id VARCHAR(50),
        event_id INT,
        role VARCHAR(50),
        FOREIGN KEY (person_id) REFERENCES PERSON(person_id),
        FOREIGN KEY (event_id) REFERENCES EVENT(event_id)
    ) ENGINE=InnoDB;
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS FAMILY (
        family_id VARCHAR(50) PRIMARY KEY,
        husband_id VARCHAR(50),
        wife_id VARCHAR(50),
        marriage_date DATE,
        notes TEXT,
        FOREIGN KEY (husband_id) REFERENCES PERSON(person_id),
        FOREIGN KEY (wife_id) REFERENCES PERSON(person_id)
    ) ENGINE=InnoDB;
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS FAMILY_LINK (
        link_id INT AUTO_INCREMENT PRIMARY KEY,
        family_id VARCHAR(50),
        child_id VARCHAR(50),
        FOREIGN KEY (family_id) REFERENCES FAMILY(family_id),
        FOREIGN KEY (child_id) REFERENCES PERSON(person_id)
    ) ENGINE=InnoDB;
    """)

    # 4. Tabelle Titoli
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS TITLE (
        title_id INT PRIMARY KEY,
        title_name VARCHAR(255) NOT NULL,
        rank VARCHAR(50),
        description TEXT
    ) ENGINE=InnoDB;
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS TITLE_ASSIGNMENT (
        assignment_id INT PRIMARY KEY,
        person_id VARCHAR(50),
        title_id INT,
        acquisition_date DATE,
        source_id INT,
        notes TEXT,
        FOREIGN KEY (person_id) REFERENCES PERSON(person_id),
        FOREIGN KEY (title_id) REFERENCES TITLE(title_id),
        FOREIGN KEY (source_id) REFERENCES SOURCE(source_id)
    ) ENGINE=InnoDB;
    """)

    conn.commit()
    print("Schema Core COMPLETO creato con successo.")
    conn.close()

if __name__ == "__main__":
    setup_core_schema()
