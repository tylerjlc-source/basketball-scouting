"""
defense_validation.py — v1
Domain 5: Defense (#15 On-Ball Pressure, #16 Help Defense, #17 Rim Protection, #18 Post Defense)
Guard Validation Set: Kyrie Irving, De'Aaron Fox, Marcus Smart, Buddy Hield

2-season 60/40 recency weighting (current/prior).
Both seasons queried independently with explicit season parameters.
Volume-weighted for percentages; simple weighted average for rate stats.

Run in Claude Code or local Python — stats.nba.com blocked in Claude.ai container.
"""

import time
import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')  # EW-F04: prevent Windows cp1252 crash on non-ASCII player names
from datetime import date
from nba_api.stats.static import players
from nba_api.stats.endpoints import (
    leaguedashptdefend,
    leaguehustlestatsplayer,
    leaguedashplayerstats,
    synergyplaytypes,
)

# ── Evaluation window — set by main() via eval_window.determine_evaluation_window ──
from eval_window import determine_evaluation_window, format_window

CURRENT_SEASON = None
PRIOR_SEASON = None  # None triggers single-season path (R12_ANCHOR, OVERRIDE, ROOKIE)
W_CURRENT = 0.60
W_PRIOR = 0.40
DELAY = 1.0  # seconds between API calls

TEST_GUARDS = {}  # populated by main() from argparse

# ── Helper Functions ────────────────────────────────────────────────────────

def find_player_id(full_name):
    """Look up NBA player ID by full name."""
    all_players = players.find_players_by_full_name(full_name)
    if all_players:
        return all_players[0]["id"]
    return None


def safe_div(num, den, default=0.0):
    """Safe division with default."""
    if den and den > 0:
        return num / den
    return default


# NOTE (Session 94): w_c/w_p defaults pin to W_CURRENT/W_PRIOR at module-load time,
# not call time. Safe in DEFAULT mode (defaults match globals) and R12_ANCHOR
# (prior=None short-circuit skips the weighted math). UNSAFE in R12_AGGREGATE --
# would use 0.60/0.40 instead of proportional weights. When R12_AGGREGATE first
# surfaces on Domain_5, change signatures to w_c=None/w_p=None and resolve inside
# the function body.
def weighted_avg(current_val, prior_val, w_c=W_CURRENT, w_p=W_PRIOR):
    """Simple weighted average for rate stats."""
    if current_val is None and prior_val is None:
        return None
    if current_val is None:
        return prior_val
    if prior_val is None:
        return current_val
    return current_val * w_c + prior_val * w_p


def volume_weighted_pct(c_made, c_att, p_made, p_att, w_c=W_CURRENT, w_p=W_PRIOR):
    """Volume-weighted percentage across two seasons."""
    c_att_w = (c_att or 0) * w_c
    p_att_w = (p_att or 0) * w_p
    c_made_w = (c_made or 0) * w_c
    p_made_w = (p_made or 0) * w_p
    total_att = c_att_w + p_att_w
    total_made = c_made_w + p_made_w
    if total_att > 0:
        return total_made / total_att
    return None


# ── Data Pull Functions ─────────────────────────────────────────────────────

def pull_pt_defend(season, defense_category="Overall"):
    """
    Pull LeagueDashPtDefend — opponent FG% as closest defender.
    Categories: Overall, 3 Pointers, 2 Pointers, Less Than 6Ft, Less Than 10Ft, Greater Than 15Ft
    Returns dict keyed by player_id.
    """
    time.sleep(DELAY)
    try:
        data = leaguedashptdefend.LeagueDashPtDefend(
            season=season,
            season_type_all_star="Regular Season",
            defense_category=defense_category,
            per_mode_simple="PerGame",
        )
        df = data.get_data_frames()[0]
        result = {}
        for _, row in df.iterrows():
            pid = row.get("CLOSE_DEF_PERSON_ID")
            result[pid] = {
                "player_name": row.get("PLAYER_NAME"),
                "gp": row.get("GP"),
                "g": row.get("G"),
                "freq": row.get("FREQ"),
                "d_fgm": row.get("D_FGM"),
                "d_fga": row.get("D_FGA"),
                "d_fg_pct": row.get("D_FG_PCT"),
                "normal_fg_pct": row.get("NORMAL_FG_PCT"),
                "pct_plusminus": row.get("PCT_PLUSMINUS"),
            }
        return result
    except Exception as e:
        print(f"  ERROR pulling LeagueDashPtDefend ({defense_category}, {season}): {e}")
        return {}


