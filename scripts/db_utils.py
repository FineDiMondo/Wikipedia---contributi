#!/usr/bin/env python3
"""Database utilities for Consolidated MariaDB architecture (SDCP 2026)."""

import os
import json
import mysql.connector
from pathlib import Path

# Load environment logic
def load_env():
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value

load_env()

def get_db_connection(db_type="MGMT"):
    """
    Get a connection to MariaDB.
    db_type: "MGMT" (db_wikipedia_mgmt) or "CORE" (db_giardina_core)
    """
    db_name = os.environ.get("DB_NAME", "db_wikipedia_mgmt") if db_type == "MGMT" else os.environ.get("DB_CORE_NAME", "db_giardina_core")
    
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            port=int(os.environ.get("DB_PORT", 3306)),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASS", "root"),
            database=db_name
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to MariaDB ({db_type}): {err}")
        return None

def log_agent_action(project_id, action, subject_id=None, details=None, status="success"):
    """
    Logs an agent action into db_wikipedia_mgmt.MGMT_LOG.
    """
    conn = get_db_connection("MGMT")
    if not conn:
        return False
    
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO MGMT_LOG (project_id, subject_id, entry_type, action, details, status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            project_id, 
            subject_id, 
            "agent_automation", 
            action, 
            json.dumps(details) if details else None, 
            status
        ))
        conn.commit()
        return True
    except Exception as e:
        print(f"Failed to log agent action: {e}")
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    # Test logging
    if log_agent_action("proj_1", "test_connection", details={"info": "Accenture DB Utils Test"}):
        print("Agent log test: SUCCESS")
    else:
        print("Agent log test: FAILED")
