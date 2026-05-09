"""
Skill 7 — Public Career Stats puller.

Pulls a player's full career per-game stats (Regular Season + Playoffs) from
nba_api.PlayerCareerStats for inclusion in the public profile artifact
(`output/[Player]/[YYYY-MM-DD]_public.md`).

NBA only. College/HS handled by Skill 7 fallback (web search), not this script.

Outputs:
  - stdout: two markdown tables (RS + Playoffs) with bolded career row,
    ready to paste into the `## Career stats` section of `_public.md`.
  - file:   `scripts/public_career_stats_output.json` with structured payload
    matching the `career_stats_row` schema for the export pipeline.

Endpoint frames (per_mode36="PerGame"):
  frames[0] = SeasonTotalsRegularSeason   -> per-season per-game RS rows
  frames[1] = CareerTotalsRegularSeason   -> single career-aggregate RS row
  frames[2] = SeasonTotalsPostSeason      -> per-season per-game PO rows
  frames[3] = CareerTotalsPostSeason      -> single career-aggregate PO row

Trade handling: when a player was traded mid-season, PlayerCareerStats emits
one row per team plus a TOT row. We use the TOT row for the season's numbers
and join non-TOT team abbreviations with "/" for the team display.

Usage:
  python Public_Career_Stats.py "Player Name"
"""

import json
import math
import os
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

from nba_api.stats.static import players as nba_players
from nba_api.stats.endpoints import playercareerstats

from config import SCRIPTS_DIR

DELAY = 1.0


def find_player(player_name: str) -> dict:
    matches = nba_players.find_players_by_full_name(player_name)
    if not matches:
        raise ValueError(f"No player found for '{player_name}'")
    active = [p for p in matches if p["is_active"]]
    chosen = active[0] if active else matches[0]
    return {"id": chosen["id"], "full_name": chosen["full_name"]}


def _num(v):
    """Coerce to float; treat NaN/None as None."""
    if v is None:
        return None
    try:
        f = float(v)
        if math.isnan(f):
            return None
        return f
    except (ValueError, TypeError):
        return None


def _intnum(v):
    n = _num(v)
    return int(n) if n is not None else None


def collapse_season_rows(season_df, season_id):
    """Return one canonical row per season (trade-aware).

    PlayerCareerStats with per_mode36='PerGame' emits one row per (season, team)
    plus a TOT row for traded seasons. Use the TOT row for the per-game numbers
    and join non-TOT team abbreviations with '/' for the team display.
    """
    rows = season_df[season_df["SEASON_ID"] == season_id]
    if rows.empty:
        return None

    tot_rows = rows[rows["TEAM_ABBREVIATION"] == "TOT"]
    team_rows = rows[rows["TEAM_ABBREVIATION"] != "TOT"]

    if not tot_rows.empty:
        canonical = tot_rows.iloc[0].to_dict()
        teams = [t for t in team_rows["TEAM_ABBREVIATION"].tolist() if t]
        canonical["TEAM_DISPLAY"] = "/".join(teams) if teams else "TOT"
    else:
        canonical = rows.iloc[0].to_dict()
        canonical["TEAM_DISPLAY"] = canonical.get("TEAM_ABBREVIATION", "")
    return canonical


def row_to_payload(row, season_id, team_display, is_career=False):
    """Convert a PlayerCareerStats row to the structured JSON payload shape."""
    return {
        "season_id": season_id,
        "team": team_display,
        "gp": _intnum(row.get("GP")),
        "gs": _intnum(row.get("GS")),
        "min": _num(row.get("MIN")),
        "pts": _num(row.get("PTS")),
        "reb": _num(row.get("REB")),
        "ast": _num(row.get("AST")),
        "stl": _num(row.get("STL")),
        "blk": _num(row.get("BLK")),
        "tov": _num(row.get("TOV")),
        "fg_pct": _num(row.get("FG_PCT")),
        "fg3_pct": _num(row.get("FG3_PCT")),
        "ft_pct": _num(row.get("FT_PCT")),
        "is_career": is_career,
    }


