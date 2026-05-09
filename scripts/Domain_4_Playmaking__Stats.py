"""
playmaking_validation.py — Domain 4: Playmaking
Pulls data for sub-domains #11 (Court Vision), #12 (Decision-Making),
#13 (Passing Execution), #14 (Off-Ball Movement)

Four test guards: Kyrie Irving, De'Aaron Fox, Marcus Smart, Buddy Hield
2-season window with 60/40 recency weighting (current/prior)

Run in Claude Code or local Python — stats.nba.com blocked in Claude.ai container.
"""

import time
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')  # EW-F04: prevent Windows cp1252 crash on non-ASCII player names
import os
from datetime import date
from nba_api.stats.endpoints import (
    leaguedashptstats,
    leaguedashplayerstats,
    synergyplaytypes,
)
from nba_api.stats.static import players

# --- CONFIG ---
# Evaluation window + player ID set at module load via eval_window.determine_evaluation_window
from eval_window import determine_evaluation_window, format_window
from config import SCRIPTS_DIR

import argparse
_parser = argparse.ArgumentParser()
_parser.add_argument("player")
_parser.add_argument("--current-season", help="Override current season (e.g. '2021-22')")
_parser.add_argument("--season-override", help="Force a specific season at 100%% weight")
args = _parser.parse_args()

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

PLAYERS = {args.player: None}

# Populate SEASONS and WEIGHTS from window
if len(window.seasons_used) == 1:
    _cur = window.seasons_used[0][0]
    _pri = None
    SEASONS = {"current": _cur}
    WEIGHTS = {"current": window.seasons_used[0][1], "prior": 0.0}
else:
    _cur = window.seasons_used[0][0]
    _pri = window.seasons_used[1][0]
    SEASONS = {"current": _cur, "prior": _pri}
    WEIGHTS = {"current": window.seasons_used[0][1], "prior": window.seasons_used[1][1]}

# Resolve player IDs
for name in PLAYERS:
    match = players.find_players_by_full_name(name)
    if match:
        PLAYERS[name] = match[0]["id"]
    else:
        print(f"WARNING: Could not find player ID for {name}")

print("Player IDs resolved:")
for name, pid in PLAYERS.items():
    print(f"  {name}: {pid}")
print()


def safe_get(row, col, default=0):
    """Safely get a value from a row dict/series."""
    val = row.get(col, default)
    if val is None:
        return default
    return val


# ============================================================
# SECTION 1: PASSING TRACKING DATA (#11, #13)
# LeagueDashPtStats — Passing category
# Fields: POTENTIAL_AST, AST_ADJ, FT_AST, PASSES_MADE,
#         AST_POINTS_CREATED, SECONDARY_AST
# ============================================================
print("=" * 60)
print("SECTION 1: PASSING TRACKING DATA")
print("=" * 60)

passing_data = {}

for label, season in SEASONS.items():
    print(f"\nPulling passing data for {season} ({label})...")
    time.sleep(1)
    try:
        resp = leaguedashptstats.LeagueDashPtStats(
            season=season,
            per_mode_simple="PerGame",
            player_or_team="Player",
            pt_measure_type="Passing",
            season_type_all_star="Regular Season",
        )
        df = resp.get_data_frames()[0]
        for name, pid in PLAYERS.items():
            row = df[df["PLAYER_ID"] == pid]
            if row.empty:
                print(f"  {name}: NO DATA for {season}")
                continue
            r = row.iloc[0]
            passing_data.setdefault(name, {})[label] = {
                "GP": safe_get(r, "GP"),
                "MIN": safe_get(r, "MIN"),
                "PASSES_MADE": safe_get(r, "PASSES_MADE"),
                "PASSES_RECEIVED": safe_get(r, "PASSES_RECEIVED"),
                "AST": safe_get(r, "AST"),
                "SECONDARY_AST": safe_get(r, "SECONDARY_AST"),
                "POTENTIAL_AST": safe_get(r, "POTENTIAL_AST"),
                "AST_POINTS_CREATED": safe_get(r, "AST_POINTS_CREATED"),
                "AST_ADJ": safe_get(r, "AST_ADJ"),
                "FT_AST": safe_get(r, "FT_AST"),
            }
    except Exception as e:
        print(f"  ERROR pulling passing data for {season}: {e}")

