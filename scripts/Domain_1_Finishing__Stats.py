"""
Layer 1 Scouting Rubric — Domain 1: Finishing
Data pipeline using nba_api.

v3 — 2-season evaluation window with 60/40 recency weighting (S83 decision).
Each endpoint queried independently per season with explicit Season= parameter.
Volume-weighted percentages for shooting stats; simple weighted average for rate stats.

Sub-Domain #1 — At-Basket Finishing:
  - Restricted Area FG% + Volume (co-primary per S82-F01)
  - % assisted at rim (secondary #1 — overall FGM assisted %)
  - Dunk rate as share of rim attempts (secondary #2)
  - FT% (secondary #3)
  - FG% vs tight/very tight defense (secondary #4 — all shots, not rim-only)

Sub-Domain #2 — Contact Finishing / Foul Drawing:
  - FTR (FTA/FGA) (primary — totals-based per S83-F01)
  - FT% (secondary #1)
  - Drive data (secondary #2 — drives/game, drive FG%, drive PTS)
  - Paint (non-RA) FG% (secondary #3)
"""

import json
import time
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')  # EW-F04: prevent Windows cp1252 crash on non-ASCII player names
from datetime import date
from nba_api.stats.static import players
from nba_api.stats.endpoints import (
    shotchartdetail,
    playercareerstats,
    playerdashboardbyshootingsplits,
    leaguedashptstats,
    leaguedashplayerptshot,
)

# ──────────────────────────────────────────────────────────────────────
# Evaluation window — set by main() via eval_window.determine_evaluation_window
# ──────────────────────────────────────────────────────────────────────

from eval_window import determine_evaluation_window, format_window

CURRENT_SEASON = None
PRIOR_SEASON = None  # None triggers single-season path (R12_ANCHOR, OVERRIDE, ROOKIE)
W_CURRENT = 0.60
W_PRIOR = 0.40


# ──────────────────────────────────────────────────────────────────────
# Weighting helpers
# ──────────────────────────────────────────────────────────────────────

def volume_weighted_pct(cur_made, cur_att, pri_made, pri_att):
    """Volume-weighted percentage for shooting stats (S83 rule 5)."""
    if pri_att is None or pri_att == "N/A":
        return round(cur_made / cur_att, 3) if cur_att > 0 else 0
    w_made = cur_made * W_CURRENT + pri_made * W_PRIOR
    w_att = cur_att * W_CURRENT + pri_att * W_PRIOR
    return round(w_made / w_att, 3) if w_att > 0 else 0


def simple_weighted(cur_val, pri_val):
    """Simple 60/40 weighted average for rate stats (S83 rule 6)."""
    if pri_val is None or pri_val == "N/A":
        return cur_val
    return round(cur_val * W_CURRENT + pri_val * W_PRIOR, 3)


def stat_block(cur_val, pri_val, cur_vol=None, pri_vol=None, is_rate=False):
    """Build a 3-value stat block: current, prior, weighted."""
    if pri_val is None or pri_val == "N/A":
        weighted = cur_val
        pri_display = "N/A"
    else:
        pri_display = pri_val
        if is_rate:
            weighted = simple_weighted(cur_val, pri_val)
        elif cur_vol is not None and pri_vol is not None:
            # Volume-weighted for percentages
            weighted = volume_weighted_pct(
                cur_val * cur_vol if cur_vol > 0 else 0, cur_vol or 0,
                pri_val * pri_vol if pri_vol > 0 else 0, pri_vol or 0,
            )
        else:
            weighted = simple_weighted(cur_val, pri_val)

    block = {"current": cur_val, "prior": pri_display, "weighted": weighted}
    if cur_vol is not None:
        block["current_volume"] = cur_vol
        block["prior_volume"] = pri_vol if pri_vol is not None else "N/A"
        block["total_volume"] = (cur_vol or 0) + (pri_vol or 0) if pri_vol not in (None, "N/A") else cur_vol
    return block


# ──────────────────────────────────────────────────────────────────────
# Player lookup
# ──────────────────────────────────────────────────────────────────────

