"""
rebounding_validation.py — Domain 6: Rebounding
Pulls rebounding data for guard validation set.
2-season window with 60/40 recency weighting.

Endpoints:
1. LeagueDashPlayerStats (Advanced) — OREB_PCT, DREB_PCT, REB_PCT
2. LeagueDashPlayerStats (Base) — raw OREB, DREB, REB, GP, MIN
3. LeagueDashPtStats (Rebounding) — contested/uncontested splits, rebound chances
4. LeagueHustleStatsPlayer — box-outs (offensive + defensive)

Players: Kyrie Irving, De'Aaron Fox, Marcus Smart, Buddy Hield
"""

import time
import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')  # EW-F04: prevent Windows cp1252 crash on non-ASCII player names
from datetime import date
from nba_api.stats.endpoints import (
    leaguedashplayerstats,
    leaguedashptstats,
    leaguehustlestatsplayer,
)
from nba_api.stats.static import players as nba_players

# --- CONFIG ---
# Evaluation window + player ID set by main() via eval_window.determine_evaluation_window
from eval_window import determine_evaluation_window, format_window

PLAYERS = {}  # populated by main() from argparse
SEASONS = []  # populated by main() from window

DELAY = 3  # seconds between API calls


def get_player_row(rows, player_id):
    """Find a player's row by ID from API results."""
    for row in rows:
        if row.get("PLAYER_ID") == player_id:
            return row
    return None


# safe_get lives in shared_math; the canonical version is more permissive
# (handles row[key] for non-dict-like rows) but identical for dict-like rows.
from shared_math import safe_get


def pull_advanced_stats(season):
    """Pull OREB_PCT, DREB_PCT, REB_PCT from LeagueDashPlayerStats (Advanced)."""
    print(f"  Pulling Advanced stats for {season}...")
    resp = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season,
        measure_type_detailed_defense="Advanced",
        per_mode_detailed="PerGame",
        season_type_all_star="Regular Season",
    )
    time.sleep(DELAY)
    return resp.get_normalized_dict()["LeagueDashPlayerStats"]


def pull_base_stats(season):
    """Pull raw OREB, DREB, REB, GP, MIN from LeagueDashPlayerStats (Base)."""
    print(f"  Pulling Base stats for {season}...")
    resp = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season,
        measure_type_detailed_defense="Base",
        per_mode_detailed="PerGame",
        season_type_all_star="Regular Season",
    )
    time.sleep(DELAY)
    return resp.get_normalized_dict()["LeagueDashPlayerStats"]


def pull_tracking_rebounding(season):
    """Pull contested/uncontested splits and rebound chances from LeagueDashPtStats (Rebounding)."""
    print(f"  Pulling Tracking Rebounding for {season}...")
    resp = leaguedashptstats.LeagueDashPtStats(
        season=season,
        pt_measure_type="Rebounding",
        per_mode_simple="PerGame",
        player_or_team="Player",
        season_type_all_star="Regular Season",
    )
    time.sleep(DELAY)
    return resp.get_normalized_dict()["LeagueDashPtStats"]


