#!/usr/bin/env python3
"""Database utilities for MariaDB connection - CONSOLIDATED ARCHITECTURE."""

import os
import mysql.connector
from pathlib import Path
from .env_utils import load_env_file

# Load environment from .env at project root
ROOT_DIR = Path(__file__).parent.parent
load_env_file(ROOT_DIR / ".env")

def get_db_connection(database='db_giardina_core'):
    """Get a connection to the MariaDB database. Default: db_giardina_core."""
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            port=int(os.environ.get("DB_PORT", 3306)),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASS", "root"),
            database=database
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to MariaDB [{database}]: {err}")
        return None

if __name__ == "__main__":
    connection = get_db_connection()
    if connection:
        print(f"Connected to CONSOLIDATED CORE: {connection.database}")
        connection.close()
    
    connection_mgmt = get_db_connection('db_wikipedia_mgmt')
    if connection_mgmt:
        print(f"Connected to CONSOLIDATED MGMT: {connection_mgmt.database}")
        connection_mgmt.close()