def find_player_id(player_name: str) -> dict:
    matches = players.find_players_by_full_name(player_name)
    if not matches:
        raise ValueError(f"No player found for '{player_name}'")
    active = [p for p in matches if p["is_active"]]
    player = active[0] if active else matches[0]
    return {"id": player["id"], "full_name": player["full_name"],
            "is_active": player["is_active"]}


# ──────────────────────────────────────────────────────────────────────
# Per-player endpoints — each takes explicit season parameter
# ──────────────────────────────────────────────────────────────────────

def get_shooting_splits(player_id: int, season: str) -> dict:
    """PlayerDashboardByShootingSplits — explicit season."""
    time.sleep(0.6)
    try:
        dashboard = playerdashboardbyshootingsplits.PlayerDashboardByShootingSplits(
            player_id=player_id,
            season=season,
            per_mode_detailed="Totals",
        )
        frames = dashboard.get_data_frames()
        result = {}

        # Frame 3: ShotAreaPlayerDashboard
        for _, row in frames[3].iterrows():
            area = str(row.get("GROUP_VALUE", ""))
            if "Restricted Area" in area:
                result["restricted_area"] = {
                    "fgm": int(row.get("FGM", 0) or 0),
                    "fga": int(row.get("FGA", 0) or 0),
                    "fg_pct": round(float(row.get("FG_PCT", 0) or 0), 3),
                }
            elif "Paint" in area and "Non-RA" in area:
                result["paint_non_ra"] = {
                    "fgm": int(row.get("FGM", 0) or 0),
                    "fga": int(row.get("FGA", 0) or 0),
                    "fg_pct": round(float(row.get("FG_PCT", 0) or 0), 3),
                }

        # Frame 0: Overall totals
        if not frames[0].empty:
            r = frames[0].iloc[0]
            result["overall_fga"] = int(r.get("FGA", 0) or 0)

        # Frame 4: Assisted vs Unassisted
        try:
            for _, row in frames[4].iterrows():
                group = str(row.get("GROUP_VALUE", ""))
                if group == "Assisted":
                    result["assisted_fgm"] = int(row.get("FGM", 0) or 0)
                elif group == "Unassisted":
                    result["unassisted_fgm"] = int(row.get("FGM", 0) or 0)
        except (IndexError, KeyError):
            pass

        return result
    except Exception as e:
        return {"error": str(e)}


def get_shot_chart_data(player_id: int, season: str) -> dict:
    """ShotChartDetail — explicit season (critical: prevents cross-season bleed)."""
    time.sleep(0.6)
    try:
        shots = shotchartdetail.ShotChartDetail(
            player_id=player_id,
            team_id=0,
            season_nullable=season,
            context_measure_simple="FGA",
        )
        df = shots.get_data_frames()[0]
        if df.empty:
            return {"error": "No shot chart data"}

        total_shots = len(df)
        rim = df[df["SHOT_ZONE_BASIC"] == "Restricted Area"]
        rim_total = len(rim)
        rim_made = int((rim["SHOT_MADE_FLAG"] == 1).sum())

        dunks = rim[rim["ACTION_TYPE"].str.contains("dunk", case=False, na=False)]
        dunk_total = len(dunks)
        dunk_made = int((dunks["SHOT_MADE_FLAG"] == 1).sum())
        nd_total = rim_total - dunk_total
        nd_made = rim_made - dunk_made

        return {
            "total_fga": total_shots,
            "rim_fga": rim_total, "rim_fgm": rim_made,
            "rim_fg_pct": round(rim_made / rim_total, 3) if rim_total > 0 else 0,
            "pct_shots_at_rim": round(rim_total / total_shots, 3) if total_shots > 0 else 0,
            "dunks": dunk_total, "dunks_made": dunk_made,
            "dunk_rate_of_rim": round(dunk_total / rim_total, 3) if rim_total > 0 else 0,
            "non_dunk_rim_fga": nd_total, "non_dunk_rim_fgm": nd_made,
            "non_dunk_rim_fg_pct": round(nd_made / nd_total, 3) if nd_total > 0 else 0,
        }
    except Exception as e:
        return {"error": str(e)}


