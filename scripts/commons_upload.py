#!/usr/bin/env python3
"""Upload a local file to Wikimedia Commons via MediaWiki API."""

from __future__ import annotations

import argparse
import hashlib
import mimetypes
import os
import sys
from pathlib import Path

import requests


API = "https://commons.wikimedia.org/w/api.php"
USER_AGENT = "WikiCommonsUploadTest/1.0 (user script; contact via Wikimedia user page)"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Upload a file to Wikimedia Commons using BotPassword credentials."
    )
    parser.add_argument("file", help="Local file to upload")
    parser.add_argument("--filename", required=True, help="Target filename on Commons")
    parser.add_argument(
        "--description-file",
        help="Path to a UTF-8 wikitext file to use as the full file description page",
    )
    parser.add_argument("--description-it", help="Italian description")
    parser.add_argument("--description-en", help="English description")
    parser.add_argument("--source-url", help="Original source URL")
    parser.add_argument("--author", help="Author or publisher")
    parser.add_argument(
        "--license-template",
        default="Cc-by-sa-3.0",
        help="Commons license template without braces, default: Cc-by-sa-3.0",
    )
    parser.add_argument(
        "--attribution",
        help="Attribution string for the license template, if required by the source",
    )
    parser.add_argument(
        "--category",
        action="append",
        default=[],
        help="Commons category without brackets; can be repeated",
    )
    parser.add_argument(
        "--date",
        default="unknown",
        help='Date field for {{Information}}, default: "unknown"',
    )
    parser.add_argument(
        "--summary",
        default="Upload via API test",
        help="Upload log summary",
    )
    parser.add_argument(
        "--ignore-warnings",
        action="store_true",
        help="Pass ignorewarnings=1 to the upload API",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not upload; print preflight information and generated wikitext",
    )
    return parser.parse_args()


def load_credentials() -> tuple[str, str]:
    user = os.getenv("COMMONS_BOT_USER", "").strip()
    password = os.getenv("COMMONS_BOT_PASS", "").strip()
    if not user or not password:
        raise RuntimeError(
            "Missing COMMONS_BOT_USER / COMMONS_BOT_PASS environment variables."
        )
    return user, password


def sha1_hex(path: Path) -> str:
    digest = hashlib.sha1()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_wikitext(args: argparse.Namespace) -> str:
    if args.description_file:
        return Path(args.description_file).read_text(encoding="utf-8")

    if not args.description_it and not args.description_en:
        raise RuntimeError(
            "Either --description-file or at least one of --description-it / "
            "--description-en is required."
        )

    description_lines: list[str] = []
    if args.description_en:
        description_lines.append(f"{{{{en|1={args.description_en}}}}}")
    if args.description_it:
        description_lines.append(f"{{{{it|1={args.description_it}}}}}")

    source = args.source_url or "unknown"
    author = args.author or "unknown"
    permission = "See licensing section below."
    attribution_suffix = f"|{args.attribution}" if args.attribution else ""
    categories = "\n".join(f"[[Category:{name}]]" for name in args.category)

    parts = [
        "== {{int:filedesc}} ==",
        "{{Information",
        f"|description={' '.join(description_lines)}",
        f"|date={args.date}",
        f"|source={source}",
        f"|author={author}",
        f"|permission={permission}",
        "|other_versions=",
        "}}",
        "",
        "== {{int:license-header}} ==",
        f"{{{{{args.license_template}{attribution_suffix}}}}}",
    ]
    if categories:
        parts.extend(["", categories])
    return "\n".join(parts).strip() + "\n"


def create_session() -> requests.Session:
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    return session


def api_get(session: requests.Session, params: dict) -> dict:
    response = session.get(API, params={**params, "format": "json"}, timeout=60)
    response.raise_for_status()
    data = response.json()
    if "error" in data:
        raise RuntimeError(f"API error: {data['error']}")
    return data


