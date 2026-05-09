"""
iq_motor_validation.py v1
Domain 8 (#24 Shot Selection, #26 Competitive Character) + Domain 7 supplement (#21 SpeedDistance)

Endpoints:
  1. LeagueDashPtShots — closest defender distance bands (shot quality distribution)
  2. LeagueDashPtShots — shot clock bands (shot clock discipline)
  3. LeagueDashPlayerClutch — clutch performance splits
  4. LeagueDashPtStats (SpeedDistance) — average speed, distance covered

2-season window: 2024-25 (current, weight 0.60) + 2023-24 (prior, weight 0.40)
Follows established pipeline pattern from defense_validation.py

Run locally via Claude Code — nba_api requires stats.nba.com access.
"""

import time
import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')  # EW-F04: prevent Windows cp1252 crash on non-ASCII player names
from datetime import date
from nba_api.stats.endpoints import (
    leaguedashplayerptshot,
    leaguedashplayerclutch,
    leaguedashptstats,
)
from nba_api.stats.static import players as nba_players

# === CONFIGURATION ===

# Evaluation window + player ID set by main() via eval_window.determine_evaluation_window
from eval_window import determine_evaluation_window, format_window
from config import SCRIPTS_DIR

PLAYERS = {}  # populated by main() from argparse
SEASONS = {}  # populated by main() from window: {season: weight}
_cur = None
_pri = None  # None triggers single-season path
W_CURRENT = 0.60
W_PRIOR = 0.40

DEFENDER_BANDS = [
    "0-2 Feet - Very Tight",
    "2-4 Feet - Tight",
    "4-6 Feet - Open",
    "6+ Feet - Wide Open",
]

SHOT_CLOCK_RANGES = [
    "24-22",
    "22-18 Very Early",
    "18-15 Early",
    "15-7 Average",
    "7-4 Late",
    "4-0 Very Late",
]

SLEEP = 1.0  # seconds between API calls to avoid rate limiting


# === HELPERS ===

def safe_div(num, den):
    """Safe division — returns 0.0 if denominator is 0."""
    return round(num / den, 3) if den else 0.0


def weighted_avg(current, prior, stat_key):
    """Weighted average using runtime W_CURRENT/W_PRIOR (set by main from eval_window)."""
    c = current.get(stat_key, 0) or 0
    p = prior.get(stat_key, 0) or 0
    return round(c * W_CURRENT + p * W_PRIOR, 3)


# === SECTION 1: CLOSEST DEFENDER DISTANCE ===

def pull_defender_distance_league(season, band):
    """Pull LeagueDashPlayerPtShot for one defender band / one season.
    Returns full dataframe for all players."""
    time.sleep(SLEEP)
    try:
        resp = leaguedashplayerptshot.LeagueDashPlayerPtShot(
            season=season,
            season_type_all_star="Regular Season",
            per_mode_simple="Totals",
            close_def_dist_range_nullable=band,
        )
        return resp.get_data_frames()[0]
    except Exception as e:
        print(f"    ERROR pulling defender distance {band} for {season}: {e}")
        return None


def extract_dd_player(df, player_id):
    """Extract one player's row from a defender distance dataframe."""
    if df is None or df.empty:
        return None
    row = df[df["PLAYER_ID"] == player_id]
    if row.empty:
        return None
    r = row.iloc[0]
    return {
        "FGA": int(r.get("FGA", 0) or 0),
        "FGA_FREQUENCY": float(r.get("FGA_FREQUENCY", 0) or 0),
        "FGM": int(r.get("FGM", 0) or 0),
        "FG_PCT": float(r.get("FG_PCT", 0) or 0),
        "FG3A": int(r.get("FG3A", 0) or 0),
        "FG3M": int(r.get("FG3M", 0) or 0),
        "FG3_PCT": float(r.get("FG3_PCT", 0) or 0),
        "EFG_PCT": float(r.get("EFG_PCT", 0) or 0),
    }


# === SECTION 2: SHOT CLOCK DISTRIBUTION ===

def pull_shot_clock_league(season, sc_range):
    """Pull LeagueDashPlayerPtShot for one shot clock range / one season."""
    time.sleep(SLEEP + 2.0)  # Extra delay — shot clock queries are slow
    try:
        resp = leaguedashplayerptshot.LeagueDashPlayerPtShot(
            season=season,
            season_type_all_star="Regular Season",
            per_mode_simple="Totals",
            shot_clock_range_nullable=sc_range,
        )
        return resp.get_data_frames()[0]
    except Exception as e:
        print(f"    ERROR pulling shot clock {sc_range} for {season}: {e}")
        return None