# Print passing results
for name in PLAYERS:
    print(f"\n--- {name} ---")
    if name not in passing_data:
        print("  No passing data found.")
        continue
    for label in ["current", "prior"]:
        d = passing_data[name].get(label)
        if d:
            pot_ast = d["POTENTIAL_AST"]
            ast = d["AST"]
            conv_rate = (ast / pot_ast * 100) if pot_ast > 0 else 0
            adj_ast_pct = (d["AST_ADJ"] / d["PASSES_MADE"] * 100) if d["PASSES_MADE"] > 0 else 0
            print(f"  {label} ({SEASONS[label]}): {d['GP']}G, {d['MIN']:.1f} MIN")
            print(f"    Passes/game: {d['PASSES_MADE']:.1f}")
            print(f"    Potential AST: {pot_ast:.1f} | Actual AST: {ast:.1f} | Conv rate: {conv_rate:.1f}%")
            print(f"    Secondary AST: {d['SECONDARY_AST']:.1f}")
            print(f"    FT AST: {d['FT_AST']:.1f}")
            print(f"    Adjusted AST: {d['AST_ADJ']:.1f} | Adj AST %: {adj_ast_pct:.1f}%")
            print(f"    AST Points Created: {d['AST_POINTS_CREATED']:.1f}")


# ============================================================
# SECTION 2: TURNOVER TYPE BREAKDOWN (#12)
# LeagueDashPlayerStats — includes BAD_PASS_TOV, LOST_BALL_TOV
# ============================================================
print("\n" + "=" * 60)
print("SECTION 2: TURNOVER TYPE BREAKDOWN")
print("=" * 60)

tov_data = {}

for label, season in SEASONS.items():
    print(f"\nPulling turnover breakdown for {season} ({label})...")
    time.sleep(1)
    try:
        resp = leaguedashplayerstats.LeagueDashPlayerStats(
            season=season,
            per_mode_detailed="PerGame",
            season_type_all_star="Regular Season",
        )
        df = resp.get_data_frames()[0]
        for name, pid in PLAYERS.items():
            row = df[df["PLAYER_ID"] == pid]
            if row.empty:
                print(f"  {name}: NO DATA for {season}")
                continue
            r = row.iloc[0]
            tov_data.setdefault(name, {})[label] = {
                "GP": safe_get(r, "GP"),
                "MIN": safe_get(r, "MIN"),
                "AST": safe_get(r, "AST"),
                "TOV": safe_get(r, "TOV"),
                "STL": safe_get(r, "STL"),
                "A_TO_RATIO": safe_get(r, "AST") / safe_get(r, "TOV", 1) if safe_get(r, "TOV", 0) > 0 else 0,
            }
    except Exception as e:
        print(f"  ERROR pulling TOV data for {season}: {e}")

# Note: LeagueDashPlayerStats may not include turnover type breakdown directly.
# The NBA.com endpoint for turnover types may need a different approach.
# Trying the hustle stats or player dashboard endpoint.

print("\nAttempting turnover type breakdown via alternate method...")
# Try pulling from the general stats with MeasureType='Advanced' or specific endpoint
for label, season in SEASONS.items():
    time.sleep(1)
    try:
        # Some versions of nba_api expose this through different measure types
        resp = leaguedashplayerstats.LeagueDashPlayerStats(
            season=season,
            per_mode_detailed="Totals",
            season_type_all_star="Regular Season",
            measure_type_detailed_defense="Base",
        )
        df = resp.get_data_frames()[0]
        cols = list(df.columns)
        # Check if turnover breakdown columns exist
        tov_cols = [c for c in cols if "TOV" in c.upper() or "PASS" in c.upper() or "LOST" in c.upper()]
        if tov_cols:
            print(f"  Found TOV-related columns for {season}: {tov_cols}")
        else:
            print(f"  No turnover breakdown columns found in LeagueDashPlayerStats for {season}")
            print(f"  Available columns sample: {cols[:20]}...")
    except Exception as e:
        print(f"  ERROR: {e}")

# Print TOV results (standard A:TO)
for name in PLAYERS:
    print(f"\n--- {name} ---")
    if name not in tov_data:
        print("  No TOV data found.")
        continue
    for label in ["current", "prior"]:
        d = tov_data[name].get(label)
        if d:
            print(f"  {label} ({SEASONS[label]}): {d['GP']}G, {d['MIN']:.1f} MIN")
            print(f"    AST: {d['AST']:.1f} | TOV: {d['TOV']:.1f} | A:TO: {d['A_TO_RATIO']:.2f}")
            # Cross-ref with potential assists if available
            if name in passing_data and label in passing_data[name]:
                pot = passing_data[name][label]["POTENTIAL_AST"]
                if pot > 0:
                    print(f"    TOV / Potential AST: {d['TOV'] / pot:.2f}")


