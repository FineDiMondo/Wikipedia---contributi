#!/usr/bin/env python3
"""Validate the central subject registry used by agents and contributors."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REGISTRY = REPO_ROOT / "ricerca" / "registro_soggetti.json"


@dataclass
class Issue:
    severity: str
    message: str


def add_issue(issues: list[Issue], severity: str, message: str) -> None:
    issues.append(Issue(severity=severity, message=message))


def validate_allowed_values(data: dict, issues: list[Issue]) -> dict[str, set[str]]:
    allowed = data.get("allowed_values")
    if not isinstance(allowed, dict):
        add_issue(issues, "ERROR", "Top-level key 'allowed_values' missing or invalid.")
        return {}

    result: dict[str, set[str]] = {}
    for key in (
        "track",
        "status",
        "publishability",
        "priority",
        "coi",
        "evidence_strength",
    ):
        values = allowed.get(key)
        if not isinstance(values, list) or not values or not all(isinstance(item, str) for item in values):
            add_issue(issues, "ERROR", f"allowed_values.{key} missing or invalid.")
            continue
        result[key] = set(values)
    return result


def validate_path(path_value: str, label: str, issues: list[Issue]) -> None:
    path = REPO_ROOT / path_value
    if not path.exists():
        add_issue(issues, "ERROR", f"{label} points to missing path: {path_value}")


def validate_subject(
    subject: dict,
    index: int,
    allowed: dict[str, set[str]],
    issues: list[Issue],
) -> None:
    prefix = f"subjects[{index}]"
    required_string_fields = (
        "id",
        "title",
        "type",
        "track",
        "status",
        "publishability",
        "priority",
        "coi",
        "evidence_strength",
        "why_exists",
    )
    for field in required_string_fields:
        value = subject.get(field)
        if not isinstance(value, str) or not value.strip():
            add_issue(issues, "ERROR", f"{prefix}.{field} missing or invalid.")

    for field in ("blocked_by", "next_actions"):
        value = subject.get(field)
        if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
            add_issue(issues, "ERROR", f"{prefix}.{field} must be a non-empty list of strings.")

    for field in ("track", "status", "publishability", "priority", "coi", "evidence_strength"):
        value = subject.get(field)
        if field in allowed and value not in allowed[field]:
            add_issue(issues, "ERROR", f"{prefix}.{field} has unsupported value: {value!r}")

    paths = subject.get("paths")
    if not isinstance(paths, dict) or not paths:
        add_issue(issues, "ERROR", f"{prefix}.paths missing or invalid.")
    else:
        for path_key, path_value in paths.items():
            if not isinstance(path_value, str) or not path_value.strip():
                add_issue(issues, "ERROR", f"{prefix}.paths.{path_key} missing or invalid.")
                continue
            validate_path(path_value, f"{prefix}.paths.{path_key}", issues)

    track = subject.get("track")
    status = subject.get("status")
    publishability = subject.get("publishability")

    if status == "published" and publishability != "published":
        add_issue(issues, "ERROR", f"{prefix} has status 'published' but publishability is not 'published'.")
    if publishability == "published" and status != "published":
        add_issue(issues, "ERROR", f"{prefix} has publishability 'published' but status is not 'published'.")
    if status in {"publishable", "sandboxed", "published"} and track != "publishing_track":
        add_issue(issues, "ERROR", f"{prefix} uses a publication status outside 'publishing_track'.")
    if publishability == "do_not_publish" and track == "publishing_track":
        add_issue(issues, "WARN", f"{prefix} is in 'publishing_track' but gate is 'do_not_publish'.")
    if status not in {"published", "parked"} and not subject.get("next_actions"):
        add_issue(issues, "WARN", f"{prefix} has no next actions.")


def validate_registry(path: Path) -> list[Issue]:
    issues: list[Issue] = []

    if not path.is_file():
        add_issue(issues, "ERROR", f"Registry file not found: {path}")
        return issues

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        add_issue(issues, "ERROR", f"Invalid JSON: {exc}")
        return issues

    if not isinstance(data, dict):
        add_issue(issues, "ERROR", "Registry root must be a JSON object.")
        return issues

    if not isinstance(data.get("schema_version"), int):
        add_issue(issues, "ERROR", "Top-level key 'schema_version' missing or invalid.")
    if not isinstance(data.get("last_updated"), str) or not data["last_updated"].strip():
        add_issue(issues, "ERROR", "Top-level key 'last_updated' missing or invalid.")

    project_policy = data.get("project_policy")
    if not isinstance(project_policy, dict):
        add_issue(issues, "ERROR", "Top-level key 'project_policy' missing or invalid.")

    allowed = validate_allowed_values(data, issues)

    subjects = data.get("subjects")
    if not isinstance(subjects, list) or not subjects:
        add_issue(issues, "ERROR", "Top-level key 'subjects' missing or empty.")
        return issues

    seen_ids: set[str] = set()
    seen_titles: set[str] = set()
    for index, subject in enumerate(subjects):
        if not isinstance(subject, dict):
            add_issue(issues, "ERROR", f"subjects[{index}] must be an object.")
            continue

        subject_id = subject.get("id")
        title = subject.get("title")
        if isinstance(subject_id, str):
            if subject_id in seen_ids:
                add_issue(issues, "ERROR", f"Duplicate subject id: {subject_id}")
            seen_ids.add(subject_id)
        if isinstance(title, str):
            if title in seen_titles:
                add_issue(issues, "ERROR", f"Duplicate subject title: {title}")
            seen_titles.add(title)

        validate_subject(subject, index, allowed, issues)

    return issues


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate ricerca/registro_soggetti.json.")
    parser.add_argument(
        "registry",
        nargs="?",
        default=str(DEFAULT_REGISTRY),
        help="Path to the registry JSON file (default: ricerca/registro_soggetti.json)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    registry_path = Path(args.registry)
    if not registry_path.is_absolute():
        registry_path = REPO_ROOT / registry_path

    issues = validate_registry(registry_path)
    error_count = 0
    warn_count = 0

    print(f"Registry: {registry_path}")
    print()
    for issue in issues:
        if issue.severity == "ERROR":
            error_count += 1
        elif issue.severity == "WARN":
            warn_count += 1
        print(f"[{issue.severity}] {issue.message}")

    if not issues:
        print("[OK] No validation issues found.")

    print()
    print(f"Summary: ERROR={error_count} WARN={warn_count}")
    return 1 if error_count else 0


if __name__ == "__main__":
    sys.exit(main())
