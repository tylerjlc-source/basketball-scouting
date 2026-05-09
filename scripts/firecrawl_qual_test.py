"""
Firecrawl qualitative-research smoke test — throwaway.

Pulls scouting articles for a player via Firecrawl search + scrape and saves
clean markdown to raw/[Player_Name]/scraped/[YYYY-MM-DD]/.

Purpose: measure whether externalizing Skill 1's Phase B (qualitative web research)
saves real tokens vs. Claude doing WebFetch in-session, without losing verbatim
scouting language (R1).

Setup:
    pip install firecrawl-py
    # Windows PowerShell:
    $env:FIRECRAWL_API_KEY = "fc-..."

Usage:
    python scripts/firecrawl_qual_test.py "Myles Turner"

Notes:
- Free tier on Firecrawl is fine for this test (search ~1 credit, scrape 1 credit each).
- SDK call shapes here match firecrawl-py v2.x. If on an older SDK, scrape_url may
  want params={"formats": ["markdown"]} instead of formats=["markdown"].
- Domain allowlist sticks to free, non-login-gated sources. EvanMiya / The Athletic
  / Cleaning the Glass excluded — those are a separate browser-sandbox question.
"""

import os
import re
import sys
import time
from datetime import date
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from firecrawl import FirecrawlApp

from config import RAW_DIR, require_firecrawl_key

PLAYER = sys.argv[1] if len(sys.argv) > 1 else "Myles Turner"
SLUG = PLAYER.replace(" ", "_")
TODAY = date.today().isoformat()

OUT_DIR = RAW_DIR / SLUG / "scraped" / TODAY
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Focused queries mirror the scouting-language hunts scout-research does in Step 3.
# Tweak per player — current-team / Finals / current-season strings below are
# Turner-specific (Bucks 2025-26, prior Pacers 2024-25, 2025 Finals run) and
# should be edited when running on a different player.
QUERIES = [
    f'"{PLAYER}" scouting report',
    f'"{PLAYER}" defense rim protection',
    f'"{PLAYER}" shooting development',
    f'"{PLAYER}" playoff performance',
    # iter-2 additions per Phase B comparison report (2026-04-26):
    # surface 2024–26 beat coverage missed in iter-1.
    f'"{PLAYER}" Bucks 2025-26 season',
    f'"{PLAYER}" 2025 NBA Finals',
    f'"{PLAYER}" Pacers 2024-25 season',
]

ALLOWED_DOMAINS = (
    "espn.com",
    "bleacherreport.com",
    "theringer.com",
    "nba.com",
    "cbssports.com",
    "sports.yahoo.com",
    "nbadraft.net",
    "draftexpress.com",
    "si.com",
    "theathletic.com",  # most articles paywalled — kept to see what slips through
    "foxsports.com",
    "bball-index.com",
    # basketball-reference.com removed iter-2: playoff gamelog is a strict subset
    # of Playoff_Track_Record.py output (~16K tokens of pure stat tables).
    "8points9seconds.com",      # SB Nation Pacers
    "burntorangenation.com",    # SB Nation Texas (draft scouting)
    "hoopshype.com",
    "basketballnews.com",
)

app = FirecrawlApp(api_key=require_firecrawl_key())


def domain_of(url: str) -> str:
    return urlparse(url).netloc.lower().removeprefix("www.")


def allowed(url: str) -> bool:
    d = domain_of(url)
    return any(d == a or d.endswith("." + a) for a in ALLOWED_DOMAINS)


def unwrap(obj, key: str):
    """Handle both dict-shaped (older SDK) and pydantic-shaped (newer) responses."""
    if isinstance(obj, dict):
        return obj.get(key)
    return getattr(obj, key, None)


_TRACKING_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "fbclid", "gclid", "mc_eid", "mc_cid", "ref", "ref_", "ref_src",
    "share", "share_id", "_ga", "source", "amp",
}


def normalize(url: str) -> str:
    """Dedup key: lowercase host (strip www), drop tracking params, drop fragment + trailing slash."""
    p = urlparse(url)
    kept = [(k, v) for k, v in parse_qsl(p.query) if k.lower() not in _TRACKING_PARAMS]
    host = p.netloc.lower().removeprefix("www.")
    path = p.path.rstrip("/") or "/"
    return urlunparse((p.scheme.lower(), host, path, "", urlencode(kept), ""))


# 1) Search — collect candidate URLs
seen = set()
candidates: list[tuple[str, str]] = []
for q in QUERIES:
    print(f"[search] {q}")
    try:
        res = app.search(q, limit=5)
    except Exception as e:
        print(f"  search error: {e}")
        continue
    items = unwrap(res, "web") or unwrap(res, "data") or (res if isinstance(res, list) else [])
    for item in items:
        url = unwrap(item, "url")
        if url:
            print(f"    url={url}  allowed={allowed(url)}")
        if url and allowed(url):
            key = normalize(url)
            if key not in seen:
                seen.add(key)
                candidates.append((q, url))
    time.sleep(0.5)

print(f"[search] {len(candidates)} unique in-scope URLs")

# 2) Scrape each — save clean markdown to disk
saved: list[Path] = []
for i, (q, url) in enumerate(candidates, 1):
    print(f"[scrape] {i}/{len(candidates)} {url}")
    try:
        result = app.scrape(url, formats=["markdown"])
    except Exception as e:
        print(f"  scrape error: {e}")
        continue
    md = unwrap(result, "markdown") or ""
    if not md.strip():
        print("  (empty markdown — skipping)")
        continue
    domain_slug = re.sub(r"[^a-z0-9]+", "-", domain_of(url))[:40]
    path = OUT_DIR / f"{i:02d}_{domain_slug}.md"
    header = f"<!-- source: {url} -->\n<!-- query: {q} -->\n<!-- scraped: {TODAY} -->\n\n"
    path.write_text(header + md, encoding="utf-8")
    saved.append(path)

# 3) Summary
total_bytes = sum(p.stat().st_size for p in saved)
approx_tokens = total_bytes // 4  # rough — 1 token ≈ 4 chars for English text
print()
print("=== DONE ===")
print(f"Player:        {PLAYER}")
print(f"Queries run:   {len(QUERIES)}")
print(f"URLs scraped:  {len(saved)} / {len(candidates)}")
print(f"Output dir:    {OUT_DIR}")
print(f"Markdown size: {total_bytes:,} bytes  (~{approx_tokens:,} tokens)")
print()
print("Next: open the .md files and spot-check that scouting language is preserved.")
print("Then run scout-research Phase B against these local files only and compare.")
