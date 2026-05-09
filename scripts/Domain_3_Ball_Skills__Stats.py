"""
Layer 1 Scouting Rubric — Domain 3: Ball Skills
Data pipeline using nba_api.

2-season evaluation window with 60/40 recency weighting (S83 decision).
Each endpoint queried independently per season with explicit Season= parameter.

Sub-Domain #8  — Handling / Creation
Sub-Domain #9  — Touch / Feel
Sub-Domain #10 — Ball Security

Session 84.
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
    playerdashboardbyclutch,
    leaguedashptstats,
    leaguedashplayerstats,
    synergyplaytypes,
)

# ──────────────────────────────────────────────────────────────────────
# Evaluation window — set by main() via eval_window.determine_evaluation_window
# ──────────────────────────────────────────────────────────────────────

from eval_window import determine_evaluation_window, format_window
from config import SCRIPTS_DIR

CURRENT_SEASON = None
PRIOR_SEASON = None  # None triggers single-season path (R12_ANCHOR, OVERRIDE, ROOKIE)
W_CURRENT = 0.60
W_PRIOR = 0.40
DELAY = 1.0  # seconds between API calls


# ──────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────

# Math lives in shared_math; thin local delegations preserve the
# runtime-mutated W_CURRENT / W_PRIOR module globals as the per-call
# weight source. `sb` stays local because Domain_3 omits total_volume
# from its output dicts (shared_math.stat_block always emits it).

from shared_math import (
    safe_int as _si,
    safe_float as _sf,
    safe_round as _sr,
    volume_weighted_pct as _shared_volume_weighted_pct,
    simple_weighted as _shared_simple_weighted,
)


def vol_wt(cur_m, cur_a, pri_m, pri_a):
    return _shared_volume_weighted_pct(cur_m, cur_a, pri_m, pri_a,
                                       w_cur=W_CURRENT, w_pri=W_PRIOR)


def sw(cur, pri):
    return _shared_simple_weighted(cur, pri, w_cur=W_CURRENT, w_pri=W_PRIOR)


def sb(cur, pri, cur_vol=None, pri_vol=None, is_rate=False):
    """Stat block: current / prior / weighted."""
    if pri is None:
        bl = {"current": cur, "prior": "N/A", "weighted": cur}
        if cur_vol is not None:
            bl["current_volume"] = cur_vol
            bl["prior_volume"] = "N/A"
        return bl

    if is_rate:
        w = sw(cur, pri)
    elif cur_vol is not None and pri_vol is not None:
        w = vol_wt(
            cur * cur_vol if cur_vol > 0 else 0, cur_vol,
            pri * pri_vol if pri_vol > 0 else 0, pri_vol,
        )
    else:
        w = sw(cur, pri)

    bl = {"current": cur, "prior": pri, "weighted": w}
    if cur_vol is not None:
        bl["current_volume"] = cur_vol
        bl["prior_volume"] = pri_vol
    return bl


def find_player_id(name: str) -> dict:
    matches = players.find_players_by_full_name(name)
    if not matches:
        raise ValueError(f"No player found for '{name}'")
    active = [p for p in matches if p["is_active"]]
    p = active[0] if active else matches[0]
    return {"id": p["id"], "full_name": p["full_name"]}


# ──────────────────────────────────────────────────────────────────────
# Stream 1 — Play-Type Creation (Synergy)
# ──────────────────────────────────────────────────────────────────────

def get_synergy_play_type(play_type: str, season: str, retries: int = 3) -> dict:
    """Pull a Synergy play type for all players. Retry on failure."""
    for attempt in range(retries):
        time.sleep(DELAY + attempt * 1.0)  # Increasing backoff
        try:
            s = synergyplaytypes.SynergyPlayTypes(
                play_type_nullable=play_type,
                per_mode_simple="Totals",
                season=season,
                season_type_all_star="Regular Season",
                player_or_team_abbreviation="P",
                type_grouping_nullable="offensive",
            )
            df = s.get_data_frames()[0]
            if not df.empty:
                return {"df": df}
        except Exception as e:
            if attempt == retries - 1:
                return {"error": str(e)}
            print(f"    Synergy {play_type} {season} attempt {attempt+1} failed, retrying...")
    return {"error": "Max retries exceeded"}


def extract_synergy(result: dict, pid: int) -> dict:
    if "error" in result:
        return None
    df = result["df"]
    row = df[df["PLAYER_ID"] == pid]
    if row.empty:
        return None
    r = row.iloc[0]
    return {
        "poss": _si(r.get("POSS", 0)),
        "ppp": _sr(r.get("PPP", 0)),
        "fg_pct": _sr(r.get("FG_PCT", 0)),
        "tov_pct": _sr(r.get("TOV_POSS_PCT", 0)),
        "percentile": _sr(r.get("PERCENTILE", 0)),
        "poss_pct": _sr(r.get("POSS_PCT", 0)),
    }


# ──────────────────────────────────────────────────────────────────────
# Stream 2 — Tracking Possessions
# ──────────────────────────────────────────────────────────────────────

def get_league_possessions(season: str) -> dict:
    time.sleep(DELAY)
    try:
        s = leaguedashptstats.LeagueDashPtStats(
            pt_measure_type="Possessions",
            season=season,
            per_mode_simple="PerGame",
            player_or_team="Player",
            season_type_all_star="Regular Season",
        )
        return {"df": s.get_data_frames()[0]}
    except Exception as e:
        return {"error": str(e)}


def extract_possessions(result: dict, pid: int) -> dict:
    if "error" in result:
        return None
    df = result["df"]
    row = df[df["PLAYER_ID"] == pid]
    if row.empty:
        return None
    r = row.iloc[0]
    return {
        "touches_pg": _sr(r.get("TOUCHES", 0), 1),
        "time_of_poss": _sr(r.get("TIME_OF_POSS", 0), 1),
        "avg_sec_per_touch": _sr(r.get("AVG_SEC_PER_TOUCH", 0), 2),
        "avg_drib_per_touch": _sr(r.get("AVG_DRIB_PER_TOUCH", 0), 2),
        "pts_per_touch": _sr(r.get("PTS_PER_TOUCH", 0), 3),
        "paint_touches": _sr(r.get("PAINT_TOUCHES", 0), 1),
        "elbow_touches": _sr(r.get("ELBOW_TOUCHES", 0), 1),
        "front_ct_touches": _sr(r.get("FRONT_CT_TOUCHES", 0), 1),
    }


# ──────────────────────────────────────────────────────────────────────
# Stream 3 — Drives
# ──────────────────────────────────────────────────────────────────────

def get_league_drives(season: str) -> dict:
    time.sleep(DELAY)
    try:
        s = leaguedashptstats.LeagueDashPtStats(
            pt_measure_type="Drives",
            season=season,
            per_mode_simple="PerGame",
            player_or_team="Player",
            season_type_all_star="Regular Season",
        )
        return {"df": s.get_data_frames()[0]}
    except Exception as e:
        return {"error": str(e)}


def extract_drives(result: dict, pid: int) -> dict:
    if "error" in result:
        return None
    df = result["df"]
    row = df[df["PLAYER_ID"] == pid]
    if row.empty:
        return None
    r = row.iloc[0]
    drives = _sf(r.get("DRIVES", 0))
    pts = _sf(r.get("DRIVE_PTS", 0))
    tov = _sf(r.get("DRIVE_TOV", 0))
    return {
        "drives_pg": round(drives, 1),
        "drive_fg_pct": _sr(r.get("DRIVE_FG_PCT", 0)),
        "drive_pts_pg": round(pts, 1),
        "drive_ppp": round(pts / drives, 3) if drives > 0 else 0,
        "drive_tov_pg": round(tov, 1),
        "drive_tov_pct": round(tov / drives, 3) if drives > 0 else 0,
        "drive_ast_pg": _sr(r.get("DRIVE_AST", 0), 1),
    }


# ──────────────────────────────────────────────────────────────────────
# Stream 4 — Floater-Range Shots (ShotChartDetail)
# ──────────────────────────────────────────────────────────────────────

def get_floater_data(player_id: int, season: str) -> dict:
    """ShotChartDetail — filter to 4-14 ft range."""
    time.sleep(DELAY)
    try:
        shots = shotchartdetail.ShotChartDetail(
            player_id=player_id,
            team_id=0,
            season_nullable=season,
            context_measure_simple="FGA",
        )
        df = shots.get_data_frames()[0]
        if df.empty:
            return None

        total_fga = len(df)

        # Floater range: 4-14 feet
        floater = df[(df["SHOT_DISTANCE"] >= 4) & (df["SHOT_DISTANCE"] <= 14)]
        fl_fga = len(floater)
        fl_fgm = int((floater["SHOT_MADE_FLAG"] == 1).sum())

        # Non-dunk rim FG% (cross-reference for #9)
        rim = df[df["SHOT_ZONE_BASIC"] == "Restricted Area"]
        rim_total = len(rim)
        rim_made = int((rim["SHOT_MADE_FLAG"] == 1).sum())
        dunks = rim[rim["ACTION_TYPE"].str.contains("dunk", case=False, na=False)]
        nd_fga = rim_total - len(dunks)
        nd_fgm = rim_made - int((dunks["SHOT_MADE_FLAG"] == 1).sum())

        return {
            "floater_fga": fl_fga,
            "floater_fgm": fl_fgm,
            "floater_pct": round(fl_fgm / fl_fga, 3) if fl_fga > 0 else 0,
            "floater_pct_of_total": round(fl_fga / total_fga, 3) if total_fga > 0 else 0,
            "non_dunk_rim_fga": nd_fga,
            "non_dunk_rim_fgm": nd_fgm,
            "non_dunk_rim_pct": round(nd_fgm / nd_fga, 3) if nd_fga > 0 else 0,
            "total_fga": total_fga,
        }
    except Exception as e:
        return None


# ──────────────────────────────────────────────────────────────────────
# Stream 5 — Basic + Advanced Stats
# ──────────────────────────────────────────────────────────────────────

def get_league_advanced(season: str) -> dict:
    time.sleep(DELAY)
    try:
        s = leaguedashplayerstats.LeagueDashPlayerStats(
            season=season,
            per_mode_detailed="Totals",
            measure_type_detailed_defense="Advanced",
            season_type_all_star="Regular Season",
        )
        return {"df": s.get_data_frames()[0]}
    except Exception as e:
        return {"error": str(e)}


def get_league_base(season: str) -> dict:
    time.sleep(DELAY)
    try:
        s = leaguedashplayerstats.LeagueDashPlayerStats(
            season=season,
            per_mode_detailed="Totals",
            season_type_all_star="Regular Season",
        )
        return {"df": s.get_data_frames()[0]}
    except Exception as e:
        return {"error": str(e)}


def extract_advanced(result: dict, pid: int) -> dict:
    if "error" in result:
        return None
    df = result["df"]
    row = df[df["PLAYER_ID"] == pid]
    if row.empty:
        return None
    r = row.iloc[0]
    return {
        "e_tov_pct": _sr(r.get("E_TOV_PCT", 0), 1),
        "usg_pct": _sr(r.get("USG_PCT", 0), 3),
        "ast_to": _sr(r.get("AST_TO", 0), 2),
        "ast_ratio": _sr(r.get("AST_RATIO", 0), 1),
        "ast_pct": _sr(r.get("AST_PCT", 0), 3),
    }


def extract_base(result: dict, pid: int) -> dict:
    if "error" in result:
        return None
    df = result["df"]
    row = df[df["PLAYER_ID"] == pid]
    if row.empty:
        return None
    r = row.iloc[0]
    return {
        "ast": _si(r.get("AST", 0)),
        "tov": _si(r.get("TOV", 0)),
        "gp": _si(r.get("GP", 0)),
        "min": _sr(r.get("MIN", 0), 1),
        "fta": _si(r.get("FTA", 0)),
        "ftm": _si(r.get("FTM", 0)),
        "fga": _si(r.get("FGA", 0)),
    }


# ──────────────────────────────────────────────────────────────────────
# Stream 6 — Clutch TOV
# ──────────────────────────────────────────────────────────────────────

def get_clutch_data(player_id: int, season: str) -> dict:
    time.sleep(DELAY)
    try:
        c = playerdashboardbyclutch.PlayerDashboardByClutch(
            player_id=player_id,
            season=season,
            per_mode_detailed="Totals",
        )
        frames = c.get_data_frames()
        # Frame 6 = Last 5 Min +/- 5 Points
        if len(frames) > 6 and not frames[6].empty:
            r = frames[6].iloc[0]
            return {
                "clutch_tov": _si(r.get("TOV", 0)),
                "clutch_min": _sr(r.get("MIN", 0), 1),
                "clutch_ast": _si(r.get("AST", 0)),
                "clutch_fga": _si(r.get("FGA", 0)),
                "clutch_fta": _si(r.get("FTA", 0)),
                "clutch_ft_pct": _sr(r.get("FT_PCT", 0)),
            }
        return None
    except Exception as e:
        return None


# ──────────────────────────────────────────────────────────────────────
# Profile assembly
# ──────────────────────────────────────────────────────────────────────

def build_profile(
    player_name: str,
    # Synergy by season: dict of {play_type: result} per season
    syn_cur: dict, syn_pri: dict,
    # League-wide by season
    poss_cur, poss_pri,
    drv_cur, drv_pri,
    adv_cur, adv_pri,
    base_cur, base_pri,
) -> dict:

    print(f"\n{'='*60}")
    print(f"Building profile: {player_name}")
    if PRIOR_SEASON:
        print(f"  Window: {CURRENT_SEASON} ({int(W_CURRENT*100)}%) + {PRIOR_SEASON} ({int(W_PRIOR*100)}%)")
    else:
        print(f"  Window: {CURRENT_SEASON} (single-season)")
    print(f"{'='*60}")

    player = find_player_id(player_name)
    pid = player["id"]
    print(f"  Found: {player['full_name']} (ID: {pid})")

    # ── Per-player endpoints (current, then prior or stubs for single-season) ──
    print(f"  Floater data {CURRENT_SEASON}...")
    fl_c = get_floater_data(pid, CURRENT_SEASON)
    print(f"  Clutch {CURRENT_SEASON}...")
    cl_c = get_clutch_data(pid, CURRENT_SEASON)

    if PRIOR_SEASON is None:
        print("  (single-season mode -- skipping prior-season pulls)")
        fl_p = None
        cl_p = None
    else:
        print(f"  Floater data {PRIOR_SEASON}...")
        fl_p = get_floater_data(pid, PRIOR_SEASON)
        print(f"  Clutch {PRIOR_SEASON}...")
        cl_p = get_clutch_data(pid, PRIOR_SEASON)

    # ── League-wide extractions ──
    print("  Extracting league data...")

    def _syn(play_type, season_data):
        return extract_synergy(season_data.get(play_type, {"error": "not pulled"}), pid)

    # Synergy play types
    iso_c = _syn("Isolation", syn_cur)
    iso_p = _syn("Isolation", syn_pri)
    pnr_c = _syn("PRBallHandler", syn_cur)
    pnr_p = _syn("PRBallHandler", syn_pri)
    ho_c = _syn("Handoff", syn_cur)
    ho_p = _syn("Handoff", syn_pri)

    # Possessions
    pos_c = extract_possessions(poss_cur, pid)
    pos_p = extract_possessions(poss_pri, pid)

    # Drives
    dr_c = extract_drives(drv_cur, pid)
    dr_p = extract_drives(drv_pri, pid)

    # Advanced + Base
    av_c = extract_advanced(adv_cur, pid)
    av_p = extract_advanced(adv_pri, pid)
    bs_c = extract_base(base_cur, pid)
    bs_p = extract_base(base_pri, pid)

    # ── Helper ──
    def _g(d, k):
        if d is None:
            return None
        return d.get(k)

    def syn_block(cur, pri, key):
        """Build stat block for a synergy metric."""
        c = _g(cur, key)
        p = _g(pri, key)
        if c is None:
            c = 0
        return sb(c, p, is_rate=True)

    def syn_vol_block(cur, pri, key):
        c = _g(cur, key) if cur else 0
        p = _g(pri, key) if pri else None
        return sb(c or 0, p)

    # ── Stream 7: Derived metrics ──
    # TOV per 100 touches
    touches_c = _g(pos_c, "touches_pg") or 0
    touches_p = _g(pos_p, "touches_pg")
    tov_c = (_g(bs_c, "tov") or 0) / (_g(bs_c, "gp") or 1) if bs_c else 0  # TOV per game
    tov_p = (_g(bs_p, "tov") or 0) / (_g(bs_p, "gp") or 1) if bs_p else None
    tov_per_100_c = round((tov_c / touches_c) * 100, 1) if touches_c > 0 else 0
    tov_per_100_p = round((tov_p / touches_p) * 100, 1) if touches_p and touches_p > 0 else None

    # A:TO from base stats
    ast_c = _g(bs_c, "ast") or 0
    tov_total_c = _g(bs_c, "tov") or 0
    ato_c = round(ast_c / tov_total_c, 2) if tov_total_c > 0 else 0
    ast_p = _g(bs_p, "ast")
    tov_total_p = _g(bs_p, "tov")
    ato_p = round(ast_p / tov_total_p, 2) if tov_total_p and tov_total_p > 0 else None

    # FT% (from base stats totals)
    ft_pct_c = round((_g(bs_c, "ftm") or 0) / (_g(bs_c, "fta") or 1), 3) if (_g(bs_c, "fta") or 0) > 0 else 0
    ft_pct_p = round((_g(bs_p, "ftm") or 0) / (_g(bs_p, "fta") or 1), 3) if bs_p and (_g(bs_p, "fta") or 0) > 0 else None

    # ── Assemble ──
    profile = {
        "player": player["full_name"],
        "evaluation_window": {
            "current_season": CURRENT_SEASON,
            "prior_season": PRIOR_SEASON,
            "weighting": "60/40 current/prior",
        },

        # ── #8 Handling / Creation ──
        "subdomain_8_handling_creation": {
            "play_type_creation": {
                "isolation": {
                    "ppp": syn_block(iso_c, iso_p, "ppp"),
                    "poss": syn_vol_block(iso_c, iso_p, "poss"),
                    "fg_pct": syn_block(iso_c, iso_p, "fg_pct"),
                    "tov_pct": syn_block(iso_c, iso_p, "tov_pct"),
                    "percentile": syn_block(iso_c, iso_p, "percentile"),
                },
                "pnr_ball_handler": {
                    "ppp": syn_block(pnr_c, pnr_p, "ppp"),
                    "poss": syn_vol_block(pnr_c, pnr_p, "poss"),
                    "fg_pct": syn_block(pnr_c, pnr_p, "fg_pct"),
                    "tov_pct": syn_block(pnr_c, pnr_p, "tov_pct"),
                    "percentile": syn_block(pnr_c, pnr_p, "percentile"),
                },
                "handoff": {
                    "ppp": syn_block(ho_c, ho_p, "ppp"),
                    "poss": syn_vol_block(ho_c, ho_p, "poss"),
                    "fg_pct": syn_block(ho_c, ho_p, "fg_pct"),
                    "tov_pct": syn_block(ho_c, ho_p, "tov_pct"),
                },
            },
            "tracking_possessions": {
                "touches_pg": sb(_g(pos_c, "touches_pg") or 0, _g(pos_p, "touches_pg"), is_rate=True),
                "time_of_poss": sb(_g(pos_c, "time_of_poss") or 0, _g(pos_p, "time_of_poss"), is_rate=True),
                "avg_drib_per_touch": sb(_g(pos_c, "avg_drib_per_touch") or 0, _g(pos_p, "avg_drib_per_touch"), is_rate=True),
                "pts_per_touch": sb(_g(pos_c, "pts_per_touch") or 0, _g(pos_p, "pts_per_touch"), is_rate=True),
            },
            "drives": {
                "drives_pg": sb(_g(dr_c, "drives_pg") or 0, _g(dr_p, "drives_pg"), is_rate=True),
                "drive_fg_pct": sb(_g(dr_c, "drive_fg_pct") or 0, _g(dr_p, "drive_fg_pct"), is_rate=True),
                "drive_pts_pg": sb(_g(dr_c, "drive_pts_pg") or 0, _g(dr_p, "drive_pts_pg"), is_rate=True),
                "drive_tov_pct": sb(_g(dr_c, "drive_tov_pct") or 0, _g(dr_p, "drive_tov_pct"), is_rate=True),
                "drive_ast_pg": sb(_g(dr_c, "drive_ast_pg") or 0, _g(dr_p, "drive_ast_pg"), is_rate=True),
            },
            "context": {
                "usg_pct": sb(_g(av_c, "usg_pct") or 0, _g(av_p, "usg_pct"), is_rate=True),
            },
        },

        # ── #9 Touch / Feel ──
        "subdomain_9_touch_feel": {
            "floater_range_4_14ft": {
                "fg_pct": sb(
                    _g(fl_c, "floater_pct") or 0,
                    _g(fl_p, "floater_pct"),
                    _g(fl_c, "floater_fga") or 0,
                    _g(fl_p, "floater_fga"),
                ),
                "fga": sb(_g(fl_c, "floater_fga") or 0, _g(fl_p, "floater_fga")),
                "pct_of_total_fga": sb(
                    _g(fl_c, "floater_pct_of_total") or 0,
                    _g(fl_p, "floater_pct_of_total"),
                    is_rate=True,
                ),
            },
            "non_dunk_rim_fg_pct": sb(
                _g(fl_c, "non_dunk_rim_pct") or 0,
                _g(fl_p, "non_dunk_rim_pct"),
                _g(fl_c, "non_dunk_rim_fga") or 0,
                _g(fl_p, "non_dunk_rim_fga"),
            ),
            "ft_pct": sb(ft_pct_c, ft_pct_p,
                         _g(bs_c, "fta") or 0, _g(bs_p, "fta")),
        },

        # ── #10 Ball Security ──
        "subdomain_10_ball_security": {
            "tov_per_100_touches": sb(tov_per_100_c, tov_per_100_p, is_rate=True),
            "e_tov_pct": sb(_g(av_c, "e_tov_pct") or 0, _g(av_p, "e_tov_pct"), is_rate=True),
            "ast_to_ratio": sb(ato_c, ato_p, is_rate=True),
            "touches_pg": sb(touches_c, touches_p, is_rate=True),
            "raw_ast": sb(ast_c, ast_p),
            "raw_tov": sb(tov_total_c, tov_total_p),
            "clutch": {
                "tov": sb(_g(cl_c, "clutch_tov") or 0, _g(cl_p, "clutch_tov")),
                "min": sb(_g(cl_c, "clutch_min") or 0, _g(cl_p, "clutch_min")),
                "ast": sb(_g(cl_c, "clutch_ast") or 0, _g(cl_p, "clutch_ast")),
            },
        },
    }
    return profile


# ──────────────────────────────────────────────────────────────────────
# Display
# ──────────────────────────────────────────────────────────────────────

def print_results(profiles: list):
    W = 14
    header = f"{'Metric':<40}"
    for p in profiles:
        name = p["player"].split()[-1][:W]
        header += f"  {name:>{W}}"

    def val(p, path, field="weighted"):
        d = p
        for k in path:
            d = d.get(k, {}) if isinstance(d, dict) else {}
        v = d.get(field, "N/A") if isinstance(d, dict) else "N/A"
        return v

    def pct(v):
        if isinstance(v, (int, float)) and v == v:
            return f"  {v:>{W}.1%}"
        return f"  {'N/A':>{W}}"

    def dec(v, d=3):
        if isinstance(v, (int, float)) and v == v:
            return f"  {v:>{W}.{d}f}"
        return f"  {'N/A':>{W}}"

    def num(v):
        if isinstance(v, (int, float)) and v == v:
            return f"  {int(v):>{W}}"
        return f"  {'N/A':>{W}}"

    def row(label, path, fmt_fn, field="weighted"):
        r = f"{label:<40}"
        for p in profiles:
            r += fmt_fn(val(p, path, field))
        print(r)

    # ═══ #8 ═══
    s8 = "subdomain_8_handling_creation"
    print(f"\n{'='*105}")
    print("=== #8 HANDLING / CREATION (2-season 60/40) ===")
    print(f"{'='*105}")
    print(header)
    print("-" * 105)

    print("  Play-Type Creation:")
    row("    ISO PPP", [s8, "play_type_creation", "isolation", "ppp"], lambda v: dec(v))
    row("    ISO Poss", [s8, "play_type_creation", "isolation", "poss"], num)
    row("    ISO FG%", [s8, "play_type_creation", "isolation", "fg_pct"], pct)
    row("    ISO TOV%", [s8, "play_type_creation", "isolation", "tov_pct"], pct)
    row("    ISO Percentile", [s8, "play_type_creation", "isolation", "percentile"], pct)
    row("    PnR BH PPP", [s8, "play_type_creation", "pnr_ball_handler", "ppp"], lambda v: dec(v))
    row("    PnR BH Poss", [s8, "play_type_creation", "pnr_ball_handler", "poss"], num)
    row("    PnR BH FG%", [s8, "play_type_creation", "pnr_ball_handler", "fg_pct"], pct)
    row("    PnR BH TOV%", [s8, "play_type_creation", "pnr_ball_handler", "tov_pct"], pct)
    row("    PnR BH Percentile", [s8, "play_type_creation", "pnr_ball_handler", "percentile"], pct)
    row("    Handoff PPP", [s8, "play_type_creation", "handoff", "ppp"], lambda v: dec(v))
    row("    Handoff Poss", [s8, "play_type_creation", "handoff", "poss"], num)

    print("  Tracking Possessions:")
    row("    Touches/G", [s8, "tracking_possessions", "touches_pg"], lambda v: dec(v, 1))
    row("    Time of Poss (min)", [s8, "tracking_possessions", "time_of_poss"], lambda v: dec(v, 1))
    row("    Dribbles/Touch", [s8, "tracking_possessions", "avg_drib_per_touch"], lambda v: dec(v, 2))
    row("    Points/Touch", [s8, "tracking_possessions", "pts_per_touch"], lambda v: dec(v, 3))

    print("  Drives:")
    row("    Drives/G", [s8, "drives", "drives_pg"], lambda v: dec(v, 1))
    row("    Drive FG%", [s8, "drives", "drive_fg_pct"], pct)
    row("    Drive PTS/G", [s8, "drives", "drive_pts_pg"], lambda v: dec(v, 1))
    row("    Drive TOV%", [s8, "drives", "drive_tov_pct"], pct)
    row("    Drive AST/G", [s8, "drives", "drive_ast_pg"], lambda v: dec(v, 1))

    print("  Context:")
    row("    USG%", [s8, "context", "usg_pct"], pct)

    # ═══ #9 ═══
    s9 = "subdomain_9_touch_feel"
    print(f"\n{'='*105}")
    print("=== #9 TOUCH / FEEL (2-season 60/40) ===")
    print(f"{'='*105}")
    print(header)
    print("-" * 105)

    row("Floater FG% (4-14ft)", [s9, "floater_range_4_14ft", "fg_pct"], pct)
    row("  current", [s9, "floater_range_4_14ft", "fg_pct"], pct, "current")
    row("  prior", [s9, "floater_range_4_14ft", "fg_pct"], pct, "prior")
    row("Floater FGA", [s9, "floater_range_4_14ft", "fga"], num)
    row("Floater as % of Total FGA", [s9, "floater_range_4_14ft", "pct_of_total_fga"], pct)
    row("Non-Dunk Rim FG%", [s9, "non_dunk_rim_fg_pct"], pct)
    row("FT% (touch proxy)", [s9, "ft_pct"], pct)

    # ═══ #10 ═══
    s10 = "subdomain_10_ball_security"
    print(f"\n{'='*105}")
    print("=== #10 BALL SECURITY (2-season 60/40) ===")
    print(f"{'='*105}")
    print(header)
    print("-" * 105)

    row("TOV per 100 Touches", [s10, "tov_per_100_touches"], lambda v: dec(v, 1))
    row("  current", [s10, "tov_per_100_touches"], lambda v: dec(v, 1), "current")
    row("  prior", [s10, "tov_per_100_touches"], lambda v: dec(v, 1), "prior")
    row("Estimated TOV%", [s10, "e_tov_pct"], lambda v: dec(v, 1))
    row("A:TO Ratio", [s10, "ast_to_ratio"], lambda v: dec(v, 2))
    row("Touches/G", [s10, "touches_pg"], lambda v: dec(v, 1))
    row("Raw AST (season)", [s10, "raw_ast"], num)
    row("Raw TOV (season)", [s10, "raw_tov"], num)
    row("Clutch TOV", [s10, "clutch", "tov"], num)
    row("Clutch MIN", [s10, "clutch", "min"], lambda v: dec(v, 1))
    row("Clutch AST", [s10, "clutch", "ast"], num)

    print(f"\n{'='*105}")


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

    target_player = args.player

    # ── League-wide pulls: current season ──
    PLAY_TYPES = ["Isolation", "PRBallHandler", "Handoff"]

    syn_cur = {}
    for pt in PLAY_TYPES:
        print(f"Pulling Synergy {pt} ({CURRENT_SEASON})...")
        syn_cur[pt] = get_synergy_play_type(pt, CURRENT_SEASON)
        status = f"{len(syn_cur[pt]['df'])} rows" if "df" in syn_cur[pt] else f"ERROR: {syn_cur[pt].get('error','?')}"
        print(f"  -> {status}")

    # ── League-wide pulls: prior (or stubs for single-season) ──
    syn_pri = {}
    if PRIOR_SEASON:
        for pt in PLAY_TYPES:
            print(f"Pulling Synergy {pt} ({PRIOR_SEASON})...")
            syn_pri[pt] = get_synergy_play_type(pt, PRIOR_SEASON)
            status = f"{len(syn_pri[pt]['df'])} rows" if "df" in syn_pri[pt] else f"ERROR: {syn_pri[pt].get('error','?')}"
            print(f"  -> {status}")
    else:
        for pt in PLAY_TYPES:
            syn_pri[pt] = {"error": "single-season mode"}

    print(f"\nPulling possessions tracking ({CURRENT_SEASON})...")
    poss_cur = get_league_possessions(CURRENT_SEASON)
    if PRIOR_SEASON:
        print(f"Pulling possessions tracking ({PRIOR_SEASON})...")
        poss_pri = get_league_possessions(PRIOR_SEASON)
    else:
        poss_pri = {"error": "single-season mode"}

    print(f"Pulling drives ({CURRENT_SEASON})...")
    drv_cur = get_league_drives(CURRENT_SEASON)
    if PRIOR_SEASON:
        print(f"Pulling drives ({PRIOR_SEASON})...")
        drv_pri = get_league_drives(PRIOR_SEASON)
    else:
        drv_pri = {"error": "single-season mode"}

    print(f"Pulling advanced stats ({CURRENT_SEASON})...")
    adv_cur = get_league_advanced(CURRENT_SEASON)
    if PRIOR_SEASON:
        print(f"Pulling advanced stats ({PRIOR_SEASON})...")
        adv_pri = get_league_advanced(PRIOR_SEASON)
    else:
        adv_pri = {"error": "single-season mode"}

    print(f"Pulling base stats ({CURRENT_SEASON})...")
    base_cur = get_league_base(CURRENT_SEASON)
    if PRIOR_SEASON:
        print(f"Pulling base stats ({PRIOR_SEASON})...")
        base_pri = get_league_base(PRIOR_SEASON)
    else:
        base_pri = {"error": "single-season mode"}

    # ── Per-player profile ──
    profiles = []
    try:
        p = build_profile(
            target_player,
            syn_cur, syn_pri,
            poss_cur, poss_pri,
            drv_cur, drv_pri,
            adv_cur, adv_pri,
            base_cur, base_pri,
        )
        p["evaluation_window"] = {
            "mode": window.mode,
            "seasons_used": [{"season": s, "weight": w} for s, w in window.seasons_used],
            "flag_template": window.flag_template,
            "age_concern": window.age_concern,
        }
        profiles.append(p)
    except Exception as e:
        print(f"ERROR pulling {target_player}: {e}")

    if profiles:
        print_results(profiles)

    # Save
    save_path = SCRIPTS_DIR / "ball_skills_output.json"
    with open(save_path, "w") as f:
        json.dump(profiles, f, indent=2, default=str)
    print(f"\nRaw data saved to {save_path}")
