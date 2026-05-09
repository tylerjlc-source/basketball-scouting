"""
Layer 1 Scouting Rubric — Domain 2: Shooting
Data pipeline using nba_api.

v2 — 2-season evaluation window with 60/40 recency weighting (S83 decision).
Each endpoint queried independently per season with explicit Season= parameter.
Volume-weighted percentages for shooting stats; simple weighted average for rate stats.

Sub-Domain #4  — Catch-and-Shoot 3PT
Sub-Domain #5  — Off-Dribble Shooting
Sub-Domain #6  — Mid-Range
Sub-Domain #7  — Free Throw
Plus overall shooting context (3PT%, 2PT%, TS%, eFG%).
"""

import json
import time
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')  # EW-F04: prevent Windows cp1252 crash on non-ASCII player names
from datetime import date
from nba_api.stats.static import players
from nba_api.stats.endpoints import (
    playercareerstats,
    playerdashboardbyclutch,
    leaguedashptstats,
    leaguedashplayershotlocations,
    leaguedashplayerptshot,
    shotchartdetail,
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


# ──────────────────────────────────────────────────────────────────────
# Helpers — math lives in shared_math; thin local delegations preserve
# the runtime-mutated W_CURRENT / W_PRIOR module globals as the per-call
# weight source.
# ──────────────────────────────────────────────────────────────────────

from shared_math import (
    safe_int as _si,
    safe_round as _sr,
    volume_weighted_pct as _shared_volume_weighted_pct,
    simple_weighted as _shared_simple_weighted,
    stat_block as _shared_stat_block,
)


def vol_wt_pct(cur_m, cur_a, pri_m, pri_a):
    return _shared_volume_weighted_pct(cur_m, cur_a, pri_m, pri_a,
                                       w_cur=W_CURRENT, w_pri=W_PRIOR)


def simple_wt(cur, pri):
    return _shared_simple_weighted(cur, pri, w_cur=W_CURRENT, w_pri=W_PRIOR)


def sb(cur, pri, cur_vol=None, pri_vol=None, is_rate=False):
    return _shared_stat_block(cur, pri, cur_vol=cur_vol, pri_vol=pri_vol,
                              is_rate=is_rate, w_cur=W_CURRENT, w_pri=W_PRIOR)


def find_player_id(player_name: str) -> dict:
    matches = players.find_players_by_full_name(player_name)
    if not matches:
        raise ValueError(f"No player found for '{player_name}'")
    active = [p for p in matches if p["is_active"]]
    player = active[0] if active else matches[0]
    return {"id": player["id"], "full_name": player["full_name"]}


# ──────────────────────────────────────────────────────────────────────
# League-wide endpoints — explicit season on every call
# ──────────────────────────────────────────────────────────────────────

def get_league_cas(season: str) -> dict:
    time.sleep(0.6)
    try:
        s = leaguedashptstats.LeagueDashPtStats(
            pt_measure_type="CatchShoot", season=season,
            per_mode_simple="Totals", player_or_team="Player",
            season_type_all_star="Regular Season",
        )
        return {"df": s.get_data_frames()[0]}
    except Exception as e:
        return {"error": str(e)}


def get_league_pullup(season: str) -> dict:
    time.sleep(0.6)
    try:
        s = leaguedashptstats.LeagueDashPtStats(
            pt_measure_type="PullUpShot", season=season,
            per_mode_simple="Totals", player_or_team="Player",
            season_type_all_star="Regular Season",
        )
        return {"df": s.get_data_frames()[0]}
    except Exception as e:
        return {"error": str(e)}


def get_league_locs(season: str) -> dict:
    time.sleep(0.6)
    try:
        l = leaguedashplayershotlocations.LeagueDashPlayerShotLocations(
            season=season, per_mode_detailed="Totals",
            season_type_all_star="Regular Season",
        )
        return {"df": l.get_data_frames()[0]}
    except Exception as e:
        return {"error": str(e)}


def get_league_iso(season: str) -> dict:
    time.sleep(0.6)
    try:
        s = synergyplaytypes.SynergyPlayTypes(
            play_type_nullable="Isolation", per_mode_simple="Totals",
            season=season, season_type_all_star="Regular Season",
            player_or_team_abbreviation="P", type_grouping_nullable="offensive",
        )
        return {"df": s.get_data_frames()[0]}
    except Exception as e:
        return {"error": str(e)}


def get_league_dd(season: str) -> dict:
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
# Per-player endpoints — explicit season
# ──────────────────────────────────────────────────────────────────────

def get_shot_chart(player_id: int, season: str) -> dict:
    """ShotChartDetail — explicit season. Pull-up zone classification."""
    time.sleep(0.6)
    try:
        shots = shotchartdetail.ShotChartDetail(
            player_id=player_id, team_id=0,
            season_nullable=season, context_measure_simple="FGA",
        )
        df = shots.get_data_frames()[0]
        if df.empty:
            return {"error": "No shot chart data"}

        pullup_types = ["Pullup Jump shot", "Running Pull-Up Jump Shot",
                        "Step Back Jump shot", "Step Back Bank Jump Shot"]
        pu = df[df["ACTION_TYPE"].isin(pullup_types)]

        zones = {}
        for z in ["Above the Break 3", "Left Corner 3", "Right Corner 3",
                   "Mid-Range", "In The Paint (Non-RA)", "Restricted Area"]:
            zf = pu[pu["SHOT_ZONE_BASIC"] == z]
            m = int((zf["SHOT_MADE_FLAG"] == 1).sum())
            a = len(zf)
            zones[z] = {"fgm": m, "fga": a, "fg_pct": round(m / a, 3) if a > 0 else 0}

        pu3a = sum(zones.get(z, {}).get("fga", 0)
                   for z in ["Above the Break 3", "Left Corner 3", "Right Corner 3"])
        pu3m = sum(zones.get(z, {}).get("fgm", 0)
                   for z in ["Above the Break 3", "Left Corner 3", "Right Corner 3"])
        pu_mid_a = zones.get("Mid-Range", {}).get("fga", 0)
        pu_mid_m = zones.get("Mid-Range", {}).get("fgm", 0)

        mid_all = df[df["SHOT_ZONE_BASIC"] == "Mid-Range"]
        mid_splits = {}
        for area in mid_all["SHOT_ZONE_AREA"].unique():
            af = mid_all[mid_all["SHOT_ZONE_AREA"] == area]
            m = int((af["SHOT_MADE_FLAG"] == 1).sum())
            a = len(af)
            mid_splits[area] = {"fgm": m, "fga": a, "fg_pct": round(m / a, 3) if a > 0 else 0}

        total_3pa = len(df[df["SHOT_TYPE"] == "3PT Field Goal"])

        return {
            "pu3_fga": pu3a, "pu3_fgm": pu3m,
            "pu3_pct": round(pu3m / pu3a, 3) if pu3a > 0 else 0,
            "pu_mid_fga": pu_mid_a, "pu_mid_fgm": pu_mid_m,
            "pu_mid_pct": round(pu_mid_m / pu_mid_a, 3) if pu_mid_a > 0 else 0,
            "mid_area_splits": mid_splits,
            "total_3pa": total_3pa,
            "total_fga": len(df),
        }
    except Exception as e:
        return {"error": str(e)}


def get_career_ft(player_id: int) -> dict:
    """Career FT% — season-by-season + career totals. Not season-filtered."""
    time.sleep(0.6)
    try:
        career = playercareerstats.PlayerCareerStats(
            player_id=player_id, per_mode36="Totals",
        )
        season_df = career.get_data_frames()[0]
        career_df = career.get_data_frames()[1]

        ft_career = _sr(career_df.iloc[0]["FT_PCT"]) if not career_df.empty else "N/A"

        trend = []
        for sid in season_df["SEASON_ID"].unique()[-5:]:
            rows = season_df[season_df["SEASON_ID"] == sid]
            fta = int(rows["FTA"].sum())
            ftm = int(rows["FTM"].sum())
            trend.append({"season": sid, "ft_pct": round(ftm / fta, 3) if fta > 0 else 0, "fta": fta})

        return {"ft_pct_career": ft_career, "trend": trend}
    except Exception as e:
        return {"error": str(e)}


def get_season_totals(player_id: int, season: str) -> dict:
    """PlayerCareerStats (Totals) — single season, summed across teams."""
    time.sleep(0.6)
    try:
        career = playercareerstats.PlayerCareerStats(
            player_id=player_id, per_mode36="Totals",
        )
        df = career.get_data_frames()[0]
        rows = df[df["SEASON_ID"] == season]
        if rows.empty:
            return None
        return {
            "fga": int(rows["FGA"].sum()), "fgm": int(rows["FGM"].sum()),
            "fg3a": int(rows["FG3A"].sum()), "fg3m": int(rows["FG3M"].sum()),
            "fta": int(rows["FTA"].sum()), "ftm": int(rows["FTM"].sum()),
            "pts": int(rows["PTS"].sum()), "gp": int(rows["GP"].sum()),
        }
    except Exception as e:
        return None


def get_clutch_ft(player_id: int, season: str) -> dict:
    time.sleep(0.6)
    try:
        c = playerdashboardbyclutch.PlayerDashboardByClutch(
            player_id=player_id, season=season, per_mode_detailed="Totals",
        )
        f = c.get_data_frames()
        if len(f) > 6 and not f[6].empty:
            r = f[6].iloc[0]
            fta = _si(r.get("FTA", 0))
            ftm = _si(r.get("FTM", 0))
            return {"clutch_ft_pct": round(ftm / fta, 3) if fta > 0 else 0,
                    "clutch_fta": fta, "clutch_ftm": ftm}
        return None
    except Exception as e:
        return None


# ──────────────────────────────────────────────────────────────────────
# Extraction helpers
# ──────────────────────────────────────────────────────────────────────

def ex_df(result: dict, pid: int, cols: list) -> dict:
    if "error" in result:
        return None
    df = result["df"]
    row = df[df["PLAYER_ID"] == pid]
    if row.empty:
        return None
    r = row.iloc[0]
    return {c: r.get(c, 0) for c in cols}


def ex_locs(result: dict, pid: int) -> dict:
    if "error" in result:
        return None
    df = result["df"]
    pid_col = df.columns[0]
    row = df[df[pid_col] == pid]
    if row.empty:
        return None
    r = row.iloc[0]
    out = {}
    for z in ["Mid-Range", "Left Corner 3", "Right Corner 3",
              "Above the Break 3", "Corner 3"]:
        try:
            fgm = r[(z, "FGM")]
            fga = r[(z, "FGA")]
            out[z] = {
                "fgm": _si(fgm), "fga": _si(fga),
                "fg_pct": round(_si(fgm) / _si(fga), 3) if _si(fga) > 0 else 0,
            }
        except (KeyError, TypeError):
            out[z] = {"fgm": 0, "fga": 0, "fg_pct": 0}
    return out


def ex_iso(result: dict, pid: int) -> dict:
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
    }


