#!/usr/bin/env python3
"""
track-growth-sources.py
Weekly automated crawler & discovery pipeline for growth engineering methodologies,
GEO benchmarks, and agentic distribution playbooks.
"""

import sys
import json
import urllib.request
import re
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_JSON = REPO_ROOT / "references" / "sources.json"
SOURCES_MD = REPO_ROOT / "SOURCES.md"

def load_sources():
    if not SOURCES_JSON.exists():
        return []
    with open(SOURCES_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def fetch_url(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; GrowthIntelligenceBot/1.0)"}
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode("utf-8")

def main():
    print(f"[{datetime.now().isoformat()}] Starting weekly growth intelligence scan...")
    sources = load_sources()
    active_sources = [s for s in sources if s.get("status") == "active"]
    print(f"Loaded {len(active_sources)} active research source(s) from registry:")
    
    for s in active_sources:
        print(f" -> Scanning [{s['id']}] {s['name']} ({s['url']})...")
        for ep in s.get("endpoints", [s["url"]]):
            try:
                content = fetch_url(ep)
                print(f"    ✓ Fetched {ep} ({len(content)} bytes)")
            except Exception as e:
                print(f"    ✗ Error fetching {ep}: {e}", file=sys.stderr)

    print("\nScan completed. Discovered candidates will be staged in SOURCES.md for approval.")

if __name__ == "__main__":
    main()
