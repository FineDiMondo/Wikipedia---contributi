from scripts.db_utils import get_db_connection

def setup_mgmt():
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor()
    
    # 1. Tabella PROGETTI
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS MGMT_PROJECT (
        project_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        description TEXT,
        status ENUM('ACTIVE', 'PARKED', 'COMPLETED') DEFAULT 'ACTIVE',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB;
    """)

    # 2. Tabella SOGGETTI (Agganciata ai progetti)
    # Usiamo VARCHAR per subject_id per allinearci agli ID del registro (es. famiglia_giardina)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS MGMT_SUBJECT (
        subject_id VARCHAR(50) PRIMARY KEY,
        project_id INT,
        title VARCHAR(255) NOT NULL,
        track ENUM('publishing_track', 'knowledge_graph') NOT NULL,
        status ENUM('candidate', 'researching', 'sourced', 'publishable', 'sandboxed', 'published', 'parked') DEFAULT 'candidate',
        gate ENUM('do_not_publish', 'sandbox_only', 'candidate_for_review', 'published') DEFAULT 'do_not_publish',
        priority ENUM('high', 'medium', 'low') DEFAULT 'medium',
        evidence_strength ENUM('weak', 'mixed', 'strong') DEFAULT 'weak',
        last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (project_id) REFERENCES MGMT_PROJECT(project_id)
    ) ENGINE=InnoDB;
    """)

    # 3. Tabella TASK (Backlog)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS MGMT_TASK (
        task_id INT AUTO_INCREMENT PRIMARY KEY,
        subject_id VARCHAR(50),
        description TEXT NOT NULL,
        area VARCHAR(50),
        priority ENUM('RED', 'YELLOW', 'GREEN') DEFAULT 'YELLOW',
        status ENUM('PENDING', 'IN_PROGRESS', 'COMPLETED', 'CANCELLED') DEFAULT 'PENDING',
        reference_file VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (subject_id) REFERENCES MGMT_SUBJECT(subject_id)
    ) ENGINE=InnoDB;
    """)

    # 4. Tabella GOVERNANCE LOG (Audit Trail)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS MGMT_GOVERNANCE_LOG (
        log_id INT AUTO_INCREMENT PRIMARY KEY,
        subject_id VARCHAR(50),
        action VARCHAR(255) NOT NULL,
        previous_status VARCHAR(50),
        new_status VARCHAR(50),
        agent_type VARCHAR(50) DEFAULT 'AI_CONSULTANT',
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (subject_id) REFERENCES MGMT_SUBJECT(subject_id)
    ) ENGINE=InnoDB;
    """)

    conn.commit()
    print("Infrastruttura di Gestione Progettuale (Accenture PMF) creata su MariaDB.")
    conn.close()

if __name__ == "__main__":
    setup_mgmt()