def ex_dd(result: dict, pid: int) -> dict:
    out = {}
    for key, data in result.items():
        if isinstance(data, dict) and "error" in data:
            out[key] = None
            continue
        row = data[data["PLAYER_ID"] == pid]
        if row.empty:
            out[key] = None
            continue
        r = row.iloc[0]
        fg3a = _si(r.get("FG3A", 0))
        fg3m = _si(r.get("FG3M", 0))
        out[key] = {
            "fg3_pct": round(fg3m / fg3a, 3) if fg3a > 0 else 0,
            "fg3a": fg3a, "fg3m": fg3m,
            "fg_pct": _sr(r.get("FG_PCT", 0)),
            "fga": _si(r.get("FGA", 0)),
        }
    return out


# ──────────────────────────────────────────────────────────────────────
# 2-season profile assembly
# ──────────────────────────────────────────────────────────────────────

def pull_shooting_profile_2season(
    player_name: str,
    cur: str, pri: str,
    cas_c, cas_p, pu_c, pu_p, loc_c, loc_p, iso_c, iso_p, dd_c, dd_p,
) -> dict:
    print(f"\n{'='*60}")
    print(f"Pulling shooting data: {player_name}")
    if pri:
        print(f"  Window: {cur} ({int(W_CURRENT*100)}%) + {pri} ({int(W_PRIOR*100)}%)")
    else:
        print(f"  Window: {cur} (single-season)")
    print(f"{'='*60}")

    player = find_player_id(player_name)
    pid = player["id"]
    print(f"  Found: {player['full_name']} (ID: {pid})")

    # Per-player: current season, then prior (or stubs for single-season)
    print(f"  Shot chart {cur}...")
    sc_c = get_shot_chart(pid, cur)
    print(f"  Season totals {cur}...")
    tot_c = get_season_totals(pid, cur)
    print("  Career FT%...")
    ft_car = get_career_ft(pid)
    print(f"  Clutch FT {cur}...")
    clutch_c = get_clutch_ft(pid, cur)

    if pri is None:
        print("  (single-season mode -- skipping prior-season pulls)")
        sc_p = {"error": "single-season mode"}
        tot_p = None
        clutch_p = None
    else:
        print(f"  Shot chart {pri}...")
        sc_p = get_shot_chart(pid, pri)
        print(f"  Season totals {pri}...")
        tot_p = get_season_totals(pid, pri)
        print(f"  Clutch FT {pri}...")
        clutch_p = get_clutch_ft(pid, pri)

    # Extract from league-wide
    print("  Extracting league data...")
    cas_cols = ["CATCH_SHOOT_FG3M", "CATCH_SHOOT_FG3A", "CATCH_SHOOT_FG3_PCT",
                "CATCH_SHOOT_FGM", "CATCH_SHOOT_FGA", "CATCH_SHOOT_EFG_PCT"]
    pu_cols = ["PULL_UP_FG3M", "PULL_UP_FG3A", "PULL_UP_FG3_PCT",
               "PULL_UP_FGM", "PULL_UP_FGA", "PULL_UP_EFG_PCT"]

    cc = ex_df(cas_c, pid, cas_cols)
    cp = ex_df(cas_p, pid, cas_cols)
    pc = ex_df(pu_c, pid, pu_cols)
    pp = ex_df(pu_p, pid, pu_cols)
    lc = ex_locs(loc_c, pid)
    lp = ex_locs(loc_p, pid)
    ic = ex_iso(iso_c, pid)
    ip = ex_iso(iso_p, pid)
    dc = ex_dd(dd_c, pid)
    dp = ex_dd(dd_p, pid)

    has_pri_chart = sc_p is not None and "error" not in sc_p
    has_pri_tot = tot_p is not None

    def _g(d, k, default=0):
        if d is None:
            return None
        return d.get(k, default)

    # ── #4 CAS 3PT ──
    c_cas3a = _si(_g(cc, "CATCH_SHOOT_FG3A")) if cc else 0
    c_cas3m = _si(_g(cc, "CATCH_SHOOT_FG3M")) if cc else 0
    p_cas3a = _si(_g(cp, "CATCH_SHOOT_FG3A")) if cp else None
    p_cas3m = _si(_g(cp, "CATCH_SHOOT_FG3M")) if cp else None

    cas3_pct = sb(
        round(c_cas3m / c_cas3a, 3) if c_cas3a > 0 else 0,
        round(p_cas3m / p_cas3a, 3) if p_cas3a and p_cas3a > 0 else None,
        c_cas3a, p_cas3a,
    )

    # Corner / ATB
    c_corner = lc.get("Corner 3", {}) if lc else {}
    p_corner = lp.get("Corner 3", {}) if lp else {}
    corner_pct = sb(
        c_corner.get("fg_pct", 0),
        p_corner.get("fg_pct", 0) if lp else None,
        c_corner.get("fga", 0),
        p_corner.get("fga", 0) if lp else None,
    )

    c_atb = lc.get("Above the Break 3", {}) if lc else {}
    p_atb = lp.get("Above the Break 3", {}) if lp else {}
    atb_pct = sb(
        c_atb.get("fg_pct", 0),
        p_atb.get("fg_pct", 0) if lp else None,
        c_atb.get("fga", 0),
        p_atb.get("fga", 0) if lp else None,
    )

    # Defender distance 3PT
    dd_3pt = {}
    for key in ["wide_open_6plus", "open_4_6", "tight_2_4", "very_tight_0_2"]:
        c_d = dc.get(key)
        p_d = dp.get(key)
        if c_d:
            dd_3pt[key] = sb(
                c_d["fg3_pct"], p_d["fg3_pct"] if p_d else None,
                c_d["fg3a"], p_d["fg3a"] if p_d else None,
            )
        else:
            dd_3pt[key] = {"current": "N/A", "prior": "N/A", "weighted": "N/A"}

    # Total 3PA
    c_3pa = _g(tot_c, "fg3a", 0) if tot_c else 0
    p_3pa = _g(tot_p, "fg3a", 0) if has_pri_tot else None

    # ── #5 Off-Dribble ──
    c_pu3a = _si(_g(pc, "PULL_UP_FG3A")) if pc else 0
    c_pu3m = _si(_g(pc, "PULL_UP_FG3M")) if pc else 0
    p_pu3a = _si(_g(pp, "PULL_UP_FG3A")) if pp else None
    p_pu3m = _si(_g(pp, "PULL_UP_FG3M")) if pp else None

    pu3_pct = sb(
        round(c_pu3m / c_pu3a, 3) if c_pu3a > 0 else 0,
        round(p_pu3m / p_pu3a, 3) if p_pu3a and p_pu3a > 0 else None,
        c_pu3a, p_pu3a,
    )

    # Pull-up zone split from ShotChart
    sc_pu3 = sb(
        _g(sc_c, "pu3_pct", 0) if sc_c and "error" not in sc_c else 0,
        _g(sc_p, "pu3_pct") if has_pri_chart else None,
        _g(sc_c, "pu3_fga", 0) if sc_c and "error" not in sc_c else 0,
        _g(sc_p, "pu3_fga") if has_pri_chart else None,
    )
    sc_mid = sb(
        _g(sc_c, "pu_mid_pct", 0) if sc_c and "error" not in sc_c else 0,
        _g(sc_p, "pu_mid_pct") if has_pri_chart else None,
        _g(sc_c, "pu_mid_fga", 0) if sc_c and "error" not in sc_c else 0,
        _g(sc_p, "pu_mid_fga") if has_pri_chart else None,
    )

    # ISO
    iso_ppp = sb(
        ic["ppp"] if ic else 0,
        ip["ppp"] if ip else None,
        is_rate=True,
    )

    # ── #6 Mid-Range ──
    c_mid = lc.get("Mid-Range", {}) if lc else {}
    p_mid = lp.get("Mid-Range", {}) if lp else {}
    mid_pct = sb(
        c_mid.get("fg_pct", 0),
        p_mid.get("fg_pct", 0) if lp else None,
        c_mid.get("fga", 0),
        p_mid.get("fga", 0) if lp else None,
    )

    # ── #7 FT ──
    c_fta = _g(tot_c, "fta", 0) if tot_c else 0
    c_ftm = _g(tot_c, "ftm", 0) if tot_c else 0
    p_fta = _g(tot_p, "fta", 0) if has_pri_tot else None
    p_ftm = _g(tot_p, "ftm", 0) if has_pri_tot else None

    ft_pct = sb(
        round(c_ftm / c_fta, 3) if c_fta > 0 else 0,
        round(p_ftm / p_fta, 3) if p_fta and p_fta > 0 else None,
        c_fta, p_fta,
    )

    clutch = sb(
        clutch_c["clutch_ft_pct"] if clutch_c else 0,
        clutch_p["clutch_ft_pct"] if clutch_p else None,
        clutch_c["clutch_fta"] if clutch_c else 0,
        clutch_p["clutch_fta"] if clutch_p else None,
    )

    # ── Overall context ──
    c_fga = _g(tot_c, "fga", 0) if tot_c else 0
    c_fgm = _g(tot_c, "fgm", 0) if tot_c else 0
    c_fg3a = _g(tot_c, "fg3a", 0) if tot_c else 0
    c_fg3m = _g(tot_c, "fg3m", 0) if tot_c else 0
    c_pts = _g(tot_c, "pts", 0) if tot_c else 0
    c_ts = round(c_pts / (2 * (c_fga + 0.44 * c_fta)), 3) if (c_fga + 0.44 * c_fta) > 0 else 0
    c_efg = round((c_fgm + 0.5 * c_fg3m) / c_fga, 3) if c_fga > 0 else 0

    if has_pri_tot:
        p_fga = tot_p["fga"]
        p_fgm = tot_p["fgm"]
        p_fg3a_t = tot_p["fg3a"]
        p_fg3m_t = tot_p["fg3m"]
        p_pts = tot_p["pts"]
        p_fta_t = tot_p["fta"]
        p_ts = round(p_pts / (2 * (p_fga + 0.44 * p_fta_t)), 3) if (p_fga + 0.44 * p_fta_t) > 0 else 0
        p_efg = round((p_fgm + 0.5 * p_fg3m_t) / p_fga, 3) if p_fga > 0 else 0
    else:
        p_ts = None
        p_efg = None

    # ── Assemble ──
    profile = {
        "player": player["full_name"],
        "evaluation_window": {
            "current_season": cur, "prior_season": pri,
            "weighting": "60/40 current/prior",
        },
        "subdomain_4_cas_3pt": {
            "cas_3pt_pct": cas3_pct,
            "cas_3pa": sb(c_cas3a, p_cas3a),
            "corner_3_pct": corner_pct,
            "atb_3_pct": atb_pct,
            "defender_distance_3pt": dd_3pt,
            "total_3pa": sb(c_3pa, p_3pa),
        },
        "subdomain_5_off_dribble": {
            "pullup_3pt_pct": pu3_pct,
            "pullup_3pa": sb(c_pu3a, p_pu3a),
            "pullup_zone_3pt": sc_pu3,
            "pullup_zone_midrange": sc_mid,
            "isolation": {
                "ppp": iso_ppp,
                "poss": sb(ic["poss"] if ic else 0, ip["poss"] if ip else None),
                "fg_pct": sb(ic["fg_pct"] if ic else 0, ip["fg_pct"] if ip else None, is_rate=True),
                "percentile": sb(ic["percentile"] if ic else 0, ip["percentile"] if ip else None, is_rate=True),
            },
        },
        "subdomain_6_midrange": {
            "midrange_fg_pct": mid_pct,
            "midrange_fga": sb(c_mid.get("fga", 0), p_mid.get("fga", 0) if lp else None),
            "pullup_midrange": sc_mid,
        },
        "subdomain_7_ft": {
            "ft_pct": ft_pct,
            "ft_pct_career": ft_car.get("ft_pct_career", "N/A") if ft_car and "error" not in ft_car else "N/A",
            "trend": ft_car.get("trend", []) if ft_car and "error" not in ft_car else [],
            "clutch_ft": clutch,
        },
        "overall_context": {
            "ts_pct": sb(c_ts, p_ts, is_rate=True),
            "efg_pct": sb(c_efg, p_efg, is_rate=True),
            "three_pt_pct": sb(
                round(c_fg3m / c_fg3a, 3) if c_fg3a > 0 else 0,
                round(p_fg3m_t / p_fg3a_t, 3) if has_pri_tot and p_fg3a_t > 0 else None,
                c_fg3a, p_3pa,
            ),
            "total_fga": sb(c_fga, tot_p["fga"] if has_pri_tot else None),
        },
    }
    return profile