def pull_hustle_stats(season):
    """
    Pull LeagueHustleStatsPlayer — contested shots, deflections, charges drawn,
    loose balls, box-outs.
    Returns dict keyed by player_id.
    """
    time.sleep(DELAY)
    try:
        data = leaguehustlestatsplayer.LeagueHustleStatsPlayer(
            season=season,
            season_type_all_star="Regular Season",
            per_mode_time="PerGame",
        )
        df = data.get_data_frames()[0]
        result = {}
        for _, row in df.iterrows():
            pid = row.get("PLAYER_ID")
            result[pid] = {
                "player_name": row.get("PLAYER_NAME"),
                "g": row.get("G"),
                "min": row.get("MIN"),
                "contested_shots": row.get("CONTESTED_SHOTS"),
                "contested_shots_2pt": row.get("CONTESTED_SHOTS_2PT"),
                "contested_shots_3pt": row.get("CONTESTED_SHOTS_3PT"),
                "deflections": row.get("DEFLECTIONS"),
                "charges_drawn": row.get("CHARGES_DRAWN"),
                "off_loose_balls": row.get("OFF_LOOSE_BALLS_RECOVERED"),
                "def_loose_balls": row.get("DEF_LOOSE_BALLS_RECOVERED"),
                "loose_balls": row.get("LOOSE_BALLS_RECOVERED"),
                "off_boxouts": row.get("OFF_BOXOUTS"),
                "def_boxouts": row.get("DEF_BOXOUTS"),
                "boxouts": row.get("BOX_OUTS"),
            }
        return result
    except Exception as e:
        print(f"  ERROR pulling LeagueHustleStatsPlayer ({season}): {e}")
        return {}


def pull_base_stats(season, measure_type="Base"):
    """
    Pull LeagueDashPlayerStats — STL, BLK, PF, DREB, etc.
    MeasureType: Base or Advanced.
    Returns dict keyed by player_id.
    """
    time.sleep(DELAY)
    try:
        data = leaguedashplayerstats.LeagueDashPlayerStats(
            season=season,
            season_type_all_star="Regular Season",
            measure_type_detailed_defense=measure_type,
            per_mode_detailed="PerGame",
        )
        df = data.get_data_frames()[0]
        result = {}
        for _, row in df.iterrows():
            pid = row.get("PLAYER_ID")
            entry = {"player_name": row.get("PLAYER_NAME"), "gp": row.get("GP"), "min": row.get("MIN")}
            if measure_type == "Base":
                entry.update({
                    "stl": row.get("STL"),
                    "blk": row.get("BLK"),
                    "blka": row.get("BLKA"),
                    "pf": row.get("PF"),
                    "dreb": row.get("DREB"),
                    "oreb": row.get("OREB"),
                })
            elif measure_type == "Advanced":
                entry.update({
                    "def_rating": row.get("DEF_RATING"),
                    "net_rating": row.get("NET_RATING"),
                    "def_reb_pct": row.get("DREB_PCT"),
                    "oreb_pct": row.get("OREB_PCT"),
                })
            result[pid] = entry
        return result
    except Exception as e:
        print(f"  ERROR pulling LeagueDashPlayerStats ({measure_type}, {season}): {e}")
        return {}


