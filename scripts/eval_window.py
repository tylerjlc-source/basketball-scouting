#!/usr/bin/env python3
"""
eval_window.py -- R12 injury-evaluation-window detection.

Determines which seasons to pull and how to weight them for any player.
Overrides the default 0.60 / 0.40 two-season window when R12 triggers.

See docs/EVAL-WINDOW-AUTOMATION.md for full spec.
Phase 1: classification-only. Not yet wired into domain scripts.

Usage:
    python scripts/eval_window.py 'Player Name'
    python scripts/eval_window.py 'Player Name' --current-season 2021-22
    python scripts/eval_window.py 'Player Name' --season-override 2017-18
    python scripts/eval_window.py --validate
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from typing import Literal, Optional

from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players


# --- Thresholds (locked Session 94; S96 fragment-anchor exception added) ---
# See docs/EVAL-WINDOW-AUTOMATION.md for full spec.
HEALTHY_GP_MIN = 58
FRAGMENT_GP_MIN = 25
FRAGMENT_ANCHOR_FLOOR = 40  # S96: fragment seasons ≥40 GP can anchor R12 when most-recent pre-injury
MPG_BAND = 0.25
MPG_QUALIFYING_GP = 40
ANCHOR_LOOKBACK = 4
ANCHOR_AGE_CONCERN_THRESHOLD = 3
AGGREGATE_GP_MIN = 50

DEFAULT_CURRENT_WEIGHT = 0.60
DEFAULT_PRIOR_WEIGHT = 0.40


Mode = Literal[
    "DEFAULT", "R12_ANCHOR", "R12_AGGREGATE",
    "ROOKIE", "INSUFFICIENT_DATA", "OVERRIDE",
]
Classification = Literal["healthy", "fragment", "compromised"]


@dataclass
class SeasonStat:
    season: str
    gp: int
    mpg: float
    classification: Optional[Classification] = None
    synthesized: bool = False


@dataclass
class EvalWindow:
    mode: Mode
    seasons_used: list[tuple[str, float]]
    detected: list[SeasonStat]
    flag_template: str
    age_concern: bool = False
    override_reason: Optional[str] = None
    extra_info: Optional[str] = None


# --- Season helpers ---
def current_nba_season(today: Optional[date] = None) -> str:
    today = today or date.today()
    start_year = today.year if today.month >= 10 else today.year - 1
    return f"{start_year}-{(start_year + 1) % 100:02d}"


def season_int(season: str) -> int:
    return int(season.split("-")[0])


def season_from_year(year: int) -> str:
    return f"{year}-{(year + 1) % 100:02d}"


# --- Career data fetch ---
def resolve_player_id(player_name: str) -> tuple[int, str]:
    matches = players.find_players_by_full_name(player_name)
    if not matches:
        raise ValueError(f"No player found matching: {player_name!r}")
    return matches[0]["id"], matches[0]["full_name"]


def fetch_career_seasons(player_id: int) -> list[SeasonStat]:
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df = career.get_data_frames()[0]
    by_season: dict[str, dict[str, float]] = defaultdict(
        lambda: {"gp": 0, "min": 0.0}
    )
    for _, row in df.iterrows():
        season = row["SEASON_ID"]
        by_season[season]["gp"] += int(row["GP"])
        by_season[season]["min"] += float(row["MIN"])
    seasons: list[SeasonStat] = []
    for season, agg in by_season.items():
        gp = int(agg["gp"])
        mpg = round(agg["min"] / gp, 1) if gp > 0 else 0.0
        seasons.append(SeasonStat(season=season, gp=gp, mpg=mpg))
    return seasons


def synthesize_missed_seasons(
    played: list[SeasonStat], current_season: str
) -> list[SeasonStat]:
    if not played:
        return played
    played_set = {s.season for s in played}
    start = min(season_int(s.season) for s in played)
    end = season_int(current_season)
    out: list[SeasonStat] = list(played)
    for year in range(start, end + 1):
        s = season_from_year(year)
        if s not in played_set:
            out.append(SeasonStat(season=s, gp=0, mpg=0.0, synthesized=True))
    return out


# --- Classification ---
def classify(seasons: list[SeasonStat]) -> list[SeasonStat]:
    qualifying = [
        s for s in seasons
        if s.gp >= MPG_QUALIFYING_GP and not s.synthesized
    ]
    rotation_mpg: Optional[float]
    if len(qualifying) >= 2:
        rotation_mpg = sum(s.mpg for s in qualifying) / len(qualifying)
    else:
        rotation_mpg = None

    for s in seasons:
        if s.gp < FRAGMENT_GP_MIN:
            s.classification = "compromised"
        elif s.gp < HEALTHY_GP_MIN:
            s.classification = "fragment"
        else:
            if rotation_mpg is None:
                s.classification = "healthy"
            else:
                lo = rotation_mpg * (1 - MPG_BAND)
                hi = rotation_mpg * (1 + MPG_BAND)
                s.classification = "healthy" if lo <= s.mpg <= hi else "fragment"
    return seasons


# --- Decision tree ---
def determine_evaluation_window(
    player_name: str,
    season_override: Optional[str] = None,
    current_season_override: Optional[str] = None,
    today: Optional[date] = None,
) -> EvalWindow:
    if season_override:
        return _build_override(season_override)

    player_id, _ = resolve_player_id(player_name)
    played = fetch_career_seasons(player_id)
    if not played:
        raise ValueError(f"No career data for {player_name}")

    current_season = current_season_override or current_nba_season(today)
    all_seasons = synthesize_missed_seasons(played, current_season)
    all_seasons = [
        s for s in all_seasons if season_int(s.season) <= season_int(current_season)
    ]
    if not all_seasons:
        raise ValueError(f"No seasons <= {current_season} for {player_name}")

    all_seasons.sort(key=lambda s: s.season, reverse=True)
    classify(all_seasons)

    if len(all_seasons) == 1:
        return _build_rookie(all_seasons)

    c, p = all_seasons[0], all_seasons[1]
    c_ko = c.classification in ("fragment", "compromised")
    p_ko = p.classification in ("fragment", "compromised")

    # S120-F01 single-season step-back: When current is compromised but
    # prior is healthy, slide the eval window back one position (prior ->
    # current, before-prior -> prior) at default 0.60/0.40 if before-prior
    # is anchor-eligible. Avoids invoking R12 anchor mode when a clean
    # two-season window is still available. See SCORING-RULES.md R12.
    if (
        c.classification == "compromised"
        and p.classification == "healthy"
        and len(all_seasons) >= 3
    ):
        before_prior = all_seasons[2]
        bp_eligible = (
            before_prior.classification == "healthy"
            or (before_prior.classification == "fragment"
                and before_prior.gp >= FRAGMENT_ANCHOR_FLOOR)
        )
        if bp_eligible:
            return _build_stepback(c, p, before_prior, all_seasons)

    if not (c_ko and p_ko):
        return _build_default(c, p, all_seasons)

    # S96 R12 fragment exception: walk-back includes P (prior season) when
    # fragment-anchor-eligible (≥40 GP). n_back = seasons back from C (P=1).
    walk_back = all_seasons[1 : 1 + ANCHOR_LOOKBACK + 1]
    for n_back, candidate in enumerate(walk_back, start=1):
        is_eligible = (
            candidate.classification == "healthy"
            or (candidate.classification == "fragment"
                and candidate.gp >= FRAGMENT_ANCHOR_FLOOR)
        )
        if is_eligible:
            age_concern = n_back > ANCHOR_AGE_CONCERN_THRESHOLD
            return _build_anchor(candidate, all_seasons, age_concern, n_back)

    if c.gp + p.gp >= AGGREGATE_GP_MIN:
        return _build_aggregate(c, p, all_seasons)

    return _build_insufficient(c, p, all_seasons)


# --- Window builders ---
def _build_override(season: str) -> EvalWindow:
    return EvalWindow(
        mode="OVERRIDE",
        seasons_used=[(season, 1.00)],
        detected=[],
        flag_template=f"Evaluation window manually set to {season} -- reason required in packet.",
        override_reason="manual (--season-override flag)",
    )


def _build_rookie(classified: list[SeasonStat]) -> EvalWindow:
    c = classified[0]
    return EvalWindow(
        mode="ROOKIE",
        seasons_used=[(c.season, 1.00)],
        detected=classified,
        flag_template="(none required -- rookie season)",
    )


def _build_default(
    c: SeasonStat, p: SeasonStat, classified: list[SeasonStat]
) -> EvalWindow:
    return EvalWindow(
        mode="DEFAULT",
        seasons_used=[
            (c.season, DEFAULT_CURRENT_WEIGHT),
            (p.season, DEFAULT_PRIOR_WEIGHT),
        ],
        detected=classified[:2],
        flag_template="(none required)",
        extra_info="No R12 trigger.",
    )


def _build_stepback(
    c: SeasonStat, p: SeasonStat, bp: SeasonStat,
    classified: list[SeasonStat],
) -> EvalWindow:
    """S120-F01 single-season step-back. Current is compromised but
    prior is healthy and before-prior is anchor-eligible. Slide window
    back one position; preserve DEFAULT 0.60/0.40 weighting structure."""
    return EvalWindow(
        mode="DEFAULT",
        seasons_used=[
            (p.season, DEFAULT_CURRENT_WEIGHT),
            (bp.season, DEFAULT_PRIOR_WEIGHT),
        ],
        detected=classified[:3],
        flag_template=(
            f"Evaluation window: {p.season} (current) + {bp.season} (prior) "
            f"-- stepped back one position; {c.season} compromised."
        ),
        extra_info=(
            f"S120-F01 step-back: {c.season} compromised, "
            f"{p.season} healthy ({p.gp} GP), {bp.season} anchor-eligible "
            f"({bp.classification}, {bp.gp} GP)."
        ),
    )


def _build_anchor(
    anchor: SeasonStat,
    classified: list[SeasonStat],
    age_concern: bool,
    n_back: int,
) -> EvalWindow:
    c, p = classified[0], classified[1]
    age_note = "age-concern flag" if age_concern else "no age-concern flag"
    is_fragment_anchor = anchor.classification == "fragment"
    anchor_label = (
        f"Fragment anchor: {anchor.season} ({anchor.gp} GP, S96 fragment exception)"
        if is_fragment_anchor
        else f"Healthy anchor: {anchor.season}"
    )
    return EvalWindow(
        mode="R12_ANCHOR",
        seasons_used=[(anchor.season, 1.00)],
        detected=[
            s for s in classified
            if season_int(s.season) >= season_int(anchor.season)
        ],
        flag_template=(
            f"Evaluation window: {anchor.season} applied as primary per R12 "
            f"-- {c.season} and {p.season} compromised by [injury]."
        ),
        age_concern=age_concern,
        extra_info=f"{anchor_label} ({n_back} season(s) back, {age_note}).",
    )


def _build_aggregate(
    c: SeasonStat, p: SeasonStat, classified: list[SeasonStat]
) -> EvalWindow:
    total = c.gp + p.gp
    w_c = round(c.gp / total, 2)
    w_p = round(p.gp / total, 2)
    return EvalWindow(
        mode="R12_AGGREGATE",
        seasons_used=[(c.season, w_c), (p.season, w_p)],
        detected=classified[:4],
        flag_template=(
            f"Evaluation window: aggregate fragment seasons applied per R12 "
            f"-- {c.season} + {p.season} ({total} combined GP) compromised by [injury]."
        ),
        extra_info=(
            f"Aggregate: {c.season} ({c.gp} GP, {w_c:.2f}) "
            f"+ {p.season} ({p.gp} GP, {w_p:.2f})."
        ),
    )


def _build_insufficient(
    c: SeasonStat, p: SeasonStat, classified: list[SeasonStat]
) -> EvalWindow:
    return EvalWindow(
        mode="INSUFFICIENT_DATA",
        seasons_used=[],
        detected=classified[:4],
        flag_template=(
            "R12 triggered but insufficient data -- qualitative-only evaluation required."
        ),
        extra_info=(
            f"No healthy anchor within {ANCHOR_LOOKBACK} seasons back. "
            f"Aggregate GP insufficient ({c.season} + {p.season} = "
            f"{c.gp + p.gp} GP < {AGGREGATE_GP_MIN})."
        ),
    )


# --- Output formatting ---
def format_detected_entry(s: SeasonStat) -> str:
    cls = s.classification or "?"
    if s.gp == 0:
        return f"{s.season} (0 GP -- {cls})"
    if s.mpg > 0:
        return f"{s.season} ({s.gp} GP, {s.mpg} MPG -- {cls})"
    return f"{s.season} ({s.gp} GP -- {cls})"


def format_window(w: EvalWindow) -> str:
    lines = ["=== EVALUATION WINDOW ==="]
    lines.append(f"Mode: {w.mode}")
    if w.seasons_used:
        seasons_str = ", ".join(f"{s} ({wt:.2f})" for s, wt in w.seasons_used)
    else:
        seasons_str = (
            "(none -- script halted)"
            if w.mode == "INSUFFICIENT_DATA" else "(none)"
        )
    lines.append(f"Seasons used: {seasons_str}")
    if w.detected:
        detected_str = ", ".join(format_detected_entry(s) for s in w.detected)
        lines.append(f"Detected: {detected_str}")
    if w.override_reason:
        lines.append(f"Override reason: {w.override_reason}")
    elif w.extra_info:
        lines.append(w.extra_info)
    lines.append(f'Research packet flag template: "{w.flag_template}"')
    lines.append("===")
    return "\n".join(lines)


# --- Validation harness ---
VALIDATION_CASES = [
    {
        "player": "John Wall",
        "current_season": "2021-22",
        "expected_mode": "R12_ANCHOR",
        "expected_age_concern": False,
        "notes": "Achilles rupture Feb 2019. 2021-22 compromised, 2020-21 40-GP "
                 "fragment at Houston post-Achilles (exactly at FRAGMENT_ANCHOR_FLOOR). "
                 "Per S96 R12 fragment exception, 2020-21 anchors at 1 season back "
                 "with no age concern. Pre-S96 behavior walked back to 2016-17 "
                 "healthy prime Wall (4+ seasons back, age_concern=True). Updated "
                 "Session 96 to reflect S96-F01 behavior change.",
    },
    {
        "player": "Jamal Murray",
        "current_season": "2022-23",
        "expected_mode": "DEFAULT",
        "expected_age_concern": False,
        "notes": "ACL tear April 2021. Missed 2021-22 entirely. Returned healthy in "
                 "2022-23 (65 GP, 32.8 MPG) above 58 GP threshold. R12 exit clause "
                 "fires -- tests that one healthy season breaks R12 trigger. "
                 "Per EW-F01, expected=DEFAULT.",
    },
    {
        "player": "Jamal Murray",
        "current_season": "2023-24",
        "expected_mode": "DEFAULT",
        "expected_age_concern": False,
        "notes": "By 2023-24, current is healthy, prior may be fragment. "
                 "R12 does NOT trigger -- exit clause test.",
    },
    {
        "player": "Ja Morant",
        "current_season": "2025-26",
        "expected_mode": "R12_ANCHOR",
        "expected_age_concern": False,
        "notes": "S96 R12 fragment exception test. 2025-26 compromised (~20 GP "
                 "elbow UCL), 2024-25 50-GP fragment (anchor-eligible per S96), "
                 "2023-24 9-GP compromised (shoulder), 2022-23 61-GP healthy. "
                 "Expected: anchor on 2024-25 fragment (1 season back), not "
                 "walk-back to 2022-23 healthy. Age concern False.",
    },
    {
        "player": "Tyrese Haliburton",
        "current_season": "2025-26",
        "expected_mode": "DEFAULT",
        "expected_age_concern": False,
        "notes": "S120-F01 single-season step-back test. Right Achilles tear "
                 "Game 7 NBA Finals 2025-06-22; missed entire 2025-26 (0 GP, "
                 "compromised). 2024-25 healthy at 73 GP / 33.6 MPG. 2023-24 "
                 "healthy. Without S120-F01 fix, R12 trigger fails (only c "
                 "is compromised) and DEFAULT places 60% weight on 0-GP "
                 "synthesized current season. With fix, eval window steps "
                 "back one position to 2024-25 (0.60) + 2023-24 (0.40), both "
                 "healthy. Expected: DEFAULT mode with step-back flag. Age "
                 "concern False.",
    },
]


def run_validation() -> int:
    passed = failed = 0
    for case in VALIDATION_CASES:
        print(f"\n--- {case['player']} (as-of {case['current_season']}) ---")
        print(f"Notes: {case['notes']}")
        try:
            w = determine_evaluation_window(
                player_name=case["player"],
                current_season_override=case["current_season"],
            )
        except Exception as exc:
            print(f"[ERROR] {exc}")
            failed += 1
            continue
        print(format_window(w))
        mode_ok = w.mode == case["expected_mode"]
        ac_ok = w.age_concern == case["expected_age_concern"]
        if mode_ok and ac_ok:
            print(f"[PASS] mode={w.mode}, age_concern={w.age_concern}")
            passed += 1
        else:
            print(
                f"[FAIL] expected mode={case['expected_mode']}, "
                f"age_concern={case['expected_age_concern']}; "
                f"got mode={w.mode}, age_concern={w.age_concern}"
            )
            failed += 1
    print(f"\n=== VALIDATION RESULT: {passed} passed, {failed} failed ===")
    return 0 if failed == 0 else 1


# --- CLI ---
def main() -> int:
    parser = argparse.ArgumentParser(description="R12 evaluation window detection.")
    parser.add_argument("player", nargs="?", help="Player full name")
    parser.add_argument("--current-season", help="Override current season (e.g. '2021-22')")
    parser.add_argument("--season-override", help="Force a specific season at 100%% weight")
    parser.add_argument("--validate", action="store_true",
                        help="Run validation suite against known R12 cases")
    args = parser.parse_args()

    if args.validate:
        return run_validation()
    if not args.player:
        parser.error("player name required (or use --validate)")

    try:
        w = determine_evaluation_window(
            player_name=args.player,
            season_override=args.season_override,
            current_season_override=args.current_season,
        )
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(format_window(w))
    return 0


if __name__ == "__main__":
    sys.exit(main())