# ──────────────────────────────────────────────────────────────────────
# Display
# ──────────────────────────────────────────────────────────────────────

def print_comparison(profiles: list):
    W = 14
    header = f"{'Metric':<42}"
    for p in profiles:
        name = p["player"].split()[-1][:W]
        header += f"  {name:>{W}}"

    def fmt(p, path, field="weighted", as_pct=False):
        d = p
        for k in path:
            d = d.get(k, {}) if isinstance(d, dict) else {}
        val = d.get(field, "N/A") if isinstance(d, dict) else "N/A"
        if isinstance(val, (int, float)) and val == val:
            return f"  {val:>{W}.1%}" if as_pct else f"  {val:>{W}}"
        return f"  {'N/A':>{W}}"

    def row(label, path, field="weighted", as_pct=False):
        r = f"{label:<42}"
        for p in profiles:
            r += fmt(p, path, field, as_pct)
        print(r)

    for section, title, rows in [
        ("subdomain_4_cas_3pt", "SUB-DOMAIN #4: CAS 3PT (2-season 60/40)", [
            ("CAS 3PT% (weighted)", ["cas_3pt_pct"], True),
            ("  current", ["cas_3pt_pct"], True, "current"),
            ("  prior", ["cas_3pt_pct"], True, "prior"),
            ("Corner 3% (weighted)", ["corner_3_pct"], True),
            ("ATB 3% (weighted)", ["atb_3_pct"], True),
            ("Total 3PA (weighted)", ["total_3pa"], False),
        ]),
        ("subdomain_5_off_dribble", "SUB-DOMAIN #5: OFF-DRIBBLE (2-season 60/40)", [
            ("Pull-Up 3PT% (weighted)", ["pullup_3pt_pct"], True),
            ("  current", ["pullup_3pt_pct"], True, "current"),
            ("  prior", ["pullup_3pt_pct"], True, "prior"),
            ("PU Zone 3PT% (ShotChart wt)", ["pullup_zone_3pt"], True),
            ("PU Zone Mid% (ShotChart wt)", ["pullup_zone_midrange"], True),
            ("ISO PPP (weighted)", ["isolation", "ppp"], False),
            ("ISO Percentile (weighted)", ["isolation", "percentile"], True),
        ]),
        ("subdomain_6_midrange", "SUB-DOMAIN #6: MID-RANGE (2-season 60/40)", [
            ("Mid-Range FG% (weighted)", ["midrange_fg_pct"], True),
            ("  current", ["midrange_fg_pct"], True, "current"),
            ("  prior", ["midrange_fg_pct"], True, "prior"),
            ("Mid-Range FGA (weighted)", ["midrange_fga"], False),
        ]),
        ("subdomain_7_ft", "SUB-DOMAIN #7: FREE THROW (2-season 60/40)", [
            ("FT% (weighted)", ["ft_pct"], True),
            ("  current", ["ft_pct"], True, "current"),
            ("  prior", ["ft_pct"], True, "prior"),
            ("Clutch FT% (weighted)", ["clutch_ft"], True),
        ]),
        ("overall_context", "OVERALL SHOOTING CONTEXT (2-season 60/40)", [
            ("TS% (weighted)", ["ts_pct"], True),
            ("eFG% (weighted)", ["efg_pct"], True),
            ("3PT% (weighted)", ["three_pt_pct"], True),
        ]),
    ]:
        print(f"\n{'='*105}")
        print(title)
        print(f"{'='*105}")
        print(header)
        print("-" * 105)
        for r in rows:
            lbl = r[0]
            path = [section] + r[1]
            pct = r[2] if len(r) > 2 else False
            fld = r[3] if len(r) > 3 else "weighted"
            row(lbl, path, fld, pct)

    # FT career + trend (not 2-season weighted)
    print(f"\n{'='*105}")
    print("FT% CAREER + TREND")
    print(f"{'='*105}")
    print(header)
    print("-" * 105)
    r = f"{'FT% Career':<42}"
    for p in profiles:
        val = p["subdomain_7_ft"].get("ft_pct_career", "N/A")
        r += f"  {val:>{W}.1%}" if isinstance(val, (int, float)) else f"  {'N/A':>{W}}"
    print(r)

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

    CUR = CURRENT_SEASON
    PRI = PRIOR_SEASON

    print(f"Pulling league data for {CUR}...")
    cas_c = get_league_cas(CUR)
    pu_c = get_league_pullup(CUR)
    loc_c = get_league_locs(CUR)
    iso_c = get_league_iso(CUR)
    dd_c = get_league_dd(CUR)

    if PRI:
        print(f"\nPulling league data for {PRI}...")
        cas_p = get_league_cas(PRI)
        pu_p = get_league_pullup(PRI)
        loc_p = get_league_locs(PRI)
        iso_p = get_league_iso(PRI)
        dd_p = get_league_dd(PRI)
    else:
        cas_p = {"error": "single-season mode"}
        pu_p = {"error": "single-season mode"}
        loc_p = {"error": "single-season mode"}
        iso_p = {"error": "single-season mode"}
        dd_p = {k: {"error": "single-season mode"} for k in [
            "very_tight_0_2", "tight_2_4", "open_4_6", "wide_open_6plus"]}

    profiles = []
    try:
        p = pull_shooting_profile_2season(
            args.player, CUR, PRI,
            cas_c, cas_p, pu_c, pu_p, loc_c, loc_p, iso_c, iso_p, dd_c, dd_p,
        )
        p["evaluation_window"] = {
            "mode": window.mode,
            "seasons_used": [{"season": s, "weight": w} for s, w in window.seasons_used],
            "flag_template": window.flag_template,
            "age_concern": window.age_concern,
        }
        profiles.append(p)
    except Exception as e:
        print(f"ERROR pulling {args.player}: {e}")

    if profiles:
        print_comparison(profiles)

    save_path = SCRIPTS_DIR / "shooting_output.json"
    with open(save_path, "w") as f:
        json.dump(profiles, f, indent=2, default=str)
    print(f"\nRaw data saved to {save_path}")