def pull_synergy_postup_defense(season):
    """
    Pull SynergyPlayTypes for PostUp defense — opponent PPP when this player defends post-ups.
    Returns dict keyed by player_id.
    """
    time.sleep(DELAY)
    try:
        data = synergyplaytypes.SynergyPlayTypes(
            season=season,
            season_type_all_star="Regular Season",
            play_type_nullable="Postup",
            type_grouping_nullable="defensive",
            per_mode_simple="PerGame",
            player_or_team_abbreviation="P",
        )
        df = data.get_data_frames()[0]
        result = {}
        for _, row in df.iterrows():
            pid = row.get("PLAYER_ID")
            result[pid] = {
                "player_name": row.get("PLAYER_NAME"),
                "gp": row.get("GP"),
                "poss": row.get("POSS"),
                "ppp": row.get("PPP"),
                "fg_pct": row.get("FG_PCT"),
                "poss_pct": row.get("POSS_PCT"),
                "percentile": row.get("PERCENTILE"),
                "score": row.get("PTS"),
            }
        return result
    except Exception as e:
        print(f"  ERROR pulling SynergyPlayTypes PostUp defense ({season}): {e}")
        return {}


def pull_synergy_iso_defense(season):
    """
    Pull SynergyPlayTypes for Isolation defense — opponent PPP in ISO situations.
    Returns dict keyed by player_id.
    """
    time.sleep(DELAY + 1.0)  # Extra delay — Synergy defensive endpoints are slow
    try:
        data = synergyplaytypes.SynergyPlayTypes(
            season=season,
            season_type_all_star="Regular Season",
            play_type_nullable="Isolation",
            type_grouping_nullable="defensive",
            per_mode_simple="PerGame",
            player_or_team_abbreviation="P",
        )
        df = data.get_data_frames()[0]
        result = {}
        for _, row in df.iterrows():
            pid = row.get("PLAYER_ID")
            result[pid] = {
                "player_name": row.get("PLAYER_NAME"),
                "gp": row.get("GP"),
                "poss": row.get("POSS"),
                "ppp": row.get("PPP"),
                "fg_pct": row.get("FG_PCT"),
                "percentile": row.get("PERCENTILE"),
            }
        return result
    except Exception as e:
        print(f"  ERROR pulling SynergyPlayTypes ISO defense ({season}): {e}")
        return {}