def build_season_payload(season_df, career_df):
    """Build [per-season rows..., career row] for one frame pair."""
    rows = []
    seen = []
    for sid in season_df["SEASON_ID"].tolist():
        if sid in seen:
            continue
        seen.append(sid)
        canonical = collapse_season_rows(season_df, sid)
        if canonical is None:
            continue
        rows.append(row_to_payload(canonical, sid, canonical["TEAM_DISPLAY"]))

    if not career_df.empty:
        career = career_df.iloc[0].to_dict()
        rows.append(row_to_payload(career, "Career", "", is_career=True))

    return rows


# ──────────────────────────────────────────────────────────────────────
# Markdown rendering
# ──────────────────────────────────────────────────────────────────────

def fmt_pct(v):
    """0.4682 -> '.468'. None/NaN -> '-'."""
    if v is None:
        return "-"
    return f"{v:.3f}".lstrip("0") if v < 1 else f"{v:.3f}"


def fmt_pg(v):
    """Per-game value to 1 decimal. None -> '-'."""
    if v is None:
        return "-"
    return f"{v:.1f}"


def fmt_int(v):
    if v is None:
        return "-"
    return str(int(v))


COLUMNS = [
    ("Season", lambda r: r["season_id"]),
    ("Team",   lambda r: r["team"] or ""),
    ("GP",     lambda r: fmt_int(r["gp"])),
    ("GS",     lambda r: fmt_int(r["gs"])),
    ("MIN",    lambda r: fmt_pg(r["min"])),
    ("PTS",    lambda r: fmt_pg(r["pts"])),
    ("REB",    lambda r: fmt_pg(r["reb"])),
    ("AST",    lambda r: fmt_pg(r["ast"])),
    ("STL",    lambda r: fmt_pg(r["stl"])),
    ("BLK",    lambda r: fmt_pg(r["blk"])),
    ("TOV",    lambda r: fmt_pg(r["tov"])),
    ("FG%",    lambda r: fmt_pct(r["fg_pct"])),
    ("3P%",    lambda r: fmt_pct(r["fg3_pct"])),
    ("FT%",    lambda r: fmt_pct(r["ft_pct"])),
]


def render_markdown_table(rows):
    """Render rows as a markdown table; bold the row where is_career=True."""
    headers = [c[0] for c in COLUMNS]
    lines = [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join(["---"] * len(headers)) + "|",
    ]
    for r in rows:
        cells = [getter(r) for _, getter in COLUMNS]
        if r.get("is_career"):
            cells = [f"**{c}**" if c else "" for c in cells]
            cells[0] = "**Career**"
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


# ──────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Usage: python Public_Career_Stats.py 'Player Name'")
        sys.exit(1)

    player_name = sys.argv[1]
    player = find_player(player_name)
    pid = player["id"]

    print(f"Player: {player['full_name']} (ID: {pid})", file=sys.stderr)
    print("Pulling PlayerCareerStats (PerGame)...", file=sys.stderr)

    time.sleep(DELAY)
    career = playercareerstats.PlayerCareerStats(
        player_id=pid,
        per_mode36="PerGame",
    )
    frames = career.get_data_frames()
    rs_season_df = frames[0]
    rs_career_df = frames[1]
    po_season_df = frames[2]
    po_career_df = frames[3]

    rs_rows = build_season_payload(rs_season_df, rs_career_df)
    po_rows = build_season_payload(po_season_df, po_career_df) if not po_season_df.empty else []

    payload = {
        "player": player["full_name"],
        "player_id": pid,
        "career_stats": {
            "regular_season": rs_rows,
            "playoffs": po_rows,
        },
    }

    # ── stdout: markdown ready to paste into _public.md ──
    print(f"## Career stats\n")
    print(f"### Regular Season\n")
    print(render_markdown_table(rs_rows))
    if po_rows:
        print(f"\n### Playoffs\n")
        print(render_markdown_table(po_rows))

    # ── file: structured JSON for export pipeline ──
    save_path = SCRIPTS_DIR / "public_career_stats_output.json"
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, default=str)
    print(f"\nStructured payload saved to {save_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
