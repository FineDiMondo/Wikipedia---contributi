#!/usr/bin/env python3
"""Show next prioritized subjects from CONSOLIDATED MariaDB (SDCP 2026)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Add project root to sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(REPO_ROOT))

try:
    from scripts.db_utils import get_db_connection
except ImportError:
    print("Error: Could not import db_utils.")
    sys.exit(1)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print next prioritized subjects from consolidated MGMT database."
    )
    parser.add_argument(
        "--priority",
        choices=("high", "medium", "low", "all"),
        default="high",
        help="Priority filter (default: high)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Maximum number of subjects to print (default: 10)",
    )
    return parser.parse_args()

def main() -> int:
    args = parse_args()
    
    conn = get_db_connection("MGMT")
    if not conn:
        return 1

    try:
        cursor = conn.cursor(dictionary=True)
        
        # Build query for MGMT_SUBJECT (Consolidated Table)
        query = "SELECT * FROM MGMT_SUBJECT WHERE status NOT IN ('parked', 'published')"
        params = []

        if args.priority != "all":
            query += " AND priority = %s"
            params.append(args.priority)
        
        # Sort based on Priority and Title
        query += """ ORDER BY 
            FIELD(priority, 'high', 'medium', 'low'),
            title ASC
            LIMIT %s"""
        params.append(args.limit)

        cursor.execute(query, params)
        results = cursor.fetchall()

        print(f"Database: db_wikipedia_mgmt")
        print(f"Filter  : priority={args.priority}, limit={args.limit}")
        print("-" * 60)

        if not results:
            print("No subjects matched in consolidated MGMT database.")
            return 0

        for index, row in enumerate(results, start=1):
            print(f"{index}. {row['title']} [{row['subject_id']}]")
            print(f"   track={row['track']} status={row['status']} gate={row['gate']} priority={row['priority']}")
            if row['notes']:
                print(f"   note: {row['notes'][:100]}...")
            print()

    except Exception as exc:
        print(f"Database error: {exc}", file=sys.stderr)
        return 1
    finally:
        conn.close()

    return 0

if __name__ == "__main__":
    sys.exit(main())