def get_career_totals(player_id: int, season: str) -> dict:
    """PlayerCareerStats (Totals) — extract specific season row."""
    time.sleep(0.6)
    try:
        career = playercareerstats.PlayerCareerStats(
            player_id=player_id, per_mode36="Totals",
        )
        df = career.get_data_frames()[0]
        rows = df[df["SEASON_ID"] == season]
        if rows.empty:
            return {"error": f"No data for {season}"}
        # Sum across teams for traded players
        return {
            "fta": int(rows["FTA"].sum()),
            "ftm": int(rows["FTM"].sum()),
            "fga": int(rows["FGA"].sum()),
            "fgm": int(rows["FGM"].sum()),
            "ft_pct": round(int(rows["FTM"].sum()) / int(rows["FTA"].sum()), 3) if int(rows["FTA"].sum()) > 0 else 0,
            "gp": int(rows["GP"].sum()),
        }
    except Exception as e:
        return {"error": str(e)}


# ──────────────────────────────────────────────────────────────────────
# League-wide endpoints — each takes explicit season
# ──────────────────────────────────────────────────────────────────────

def get_league_drives(season: str) -> dict:
    time.sleep(0.6)
    try:
        stats = leaguedashptstats.LeagueDashPtStats(
            pt_measure_type="Drives", season=season,
            per_mode_simple="PerGame", player_or_team="Player",
            season_type_all_star="Regular Season",
        )
        return {"df": stats.get_data_frames()[0]}
    except Exception as e:
        return {"error": str(e)}


def get_league_defender_distance(season: str) -> dict:
    buckets = {
        "very_tight_0_2": "0-2 Feet - Very Tight",
        "tight_2_4": "2-4 Feet - Tight",
        "open_4_6": "4-6 Feet - Open",
        "wide_open_6plus": "6+ Feet - Wide Open",
    }
    result = {}
    for key, label in buckets.items():
        time.sleep(0.6)
        try:
            shots = leaguedashplayerptshot.LeagueDashPlayerPtShot(
                season=season, per_mode_simple="Totals",
                season_type_all_star="Regular Season",
                close_def_dist_range_nullable=label,
            )
            result[key] = shots.get_data_frames()[0]
        except Exception as e:
            result[key] = {"error": str(e)}
    return result


# ──────────────────────────────────────────────────────────────────────
# Extraction helpers
# ──────────────────────────────────────────────────────────────────────

def extract_drives(drives_result: dict, player_id: int) -> dict:
    if "error" in drives_result:
        return None
    df = drives_result["df"]
    row = df[df["PLAYER_ID"] == player_id]
    if row.empty:
        return None
    r = row.iloc[0]
    drives = float(r.get("DRIVES", 0))
    pts = float(r.get("DRIVE_PTS", 0))
    return {
        "drives_pg": round(drives, 1),
        "drive_fg_pct": round(float(r.get("DRIVE_FG_PCT", 0)), 3),
        "drive_pts": round(pts, 1),
        "drive_ppp": round(pts / drives, 3) if drives > 0 else 0,
        "drive_fta": round(float(r.get("DRIVE_FTA", 0)), 1),
    }


def extract_defender(dd_result: dict, player_id: int) -> dict:
    output = {}
    for key, data in dd_result.items():
        if isinstance(data, dict) and "error" in data:
            output[key] = None
            continue
        row = data[data["PLAYER_ID"] == player_id]
        if row.empty:
            output[key] = None
            continue
        r = row.iloc[0]
        fga = int(r.get("FGA", 0) or 0)
        fgm = int(r.get("FGM", 0) or 0)
        output[key] = {
            "fg_pct": round(fgm / fga, 3) if fga > 0 else 0,
            "fga": fga, "fgm": fgm,
        }
    return output


# ──────────────────────────────────────────────────────────────────────
# 2-season profile assembly
# ──────────────────────────────────────────────────────────────────────