# ── Main Execution ──────────────────────────────────────────────────────────

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

    global CURRENT_SEASON, PRIOR_SEASON, W_CURRENT, W_PRIOR
    if len(window.seasons_used) == 1:
        CURRENT_SEASON = window.seasons_used[0][0]
        W_CURRENT = window.seasons_used[0][1]
        PRIOR_SEASON = None
        W_PRIOR = 0.0
    else:
        CURRENT_SEASON, W_CURRENT = window.seasons_used[0]
        PRIOR_SEASON, W_PRIOR = window.seasons_used[1]

    TEST_GUARDS[args.player] = None

    # Resolve player IDs
    print("=== DEFENSE VALIDATION — Domain 5 ===")
    if PRIOR_SEASON:
        print(f"Seasons: {CURRENT_SEASON} (w={W_CURRENT}) + {PRIOR_SEASON} (w={W_PRIOR})\n")
    else:
        print(f"Season: {CURRENT_SEASON} (single-season, w={W_CURRENT})\n")

    for name in TEST_GUARDS:
        pid = find_player_id(name)
        TEST_GUARDS[name] = pid
        print(f"  {name}: ID {pid}")

    target_ids = set(TEST_GUARDS.values())
    print()

    # ── Pull all data for current (and prior unless single-season) ──

    print("--- Pulling LeagueDashPtDefend (Overall) ---")
    ptdef_overall_curr = pull_pt_defend(CURRENT_SEASON, "Overall")
    ptdef_overall_prior = pull_pt_defend(PRIOR_SEASON, "Overall") if PRIOR_SEASON else {}

    print("--- Pulling LeagueDashPtDefend (3 Pointers) ---")
    ptdef_3pt_curr = pull_pt_defend(CURRENT_SEASON, "3 Pointers")
    ptdef_3pt_prior = pull_pt_defend(PRIOR_SEASON, "3 Pointers") if PRIOR_SEASON else {}

    print("--- Pulling LeagueDashPtDefend (Less Than 6Ft) ---")
    ptdef_rim_curr = pull_pt_defend(CURRENT_SEASON, "Less Than 6Ft")
    ptdef_rim_prior = pull_pt_defend(PRIOR_SEASON, "Less Than 6Ft") if PRIOR_SEASON else {}

    print("--- Pulling LeagueDashPtDefend (Greater Than 15Ft) ---")
    ptdef_perim_curr = pull_pt_defend(CURRENT_SEASON, "Greater Than 15Ft")
    ptdef_perim_prior = pull_pt_defend(PRIOR_SEASON, "Greater Than 15Ft") if PRIOR_SEASON else {}

    print("--- Pulling Hustle Stats ---")
    hustle_curr = pull_hustle_stats(CURRENT_SEASON)
    hustle_prior = pull_hustle_stats(PRIOR_SEASON) if PRIOR_SEASON else {}

    print("--- Pulling Base Stats ---")
    base_curr = pull_base_stats(CURRENT_SEASON, "Base")
    base_prior = pull_base_stats(PRIOR_SEASON, "Base") if PRIOR_SEASON else {}

    print("--- Pulling Advanced Stats ---")
    adv_curr = pull_base_stats(CURRENT_SEASON, "Advanced")
    adv_prior = pull_base_stats(PRIOR_SEASON, "Advanced") if PRIOR_SEASON else {}

    print("--- Pulling Synergy PostUp Defense ---")
    syn_post_curr = pull_synergy_postup_defense(CURRENT_SEASON)
    syn_post_prior = pull_synergy_postup_defense(PRIOR_SEASON) if PRIOR_SEASON else {}

    print("--- Pulling Synergy Isolation Defense ---")
    syn_iso_curr = pull_synergy_iso_defense(CURRENT_SEASON)
    syn_iso_prior = pull_synergy_iso_defense(PRIOR_SEASON) if PRIOR_SEASON else {}

    print("\n=== DATA PULL COMPLETE ===\n")

    # ── Process each player ─────────────────────────────────────────────────

    all_profiles = []

    for name, pid in TEST_GUARDS.items():
        print(f"\n{'='*70}")
        print(f"  {name} (ID: {pid})")
        print(f"{'='*70}")

        # Gather raw data references for this player
        c_ov = ptdef_overall_curr.get(pid, {})
        p_ov = ptdef_overall_prior.get(pid, {})
        c_3p = ptdef_3pt_curr.get(pid, {})
        p_3p = ptdef_3pt_prior.get(pid, {})
        c_per = ptdef_perim_curr.get(pid, {})
        p_per = ptdef_perim_prior.get(pid, {})
        c_rim = ptdef_rim_curr.get(pid, {})
        p_rim = ptdef_rim_prior.get(pid, {})
        c_hus = hustle_curr.get(pid, {})
        p_hus = hustle_prior.get(pid, {})
        c_base = base_curr.get(pid, {})
        p_base = base_prior.get(pid, {})
        c_adv = adv_curr.get(pid, {})
        p_adv = adv_prior.get(pid, {})
        c_iso = syn_iso_curr.get(pid, {})
        p_iso = syn_iso_prior.get(pid, {})
        c_post = syn_post_curr.get(pid, {})
        p_post = syn_post_prior.get(pid, {})

        # ── Compute weighted stats ──

        # #15 ON-BALL PRESSURE
        d_fg_pct_w = volume_weighted_pct(c_ov.get("d_fgm"), c_ov.get("d_fga"), p_ov.get("d_fgm"), p_ov.get("d_fga"))
        d_fga_w = weighted_avg(c_ov.get("d_fga"), p_ov.get("d_fga"))
        pct_pm_w = weighted_avg(c_ov.get("pct_plusminus"), p_ov.get("pct_plusminus"))

        d_3pt_pct_w = volume_weighted_pct(c_3p.get("d_fgm"), c_3p.get("d_fga"), p_3p.get("d_fgm"), p_3p.get("d_fga"))
        d_3pt_fga_w = weighted_avg(c_3p.get("d_fga"), p_3p.get("d_fga"))
        pct_pm_3pt_w = weighted_avg(c_3p.get("pct_plusminus"), p_3p.get("pct_plusminus"))

        d_perim_pct_w = volume_weighted_pct(c_per.get("d_fgm"), c_per.get("d_fga"), p_per.get("d_fgm"), p_per.get("d_fga"))
        d_perim_fga_w = weighted_avg(c_per.get("d_fga"), p_per.get("d_fga"))
        pct_pm_perim_w = weighted_avg(c_per.get("pct_plusminus"), p_per.get("pct_plusminus"))

        defl_w = weighted_avg(c_hus.get("deflections"), p_hus.get("deflections"))
        cont_w = weighted_avg(c_hus.get("contested_shots"), p_hus.get("contested_shots"))
        cont_3pt_w = weighted_avg(c_hus.get("contested_shots_3pt"), p_hus.get("contested_shots_3pt"))
        cont_2pt_w = weighted_avg(c_hus.get("contested_shots_2pt"), p_hus.get("contested_shots_2pt"))
        stl_w = weighted_avg(c_base.get("stl"), p_base.get("stl"))
        pf_w = weighted_avg(c_base.get("pf"), p_base.get("pf"))

        iso_ppp_w = weighted_avg(c_iso.get("ppp"), p_iso.get("ppp"))
        iso_poss_total = (c_iso.get("poss") or 0) + (p_iso.get("poss") or 0)

        # #16 HELP DEFENSE
        def_rtg_w = weighted_avg(c_adv.get("def_rating"), p_adv.get("def_rating"))
        chg_w = weighted_avg(c_hus.get("charges_drawn"), p_hus.get("charges_drawn"))
        dlb_w = weighted_avg(c_hus.get("def_loose_balls"), p_hus.get("def_loose_balls"))
        dbo_w = weighted_avg(c_hus.get("def_boxouts"), p_hus.get("def_boxouts"))
        blk_w = weighted_avg(c_base.get("blk"), p_base.get("blk"))

        # #17 RIM PROTECTION
        rim_fg_pct_w = volume_weighted_pct(c_rim.get("d_fgm"), c_rim.get("d_fga"), p_rim.get("d_fgm"), p_rim.get("d_fga"))
        rim_fga_w = weighted_avg(c_rim.get("d_fga"), p_rim.get("d_fga"))
        rim_pm_w = weighted_avg(c_rim.get("pct_plusminus"), p_rim.get("pct_plusminus"))

        # #18 POST DEFENSE
        post_ppp_w = weighted_avg(c_post.get("ppp"), p_post.get("ppp"))
        post_poss_total = (c_post.get("poss") or 0) + (p_post.get("poss") or 0)

        # DREB for context
        dreb_w = weighted_avg(c_base.get("dreb"), p_base.get("dreb"))

        # ── Print ──

        print(f"\n  --- #15 ON-BALL PRESSURE ---")
        print(f"    Opp FG% (Overall): {d_fg_pct_w:.1%}" if d_fg_pct_w else "    Opp FG% (Overall): N/A")
        print(f"    D_FGA/game (Overall): {d_fga_w:.1f}" if d_fga_w else "    D_FGA/game (Overall): N/A")
        print(f"    DFGPOE (Overall): {pct_pm_w:+.1%}" if pct_pm_w else "    DFGPOE (Overall): N/A")
        print(f"    [Current: {c_ov.get('d_fga', 'N/A')} D_FGA, {c_ov.get('d_fg_pct', 'N/A')} D_FG%, DFGPOE {c_ov.get('pct_plusminus', 'N/A')}]")
        print(f"    [Prior:   {p_ov.get('d_fga', 'N/A')} D_FGA, {p_ov.get('d_fg_pct', 'N/A')} D_FG%, DFGPOE {p_ov.get('pct_plusminus', 'N/A')}]")

        print(f"    Opp 3PT FG%: {d_3pt_pct_w:.1%}" if d_3pt_pct_w else "    Opp 3PT FG%: N/A")
        print(f"    D_FGA/game (3PT): {d_3pt_fga_w:.1f}" if d_3pt_fga_w else "    D_FGA/game (3PT): N/A")
        print(f"    DFGPOE (3PT): {pct_pm_3pt_w:+.1%}" if pct_pm_3pt_w else "    DFGPOE (3PT): N/A")

        print(f"    Opp FG% (>15ft): {d_perim_pct_w:.1%}" if d_perim_pct_w else "    Opp FG% (>15ft): N/A")
        print(f"    D_FGA/game (>15ft): {d_perim_fga_w:.1f}" if d_perim_fga_w else "    D_FGA/game (>15ft): N/A")
        print(f"    DFGPOE (>15ft): {pct_pm_perim_w:+.1%}" if pct_pm_perim_w else "    DFGPOE (>15ft): N/A")

        print(f"    Deflections/game: {defl_w:.1f}" if defl_w else "    Deflections/game: N/A")
        print(f"    STL/game: {stl_w:.1f}" if stl_w else "    STL/game: N/A")
        print(f"    Contested shots/game: {cont_w:.1f}" if cont_w else "    Contested shots/game: N/A")
        print(f"    Contested 3PT/game: {cont_3pt_w:.1f}" if cont_3pt_w else "    Contested 3PT/game: N/A")
        print(f"    Contested 2PT/game: {cont_2pt_w:.1f}" if cont_2pt_w else "    Contested 2PT/game: N/A")
        print(f"    PF/game: {pf_w:.1f}" if pf_w else "    PF/game: N/A")
        print(f"    [Current hustle: {c_hus.get('deflections', 'N/A')} defl, {c_base.get('stl', 'N/A')} stl, {c_hus.get('contested_shots', 'N/A')} cont]")
        print(f"    [Prior hustle:   {p_hus.get('deflections', 'N/A')} defl, {p_base.get('stl', 'N/A')} stl, {p_hus.get('contested_shots', 'N/A')} cont]")

        print(f"    ISO Defense PPP: {iso_ppp_w:.3f}" if iso_ppp_w else "    ISO Defense PPP: N/A")
        print(f"    ISO Defense poss (2-season total): {iso_poss_total}")
        print(f"    [Current ISO: {c_iso.get('poss', 'N/A')} poss, {c_iso.get('ppp', 'N/A')} PPP, {c_iso.get('percentile', 'N/A')} pctile]")
        print(f"    [Prior ISO:   {p_iso.get('poss', 'N/A')} poss, {p_iso.get('ppp', 'N/A')} PPP, {p_iso.get('percentile', 'N/A')} pctile]")

        print(f"\n  --- #16 HELP DEFENSE ---")
        print(f"    DEF_RATING: {def_rtg_w:.1f}" if def_rtg_w else "    DEF_RATING: N/A")
        print(f"    [Current: {c_adv.get('def_rating', 'N/A')} | Prior: {p_adv.get('def_rating', 'N/A')}]")
        print(f"    Charges drawn/game: {chg_w:.2f}" if chg_w is not None else "    Charges drawn/game: N/A")
        print(f"    Def loose balls/game: {dlb_w:.2f}" if dlb_w is not None else "    Def loose balls/game: N/A")
        print(f"    Def box-outs/game: {dbo_w:.2f}" if dbo_w is not None else "    Def box-outs/game: N/A")
        print(f"    BLK/game: {blk_w:.1f}" if blk_w else "    BLK/game: N/A")
        print(f"    Deflections/game (cross-ref #15): {defl_w:.1f}" if defl_w else "    Deflections/game: N/A")

        print(f"\n  --- #17 RIM PROTECTION ---")
        print(f"    Opp FG% at rim (<6ft): {rim_fg_pct_w:.1%}" if rim_fg_pct_w else "    Opp FG% at rim: N/A")
        print(f"    D_FGA/game at rim: {rim_fga_w:.1f}" if rim_fga_w else "    D_FGA/game at rim: N/A")
        print(f"    DFGPOE at rim: {rim_pm_w:+.1%}" if rim_pm_w else "    DFGPOE at rim: N/A")
        print(f"    [Current: {c_rim.get('d_fga', 'N/A')} D_FGA, {c_rim.get('d_fg_pct', 'N/A')} D_FG%]")
        print(f"    [Prior:   {p_rim.get('d_fga', 'N/A')} D_FGA, {p_rim.get('d_fg_pct', 'N/A')} D_FG%]")
        print(f"    BLK/game (cross-ref #16): {blk_w:.1f}" if blk_w else "    BLK/game: N/A")
        print(f"    Contested 2PT/game (cross-ref #15): {cont_2pt_w:.1f}" if cont_2pt_w else "    Contested 2PT/game: N/A")

        print(f"\n  --- #18 POST DEFENSE ---")
        print(f"    PostUp Defense PPP: {post_ppp_w:.3f}" if post_ppp_w else "    PostUp Defense PPP: N/A")
        print(f"    PostUp poss (2-season total): {post_poss_total}")
        print(f"    [Current: {c_post.get('poss', 'N/A')} poss, {c_post.get('ppp', 'N/A')} PPP, {c_post.get('percentile', 'N/A')} pctile]")
        print(f"    [Prior:   {p_post.get('poss', 'N/A')} poss, {p_post.get('ppp', 'N/A')} PPP, {p_post.get('percentile', 'N/A')} pctile]")
        print(f"    Def box-outs/game (cross-ref #16): {dbo_w:.2f}" if dbo_w is not None else "    Def box-outs/game: N/A")
        print(f"    PF/game (cross-ref #15): {pf_w:.1f}" if pf_w else "    PF/game: N/A")

        # ── Build JSON profile ──

        def _sb(cur, pri, is_rate=False):
            if pri is None:
                return {"current": cur, "prior": "N/A", "weighted": cur}
            w = weighted_avg(cur, pri) if is_rate else weighted_avg(cur, pri)
            return {"current": cur, "prior": pri, "weighted": round(w, 3) if w is not None else "N/A"}

        def _vw(c_m, c_a, p_m, p_a):
            w = volume_weighted_pct(c_m, c_a, p_m, p_a)
            return {
                "current_fg_pct": round(c_m / c_a, 3) if c_a and c_a > 0 else "N/A",
                "prior_fg_pct": round(p_m / p_a, 3) if p_a and p_a > 0 else "N/A",
                "weighted_fg_pct": round(w, 3) if w is not None else "N/A",
                "current_fga": c_a, "prior_fga": p_a,
            }

        profile = {
            "player": name,
            "evaluation_window": {
                "mode": window.mode,
                "seasons_used": [{"season": s, "weight": w} for s, w in window.seasons_used],
                "flag_template": window.flag_template,
                "age_concern": window.age_concern,
            },
            "subdomain_15_on_ball_pressure": {
                "opp_fg_pct_overall": _vw(c_ov.get("d_fgm"), c_ov.get("d_fga"), p_ov.get("d_fgm"), p_ov.get("d_fga")),
                "dfgpoe_overall": _sb(c_ov.get("pct_plusminus"), p_ov.get("pct_plusminus"), is_rate=True),
                "opp_fg_pct_3pt": _vw(c_3p.get("d_fgm"), c_3p.get("d_fga"), p_3p.get("d_fgm"), p_3p.get("d_fga")),
                "dfgpoe_3pt": _sb(c_3p.get("pct_plusminus"), p_3p.get("pct_plusminus"), is_rate=True),
                "opp_fg_pct_perimeter": _vw(c_per.get("d_fgm"), c_per.get("d_fga"), p_per.get("d_fgm"), p_per.get("d_fga")),
                "dfgpoe_perimeter": _sb(c_per.get("pct_plusminus"), p_per.get("pct_plusminus"), is_rate=True),
                "deflections_pg": _sb(c_hus.get("deflections"), p_hus.get("deflections"), is_rate=True),
                "stl_pg": _sb(c_base.get("stl"), p_base.get("stl"), is_rate=True),
                "contested_shots_pg": _sb(c_hus.get("contested_shots"), p_hus.get("contested_shots"), is_rate=True),
                "contested_3pt_pg": _sb(c_hus.get("contested_shots_3pt"), p_hus.get("contested_shots_3pt"), is_rate=True),
                "contested_2pt_pg": _sb(c_hus.get("contested_shots_2pt"), p_hus.get("contested_shots_2pt"), is_rate=True),
                "pf_pg": _sb(c_base.get("pf"), p_base.get("pf"), is_rate=True),
                "iso_defense": {
                    "ppp": _sb(c_iso.get("ppp"), p_iso.get("ppp"), is_rate=True),
                    "poss_total": iso_poss_total,
                    "current_poss": c_iso.get("poss"),
                    "prior_poss": p_iso.get("poss"),
                    "current_percentile": c_iso.get("percentile"),
                    "prior_percentile": p_iso.get("percentile"),
                },
            },
            "subdomain_16_help_defense": {
                "def_rating": _sb(c_adv.get("def_rating"), p_adv.get("def_rating"), is_rate=True),
                "charges_drawn_pg": _sb(c_hus.get("charges_drawn"), p_hus.get("charges_drawn"), is_rate=True),
                "def_loose_balls_pg": _sb(c_hus.get("def_loose_balls"), p_hus.get("def_loose_balls"), is_rate=True),
                "def_boxouts_pg": _sb(c_hus.get("def_boxouts"), p_hus.get("def_boxouts"), is_rate=True),
                "blk_pg": _sb(c_base.get("blk"), p_base.get("blk"), is_rate=True),
            },
            "subdomain_17_rim_protection": {
                "opp_fg_pct_rim": _vw(c_rim.get("d_fgm"), c_rim.get("d_fga"), p_rim.get("d_fgm"), p_rim.get("d_fga")),
                "dfgpoe_rim": _sb(c_rim.get("pct_plusminus"), p_rim.get("pct_plusminus"), is_rate=True),
            },
            "subdomain_18_post_defense": {
                "postup_defense": {
                    "ppp": _sb(c_post.get("ppp"), p_post.get("ppp"), is_rate=True),
                    "poss_total": post_poss_total,
                    "current_poss": c_post.get("poss"),
                    "prior_poss": p_post.get("poss"),
                    "current_percentile": c_post.get("percentile"),
                    "prior_percentile": p_post.get("percentile"),
                },
                "dreb_pg": _sb(c_base.get("dreb"), p_base.get("dreb"), is_rate=True),
            },
        }
        all_profiles.append(profile)

    # ── Save JSON ──
    save_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "defense_output.json",
    )
    with open(save_path, "w") as f:
        json.dump(all_profiles, f, indent=2, default=str)
    print(f"\nRaw data saved to {save_path}")

    print(f"\n\n{'='*70}")
    print("=== DEFENSE VALIDATION COMPLETE ===")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
