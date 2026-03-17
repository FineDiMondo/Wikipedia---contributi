#!/usr/bin/env python3
"""Diagnostica operativa per il repository Wikipedia/GitHub."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from importlib import metadata
from pathlib import Path

from env_utils import load_env_file


REPO_ROOT = Path(__file__).resolve().parent.parent
DOTENV_PATH = REPO_ROOT / ".env"
ENV_LOADED = load_env_file(DOTENV_PATH)
ENV_VARS = (
    "WIKI_BOT_USER",
    "WIKI_BOT_PASS",
    "COMMONS_BOT_USER",
    "COMMONS_BOT_PASS",
)
REQUIRED_FILES = (
    "scripts/wp_sync.py",
    "scripts/commons_upload.py",
    "wiki/Famiglia_Giardina.wiki",
    "wiki/Marco_Aurelio_Pasquale_Giardina.wiki",
    "wiki/index.wiki",
)


@dataclass
class CheckResult:
    name: str
    status: str
    detail: str


def run_git(*args: str) -> tuple[int, str, str]:
    process = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    return (
        process.returncode,
        process.stdout.strip(),
        process.stderr.strip(),
    )


def normalize_git_error(stderr: str) -> str:
    lines = []
    for line in stderr.splitlines():
        if "unable to access" in line and "config/git/ignore" in line:
            continue
        if line.strip():
            lines.append(line.strip())
    return " | ".join(lines)


def add_result(results: list[CheckResult], name: str, status: str, detail: str) -> None:
    results.append(CheckResult(name=name, status=status, detail=detail))


def probe_http(url: str, timeout: float) -> tuple[int, str]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "WikiRepoDoctor/1.0"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.status, response.url


def github_repo_url(origin_url: str) -> str:
    parsed = urllib.parse.urlparse(origin_url)
    if parsed.scheme in {"http", "https"} and parsed.netloc.endswith("github.com"):
        path = parsed.path[:-4] if parsed.path.endswith(".git") else parsed.path
        return urllib.parse.urlunparse(("https", parsed.netloc, path, "", "", ""))
    return "https://github.com/"


def collect_git_checks(results: list[CheckResult], network_enabled: bool, timeout: float) -> None:
    if not shutil.which("git"):
        add_result(results, "git", "FAIL", "git non trovato nel PATH")
        return

    add_result(results, "git", "OK", "git disponibile")

    rc, branch, stderr = run_git("rev-parse", "--abbrev-ref", "HEAD")
    if rc == 0 and branch:
        add_result(results, "branch", "OK", branch)
    else:
        add_result(
            results,
            "branch",
            "FAIL",
            normalize_git_error(stderr) or "impossibile leggere il branch corrente",
        )

    rc, origin_url, stderr = run_git("remote", "get-url", "origin")
    if rc == 0 and origin_url:
        add_result(results, "origin", "OK", origin_url)
    else:
        add_result(
            results,
            "origin",
            "FAIL",
            normalize_git_error(stderr) or "remoto origin non configurato",
        )
        origin_url = ""

    rc, porcelain, stderr = run_git("status", "--porcelain")
    if rc == 0:
        tracked = 0
        untracked = 0
        for line in porcelain.splitlines():
            if line.startswith("??"):
                untracked += 1
            elif line:
                tracked += 1
        if tracked or untracked:
            add_result(
                results,
                "working-tree",
                "WARN",
                f"{tracked} modifica/e tracciata/e, {untracked} percorso/i non tracciato/i",
            )
        else:
            add_result(results, "working-tree", "OK", "pulito")
    else:
        add_result(
            results,
            "working-tree",
            "FAIL",
            normalize_git_error(stderr) or "impossibile leggere lo stato del repo",
        )

    rc, counts, stderr = run_git("rev-list", "--left-right", "--count", "origin/main...HEAD")
    if rc == 0 and counts:
        behind, ahead = counts.split()
        status = "OK" if behind == "0" and ahead == "0" else "WARN"
        add_result(
            results,
            "divergence",
            status,
            f"ahead {ahead}, behind {behind} rispetto a origin/main locale",
        )
    else:
        add_result(
            results,
            "divergence",
            "WARN",
            normalize_git_error(stderr) or "origin/main non disponibile localmente",
        )

    rc, local_origin_main, stderr = run_git("rev-parse", "origin/main")
    if rc == 0 and local_origin_main:
        add_result(results, "origin/main-local", "OK", local_origin_main)
    else:
        add_result(
            results,
            "origin/main-local",
            "WARN",
            normalize_git_error(stderr) or "riferimento locale origin/main assente",
        )
        local_origin_main = ""

    if not network_enabled:
        add_result(results, "github-remote", "SKIP", "controllo rete disattivato")
        return

    if origin_url:
        try:
            status_code, resolved_url = probe_http(github_repo_url(origin_url), timeout)
            add_result(results, "github-web", "OK", f"HTTP {status_code} {resolved_url}")
        except urllib.error.URLError as exc:
            add_result(results, "github-web", "FAIL", str(exc.reason))
        except Exception as exc:  # noqa: BLE001
            add_result(results, "github-web", "FAIL", str(exc))

    rc, remote_refs, stderr = run_git("ls-remote", "origin", "refs/heads/main")
    if rc == 0 and remote_refs:
        remote_commit = remote_refs.split()[0]
        status = "OK" if remote_commit == local_origin_main else "WARN"
        detail = remote_commit
        if local_origin_main and remote_commit != local_origin_main:
            detail += " (diverso dal riferimento locale origin/main)"
        add_result(results, "github-remote", status, detail)
    else:
        add_result(
            results,
            "github-remote",
            "FAIL",
            normalize_git_error(stderr) or "impossibile interrogare origin via rete",
        )


def collect_file_checks(results: list[CheckResult]) -> None:
    missing = [path for path in REQUIRED_FILES if not (REPO_ROOT / path).is_file()]
    if missing:
        add_result(results, "required-files", "FAIL", ", ".join(missing))
    else:
        add_result(results, "required-files", "OK", f"{len(REQUIRED_FILES)} file chiave presenti")


def collect_python_checks(results: list[CheckResult]) -> None:
    try:
        version = metadata.version("requests")
        add_result(results, "python-requests", "OK", version)
    except metadata.PackageNotFoundError:
        add_result(
            results,
            "python-requests",
            "WARN",
            "requests non installato; esegui `python -m pip install -r requirements.txt`",
        )


def collect_env_checks(results: list[CheckResult]) -> None:
    env_source = ".env caricato" if ENV_LOADED else "solo ambiente di shell"
    add_result(results, "env-source", "OK", env_source)

    missing = [name for name in ENV_VARS if not os.getenv(name, "").strip()]
    if missing:
        add_result(results, "credentials", "WARN", f"mancano: {', '.join(missing)}")
    else:
        add_result(results, "credentials", "OK", "variabili di sync/upload presenti")


def collect_network_checks(results: list[CheckResult], network_enabled: bool, timeout: float) -> None:
    targets = (
        ("wikipedia-api", "https://it.wikipedia.org/w/api.php?action=query&meta=siteinfo&siprop=general&format=json"),
        ("commons-api", "https://commons.wikimedia.org/w/api.php?action=query&meta=siteinfo&siprop=general&format=json"),
    )

    if not network_enabled:
        for name, _ in targets:
            add_result(results, name, "SKIP", "controllo rete disattivato")
        return

    for name, url in targets:
        try:
            status_code, resolved_url = probe_http(url, timeout)
            add_result(results, name, "OK", f"HTTP {status_code} {resolved_url}")
        except urllib.error.URLError as exc:
            add_result(results, name, "FAIL", str(exc.reason))
        except Exception as exc:  # noqa: BLE001
            add_result(results, name, "FAIL", str(exc))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verifica setup locale, remoto GitHub e API Wikipedia/Commons."
    )
    parser.add_argument(
        "--no-network",
        action="store_true",
        help="salta i controlli remoti HTTP e git ls-remote",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="stampa i risultati in JSON",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="timeout in secondi per i controlli di rete (default: 10)",
    )
    return parser.parse_args()


def print_human(results: list[CheckResult]) -> None:
    print(f"Repository : {REPO_ROOT}")
    print()
    for item in results:
        print(f"[{item.status:<4}] {item.name:<16} {item.detail}")

    counts = {status: 0 for status in ("OK", "WARN", "FAIL", "SKIP")}
    for item in results:
        counts[item.status] = counts.get(item.status, 0) + 1

    print()
    print(
        "Summary    : "
        f"OK={counts['OK']} WARN={counts['WARN']} FAIL={counts['FAIL']} SKIP={counts['SKIP']}"
    )


def main() -> int:
    args = parse_args()
    results: list[CheckResult] = []

    collect_file_checks(results)
    collect_python_checks(results)
    collect_env_checks(results)
    collect_git_checks(results, network_enabled=not args.no_network, timeout=args.timeout)
    collect_network_checks(results, network_enabled=not args.no_network, timeout=args.timeout)

    if args.json:
        print(json.dumps([asdict(item) for item in results], ensure_ascii=False, indent=2))
    else:
        print_human(results)

    return 1 if any(item.status == "FAIL" for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