def pull_finishing_profile_2season(
    player_name: str,
    cur_season: str,
    pri_season: str,
    drives_cur: dict, drives_pri: dict,
    dd_cur: dict, dd_pri: dict,
) -> dict:
    print(f"\n{'='*60}")
    print(f"Pulling finishing data: {player_name}")
    if pri_season:
        print(f"  Window: {cur_season} ({int(W_CURRENT*100)}%) + {pri_season} ({int(W_PRIOR*100)}%)")
    else:
        print(f"  Window: {cur_season} (single-season)")
    print(f"{'='*60}")

    player = find_player_id(player_name)
    pid = player["id"]
    print(f"  Found: {player['full_name']} (ID: {pid})")

    # ── Per-player: query current season, then prior (or stub for single-season) ──
    print(f"  Pulling {cur_season} splits...")
    splits_cur = get_shooting_splits(pid, cur_season)
    print(f"  Pulling {cur_season} shot chart...")
    chart_cur = get_shot_chart_data(pid, cur_season)
    print(f"  Pulling {cur_season} career totals...")
    career_cur = get_career_totals(pid, cur_season)

    if pri_season is None:
        print("  (single-season mode -- skipping prior-season pulls)")
        splits_pri = {"error": "single-season mode"}
        chart_pri = {"error": "single-season mode"}
        career_pri = {"error": "single-season mode"}
    else:
        print(f"  Pulling {pri_season} splits...")
        splits_pri = get_shooting_splits(pid, pri_season)
        print(f"  Pulling {pri_season} shot chart...")
        chart_pri = get_shot_chart_data(pid, pri_season)
        print(f"  Pulling {pri_season} career totals...")
        career_pri = get_career_totals(pid, pri_season)

    # ── League-wide extractions ──
    print("  Extracting drive + defender data...")
    drv_cur = extract_drives(drives_cur, pid)
    drv_pri = extract_drives(drives_pri, pid)
    def_cur = extract_defender(dd_cur, pid)
    def_pri = extract_defender(dd_pri, pid)

    # ── Helper to safely get nested values ──
    def _g(d, *keys, default=0):
        """Safe nested get."""
        if d is None or "error" in d:
            return None
        for k in keys:
            if isinstance(d, dict):
                d = d.get(k, None)
            else:
                return None
            if d is None:
                return None
        return d

    has_prior_chart = "error" not in chart_pri
    has_prior_career = "error" not in career_pri

    # ── Build stat blocks ──

    # #1: Rim FG%
    cur_rim_fgm = _g(chart_cur, "rim_fgm") or 0
    cur_rim_fga = _g(chart_cur, "rim_fga") or 0
    pri_rim_fgm = _g(chart_pri, "rim_fgm") if has_prior_chart else None
    pri_rim_fga = _g(chart_pri, "rim_fga") if has_prior_chart else None

    rim_fg_pct = stat_block(
        _g(chart_cur, "rim_fg_pct") or 0,
        _g(chart_pri, "rim_fg_pct") if has_prior_chart else None,
        cur_rim_fga, pri_rim_fga,
    )

    # FTR
    cur_fta = _g(career_cur, "fta") or 0
    cur_fga_t = _g(career_cur, "fga") or 0
    pri_fta = _g(career_pri, "fta") if has_prior_career else None
    pri_fga_t = _g(career_pri, "fga") if has_prior_career else None
    cur_ftr = round(cur_fta / cur_fga_t, 3) if cur_fga_t > 0 else 0
    pri_ftr = round(pri_fta / pri_fga_t, 3) if pri_fga_t and pri_fga_t > 0 else None

    ftr_block = stat_block(cur_ftr, pri_ftr, is_rate=True)

    # FT%
    cur_ftm = _g(career_cur, "ftm") or 0
    pri_ftm = _g(career_pri, "ftm") if has_prior_career else None
    ft_pct = stat_block(
        _g(career_cur, "ft_pct") or 0,
        _g(career_pri, "ft_pct") if has_prior_career else None,
        cur_fta, pri_fta,
    )

    # Drive PPP (rate stat)
    drive_ppp = stat_block(
        _g(drv_cur, "drive_ppp") or 0,
        _g(drv_pri, "drive_ppp"),
        is_rate=True,
    )

    # Paint non-RA FG%
    cur_paint_fgm = _g(splits_cur, "paint_non_ra", "fgm") or 0
    cur_paint_fga = _g(splits_cur, "paint_non_ra", "fga") or 0
    pri_paint_fgm = _g(splits_pri, "paint_non_ra", "fgm")
    pri_paint_fga = _g(splits_pri, "paint_non_ra", "fga")
    paint_fg = stat_block(
        _g(splits_cur, "paint_non_ra", "fg_pct") or 0,
        _g(splits_pri, "paint_non_ra", "fg_pct"),
        cur_paint_fga, pri_paint_fga,
    )

    # Assisted %
    cur_ast = _g(splits_cur, "assisted_fgm") or 0
    cur_uast = _g(splits_cur, "unassisted_fgm") or 0
    cur_total_fgm = cur_ast + cur_uast
    cur_ast_pct = round(cur_ast / cur_total_fgm, 3) if cur_total_fgm > 0 else 0

    pri_ast = _g(splits_pri, "assisted_fgm")
    pri_uast = _g(splits_pri, "unassisted_fgm")
    if pri_ast is not None and pri_uast is not None:
        pri_total_fgm = pri_ast + pri_uast
        pri_ast_pct = round(pri_ast / pri_total_fgm, 3) if pri_total_fgm > 0 else 0
    else:
        pri_ast_pct = None

    assisted_block = stat_block(cur_ast_pct, pri_ast_pct, is_rate=True)

    # Defender distance — build per bucket
    dd_blocks = {}
    for key in ["very_tight_0_2", "tight_2_4", "open_4_6", "wide_open_6plus"]:
        c = def_cur.get(key)
        p = def_pri.get(key)
        if c:
            dd_blocks[key] = stat_block(
                c["fg_pct"], p["fg_pct"] if p else None,
                c["fga"], p["fga"] if p else None,
            )
        else:
            dd_blocks[key] = {"current": "N/A", "prior": "N/A", "weighted": "N/A"}

    # ── Assemble profile ──
    profile = {
        "player": player["full_name"],
        "evaluation_window": {
            "current_season": cur_season,
            "prior_season": pri_season,
            "weighting": "60/40 current/prior",
        },
        "subdomain_1_at_basket_finishing": {
            "rim_fg_pct": rim_fg_pct,
            "rim_volume": stat_block(
                cur_rim_fga, pri_rim_fga if pri_rim_fga else None,
            ),
            "pct_shots_at_rim": stat_block(
                _g(chart_cur, "pct_shots_at_rim") or 0,
                _g(chart_pri, "pct_shots_at_rim") if has_prior_chart else None,
                is_rate=True,
            ),
            "dunk_rate": stat_block(
                _g(chart_cur, "dunk_rate_of_rim") or 0,
                _g(chart_pri, "dunk_rate_of_rim") if has_prior_chart else None,
                is_rate=True,
            ),
            "non_dunk_rim_fg_pct": stat_block(
                _g(chart_cur, "non_dunk_rim_fg_pct") or 0,
                _g(chart_pri, "non_dunk_rim_fg_pct") if has_prior_chart else None,
                _g(chart_cur, "non_dunk_rim_fga") or 0,
                _g(chart_pri, "non_dunk_rim_fga") if has_prior_chart else None,
            ),
            "ft_pct": ft_pct,
            "pct_assisted_overall": assisted_block,
            "vs_tight_defense": dd_blocks,
        },
        "subdomain_2_contact_finishing": {
            "ftr": ftr_block,
            "ft_pct": ft_pct,
            "drives": {
                "drives_pg": stat_block(
                    _g(drv_cur, "drives_pg") or 0,
                    _g(drv_pri, "drives_pg"),
                    is_rate=True,
                ),
                "drive_fg_pct": stat_block(
                    _g(drv_cur, "drive_fg_pct") or 0,
                    _g(drv_pri, "drive_fg_pct"),
                    is_rate=True,
                ),
                "drive_ppp": drive_ppp,
            },
            "paint_non_ra_fg_pct": paint_fg,
        },
    }
    return profile


