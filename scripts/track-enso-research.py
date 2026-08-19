#!/usr/bin/env python3
"""
track-enso-research.py
Scrapes and monitors https://www.enso.bot/research and https://www.enso.bot/llms-full.txt
for new growth experiments, methodologies, and pattern discoveries.
"""

import sys
import json
import urllib.request
import re
from datetime import datetime

RESEARCH_URL = "https://www.enso.bot/research"
LLMS_FULL_URL = "https://www.enso.bot/llms-full.txt"

def fetch_content(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; EliKopterGrowthLab/1.0)"}
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode("utf-8")

def parse_experiments(text):
    # Matches EXP-xxx patterns
    exp_pattern = re.compile(r"(EXP-\d{3})[^\n]*?([A-Za-z0-9\s·]+?)\s+([^\n]+?)\s+(Tested|Working)\s+([^\n]+?)\s+([A-Za-z]{3}\s+\d{1,2},\s+\d{4})")
    matches = exp_pattern.findall(text)
    return matches

def main():
    print(f"[{datetime.now().isoformat()}] Checking enso.bot research database...")
    try:
        html = fetch_content(RESEARCH_URL)
        print("Successfully fetched research database.")
        print(f"Content length: {len(html)} bytes")
    except Exception as e:
        print(f"Error fetching enso research: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
