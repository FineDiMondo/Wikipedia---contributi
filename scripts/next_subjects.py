#!/usr/bin/env python3
"""Show the next prioritized subjects from the central registry."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REGISTRY = REPO_ROOT / "ricerca" / "registro_soggetti.json"
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
STATUS_ORDER = {
    "publishable": 0,
    "sandboxed": 1,
    "sourced": 2,
    "researching": 3,
    "candidate": 4,
    "parked": 5,
    "published": 6,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print the next prioritized subjects from ricerca/registro_soggetti.json."
    )
    parser.add_argument(
        "registry",
        nargs="?",
        default=str(DEFAULT_REGISTRY),
        help="Path to the registry JSON file (default: ricerca/registro_soggetti.json)",
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
    parser.add_argument(
        "--include-do-not-publish",
        action="store_true",
        help="Include subjects gated as do_not_publish.",
    )
    return parser.parse_args()


def load_registry(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def priority_allowed(value: str, selected: str) -> bool:
    if selected == "all":
        return True
    return value == selected


def subject_sort_key(subject: dict) -> tuple[int, int, str]:
    return (
        PRIORITY_ORDER.get(subject.get("priority", "low"), 99),
        STATUS_ORDER.get(subject.get("status", "candidate"), 99),
        subject.get("title", ""),
    )


def main() -> int:
    args = parse_args()
    registry_path = Path(args.registry)
    if not registry_path.is_absolute():
        registry_path = REPO_ROOT / registry_path

    if not registry_path.is_file():
        print(f"Registry not found: {registry_path}", file=sys.stderr)
        return 1

    try:
        data = load_registry(registry_path)
    except json.JSONDecodeError as exc:
        print(f"Invalid registry JSON: {exc}", file=sys.stderr)
        return 1

    subjects = data.get("subjects", [])
    if not isinstance(subjects, list):
        print("Registry field 'subjects' missing or invalid.", file=sys.stderr)
        return 1

    filtered = []
    for subject in subjects:
        if not isinstance(subject, dict):
            continue
        if subject.get("status") in {"parked", "published"}:
            continue
        if not priority_allowed(subject.get("priority", "low"), args.priority):
            continue
        if not args.include_do_not_publish and subject.get("publishability") == "do_not_publish":
            continue
        filtered.append(subject)

    filtered.sort(key=subject_sort_key)

    print(f"Registry: {registry_path}")
    print(f"Filter  : priority={args.priority}, limit={args.limit}, include_do_not_publish={args.include_do_not_publish}")
    print()

    if not filtered:
        print("No subjects matched the selected criteria.")
        return 0

    for index, subject in enumerate(filtered[: args.limit], start=1):
        print(
            f"{index}. {subject['title']} [{subject['id']}]"
        )
        print(
            f"   track={subject['track']} status={subject['status']} gate={subject['publishability']} priority={subject['priority']} evidence={subject['evidence_strength']}"
        )
        print(f"   why: {subject['why_exists']}")
        blocked_by = subject.get("blocked_by", [])
        if blocked_by:
            print(f"   block: {blocked_by[0]}")
        next_actions = subject.get("next_actions", [])
        if next_actions:
            print(f"   next: {next_actions[0]}")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