def api_post(session: requests.Session, data: dict, files: dict | None = None) -> dict:
    response = session.post(
        API,
        data={**data, "format": "json"},
        files=files,
        timeout=180,
    )
    response.raise_for_status()
    payload = response.json()
    if "error" in payload:
        raise RuntimeError(f"API error: {payload['error']}")
    return payload


def check_remote_file(session: requests.Session, filename: str) -> dict:
    data = api_get(
        session,
        {
            "action": "query",
            "titles": f"File:{filename}",
            "prop": "imageinfo",
            "iiprop": "sha1|size|mime|url",
        },
    )
    page = next(iter(data["query"]["pages"].values()))
    return page


def login(session: requests.Session, user: str, password: str) -> str:
    login_token = api_get(
        session,
        {"action": "query", "meta": "tokens", "type": "login"},
    )["query"]["tokens"]["logintoken"]

    login_result = api_post(
        session,
        {
            "action": "login",
            "lgname": user,
            "lgpassword": password,
            "lgtoken": login_token,
        },
    )["login"]

    if login_result.get("result") != "Success":
        raise RuntimeError(f"Login failed: {login_result}")

    return api_get(session, {"action": "query", "meta": "tokens"})["query"]["tokens"][
        "csrftoken"
    ]


def upload_file(
    session: requests.Session,
    csrf_token: str,
    path: Path,
    filename: str,
    text: str,
    summary: str,
    ignore_warnings: bool,
) -> dict:
    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    with path.open("rb") as handle:
        files = {"file": (path.name, handle, mime_type)}
        data = {
            "action": "upload",
            "filename": filename,
            "text": text,
            "comment": summary,
            "token": csrf_token,
            "watchlist": "nochange",
        }
        if ignore_warnings:
            data["ignorewarnings"] = "1"
        return api_post(session, data, files=files)


def print_preflight(path: Path, filename: str, page: dict, text: str) -> None:
    local_sha1 = sha1_hex(path)
    print("== Preflight ==")
    print(f"Local file      : {path}")
    print(f"Target filename : {filename}")
    print(f"Size (bytes)    : {path.stat().st_size}")
    print(f"SHA1            : {local_sha1}")
    if "missing" in page:
        print("Commons status  : filename currently available")
    else:
        title = page.get("title", f"File:{filename}")
        imageinfo = (page.get("imageinfo") or [{}])[0]
        print(f"Commons status  : already exists as {title}")
        print(f"Remote SHA1     : {imageinfo.get('sha1', 'unknown')}")
        print(f"Remote size     : {imageinfo.get('size', 'unknown')}")
        print(f"Remote mime     : {imageinfo.get('mime', 'unknown')}")
        print(f"Remote URL      : {imageinfo.get('url', 'unknown')}")
    print()
    print("== Generated file description ==")
    print(text)


def main() -> int:
    args = parse_args()
    path = Path(args.file)
    if not path.is_file():
        print(f"Local file not found: {path}", file=sys.stderr)
        return 1

    try:
        text = build_wikitext(args)
    except Exception as exc:  # noqa: BLE001
        print(str(exc), file=sys.stderr)
        return 1

    session = create_session()

    try:
        remote_page = check_remote_file(session, args.filename)
        print_preflight(path, args.filename, remote_page, text)

        if args.dry_run:
            return 0

        if "missing" not in remote_page and not args.ignore_warnings:
            print(
                "Refusing upload because the target filename already exists. "
                "Use --ignore-warnings only if replacement is intended.",
                file=sys.stderr,
            )
            return 2

        user, password = load_credentials()
        csrf_token = login(session, user, password)
        result = upload_file(
            session=session,
            csrf_token=csrf_token,
            path=path,
            filename=args.filename,
            text=text,
            summary=args.summary,
            ignore_warnings=args.ignore_warnings,
        )
        print("== Upload result ==")
        print(result)
        return 0
    except Exception as exc:  # noqa: BLE001
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