# ============================================================
# SECTION 3: SYNERGY PLAY TYPES — Cut, OffScreen, Transition (#12, #14)
# ============================================================
print("\n" + "=" * 60)
print("SECTION 3: SYNERGY PLAY TYPES (Cut, OffScreen, Transition)")
print("=" * 60)

synergy_types = {
    "Cut": "Cut",
    "OffScreen": "OffScreen",
    "Transition": "Transition",
}

synergy_data = {}

for play_type, pt_name in synergy_types.items():
    for label, season in SEASONS.items():
        print(f"\nPulling Synergy {play_type} for {season} ({label})...")
        time.sleep(1.5)
        try:
            resp = synergyplaytypes.SynergyPlayTypes(
                season=season,
                play_type_nullable=pt_name,
                player_or_team_abbreviation="P",
                season_type_all_star="Regular Season",
                type_grouping_nullable="offensive",
            )
            df = resp.get_data_frames()[0]
            for name, pid in PLAYERS.items():
                row = df[df["PLAYER_ID"] == pid]
                if row.empty:
                    continue
                r = row.iloc[0]
                synergy_data.setdefault(name, {}).setdefault(play_type, {})[label] = {
                    "GP": safe_get(r, "GP"),
                    "POSS": safe_get(r, "POSS"),
                    "PPP": safe_get(r, "PPP"),
                    "FG_PCT": safe_get(r, "FG_PCT"),
                    "TOV_PCT": safe_get(r, "TOV_POSS_PCT") if "TOV_POSS_PCT" in r.index else safe_get(r, "TOV_PCT", 0),
                    "PERCENTILE": safe_get(r, "PERCENTILE"),
                    "POSS_PCT": safe_get(r, "POSS_PCT"),
                }
        except Exception as e:
            print(f"  ERROR pulling {play_type} for {season}: {e}")

# Print Synergy results
for name in PLAYERS:
    print(f"\n--- {name} ---")
    if name not in synergy_data:
        print("  No Synergy data found.")
        continue
    for pt in synergy_types:
        if pt not in synergy_data[name]:
            print(f"  {pt}: No data")
            continue
        print(f"  {pt}:")
        for label in ["current", "prior"]:
            d = synergy_data[name][pt].get(label)
            if d:
                pctile = d.get("PERCENTILE", 0)
                pctile_str = f"{pctile * 100:.0f}th" if pctile and pctile > 0 else "N/A"
                print(f"    {label} ({SEASONS[label]}): {d['POSS']} poss, {d['PPP']:.3f} PPP, "
                      f"FG: {d['FG_PCT']:.1%}, TOV: {d.get('TOV_PCT', 0):.1%}, "
                      f"Pctile: {pctile_str}, Freq: {d.get('POSS_PCT', 0):.1%}")


# ============================================================
# SECTION 4: SPEED & DISTANCE (#14)
# LeagueDashPtStats — SpeedDistance category
# ============================================================
print("\n" + "=" * 60)
print("SECTION 4: SPEED & DISTANCE (Off-Ball Movement)")
print("=" * 60)

speed_data = {}

for label, season in SEASONS.items():
    print(f"\nPulling speed/distance data for {season} ({label})...")
    time.sleep(1)
    try:
        resp = leaguedashptstats.LeagueDashPtStats(
            season=season,
            per_mode_simple="PerGame",
            player_or_team="Player",
            pt_measure_type="SpeedDistance",
            season_type_all_star="Regular Season",
        )
        df = resp.get_data_frames()[0]
        for name, pid in PLAYERS.items():
            row = df[df["PLAYER_ID"] == pid]
            if row.empty:
                print(f"  {name}: NO DATA for {season}")
                continue
            r = row.iloc[0]
            speed_data.setdefault(name, {})[label] = {
                "GP": safe_get(r, "GP"),
                "DIST_FEET": safe_get(r, "DIST_FEET") if "DIST_FEET" in r.index else safe_get(r, "DIST_MILES", 0),
                "DIST_MILES": safe_get(r, "DIST_MILES") if "DIST_MILES" in r.index else 0,
                "DIST_MILES_OFF": safe_get(r, "DIST_MILES_OFF") if "DIST_MILES_OFF" in r.index else 0,
                "DIST_MILES_DEF": safe_get(r, "DIST_MILES_DEF") if "DIST_MILES_DEF" in r.index else 0,
                "AVG_SPEED": safe_get(r, "AVG_SPEED") if "AVG_SPEED" in r.index else 0,
                "AVG_SPEED_OFF": safe_get(r, "AVG_SPEED_OFF") if "AVG_SPEED_OFF" in r.index else 0,
                "AVG_SPEED_DEF": safe_get(r, "AVG_SPEED_DEF") if "AVG_SPEED_DEF" in r.index else 0,
            }
    except Exception as e:
        print(f"  ERROR pulling speed data for {season}: {e}")