# ──────────────────────────────────────────────────────────────────────
# Display
# ──────────────────────────────────────────────────────────────────────

def print_comparison(profiles: list):
    W = 14
    header = f"{'Metric':<35}"
    for p in profiles:
        name = p["player"].split()[-1][:W]
        header += f"  {name:>{W}}"

    def fmt_block(p, path, field="weighted", as_pct=False):
        """Navigate to a stat_block and format the requested field."""
        d = p
        for k in path:
            d = d.get(k, {}) if isinstance(d, dict) else {}
        val = d.get(field, "N/A") if isinstance(d, dict) else "N/A"
        if isinstance(val, (int, float)) and val == val:
            return f"  {val:>{W}.1%}" if as_pct else f"  {val:>{W}}"
        return f"  {'N/A':>{W}}"

    def row(label, path, field="weighted", as_pct=False):
        r = f"{label:<35}"
        for p in profiles:
            r += fmt_block(p, path, field, as_pct)
        print(r)

    print(f"\n{'='*100}")
    print("SUB-DOMAIN #1: AT-BASKET FINISHING (2-season 60/40)")
    print(f"{'='*100}")
    print(header)
    print("-" * 100)

    s1 = ["subdomain_1_at_basket_finishing"]
    row("Rim FG% (weighted)", s1 + ["rim_fg_pct"], "weighted", True)
    row("  current", s1 + ["rim_fg_pct"], "current", True)
    row("  prior", s1 + ["rim_fg_pct"], "prior", True)
    row("Rim FGA (weighted vol)", s1 + ["rim_volume"], "weighted")
    row("% Shots at Rim (weighted)", s1 + ["pct_shots_at_rim"], "weighted", True)
    row("Dunk Rate (weighted)", s1 + ["dunk_rate"], "weighted", True)
    row("Non-Dunk Rim FG% (weighted)", s1 + ["non_dunk_rim_fg_pct"], "weighted", True)
    row("FT% (weighted)", s1 + ["ft_pct"], "weighted", True)
    row("% Assisted (weighted)", s1 + ["pct_assisted_overall"], "weighted", True)

    s2 = ["subdomain_2_contact_finishing"]
    print(f"\n{'='*100}")
    print("SUB-DOMAIN #2: CONTACT FINISHING (2-season 60/40)")
    print(f"{'='*100}")
    print(header)
    print("-" * 100)

    row("FTR (weighted)", s2 + ["ftr"], "weighted")
    row("  current", s2 + ["ftr"], "current")
    row("  prior", s2 + ["ftr"], "prior")
    row("FT% (weighted)", s2 + ["ft_pct"], "weighted", True)
    row("Drives/game (weighted)", s2 + ["drives", "drives_pg"], "weighted")
    row("Drive FG% (weighted)", s2 + ["drives", "drive_fg_pct"], "weighted", True)
    row("Drive PPP (weighted)", s2 + ["drives", "drive_ppp"], "weighted")
    row("Paint non-RA FG% (weighted)", s2 + ["paint_non_ra_fg_pct"], "weighted", True)

    print(f"\n{'='*100}")


