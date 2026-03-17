#!/usr/bin/env python3
"""Sincronizzazione bozze Wikipedia via API MediaWiki con bot password."""
import os
import sys
from pathlib import Path

import requests
from env_utils import load_env_file

API = "https://it.wikipedia.org/w/api.php"
REPO_ROOT = Path(__file__).resolve().parent.parent
load_env_file(REPO_ROOT / ".env")
BOT_USER = os.getenv("WIKI_BOT_USER", "").strip()
BOT_PASS = os.getenv("WIKI_BOT_PASS", "").strip()

PAGES = [
    (
        "wiki/Famiglia_Giardina.wiki",
        "Utente:Daniel Giardina/Sandbox/Famiglia Giardina",
        "Consolidamento biografie XX secolo",
    ),
    (
        "wiki/Marco_Aurelio_Pasquale_Giardina.wiki",
        "Utente:Daniel Giardina/Sandbox/Marco Aurelio Pasquale Giardina",
        "Aggiornamento link incrociati",
    ),
    (
        "wiki/Franco_Giardina_senior.wiki",
        "Utente:Daniel Giardina/Sandbox/Franco Giardina senior",
        "Rafforzamento incipit martire accademico",
    ),
    (
        "wiki/Giuseppe_Giardina.wiki",
        "Utente:Daniel Giardina/Sandbox/Giuseppe Giardina",
        "Sincronizzazione biografia",
    ),
    (
        "wiki/index.wiki",
        "Utente:Daniel Giardina/Sandbox",
        "Aggiornamento indice sandbox",
    ),
]


def load_credentials() -> tuple[str, str]:
    if not BOT_USER or not BOT_PASS:
        raise RuntimeError(
            "Missing WIKI_BOT_USER / WIKI_BOT_PASS environment variables."
        )
    return BOT_USER, BOT_PASS


def create_session() -> requests.Session:
    session = requests.Session()
    session.headers.update({"User-Agent": "WikiDraftSync/1.1 (bot; Daniel_Giardina)"})
    return session


def api_get(session: requests.Session, params: dict) -> dict:
    response = session.get(API, params={**params, "format": "json"}, timeout=60)
    response.raise_for_status()
    payload = response.json()
    if "error" in payload:
        raise RuntimeError(f"API error: {payload['error']}")
    return payload


def api_post(session: requests.Session, data: dict) -> dict:
    response = session.post(API, data={**data, "format": "json"}, timeout=180)
    response.raise_for_status()
    payload = response.json()
    if "error" in payload:
        raise RuntimeError(f"API error: {payload['error']}")
    return payload


def login(session: requests.Session, user: str, password: str) -> str:
    login_token = api_get(
        session, {"action": "query", "meta": "tokens", "type": "login"}
    )["query"]["tokens"]["logintoken"]
    print(f"[1] Login token: {login_token[:12]}…")

    login_result = api_post(
        session,
        {
            "action": "login",
            "lgname": user,
            "lgpassword": password,
            "lgtoken": login_token,
        },
    )["login"]
    print(f"[2] Login result: {login_result.get('result')}")
    if login_result.get("result") != "Success":
        raise RuntimeError(f"Login failed: {login_result}")

    csrf = api_get(session, {"action": "query", "meta": "tokens"})["query"]["tokens"][
        "csrftoken"
    ]
    print(f"[3] CSRF token: {csrf[:12]}…")
    return csrf


def edit_page(
    session: requests.Session, csrf_token: str, title: str, content: str, summary: str
) -> bool:
    data = api_post(
        session,
        {
            "action": "edit",
            "title": title,
            "text": content,
            "summary": summary,
            "token": csrf_token,
            "bot": "1",
        },
    )
    if "error" in data:
        print(f"    ERRORE edit '{title}': {data['error']}", file=sys.stderr)
        return False
    result = data["edit"]["result"]
    if result != "Success":
        print(f"    FAILURE detail: {data}", file=sys.stderr)
    newrev = data["edit"].get("newrevid", "—")
    print(f"    result={result}  newrevid={newrev}")
    return result == "Success"


def read_text(path: str) -> str:
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def main() -> int:
    try:
        user, password = load_credentials()
        session = create_session()
        csrf_token = login(session, user, password)
    except Exception as exc:  # pragma: no cover - CLI failure path
        print(f"ERRORE: {exc}", file=sys.stderr)
        return 1

    results = []
    for index, (path, title, summary) in enumerate(PAGES, start=4):
        print(f"[{index}] Editing {title} …")
        ok = edit_page(session, csrf_token, title, read_text(path), summary)
        results.append((title, ok))

    print()
    print("═══ RIEPILOGO ═══")
    for title, ok in results:
        print(f"  {title:<52} : {'OK' if ok else 'ERRORE'}")
    return 0 if all(ok for _, ok in results) else 1


if __name__ == "__main__":
    sys.exit(main())