def pull_hustle_stats(season):
    """Pull box-out data from LeagueHustleStatsPlayer."""
    print(f"  Pulling Hustle stats for {season}...")
    resp = leaguehustlestatsplayer.LeagueHustleStatsPlayer(
        season=season,
        per_mode_time="PerGame",
        season_type_all_star="Regular Season",
    )
    time.sleep(DELAY)
    return resp.get_normalized_dict()["HustleStatsPlayer"]


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("player")
    parser.add_argument("--current-season", help="Override current season (e.g. '2021-22')")
    parser.add_argument("--season-override", help="Force a specific season at 100%% weight")
    args = parser.parse_args()

    window = determine_evaluation_window(
        player_name=args.player,
        season_override=args.season_override,
        current_season_override=args.current_season,
    )
    print(format_window(window))
    print()

    if window.mode == "INSUFFICIENT_DATA":
        print(f"ERROR: {window.flag_template}", file=sys.stderr)
        sys.exit(1)

    # Resolve player ID
    match = nba_players.find_players_by_full_name(args.player)
    if not match:
        print(f"ERROR: Could not find player ID for '{args.player}'")
        sys.exit(1)
    PLAYERS[args.player] = match[0]["id"]

    # Populate SEASONS from window
    for i, (s, w) in enumerate(window.seasons_used):
        label = "Current" if i == 0 else "Prior"
        SEASONS.append({"season": s, "weight": w, "label": f"{label} ({s})"})

    print("=" * 70)
    print("DOMAIN 6: REBOUNDING")
    if len(SEASONS) == 1:
        print(f"Single-season mode: {SEASONS[0]['season']} (w={SEASONS[0]['weight']})")
    else:
        print(f"2-season window: {SEASONS[0]['season']} (w={SEASONS[0]['weight']}) + {SEASONS[1]['season']} (w={SEASONS[1]['weight']})")
    print("=" * 70)

    # Collect all data per season
    all_data = {}

    for s in SEASONS:
        season = s["season"]
        print(f"\n--- {s['label']} ({season}) ---")

        try:
            advanced = pull_advanced_stats(season)
        except Exception as e:
            print(f"  ERROR pulling Advanced: {e}")
            advanced = []

        try:
            base = pull_base_stats(season)
        except Exception as e:
            print(f"  ERROR pulling Base: {e}")
            base = []

        try:
            tracking = pull_tracking_rebounding(season)
        except Exception as e:
            print(f"  ERROR pulling Tracking Rebounding: {e}")
            tracking = []

        try:
            hustle = pull_hustle_stats(season)
        except Exception as e:
            print(f"  ERROR pulling Hustle: {e}")
            hustle = []

        all_data[season] = {
            "advanced": advanced,
            "base": base,
            "tracking": tracking,
            "hustle": hustle,
        }

    # --- OUTPUT ---
    print("\n" + "=" * 70)
    print("RESULTS BY PLAYER")
    print("=" * 70)

    all_profiles = []

    for name, pid in PLAYERS.items():
        print(f"\n{'='*50}")
        print(f"  {name} (ID: {pid})")
        print(f"{'='*50}")

        profile = {
            "player": name,
            "evaluation_window": {
                "mode": window.mode,
                "seasons_used": [{"season": s["season"], "weight": s["weight"]} for s in SEASONS],
                "flag_template": window.flag_template,
                "age_concern": window.age_concern,
            },
            "seasons": {},
        }

        for s in SEASONS:
            season = s["season"]
            label = s["label"]
            weight = s["weight"]
            data = all_data[season]

            adv_row = get_player_row(data["advanced"], pid)
            base_row = get_player_row(data["base"], pid)
            trk_row = get_player_row(data["tracking"], pid)
            hst_row = get_player_row(data["hustle"], pid)

            print(f"\n  --- {label} (weight: {weight}) ---")

            # Base stats
            gp = safe_get(base_row, "GP", "N/A")
            mpg = safe_get(base_row, "MIN", "N/A")
            oreb = safe_get(base_row, "OREB", "N/A")
            dreb = safe_get(base_row, "DREB", "N/A")
            reb = safe_get(base_row, "REB", "N/A")
            print(f"  GP: {gp} | MPG: {mpg}")
            print(f"  OREB/g: {oreb} | DREB/g: {dreb} | REB/g: {reb}")

            # Advanced stats
            oreb_pct = safe_get(adv_row, "OREB_PCT", "N/A")
            dreb_pct = safe_get(adv_row, "DREB_PCT", "N/A")
            reb_pct = safe_get(adv_row, "REB_PCT", "N/A")
            print(f"  OREB%: {oreb_pct} | DREB%: {dreb_pct} | REB%: {reb_pct}")

            # Tracking rebounding
            print(f"  --- Tracking (Contested/Uncontested) ---")
            trk_data = {}
            if trk_row:
                reb_keys = [k for k in trk_row.keys() if any(
                    term in k.upper() for term in ["REB", "OREB", "DREB", "CONTEST", "UNCONTEST", "CHANCE"]
                ) and k not in ("PLAYER_ID", "PLAYER_NAME", "TEAM_ID", "TEAM_ABBREVIATION")]
                for k in sorted(reb_keys):
                    print(f"    {k}: {trk_row[k]}")
                    trk_data[k] = trk_row[k]
                if not reb_keys:
                    print(f"    Available keys: {list(trk_row.keys())}")
            else:
                print(f"    No tracking data found")

            # Hustle stats (box-outs)
            print(f"  --- Hustle (Box-Outs) ---")
            hst_data = {}
            if hst_row:
                box_keys = [k for k in hst_row.keys() if "BOX" in k.upper()]
                for k in sorted(box_keys):
                    print(f"    {k}: {hst_row[k]}")
                    hst_data[k] = hst_row[k]
                if not box_keys:
                    print(f"    No BOX keys found. Available: {list(hst_row.keys())}")
            else:
                print(f"    No hustle data found")

            # Store season data in profile
            profile["seasons"][season] = {
                "base": {
                    "gp": gp, "mpg": mpg,
                    "oreb_pg": oreb, "dreb_pg": dreb, "reb_pg": reb,
                },
                "advanced": {
                    "oreb_pct": oreb_pct, "dreb_pct": dreb_pct, "reb_pct": reb_pct,
                },
                "tracking": trk_data,
                "hustle": hst_data,
            }

        # --- WEIGHTED COMPOSITE for this player ---
        oreb_vals, dreb_vals, reb_vals = [], [], []
        oreb_pct_vals, dreb_pct_vals = [], []

        for s in SEASONS:
            season = s["season"]
            weight = s["weight"]
            data = all_data[season]

            base_row = get_player_row(data["base"], pid)
            adv_row = get_player_row(data["advanced"], pid)

            if base_row:
                oreb_v = safe_get(base_row, "OREB")
                dreb_v = safe_get(base_row, "DREB")
                reb_v = safe_get(base_row, "REB")
                if oreb_v is not None:
                    oreb_vals.append((oreb_v, weight))
                if dreb_v is not None:
                    dreb_vals.append((dreb_v, weight))
                if reb_v is not None:
                    reb_vals.append((reb_v, weight))

            if adv_row:
                op = safe_get(adv_row, "OREB_PCT")
                dp = safe_get(adv_row, "DREB_PCT")
                if op is not None:
                    oreb_pct_vals.append((op, weight))
                if dp is not None:
                    dreb_pct_vals.append((dp, weight))

        def weighted_avg(vals):
            if not vals:
                return "N/A"
            total_w = sum(w for _, w in vals)
            if total_w == 0:
                return "N/A"
            return round(sum(v * w for v, w in vals) / total_w, 3)

        w_oreb = weighted_avg(oreb_vals)
        w_dreb = weighted_avg(dreb_vals)
        w_reb = weighted_avg(reb_vals)
        w_oreb_pct = weighted_avg(oreb_pct_vals)
        w_dreb_pct = weighted_avg(dreb_pct_vals)

        profile["weighted"] = {
            "oreb_pg": w_oreb,
            "dreb_pg": w_dreb,
            "reb_pg": w_reb,
            "oreb_pct": w_oreb_pct,
            "dreb_pct": w_dreb_pct,
        }

        all_profiles.append(profile)

    # --- WEIGHTED COMPOSITE SUMMARY ---
    print("\n" + "=" * 70)
    print("WEIGHTED COMPOSITE (60/40)")
    print("=" * 70)

    for p in all_profiles:
        w = p["weighted"]
        print(f"\n  {p['player']}:")
        print(f"    OREB/g: {w['oreb_pg']} | DREB/g: {w['dreb_pg']} | REB/g: {w['reb_pg']}")
        print(f"    OREB%: {w['oreb_pct']} | DREB%: {w['dreb_pct']}")

    # --- SAVE JSON ---
    save_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "rebounding_output.json",
    )
    with open(save_path, "w") as f:
        json.dump(all_profiles, f, indent=2, default=str)
    print(f"\nRaw data saved to {save_path}")

    print("\n" + "=" * 70)
    print("SCRIPT COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