# Print speed/distance results
for name in PLAYERS:
    print(f"\n--- {name} ---")
    if name not in speed_data:
        print("  No speed data found.")
        continue
    for label in ["current", "prior"]:
        d = speed_data[name].get(label)
        if d:
            print(f"  {label} ({SEASONS[label]}): {d['GP']}G")
            print(f"    Total dist: {d['DIST_MILES']:.2f} mi/game")
            print(f"    Off dist: {d['DIST_MILES_OFF']:.2f} mi | Def dist: {d['DIST_MILES_DEF']:.2f} mi")
            print(f"    Avg speed: {d['AVG_SPEED']:.2f} mph")
            print(f"    Off speed: {d['AVG_SPEED_OFF']:.2f} mph | Def speed: {d['AVG_SPEED_DEF']:.2f} mph")


# ============================================================
# SECTION 5: WEIGHTED COMPOSITE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("SECTION 5: 2-SEASON WEIGHTED SUMMARY")
print("=" * 60)

for name in PLAYERS:
    print(f"\n{'='*40}")
    print(f"  {name}")
    print(f"{'='*40}")

    # --- Passing (weighted) ---
    if name in passing_data:
        curr = passing_data[name].get("current", {})
        prior = passing_data[name].get("prior", {})
        if curr and prior:
            for stat in ["POTENTIAL_AST", "SECONDARY_AST", "AST", "PASSES_MADE",
                         "AST_POINTS_CREATED", "AST_ADJ", "FT_AST"]:
                wt = curr.get(stat, 0) * WEIGHTS["current"] + prior.get(stat, 0) * WEIGHTS["prior"]
                print(f"  Weighted {stat}: {wt:.1f}")
            # Weighted conversion rate
            wt_pot = curr.get("POTENTIAL_AST", 0) * WEIGHTS["current"] + prior.get("POTENTIAL_AST", 0) * WEIGHTS["prior"]
            wt_ast = curr.get("AST", 0) * WEIGHTS["current"] + prior.get("AST", 0) * WEIGHTS["prior"]
            wt_conv = (wt_ast / wt_pot * 100) if wt_pot > 0 else 0
            print(f"  Weighted AST/PotAST conv rate: {wt_conv:.1f}%")
            # Weighted adj assist %
            wt_adj = curr.get("AST_ADJ", 0) * WEIGHTS["current"] + prior.get("AST_ADJ", 0) * WEIGHTS["prior"]
            wt_passes = curr.get("PASSES_MADE", 0) * WEIGHTS["current"] + prior.get("PASSES_MADE", 0) * WEIGHTS["prior"]
            wt_adj_pct = (wt_adj / wt_passes * 100) if wt_passes > 0 else 0
            print(f"  Weighted Adj AST %: {wt_adj_pct:.1f}%")
        elif curr:
            print("  (Current season only — no prior data)")
            for stat in ["POTENTIAL_AST", "SECONDARY_AST", "AST", "PASSES_MADE",
                         "AST_POINTS_CREATED", "AST_ADJ", "FT_AST"]:
                print(f"  {stat}: {curr.get(stat, 0):.1f}")

    # --- TOV breakdown (weighted) ---
    if name in tov_data:
        curr = tov_data[name].get("current", {})
        prior = tov_data[name].get("prior", {})
        if curr and prior:
            wt_ast = curr.get("AST", 0) * WEIGHTS["current"] + prior.get("AST", 0) * WEIGHTS["prior"]
            wt_tov = curr.get("TOV", 0) * WEIGHTS["current"] + prior.get("TOV", 0) * WEIGHTS["prior"]
            wt_ato = wt_ast / wt_tov if wt_tov > 0 else 0
            print(f"  Weighted AST: {wt_ast:.1f} | TOV: {wt_tov:.1f} | A:TO: {wt_ato:.2f}")

    # --- Synergy (weighted where both seasons exist) ---
    if name in synergy_data:
        for pt in synergy_types:
            if pt in synergy_data[name]:
                curr = synergy_data[name][pt].get("current", {})
                prior = synergy_data[name][pt].get("prior", {})
                if curr and prior:
                    wt_poss = curr.get("POSS", 0) * WEIGHTS["current"] + prior.get("POSS", 0) * WEIGHTS["prior"]
                    # Volume-weighted PPP
                    total_poss = curr.get("POSS", 0) + prior.get("POSS", 0)
                    if total_poss > 0:
                        wt_ppp = (curr.get("PPP", 0) * curr.get("POSS", 0) * WEIGHTS["current"] +
                                  prior.get("PPP", 0) * prior.get("POSS", 0) * WEIGHTS["prior"]) / (
                                  curr.get("POSS", 0) * WEIGHTS["current"] + prior.get("POSS", 0) * WEIGHTS["prior"])
                    else:
                        wt_ppp = 0
                    print(f"  {pt}: Weighted {wt_poss:.0f} poss, {wt_ppp:.3f} PPP")
                elif curr:
                    print(f"  {pt}: {curr.get('POSS', 0)} poss, {curr.get('PPP', 0):.3f} PPP (current only)")

    # --- Speed (weighted) ---
    if name in speed_data:
        curr = speed_data[name].get("current", {})
        prior = speed_data[name].get("prior", {})
        if curr and prior:
            for stat in ["DIST_MILES", "DIST_MILES_OFF", "AVG_SPEED", "AVG_SPEED_OFF"]:
                wt = curr.get(stat, 0) * WEIGHTS["current"] + prior.get(stat, 0) * WEIGHTS["prior"]
                print(f"  Weighted {stat}: {wt:.2f}")

