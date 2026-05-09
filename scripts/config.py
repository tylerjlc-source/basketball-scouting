"""
Project-wide configuration: filesystem paths and external-service credentials.

All scripts in `scripts/` should import paths from here rather than computing
them with `Path(__file__).resolve().parent.parent` or hardcoding the project
root. That keeps the project portable to a server, container, or another
machine without source edits.

Defaults preserve today's behavior (everything resolves relative to the
repo root, which is the parent of this file's directory).

Overrides are read from environment variables. The most useful one is
`BBSCOUT_ROOT` — set it to point the whole tree somewhere else, e.g. a
test fixture or a deployment mount. Per-directory overrides are also
available for the rare case where one subtree lives elsewhere
(`BBSCOUT_RAW_DIR`, `BBSCOUT_OUTPUT_DIR`, etc.).

Secrets (`FIRECRAWL_API_KEY`) are read from env only; never hardcode.
See `.env.example` in the repo root for the full list.
"""

from __future__ import annotations

import os
from pathlib import Path

_DEFAULT_ROOT = Path(__file__).resolve().parent.parent


def _path_env(var: str, default: Path) -> Path:
    raw = os.environ.get(var)
    return Path(raw).expanduser().resolve() if raw else default


PROJECT_ROOT: Path = _path_env("BBSCOUT_ROOT", _DEFAULT_ROOT)

SCRIPTS_DIR: Path = _path_env("BBSCOUT_SCRIPTS_DIR", PROJECT_ROOT / "scripts")
RAW_DIR: Path = _path_env("BBSCOUT_RAW_DIR", PROJECT_ROOT / "raw")
OUTPUT_DIR: Path = _path_env("BBSCOUT_OUTPUT_DIR", PROJECT_ROOT / "output")
WIKI_DIR: Path = _path_env("BBSCOUT_WIKI_DIR", PROJECT_ROOT / "wiki")
DOCS_DIR: Path = _path_env("BBSCOUT_DOCS_DIR", PROJECT_ROOT / "docs")
PUBLISHED_DIR: Path = _path_env("BBSCOUT_PUBLISHED_DIR", PROJECT_ROOT / "published")
AUDITS_DIR: Path = _path_env("BBSCOUT_AUDITS_DIR", PUBLISHED_DIR / "audits")

FIRECRAWL_API_KEY: str | None = os.environ.get("FIRECRAWL_API_KEY")


def require_firecrawl_key() -> str:
    """Return the Firecrawl API key or raise with a helpful message."""
    if not FIRECRAWL_API_KEY:
        raise RuntimeError(
            "FIRECRAWL_API_KEY is not set. Export it in your shell, e.g.:\n"
            '  PowerShell:  $env:FIRECRAWL_API_KEY = "fc-..."\n'
            '  bash:        export FIRECRAWL_API_KEY=fc-...\n'
            "See .env.example for the full list of supported variables."
        )
    return FIRECRAWL_API_KEY


if __name__ == "__main__":
    # Quick `python scripts/config.py` sanity check.
    print(f"PROJECT_ROOT  = {PROJECT_ROOT}")
    print(f"SCRIPTS_DIR   = {SCRIPTS_DIR}")
    print(f"RAW_DIR       = {RAW_DIR}")
    print(f"OUTPUT_DIR    = {OUTPUT_DIR}")
    print(f"WIKI_DIR      = {WIKI_DIR}")
    print(f"DOCS_DIR      = {DOCS_DIR}")
    print(f"PUBLISHED_DIR = {PUBLISHED_DIR}")
    print(f"AUDITS_DIR    = {AUDITS_DIR}")
    print(f"FIRECRAWL_API_KEY set? {'yes' if FIRECRAWL_API_KEY else 'no'}")