def extract_sc_player(df, player_id):
    """Extract one player's row from a shot clock dataframe."""
    if df is None or df.empty:
        return None
    row = df[df["PLAYER_ID"] == player_id]
    if row.empty:
        return None
    r = row.iloc[0]
    return {
        "FGA": int(r.get("FGA", 0) or 0),
        "FGA_FREQUENCY": float(r.get("FGA_FREQUENCY", 0) or 0),
        "FGM": int(r.get("FGM", 0) or 0),
        "FG_PCT": float(r.get("FG_PCT", 0) or 0),
        "EFG_PCT": float(r.get("EFG_PCT", 0) or 0),
    }


# === SECTION 3: CLUTCH STATS ===

def pull_clutch_stats(season):
    """Pull clutch stats (last 5 min, within 5 pts) for all players."""
    time.sleep(SLEEP)
    try:
        resp = leaguedashplayerclutch.LeagueDashPlayerClutch(
            season=season,
            season_type_all_star="Regular Season",
            per_mode_detailed="PerGame",
            clutch_time="Last 5 Minutes",
            ahead_behind="Ahead or Behind",
            point_diff=5,
        )
        df = resp.get_data_frames()[0]
        results = {}
        for _, row in df.iterrows():
            pid = row.get("PLAYER_ID")
            results[pid] = {
                "GP": int(row.get("GP", 0) or 0),
                "W": int(row.get("W", 0) or 0),
                "L": int(row.get("L", 0) or 0),
                "MIN": float(row.get("MIN", 0) or 0),
                "FGM": float(row.get("FGM", 0) or 0),
                "FGA": float(row.get("FGA", 0) or 0),
                "FG_PCT": float(row.get("FG_PCT", 0) or 0),
                "FG3M": float(row.get("FG3M", 0) or 0),
                "FG3A": float(row.get("FG3A", 0) or 0),
                "FG3_PCT": float(row.get("FG3_PCT", 0) or 0),
                "FTM": float(row.get("FTM", 0) or 0),
                "FTA": float(row.get("FTA", 0) or 0),
                "FT_PCT": float(row.get("FT_PCT", 0) or 0),
                "PTS": float(row.get("PTS", 0) or 0),
                "AST": float(row.get("AST", 0) or 0),
                "TOV": float(row.get("TOV", 0) or 0),
                "STL": float(row.get("STL", 0) or 0),
                "PLUS_MINUS": float(row.get("PLUS_MINUS", 0) or 0),
            }
        return results
    except Exception as e:
        print(f"  ERROR pulling clutch stats for {season}: {e}")
        return {}


# === SECTION 4: SPEED & DISTANCE ===

def pull_speed_distance(season):
    """Pull speed and distance data for all players."""
    time.sleep(SLEEP)
    try:
        resp = leaguedashptstats.LeagueDashPtStats(
            season=season,
            season_type_all_star="Regular Season",
            per_mode_simple="PerGame",
            pt_measure_type="SpeedDistance",
            player_or_team="Player",
        )
        df = resp.get_data_frames()[0]
        results = {}
        for _, row in df.iterrows():
            pid = row.get("PLAYER_ID")
            results[pid] = {
                "GP": int(row.get("GP", 0) or 0),
                "MIN": float(row.get("MIN", 0) or 0),
                "DIST_MILES": float(row.get("DIST_MILES", 0) or 0),
                "DIST_MILES_OFF": float(row.get("DIST_MILES_OFF", 0) or 0),
                "DIST_MILES_DEF": float(row.get("DIST_MILES_DEF", 0) or 0),
                "AVG_SPEED": float(row.get("AVG_SPEED", 0) or 0),
                "AVG_SPEED_OFF": float(row.get("AVG_SPEED_OFF", 0) or 0),
                "AVG_SPEED_DEF": float(row.get("AVG_SPEED_DEF", 0) or 0),
            }
        return results
    except Exception as e:
        print(f"  ERROR pulling speed/distance for {season}: {e}")
        return {}


