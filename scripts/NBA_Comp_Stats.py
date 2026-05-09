"""
NBA Comp Stats — Pulls statistical similarity data for NBA Comp matching.
Used by Skill 5 (scout-output) to run the NBA Comp Methodology.

Pulls from LeagueDashPlayerStats (Advanced) + PlayerCareerStats:
  - True Shooting % (primary signal, all groups)
  - Usage rate (secondary, all groups)
  - Assist rate (secondary, Guards)
  - Turnover rate (secondary, Guards)
  - Rebound rate (secondary, Wings + Bigs)
  - Steal rate (secondary, Wings)
  - Block rate (secondary, Bigs)
  - PPG (fallback when TS% unavailable)

Usage:
  python NBA_Comp_Stats.py 'Player Name'                # rookie season (default)
  python NBA_Comp_Stats.py 'Player Name' --current      # current season
  python NBA_Comp_Stats.py 'Player Name' --season 2022-23  # specific season
"""

import sys
import json
import os
import time
from datetime import date
from nba_api.stats.static import players as nba_players
from nba_api.stats.endpoints import (
    leaguedashplayerstats,
    playercareerstats,
)

from config import SCRIPTS_DIR

DELAY = 1.5  # seconds between API calls


# ── Season auto-detection ──────────────────────────────────────────────

def current_season_string():
    _year, _month = date.today().year, date.today().month
    if _month >= 10:
        return f"{_year}-{str(_year + 1)[-2:]}"
    else:
        return f"{_year - 1}-{str(_year)[-2:]}"


# ── Player ID lookup ───────────────────────────────────────────────────

def find_player_id(full_name):
    matches = nba_players.find_players_by_full_name(full_name)
    if matches:
        return matches[0]["id"]
    return None


# ── Rookie season detection ────────────────────────────────────────────

def find_rookie_season(player_id):
    """Find the player's first NBA regular-season entry."""
    time.sleep(DELAY)
    career = playercareerstats.PlayerCareerStats(
        player_id=player_id,
        per_mode36="PerGame",
    )
    df = career.get_data_frames()[0]  # SeasonTotalsRegularSeason
    if df.empty:
        return None
    # Sort by season ascending, take first
    df = df.sort_values("SEASON_ID", ascending=True)
    first = df.iloc[0]
    return first["SEASON_ID"]


# ── Pull Advanced stats for a season ───────────────────────────────────

def pull_advanced_stats(player_id, season):
    """Pull Advanced stats from LeagueDashPlayerStats for one season."""
    time.sleep(DELAY)
    resp = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season,
        measure_type_detailed_defense="Advanced",
        per_mode_detailed="PerGame",
    )
    rows = resp.get_dict()["resultSets"][0]
    headers = rows["headers"]
    data = rows["rowSet"]

    for row in data:
        row_dict = dict(zip(headers, row))
        if row_dict.get("PLAYER_ID") == player_id:
            return row_dict
    return None


# ── Pull Base stats for PPG fallback ───────────────────────────────────

def pull_base_stats(player_id, season):
    """Pull Base stats for PPG fallback."""
    time.sleep(DELAY)
    resp = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season,
        measure_type_detailed_defense="Base",
        per_mode_detailed="PerGame",
    )
    rows = resp.get_dict()["resultSets"][0]
    headers = rows["headers"]
    data = rows["rowSet"]

    for row in data:
        row_dict = dict(zip(headers, row))
        if row_dict.get("PLAYER_ID") == player_id:
            return row_dict
    return None


# ── Safe extraction ────────────────────────────────────────────────────

def safe_pct(val):
    """Convert decimal rate to percentage (0.567 -> 56.7)."""
    if val is None or val == 0:
        return None
    return round(float(val) * 100, 1)


def safe_float(val, decimals=1):
    if val is None:
        return None
    return round(float(val), decimals)


# ── Build comp stat profile ────────────────────────────────────────────