# ============================================================
# SECTION 6: SAVE JSON OUTPUT
# ============================================================

def _sw(cur_val, pri_val):
    """Simple weighted for JSON output."""
    if pri_val is None or pri_val == 0:
        return cur_val
    return round(cur_val * WEIGHTS["current"] + pri_val * WEIGHTS["prior"], 3)

def _sb(cur, pri, is_rate=False):
    """Stat block for JSON."""
    if pri is None:
        return {"current": cur, "prior": "N/A", "weighted": cur}
    w = _sw(cur, pri) if is_rate else _sw(cur, pri)
    return {"current": cur, "prior": pri, "weighted": w}

def _syn_sb(data_dict, play_type, label_cur="current", label_pri="prior"):
    """Build synergy stat blocks from raw data."""
    if play_type not in data_dict:
        return {"ppp": _sb(0, None), "poss": _sb(0, None), "fg_pct": _sb(0, None),
                "tov_pct": _sb(0, None), "percentile": _sb(0, None)}
    c = data_dict[play_type].get(label_cur, {})
    p = data_dict[play_type].get(label_pri, {})
    if not c:
        c = {}
    if not p:
        p = None

    def g(d, k):
        if d is None:
            return None
        return d.get(k, 0)

    return {
        "ppp": _sb(g(c, "PPP") or 0, g(p, "PPP"), is_rate=True),
        "poss": _sb(g(c, "POSS") or 0, g(p, "POSS")),
        "fg_pct": _sb(g(c, "FG_PCT") or 0, g(p, "FG_PCT"), is_rate=True),
        "tov_pct": _sb(g(c, "TOV_PCT") or 0, g(p, "TOV_PCT"), is_rate=True),
        "percentile": _sb(g(c, "PERCENTILE") or 0, g(p, "PERCENTILE"), is_rate=True),
        "poss_pct": _sb(g(c, "POSS_PCT") or 0, g(p, "POSS_PCT"), is_rate=True),
    }

