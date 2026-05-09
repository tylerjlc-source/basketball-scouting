"""Disk cache for league-wide nba_api endpoint calls.

Wraps the LeagueDash* / LeagueHustle* / SynergyPlayTypes endpoints with a
JSON-on-disk cache keyed by (class name + canonical kwargs). When scouting
multiple players in a batch, the same league-wide stats only fetch once per
(season, params) per TTL window — cuts wall-clock and rate-limit pressure
without changing observable script behavior.

Player-keyed endpoints (playercareerstats, shotchartdetail, playerdashboard*)
bypass this cache by design: they are already player-specific, the same
player is rarely re-scouted within a batch, and the on-disk cache for
hundreds of players would not pay back the disk + invalidation cost.

Usage:

    from nba_api.stats.endpoints import leaguedashplayerstats
    from _league_cache import cached_call

    data = cached_call(
        leaguedashplayerstats.LeagueDashPlayerStats,
        season="2024-25",
        measure_type_detailed_defense="Advanced",
        per_mode_detailed="PerGame",
        season_type_all_star="Regular Season",
    )
    rows = data["LeagueDashPlayerStats"]

The returned value is identical to
`endpoint_class(**kwargs).get_normalized_dict()`.

Cache layout: `scripts/.cache/{season}/{ClassName}_{16hex}.json`. Manual
purge: delete `scripts/.cache/`. Per-call bypass: `cached_call(..., ttl_hours=0)`.
Process-wide bypass: set env var `BBSCOUT_NO_CACHE=1`.
"""
from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path
from typing import Any

from config import SCRIPTS_DIR

CACHE_DIR: Path = SCRIPTS_DIR / ".cache"
DEFAULT_TTL_HOURS = 24
DELAY_SECONDS = 1.5
NO_CACHE_ENV = "BBSCOUT_NO_CACHE"

_EXCLUDED_KEYS = {"timeout", "headers", "proxy"}


def _cache_key(class_name: str, kwargs: dict[str, Any]) -> str:
    canonical = sorted(
        (k, v) for k, v in kwargs.items() if k not in _EXCLUDED_KEYS
    )
    blob = json.dumps(canonical, default=str, sort_keys=True)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


def _cache_path(class_name: str, kwargs: dict[str, Any], key: str) -> Path:
    season = kwargs.get("season") or kwargs.get("season_id") or "_no_season"
    safe_season = str(season).replace("/", "-")
    return CACHE_DIR / safe_season / f"{class_name}_{key}.json"


def _is_fresh(path: Path, ttl_seconds: int) -> bool:
    if not path.is_file():
        return False
    age = time.time() - path.stat().st_mtime
    return age < ttl_seconds


def _cache_disabled(ttl_hours: int) -> bool:
    if ttl_hours <= 0:
        return True
    val = os.environ.get(NO_CACHE_ENV, "").strip().lower()
    return val in ("1", "true", "yes", "on")


def cached_call(
    endpoint_class: type,
    *,
    ttl_hours: int = DEFAULT_TTL_HOURS,
    **kwargs: Any,
) -> dict[str, Any]:
    """Call an nba_api endpoint, returning .get_normalized_dict() (with caching).

    On cache hit: read JSON from disk, return immediately, no API call, no delay.
    On cache miss: call the endpoint, sleep DELAY_SECONDS (polite client),
    write the response to disk, return.

    Args:
        endpoint_class: An nba_api endpoint class (e.g.
            `leaguedashplayerstats.LeagueDashPlayerStats`).
        ttl_hours: Cache TTL in hours. Default 24h. Pass 0 to force a fresh
            fetch (and skip writing the cache for this call).
        **kwargs: Passed verbatim to the endpoint class constructor. The
            kwargs `timeout`, `headers`, `proxy` are excluded from the cache
            key (they don't affect response shape).

    Returns:
        The dict from `.get_normalized_dict()` — table names → list-of-rows.
    """
    class_name = endpoint_class.__name__
    key = _cache_key(class_name, kwargs)
    path = _cache_path(class_name, kwargs, key)

    use_cache = not _cache_disabled(ttl_hours)
    ttl_seconds = ttl_hours * 3600

    if use_cache and _is_fresh(path, ttl_seconds):
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)

    resp = endpoint_class(**kwargs)
    data = resp.get_normalized_dict()
    time.sleep(DELAY_SECONDS)

    if use_cache:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(path.suffix + ".tmp")
        with tmp.open("w", encoding="utf-8") as f:
            json.dump(data, f)
        tmp.replace(path)

    return data


def cached_call_df(
    endpoint_class: type,
    *,
    table_index: int = 0,
    ttl_hours: int = DEFAULT_TTL_HOURS,
    **kwargs: Any,
):
    """Drop-in replacement for `endpoint_class(**kwargs).get_data_frames()[table_index]`.

    Returns a `pandas.DataFrame` constructed from the cached rows. Column
    dtypes are inferred from the row data (pandas default), which matches
    the live endpoint output for numeric/string columns. Rare dtype-edge
    cases (e.g. all-None columns) may differ from the live frame; downstream
    `.get(col)` access is unaffected.
    """
    import pandas as pd

    data = cached_call(endpoint_class, ttl_hours=ttl_hours, **kwargs)
    tables = list(data.values())
    if not tables:
        return pd.DataFrame()
    rows = tables[table_index]
    return pd.DataFrame(rows)


def cached_call_frames(
    endpoint_class: type,
    *,
    ttl_hours: int = DEFAULT_TTL_HOURS,
    **kwargs: Any,
):
    """Drop-in replacement for `endpoint_class(**kwargs).get_data_frames()`.

    Returns a list of `pandas.DataFrame` matching the live endpoint output
    table order.
    """
    import pandas as pd

    data = cached_call(endpoint_class, ttl_hours=ttl_hours, **kwargs)
    return [pd.DataFrame(rows) for rows in data.values()]


def purge_cache() -> int:
    """Delete the entire on-disk cache. Returns count of files removed."""
    if not CACHE_DIR.is_dir():
        return 0
    count = 0
    for p in CACHE_DIR.rglob("*.json"):
        p.unlink()
        count += 1
    return count


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--purge":
        n = purge_cache()
        print(f"Purged {n} cached file(s) from {CACHE_DIR}")
    else:
        print(f"League cache directory: {CACHE_DIR}")
        if CACHE_DIR.is_dir():
            files = list(CACHE_DIR.rglob("*.json"))
            total_bytes = sum(f.stat().st_size for f in files)
            print(f"Cached files: {len(files)}")
            print(f"Total size:   {total_bytes / 1024:.1f} KiB")
        else:
            print("Cache directory does not exist (no calls cached yet).")
