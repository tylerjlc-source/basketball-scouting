"""
Playoff Track Record -- R13 Stage 1/2 playoff classification support.

Pulls a player's career postseason statistics and compares to regular-season
baseline. Produces the delta summary that feeds:
  - R13 Stage 1 POT modifier (Skill 5 / PROJECTION-OUTPUT-BLOCK.md)
  - R13 Stage 2 composite modifier (Skill 4 / scout-composite.md)

Data source: PlayerCareerStats (nba_api).
  - SeasonTotalsRegularSeason DataFrame -> career regular-season rows
  - SeasonTotalsPostSeason   DataFrame -> career postseason rows

Computed stats:
  - TS% = PTS / (2 * (FGA + 0.44 * FTA))
  - PPG = PTS / GP
  - FGA/g = FGA / GP

Output:
  - Sample minimum check (>=2 playoff seasons required)
  - Recency flag (active if most recent playoff within 2 years of current season,
    else historical-only)
  - Career-aggregate playoff vs. matched-season regular-season deltas
  - Last 3 playoff runs per-season breakdown
  - Classification hint for R13 Stage 1 (statistical signal only;
    qualitative confirmation required for final classification)

Does NOT detect active-injury dormancy -- that is a manual research flag
applied per R13 when a documented injury will rule the player out of the
next playoff cycle.

Usage:
  python Playoff_Track_Record.py 'Player Name'
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

import json
import os
import time
from datetime import date
from nba_api.stats.static import players as nba_players
from nba_api.stats.endpoints import playercareerstats

DELAY = 1.5


# -- Season / year helpers -----------------------------------------------

def current_season_string():
    _year, _month = date.today().year, date.today().month
    if _month >= 10:
        return f"{_year}-{str(_year + 1)[-2:]}"
    else:
        return f"{_year - 1}-{str(_year)[-2:]}"


def season_end_year(season_id):
    """'2023-24' -> 2024"""
    if not season_id or "-" not in str(season_id):
        return None
    start, end = str(season_id).split("-")
    try:
        return int(start[:2] + end)
    except (ValueError, IndexError):
        return None


# -- Player lookup -------------------------------------------------------

def find_player_id(full_name):
    matches = nba_players.find_players_by_full_name(full_name)
    if matches:
        return matches[0]["id"]
    return None


# -- Totals row handling (trade-aware) -----------------------------------

def get_season_totals(df, season_id):
    """Return the canonical totals row for a season.
    Prefers TOT row if the player was traded mid-season."""
    rows = df[df["SEASON_ID"] == season_id]
    if rows.empty:
        return None
    tot = rows[rows["TEAM_ABBREVIATION"] == "TOT"]
    if not tot.empty:
        return tot.iloc[0].to_dict()
    return rows.iloc[0].to_dict()


def aggregate_totals(df, season_ids):
    """Aggregate totals across multiple seasons (trade-aware)."""
    agg = {"GP": 0, "PTS": 0, "FGA": 0, "FTA": 0, "MIN": 0}
    for sid in season_ids:
        row = get_season_totals(df, sid)
        if row:
            for key in agg:
                agg[key] += float(row.get(key, 0) or 0)
    agg["GP"] = int(agg["GP"])
    return agg


# -- Computed stats ------------------------------------------------------

def compute_ts_pct(row):
    pts = float(row.get("PTS", 0) or 0)
    fga = float(row.get("FGA", 0) or 0)
    fta = float(row.get("FTA", 0) or 0)
    denom = 2 * (fga + 0.44 * fta)
    if denom == 0:
        return None
    return round(pts / denom * 100, 1)


def compute_ppg(row):
    gp = int(row.get("GP", 0) or 0)
    pts = float(row.get("PTS", 0) or 0)
    if gp == 0:
        return None
    return round(pts / gp, 1)


def compute_per_game(row, stat):
    gp = int(row.get("GP", 0) or 0)
    val = float(row.get(stat, 0) or 0)
    if gp == 0:
        return None
    return round(val / gp, 1)


# -- Classification ------------------------------------------------------

def classify_delta(delta_ts):
    """R13 Stage 1 statistical signal classification from career matched TS% delta.
    Thresholds are baseline-relative (playoff efficiency drops ~2 TS% from regular
    season for star-level players -- validated S95 against Murray/Harden/Irving)."""
    if delta_ts is None:
        return "insufficient data"
    if delta_ts >= 1:
        return "strong statistical rise"
    if delta_ts > -1:
        return "moderate statistical rise"
    if delta_ts > -3:
        return "neutral (normal playoff efficiency drag)"
    if delta_ts > -5:
        return "moderate statistical shrink"
    return "strong statistical shrink"


# -- Formatting ----------------------------------------------------------

def fmt(val):
    if val is None:
        return "N/A"
    return f"{val}"


def fmt_signed(val):
    if val is None:
        return "N/A"
    return f"{val:+.1f}"


# -- Output --------------------------------------------------------------

def save_output(output):
    save_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "playoff_track_record_output.json",
    )
    with open(save_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nRaw data saved to {save_path}")


# -- Main ----------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: python Playoff_Track_Record.py 'Player Name'")
        sys.exit(1)

    player_name = sys.argv[1]
    player_id = find_player_id(player_name)

    if not player_id:
        print(f"ERROR: Could not find player '{player_name}'")
        sys.exit(1)

    print(f"Player: {player_name} (ID: {player_id})")
    print("Pulling career stats (regular season + postseason)...")

    time.sleep(DELAY)
    career = playercareerstats.PlayerCareerStats(
        player_id=player_id,
        per_mode36="Totals",
    )
    frames = career.get_data_frames()
    # frames[0] = SeasonTotalsRegularSeason
    # frames[1] = CareerTotalsRegularSeason (aggregate -- not used)
    # frames[2] = SeasonTotalsPostSeason
    # frames[3] = CareerTotalsPostSeason (aggregate -- not used)
    regular_df = frames[0]
    postseason_df = frames[2]

    # Unique playoff seasons where GP > 0
    playoff_active = postseason_df[postseason_df["GP"] > 0]
    unique_playoff_seasons = sorted(playoff_active["SEASON_ID"].unique().tolist())
    playoff_season_count = len(unique_playoff_seasons)

    print()
    print("=" * 60)
    print(f"R13 PLAYOFF TRACK RECORD -- {player_name}")
    print("=" * 60)

    # -- Sample minimum check --
    if playoff_season_count < 2:
        print(f"\nSAMPLE MINIMUM: Not met ({playoff_season_count} playoff season(s), <2 required)")
        print("  Below R13 sample minimum. Narrative mention only; no modifier applies.")
        print("=" * 60)

        output = {
            "player": player_name,
            "player_id": player_id,
            "sample_met": False,
            "playoff_season_count": playoff_season_count,
            "playoff_seasons": unique_playoff_seasons,
        }
        save_output(output)
        return

    print(f"\nSAMPLE MINIMUM: Met ({playoff_season_count} playoff seasons)")

    # -- Recency --
    latest_playoff = max(unique_playoff_seasons)
    latest_year = season_end_year(latest_playoff)
    current_end = season_end_year(current_season_string())
    gap_years = (current_end - latest_year) if (current_end and latest_year) else None

    if gap_years is not None and gap_years <= 2:
        recency_state = "active"
        recency_line = f"Active (last playoff: {latest_playoff}, gap: {gap_years} year(s))"
    else:
        recency_state = "historical-only"
        recency_line = f"Historical-only (last playoff: {latest_playoff}, gap: {gap_years} years)"
    print(f"RECENCY STATUS: {recency_line}")
    print("  (active-injury dormancy flag applied in research, not here)")

    # -- Career deltas (matched-season basis) --
    playoff_agg = aggregate_totals(postseason_df, unique_playoff_seasons)
    regular_agg = aggregate_totals(regular_df, unique_playoff_seasons)

    po_ts = compute_ts_pct(playoff_agg)
    rs_ts = compute_ts_pct(regular_agg)
    delta_ts = (po_ts - rs_ts) if (po_ts is not None and rs_ts is not None) else None

    po_ppg = compute_ppg(playoff_agg)
    rs_ppg = compute_ppg(regular_agg)
    delta_ppg = (po_ppg - rs_ppg) if (po_ppg is not None and rs_ppg is not None) else None

    po_fga = compute_per_game(playoff_agg, "FGA")
    rs_fga = compute_per_game(regular_agg, "FGA")

    print(f"\nCAREER PLAYOFF vs REGULAR SEASON (matched-season basis):")
    print(f"  Playoff TS%:   {fmt(po_ts)}%  ({playoff_agg['GP']} games across {playoff_season_count} seasons)")
    print(f"  Regular TS%:   {fmt(rs_ts)}%  ({regular_agg['GP']} games across {playoff_season_count} seasons)")
    print(f"  Delta TS%:     {fmt_signed(delta_ts)}")
    print(f"  Playoff PPG:   {fmt(po_ppg)}  |  Regular PPG:  {fmt(rs_ppg)}  |  Delta: {fmt_signed(delta_ppg)}")
    print(f"  Playoff FGA:   {fmt(po_fga)}/g  |  Regular FGA:  {fmt(rs_fga)}/g")

    # -- Last 3 playoff runs --
    recent_seasons = sorted(unique_playoff_seasons, reverse=True)[:3]

    season_breakdown = []
    print(f"\nLAST 3 PLAYOFF RUNS (most recent first):")
    for season in recent_seasons:
        po = get_season_totals(postseason_df, season) or {}
        rs = get_season_totals(regular_df, season) or {}

        po_ts_s = compute_ts_pct(po)
        rs_ts_s = compute_ts_pct(rs)
        delta_s = (po_ts_s - rs_ts_s) if (po_ts_s is not None and rs_ts_s is not None) else None
        po_ppg_s = compute_ppg(po)

        po_gp = int(po.get("GP", 0) or 0)
        print(f"  {season}  GP: {po_gp}  TS%: {fmt(po_ts_s)}% (vs RS {fmt(rs_ts_s)}%, delta {fmt_signed(delta_s)})  PPG: {fmt(po_ppg_s)}")
        season_breakdown.append({
            "season": season,
            "gp": po_gp,
            "playoff_ts_pct": po_ts_s,
            "regular_ts_pct": rs_ts_s,
            "delta_ts_pct": delta_s,
            "playoff_ppg": po_ppg_s,
        })

    # -- Classification hint --
    hint = classify_delta(delta_ts)
    print(f"\nCLASSIFICATION HINT (R13 Stage 1 -- manual confirmation required):")
    print(f"  Career matched TS% delta: {fmt_signed(delta_ts)}  -->  {hint}")
    print(f"  Recency: {recency_state}")
    print(f"  (Per R13: 'strong' requires statistical AND qualitative, 'moderate' requires either.)")
    print(f"  (Combine with scouting language from research packet for final classification.)")

    print("\n" + "=" * 60)

    output = {
        "player": player_name,
        "player_id": player_id,
        "sample_met": True,
        "playoff_season_count": playoff_season_count,
        "playoff_seasons": unique_playoff_seasons,
        "latest_playoff_season": latest_playoff,
        "recency_state": recency_state,
        "recency_gap_years": gap_years,
        "career_delta": {
            "playoff_ts_pct": po_ts,
            "regular_ts_pct": rs_ts,
            "delta_ts_pct": delta_ts,
            "playoff_ppg": po_ppg,
            "regular_ppg": rs_ppg,
            "delta_ppg": delta_ppg,
            "playoff_fga_per_game": po_fga,
            "regular_fga_per_game": rs_fga,
            "playoff_games": playoff_agg["GP"],
            "regular_games_matched": regular_agg["GP"],
        },
        "last_3_runs": season_breakdown,
        "classification_hint": hint,
    }
    save_output(output)


if __name__ == "__main__":
    main()