profiles = []
for name, pid in PLAYERS.items():
    # Passing
    pc = passing_data.get(name, {}).get("current", {})
    pp = passing_data.get(name, {}).get("prior", {})

    def pg(d, k):
        return d.get(k, 0) if d else 0

    pot_ast_c = pg(pc, "POTENTIAL_AST")
    pot_ast_p = pg(pp, "POTENTIAL_AST") if pp else None
    ast_c = pg(pc, "AST")
    ast_p = pg(pp, "AST") if pp else None
    conv_c = round(ast_c / pot_ast_c * 100, 1) if pot_ast_c > 0 else 0
    conv_p = round(ast_p / pot_ast_p * 100, 1) if pot_ast_p and pot_ast_p > 0 else None
    adj_c = pg(pc, "AST_ADJ")
    adj_p = pg(pp, "AST_ADJ") if pp else None
    passes_c = pg(pc, "PASSES_MADE")
    passes_p = pg(pp, "PASSES_MADE") if pp else None
    adj_pct_c = round(adj_c / passes_c * 100, 1) if passes_c > 0 else 0
    adj_pct_p = round(adj_p / passes_p * 100, 1) if passes_p and passes_p > 0 else None

    # TOV
    tc = tov_data.get(name, {}).get("current", {})
    tp = tov_data.get(name, {}).get("prior", {})
    tov_c = pg(tc, "TOV")
    tov_p = pg(tp, "TOV") if tp else None
    ato_c = pg(tc, "A_TO_RATIO")
    ato_p = pg(tp, "A_TO_RATIO") if tp else None
    tov_pot_c = round(tov_c / pot_ast_c, 2) if pot_ast_c > 0 else 0
    tov_pot_p = round(tov_p / pot_ast_p, 2) if pot_ast_p and pot_ast_p > 0 else None

    # Speed
    sc = speed_data.get(name, {}).get("current", {})
    sp = speed_data.get(name, {}).get("prior", {})

    # Synergy
    syn = synergy_data.get(name, {})

    profile = {
        "player": name,
        "evaluation_window": {
            "mode": window.mode,
            "seasons_used": [{"season": s, "weight": w} for s, w in window.seasons_used],
            "flag_template": window.flag_template,
            "age_concern": window.age_concern,
        },
        "subdomain_11_court_vision": {
            "potential_ast": _sb(pot_ast_c, pot_ast_p, is_rate=True),
            "actual_ast": _sb(ast_c, ast_p, is_rate=True),
            "ast_conversion_rate": _sb(conv_c, conv_p, is_rate=True),
            "secondary_ast": _sb(pg(pc, "SECONDARY_AST"), pg(pp, "SECONDARY_AST") if pp else None, is_rate=True),
            "passes_made": _sb(passes_c, passes_p, is_rate=True),
            "ast_points_created": _sb(pg(pc, "AST_POINTS_CREATED"), pg(pp, "AST_POINTS_CREATED") if pp else None, is_rate=True),
        },
        "subdomain_12_decision_making": {
            "a_to_ratio": _sb(ato_c, ato_p, is_rate=True),
            "tov_per_potential_ast": _sb(tov_pot_c, tov_pot_p, is_rate=True),
            "ast_pg": _sb(pg(tc, "AST"), pg(tp, "AST") if tp else None, is_rate=True),
            "tov_pg": _sb(tov_c, tov_p, is_rate=True),
            "transition": _syn_sb(syn, "Transition"),
        },
        "subdomain_13_passing_execution": {
            "adjusted_ast": _sb(adj_c, adj_p, is_rate=True),
            "adj_ast_pct": _sb(adj_pct_c, adj_pct_p, is_rate=True),
            "ft_ast": _sb(pg(pc, "FT_AST"), pg(pp, "FT_AST") if pp else None, is_rate=True),
            "passes_received": _sb(pg(pc, "PASSES_RECEIVED"), pg(pp, "PASSES_RECEIVED") if pp else None, is_rate=True),
        },
        "subdomain_14_off_ball_movement": {
            "cut": _syn_sb(syn, "Cut"),
            "off_screen": _syn_sb(syn, "OffScreen"),
            "speed_distance": {
                "dist_miles_off": _sb(pg(sc, "DIST_MILES_OFF"), pg(sp, "DIST_MILES_OFF") if sp else None, is_rate=True),
                "avg_speed_off": _sb(pg(sc, "AVG_SPEED_OFF"), pg(sp, "AVG_SPEED_OFF") if sp else None, is_rate=True),
                "dist_miles_total": _sb(pg(sc, "DIST_MILES"), pg(sp, "DIST_MILES") if sp else None, is_rate=True),
                "avg_speed_total": _sb(pg(sc, "AVG_SPEED"), pg(sp, "AVG_SPEED") if sp else None, is_rate=True),
            },
        },
    }
    profiles.append(profile)

save_path = SCRIPTS_DIR / "playmaking_output.json"
with open(save_path, "w") as f:
    json.dump(profiles, f, indent=2, default=str)
print(f"\nRaw data saved to {save_path}")

print("\n\nScript complete. Review raw + weighted data above.")