def build_comp_profile(player_name, player_id, season):
    """Build the full comp stat profile for one player-season."""
    adv = pull_advanced_stats(player_id, season)
    base = pull_base_stats(player_id, season)

    if not adv:
        return {
            "player": player_name,
            "season": season,
            "error": f"No advanced stats found for {season}",
        }

    gp = adv.get("GP", 0)
    min_pg = safe_float(adv.get("MIN"))

    profile = {
        "player": player_name,
        "player_id": player_id,
        "season": season,
        "games_played": gp,
        "minutes_per_game": min_pg,

        # === PRIMARY SIGNAL (all groups) ===
        "ts_pct": safe_pct(adv.get("TS_PCT")),

        # === SECONDARY SIGNALS ===
        "usg_pct": safe_pct(adv.get("USG_PCT")),
        "ast_pct": safe_pct(adv.get("AST_PCT")),
        "tov_pct": safe_pct(adv.get("TOV_PCT")),
        "oreb_pct": safe_pct(adv.get("OREB_PCT")),
        "dreb_pct": safe_pct(adv.get("DREB_PCT")),
        "reb_pct": safe_pct(adv.get("REB_PCT")),  # total
        "stl_pct": safe_pct(adv.get("STL_PCT")),  # note: may not exist in all endpoints
        "blk_pct": safe_pct(adv.get("BLK_PCT")),  # note: may not exist in all endpoints

        # === FALLBACK ===
        "ppg": safe_float(base.get("PTS")) if base else None,

        # === GROUP-SPECIFIC STAT SETS (for comp matching) ===
        "guard_stats": {
            "primary": safe_pct(adv.get("TS_PCT")),
            "usage": safe_pct(adv.get("USG_PCT")),
            "ast_rate": safe_pct(adv.get("AST_PCT")),
            "tov_rate": safe_pct(adv.get("TOV_PCT")),
        },
        "wing_stats": {
            "primary": safe_pct(adv.get("TS_PCT")),
            "usage": safe_pct(adv.get("USG_PCT")),
            "reb_rate": safe_pct(adv.get("REB_PCT")),
            "stl_rate": safe_pct(adv.get("STL_PCT")),
        },
        "big_stats": {
            "primary": safe_pct(adv.get("TS_PCT")),
            "usage": safe_pct(adv.get("USG_PCT")),
            "reb_rate": safe_pct(adv.get("REB_PCT")),
            "blk_rate": safe_pct(adv.get("BLK_PCT")),
        },

        # === TOLERANCE BANDS (from NBA-COMP-METHODOLOGY.md) ===
        "tolerance_bands": {
            "ts_pct": 5.0,
            "ppg": 4.0,
            "usg_pct": 5.0,
            "ast_pct": 4.0,
            "tov_pct": 2.0,
            "reb_pct": 5.0,
            "stl_pct": 1.5,
            "blk_pct": 2.0,
        },
    }

    return profile


# ── Display ────────────────────────────────────────────────────────────

def print_profile(profile):
    if "error" in profile:
        print(f"\n  ERROR: {profile['error']}")
        return

    print(f"\n{'='*60}")
    print(f"NBA COMP STATS — {profile['player']}")
    print(f"Season: {profile['season']}  |  GP: {profile['games_played']}  |  MIN: {profile['minutes_per_game']}")
    print(f"{'='*60}")

    print(f"\n  Primary Signal:")
    print(f"    TS%:  {profile['ts_pct']}%")
    if profile.get("ppg"):
        print(f"    PPG:  {profile['ppg']}  (fallback)")

    print(f"\n  Secondary Signals:")
    print(f"    USG%: {profile['usg_pct']}%")
    print(f"    AST%: {profile['ast_pct']}%")
    print(f"    TOV%: {profile['tov_pct']}%")
    print(f"    REB%: {profile['reb_pct']}%  (OREB: {profile['oreb_pct']}%  DREB: {profile['dreb_pct']}%)")
    print(f"    STL%: {profile['stl_pct']}%")
    print(f"    BLK%: {profile['blk_pct']}%")

    print(f"\n  Group-Specific Sets:")
    g = profile["guard_stats"]
    print(f"    Guards: TS% {g['primary']}  USG% {g['usage']}  AST% {g['ast_rate']}  TOV% {g['tov_rate']}")
    w = profile["wing_stats"]
    print(f"    Wings:  TS% {w['primary']}  USG% {w['usage']}  REB% {w['reb_rate']}  STL% {w['stl_rate']}")
    b = profile["big_stats"]
    print(f"    Bigs:   TS% {b['primary']}  USG% {b['usage']}  REB% {b['reb_rate']}  BLK% {b['blk_rate']}")

    print(f"\n{'='*60}")


# ── Main ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python NBA_Comp_Stats.py 'Player Name'              # rookie season")
        print("  python NBA_Comp_Stats.py 'Player Name' --current    # current season")
        print("  python NBA_Comp_Stats.py 'Player Name' --season 2022-23  # specific season")
        sys.exit(1)

    player_name = sys.argv[1]
    player_id = find_player_id(player_name)

    if not player_id:
        print(f"ERROR: Could not find player '{player_name}'")
        sys.exit(1)

    print(f"Player: {player_name} (ID: {player_id})")

    # Determine season
    mode = "rookie"
    target_season = None

    if "--current" in sys.argv:
        mode = "current"
        target_season = current_season_string()
    elif "--season" in sys.argv:
        mode = "specific"
        idx = sys.argv.index("--season")
        if idx + 1 < len(sys.argv):
            target_season = sys.argv[idx + 1]
        else:
            print("ERROR: --season requires a season string (e.g. 2022-23)")
            sys.exit(1)
    else:
        # Default: rookie season
        print("Finding rookie season...")
        target_season = find_rookie_season(player_id)
        if not target_season:
            print(f"ERROR: Could not find career data for {player_name}")
            sys.exit(1)

    print(f"Mode: {mode}  |  Season: {target_season}")
    print("Pulling stats...")

    profile = build_comp_profile(player_name, player_id, target_season)
    print_profile(profile)

    # Save JSON
    save_path = SCRIPTS_DIR / "comp_stats_output.json"
    with open(save_path, "w") as f:
        json.dump(profile, f, indent=2, default=str)
    print(f"\nRaw data saved to {save_path}")
