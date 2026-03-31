#!/usr/bin/env python3
"""
Autonomous Validation Agent (AVA) - DB Integrity & WP:V Checker
"""

from scripts.db_utils import get_db_connection
import sys

class ValidationAgent:
    def __init__(self):
        self.conn_core = get_db_connection('CORE')
        self.conn_mgmt = get_db_connection('MGMT')
        self.errors = []
        self.warnings = []
        self.passed = 0

    def log_error(self, rule, message):
        self.errors.append(f"[ERROR] {rule}: {message}")

    def log_warning(self, rule, message):
        self.warnings.append(f"[WARN]  {rule}: {message}")

    def check_wp_verifiability(self):
        """Rule 1: Every EVENT must have at least one CITATION (WP:V)"""
        if not self.conn_core: return
        cursor = self.conn_core.cursor(dictionary=True)
        cursor.execute("""
            SELECT e.event_id, e.description 
            FROM EVENT e 
            LEFT JOIN CITATION c ON e.event_id = c.event_id 
            WHERE c.citation_id IS NULL
        """)
        orphans = cursor.fetchall()
        for o in orphans:
            self.log_error("WP:V", f"Evento orfano di fonti (ID {o['event_id']}): {o['description'][:50]}")
        
        if not orphans: self.passed += 1

    def check_data_quality_dates(self):
        """Rule 2: Logical date checks (Death > Birth)"""
        if not self.conn_core: return
        cursor = self.conn_core.cursor(dictionary=True)
        # Semplice check stringa siccome usiamo DATE o VARCHAR per anni
        cursor.execute("""
            SELECT person_id, full_name, birth_date, death_date 
            FROM PERSON 
            WHERE birth_date IS NOT NULL AND death_date IS NOT NULL 
            AND birth_date > death_date
        """)
        anomalies = cursor.fetchall()
        for a in anomalies:
            self.log_error("DATE_LOGIC", f"Inversione temporale per {a['full_name']} (Nascita: {a['birth_date']} | Morte: {a['death_date']})")
        
        if not anomalies: self.passed += 1

    def check_data_quality_completeness(self):
        """Rule 3: Warn if Person has no birth data"""
        if not self.conn_core: return
        cursor = self.conn_core.cursor(dictionary=True)
        cursor.execute("SELECT person_id, full_name FROM PERSON WHERE birth_date IS NULL AND birth_qualifier IS NULL")
        incompletes = cursor.fetchall()
        for inc in incompletes:
            self.log_warning("COMPLETENESS", f"Soggetto privo di coordinate di nascita: {inc['full_name']} ({inc['person_id']})")
        
        if not incompletes: self.passed += 1

    def check_cross_domain_alignment(self):
        """Rule 4: Subjects in MGMT must exist in CORE (Loose matching by name)"""
        if not self.conn_mgmt or not self.conn_core: return
        
        c_mgmt = self.conn_mgmt.cursor(dictionary=True)
        c_mgmt.execute("SELECT subject_id, title FROM MGMT_SUBJECT")
        mgmt_subjects = c_mgmt.fetchall()

        c_core = self.conn_core.cursor(dictionary=True)
        c_core.execute("SELECT full_name FROM PERSON")
        core_names = [r['full_name'].lower() for r in c_core.fetchall()]

        for ms in mgmt_subjects:
            # Semplice euristica di matching: almeno parte del titolo wiki deve matchare il nome
            # Es: "Famiglia Giardina" non è una persona fisica, lo saltiamo o avvisiamo
            if "famiglia" in ms['title'].lower():
                continue
                
            # Estraiamo cognome e nome approssimativo dal titolo wiki
            parts = ms['title'].lower().split()
            found = any(all(p in cn for p in parts if len(p)>3) for cn in core_names)
            
            if not found:
                self.log_warning("ALIGNMENT", f"Soggetto Wiki '{ms['title']}' non chiaramente identificato nel DB CORE.")
        
        self.passed += 1

    def run_all(self):
        print("🤖 Avvio Autonomous Validation Agent (AVA)...")
        print("-" * 50)
        
        self.check_wp_verifiability()
        self.check_data_quality_dates()
        self.check_data_quality_completeness()
        self.check_cross_domain_alignment()
        
        print(f"📊 REPORT DI VALIDAZIONE")
        print(f"  Check Superati : {self.passed}")
        print(f"  Avvisi (WARN)  : {len(self.warnings)}")
        print(f"  Errori (ERROR) : {len(self.errors)}")
        print("-" * 50)
        
        for e in self.errors: print(e)
        for w in self.warnings: print(w)
        
        if self.conn_core: self.conn_core.close()
        if self.conn_mgmt: self.conn_mgmt.close()
        
        if self.errors:
            sys.exit(1) # Ritorna errore per eventuali pipeline CI/CD

if __name__ == "__main__":
    agent = ValidationAgent()
    agent.run_all()