# === MAIN ===

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

    match = nba_players.find_players_by_full_name(args.player)
    if not match:
        print(f"ERROR: Could not find player ID for '{args.player}'")
        sys.exit(1)
    PLAYERS[args.player] = match[0]["id"]

    global _cur, _pri, W_CURRENT, W_PRIOR
    if len(window.seasons_used) == 1:
        _cur = window.seasons_used[0][0]
        W_CURRENT = window.seasons_used[0][1]
        _pri = None
        W_PRIOR = 0.0
        SEASONS[_cur] = W_CURRENT
    else:
        _cur, W_CURRENT = window.seasons_used[0]
        _pri, W_PRIOR = window.seasons_used[1]
        SEASONS[_cur] = W_CURRENT
        SEASONS[_pri] = W_PRIOR

    all_results = {}

    # --- Pull league-wide data first ---
    print("=" * 60)
    print("PULLING LEAGUE-WIDE DATA")
    print("=" * 60)

    clutch_data = {}
    speed_data = {}
    dd_dfs = {}  # {season: {band: df}}
    sc_dfs = {}  # {season: {range: df}}

    for season in SEASONS:
        print(f"\n--- {season} ---")

        print("  Pulling clutch stats...")
        clutch_data[season] = pull_clutch_stats(season)
        print(f"  Got {len(clutch_data[season])} players")

        print("  Pulling speed/distance...")
        speed_data[season] = pull_speed_distance(season)
        print(f"  Got {len(speed_data[season])} players")

        print("  Pulling defender distance bands...")
        dd_dfs[season] = {}
        for band in DEFENDER_BANDS:
            dd_dfs[season][band] = pull_defender_distance_league(season, band)
            count = len(dd_dfs[season][band]) if dd_dfs[season][band] is not None else 0
            print(f"    {band}: {count} rows")

        print("  Pulling shot clock ranges...")
        sc_dfs[season] = {}
        for sc_range in SHOT_CLOCK_RANGES:
            sc_dfs[season][sc_range] = pull_shot_clock_league(season, sc_range)
            count = len(sc_dfs[season][sc_range]) if sc_dfs[season][sc_range] is not None else 0
            print(f"    {sc_range}: {count} rows")

    # --- Extract per-player data ---
    for name, pid in PLAYERS.items():
        print(f"\n{'=' * 60}")
        print(f"PLAYER: {name} (ID: {pid})")
        print(f"{'=' * 60}")

        player_result = {
            "player_name": name,
            "player_id": pid,
            "evaluation_window": {
                "mode": window.mode,
                "seasons_used": [{"season": s, "weight": w} for s, w in window.seasons_used],
                "flag_template": window.flag_template,
                "age_concern": window.age_concern,
            },
            "defender_distance": {},
            "shot_clock": {},
            "clutch": {},
            "speed_distance": {},
        }

        for season in SEASONS:
            print(f"\n  --- {season} ---")

            # Defender distance
            dd_season = {}
            for band in DEFENDER_BANDS:
                data = extract_dd_player(dd_dfs[season][band], pid)
                dd_season[band] = data
                if data:
                    print(f"    {band}: freq={data['FGA_FREQUENCY']:.1%}, FG%={data['FG_PCT']:.1%}, eFG%={data['EFG_PCT']:.1%}, FGA={data['FGA']}")
                else:
                    print(f"    {band}: NO DATA")
            player_result["defender_distance"][season] = dd_season

            # Shot clock
            sc_season = {}
            for sc_range in SHOT_CLOCK_RANGES:
                data = extract_sc_player(sc_dfs[season][sc_range], pid)
                sc_season[sc_range] = data
                if data:
                    print(f"    {sc_range}: freq={data['FGA_FREQUENCY']:.1%}, FG%={data['FG_PCT']:.1%}, FGA={data['FGA']}")
                else:
                    print(f"    {sc_range}: NO DATA")
            player_result["shot_clock"][season] = sc_season

            # Clutch
            clutch = clutch_data.get(season, {}).get(pid, {})
            player_result["clutch"][season] = clutch
            if clutch:
                print(f"  Clutch: {clutch.get('PTS', 0):.1f} PTS, {clutch.get('FG_PCT', 0):.1%} FG%, +/-={clutch.get('PLUS_MINUS', 0):.1f}, GP={clutch.get('GP', 0)}")
            else:
                print(f"  Clutch: NO DATA")

            # Speed/distance
            spd = speed_data.get(season, {}).get(pid, {})
            player_result["speed_distance"][season] = spd
            if spd:
                print(f"  Speed: {spd.get('DIST_MILES', 0):.2f} mi/g, avg={spd.get('AVG_SPEED', 0):.2f} mph, off={spd.get('AVG_SPEED_OFF', 0):.2f}, def={spd.get('AVG_SPEED_DEF', 0):.2f}")
            else:
                print(f"  Speed: NO DATA")

        all_results[name] = player_result

    # === SUMMARY TABLES ===

    print(f"\n{'=' * 60}")
    print("SUMMARY — DEFENDER DISTANCE DISTRIBUTION (2-season combined)")
    print(f"{'=' * 60}")
    print(f"\n{'Player':<18} {'VeryTight':<12} {'Tight':<12} {'Open':<12} {'WideOpen':<12} {'Contested%':<12}")
    print("-" * 78)

    for name, pid in PLAYERS.items():
        result = all_results[name]
        combined = {}
        for band in DEFENDER_BANDS:
            freqs = []
            for season, weight in SEASONS.items():
                dd = result["defender_distance"].get(season, {}).get(band)
                if dd:
                    freqs.append((dd.get("FGA_FREQUENCY", 0), weight))
            if freqs:
                combined[band] = sum(f * w for f, w in freqs) / sum(w for _, w in freqs)
            else:
                combined[band] = 0
        vt = combined.get("0-2 Feet - Very Tight", 0)
        t = combined.get("2-4 Feet - Tight", 0)
        o = combined.get("4-6 Feet - Open", 0)
        wo = combined.get("6+ Feet - Wide Open", 0)
        contested = vt + t
        print(f"{name:<18} {vt:>9.1%}   {t:>9.1%}   {o:>9.1%}   {wo:>9.1%}   {contested:>9.1%}")

    print(f"\n{'=' * 60}")
    print("SUMMARY — SHOT CLOCK DISTRIBUTION (2-season combined)")
    print(f"{'=' * 60}")
    print(f"\n{'Player':<18} {'24-22':<8} {'VEarly':<8} {'Early':<8} {'Avg':<8} {'Late':<8} {'VLate':<8}")
    print("-" * 66)

    for name, pid in PLAYERS.items():
        result = all_results[name]
        vals = []
        for sc_range in SHOT_CLOCK_RANGES:
            freqs = []
            for season, weight in SEASONS.items():
                sc = result["shot_clock"].get(season, {}).get(sc_range)
                if sc:
                    freqs.append((sc.get("FGA_FREQUENCY", 0), weight))
            if freqs:
                vals.append(sum(f * w for f, w in freqs) / sum(w for _, w in freqs))
            else:
                vals.append(0)
        print(f"{name:<18} {vals[0]:>5.1%}   {vals[1]:>5.1%}   {vals[2]:>5.1%}   {vals[3]:>5.1%}   {vals[4]:>5.1%}   {vals[5]:>5.1%}")

    print(f"\n{'=' * 60}")
    print("SUMMARY — CLUTCH STATS (2-season weighted)")
    print(f"{'=' * 60}")
    print(f"\n{'Player':<18} {'GP':<6} {'PTS':<8} {'FG%':<8} {'3P%':<8} {'FT%':<8} {'+/-':<8} {'AST':<6} {'TOV':<6}")
    print("-" * 74)

    for name, pid in PLAYERS.items():
        result = all_results[name]
        c = result["clutch"].get(_cur, {})
        p = result["clutch"].get(_pri, {})
        gp = (c.get("GP", 0) or 0) + (p.get("GP", 0) or 0)
        pts = weighted_avg(c, p, "PTS")
        fg_pct = weighted_avg(c, p, "FG_PCT")
        fg3_pct = weighted_avg(c, p, "FG3_PCT")
        ft_pct = weighted_avg(c, p, "FT_PCT")
        pm = weighted_avg(c, p, "PLUS_MINUS")
        ast = weighted_avg(c, p, "AST")
        tov = weighted_avg(c, p, "TOV")
        print(f"{name:<18} {gp:<6} {pts:<8.1f} {fg_pct:<8.1%} {fg3_pct:<8.1%} {ft_pct:<8.1%} {pm:<8.1f} {ast:<6.1f} {tov:<6.1f}")

    print(f"\n{'=' * 60}")
    print("SUMMARY — SPEED & DISTANCE (2-season weighted)")
    print(f"{'=' * 60}")
    print(f"\n{'Player':<18} {'Dist(mi)':<10} {'AvgSpd':<10} {'OffSpd':<10} {'DefSpd':<10} {'OffDist':<10} {'DefDist':<10}")
    print("-" * 78)

    for name, pid in PLAYERS.items():
        result = all_results[name]
        c = result["speed_distance"].get(_cur, {})
        p = result["speed_distance"].get(_pri, {})
        dist = weighted_avg(c, p, "DIST_MILES")
        avg_spd = weighted_avg(c, p, "AVG_SPEED")
        off_spd = weighted_avg(c, p, "AVG_SPEED_OFF")
        def_spd = weighted_avg(c, p, "AVG_SPEED_DEF")
        off_dist = weighted_avg(c, p, "DIST_MILES_OFF")
        def_dist = weighted_avg(c, p, "DIST_MILES_DEF")
        print(f"{name:<18} {dist:<10.2f} {avg_spd:<10.2f} {off_spd:<10.2f} {def_spd:<10.2f} {off_dist:<10.2f} {def_dist:<10.2f}")

    # === SAVE JSON ===
    save_path = SCRIPTS_DIR / "iq_motor_output.json"
    with open(save_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nRaw data saved to {save_path}")

    print(f"\n{'=' * 60}")
    print("SCRIPT COMPLETE")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
