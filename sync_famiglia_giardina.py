#!/usr/bin/env python3
"""Direct sync script - Famiglia Giardina to Wikipedia sandbox."""
import os
import sys
import requests
from pathlib import Path

# Hardcoded credentials extracted from .env
WIKI_BOT_USER = "Daniel Giardina@codexcmd@danielgiardina"
WIKI_BOT_PASS = "a0h8tn570b13gk0t1nvr292q2g8umi9m"
API = "https://it.wikipedia.org/w/api.php"

def api_get(session, params):
    response = session.get(API, params={**params, "format": "json"}, timeout=60)
    response.raise_for_status()
    return response.json()

def api_post(session, data):
    response = session.post(API, data={**data, "format": "json"}, timeout=180)
    response.raise_for_status()
    return response.json()

def login(session, user, password):
    token = api_get(session, {"action": "query", "meta": "tokens", "type": "login"})["query"]["tokens"]["logintoken"]
    result = api_post(session, {"action": "login", "lgname": user, "lgpassword": password, "lgtoken": token})["login"]
    if result.get("result") != "Success":
        raise RuntimeError(f"Login failed: {result}")
    csrf = api_get(session, {"action": "query", "meta": "tokens"})["query"]["tokens"]["csrftoken"]
    return csrf

def edit_page(session, csrf, title, content, summary):
    data = api_post(session, {"action": "edit", "title": title, "text": content, "summary": summary, "token": csrf, "bot": "1"})
    return data["edit"]["result"] == "Success"

session = requests.Session()
session.headers.update({"User-Agent": "WikiDraftSync/1.1 (bot; Daniel_Giardina)"})

print("[1] Login...")
csrf = login(session, WIKI_BOT_USER, WIKI_BOT_PASS)

print("[2] Reading wiki/Famiglia_Giardina.wiki...")
content = Path("wiki/Famiglia_Giardina.wiki").read_text(encoding="utf-8")

print("[3] Syncing to Utente:Daniel Giardina/Sandbox/Famiglia Giardina...")
ok = edit_page(session, csrf, "Utente:Daniel Giardina/Sandbox/Famiglia Giardina", content, "Refinement genealogico: correzione Bellacera, lite 1703, linea patrilineare")

print(f"\n{'✅ SINCRONIZZAZIONE COMPLETATA' if ok else '❌ ERRORE'}")
sys.exit(0 if ok else 1)