# ──────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
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

    if len(window.seasons_used) == 1:
        CURRENT_SEASON = window.seasons_used[0][0]
        W_CURRENT = window.seasons_used[0][1]
        PRIOR_SEASON = None
        W_PRIOR = 0.0
    else:
        CURRENT_SEASON, W_CURRENT = window.seasons_used[0]
        PRIOR_SEASON, W_PRIOR = window.seasons_used[1]

    print(f"Pulling league-wide data for {CURRENT_SEASON}...")
    drives_cur = get_league_drives(CURRENT_SEASON)
    dd_cur = get_league_defender_distance(CURRENT_SEASON)

    if PRIOR_SEASON:
        print(f"Pulling league-wide data for {PRIOR_SEASON}...")
        drives_pri = get_league_drives(PRIOR_SEASON)
        dd_pri = get_league_defender_distance(PRIOR_SEASON)
    else:
        drives_pri = {"error": "single-season mode"}
        dd_pri = {k: {"error": "single-season mode"} for k in [
            "very_tight_0_2", "tight_2_4", "open_4_6", "wide_open_6plus"]}

    profiles = []
    try:
        profile = pull_finishing_profile_2season(
            args.player, CURRENT_SEASON, PRIOR_SEASON,
            drives_cur, drives_pri, dd_cur, dd_pri,
        )
        profile["evaluation_window"] = {
            "mode": window.mode,
            "seasons_used": [{"season": s, "weight": w} for s, w in window.seasons_used],
            "flag_template": window.flag_template,
            "age_concern": window.age_concern,
        }
        profiles.append(profile)
    except Exception as e:
        print(f"ERROR pulling {args.player}: {e}")

    if profiles:
        print_comparison(profiles)

    save_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "finishing_output.json",
    )
    with open(save_path, "w") as f:
        json.dump(profiles, f, indent=2, default=str)
    print(f"\nRaw data saved to {save_path}")
