# scout-research — Learnings

Active calibration learnings for the scout-research skill. Loaded
just-in-time at skill invocation (P1). Governed by
SELF-LEARNING-PROTOCOL.md.

**Scope:** Category 3 findings scoped to this skill's execution.
Category 1 findings live in session logs. Category 2 findings live
in rule documents (see routing table in SELF-LEARNING-PROTOCOL.md).

---

## ACTIVE LEARNINGS

---

### S120-F01 — eval_window.py R12 trigger does not fire when only current season is compromised
**Status:** Superseded (promoted to SCORING-RULES.md R12 "Single-season step-back" subsection + eval_window.py `determine_evaluation_window()` patch, Session 120 2026-04-30)

Original entry archived at `docs/learnings/archive/S120-F01-archived.md`. 1 application (Tyrese Haliburton S120). Promoted on first application per Tyler triage — finding had a clear single-clause rule expansion + bounded script patch path; both layers shipped together rather than waiting for the 3-application threshold.

**On-eval behavior:** eval_window.py now auto-handles the case via the new step-back branch (`_build_stepback()` builder + new triggering branch in `determine_evaluation_window()`). Manual `--current-season` override no longer required for current-season-compromised + prior-season-healthy NBA-vet evaluations.

---

### S105-F01 — Web articles citing season-rate efficiency can reflect hot-stretch samples, not full-season aggregate
**Date:** 2026-04-24
**Severity:** Medium
**Context:** Sengun S105 research surfaced 3PT% claims of 37.5%, 41.9%, and 45.9% across multiple credible outlets (SI, SSBCrack, Yahoo, The Dream Shake) framing Sengun as the Rockets' new stretch big after offseason work with Cam Hodges + Serbian shooting coach Djordje Sijan. Script + StatMuse confirmed actual season aggregate is 28.2% weighted / 28.9% full-season 2025-26. The discrepancy traced to the opening-night 5-of-8 vs OKC (39 pts, season-high) and similar early hot stretches that were cited as if they were season-level numbers in articles published mid-season but aggregating against a small early-season window.
**Learning:** When qualitative web search returns a season-rate efficiency figure (3PT%, FG%, TS%, mid-range %) that differs materially from the domain script aggregate, prefer the script number and verify on StatMuse as tiebreaker. Hot-stretch citations are common for narrative-positive players in mid-season scouting articles. Tells: phrasing like "this season" or "improved to X%" without specifying sample size or game count; multi-outlet convergence on the same inflated figure (suggests cross-citation from a single early article); figures published before the All-Star break that don't match later season aggregates.
**Why:** Multi-source convergence on a wrong number is a real failure mode for the Negative Balance Rule applied to research. R1 says the worst observation anchors the score; the corollary at research-time is that the most accurate observation must beat the most repeated observation. Script aggregate over the full evaluation window is the most accurate signal for rate stats.
**How to apply:** During Skill 1 qualitative research, when web articles cite a season-rate efficiency stat: (1) check the article's date and infer the sample window; (2) compare against the script's weighted aggregate for the evaluation window; (3) if material gap (>3 percentage points), defer to the script and document the reconciliation in the research packet's Data Gap Inventory under "Conflicting signals"; (4) StatMuse cross-check is the cleanest tiebreaker when script and articles disagree.
**Applies to:** Skill 1 research packet assembly for active NBA players, especially mid-season evaluations during periods of public narrative momentum (offseason work narratives, early-season hot stretches, comeback storylines).
**Status:** Active
**Applications:** 1 (Sengun S105 — 3PT% reconciliation: script 28.2% weighted / StatMuse 28.9% full-season vs articles' 37.5–45.9% claims; resolved in research packet via "articles cherry-picked hot stretches" note in Data Gap Inventory)

---

### S100-F01 — Script output bugs surface during batch evaluations
**Status:** Superseded (promoted to docs/SCRIPT-MAINTENANCE-BACKLOG.md as B1–B5, Session 114 2026-04-28)

Original entry archived at `docs/learnings/archive/S100-F01-archived.md`. 24+ applications across 5 bug variants over S100–S113 (BLK%/STL% endpoint alone hit 24+ individual cases). Promoted to dedicated maintenance-tracker doc per Workstream 2 retrospective recommendation; backlog also inherits 2 additional bug variants from W2 retrospective (Domain 5 #17 Rim D_FGA endpoint N/A; Domain 5/6/8 partial endpoint timeouts).

**On-eval workaround lookup:** When a script run produces unexpected output during Skill 1 research, consult `docs/SCRIPT-MAINTENANCE-BACKLOG.md` for known workarounds. Not loaded by default — only when a bug fires.

---

### S95-F07 — PlayerCareerStats endpoint quirks (frame ordering + TOT rows)
**Date:** 2026-04-22
**Severity:** Medium
**Context:** Building Playoff_Track_Record.py surfaced two nba_api PlayerCareerStats quirks. (1) `get_data_frames()` returns 4 frames in order: [SeasonTotalsRegularSeason, CareerTotalsRegularSeason, SeasonTotalsPostSeason, CareerTotalsPostSeason]. Postseason is at index **2**, not 1. Initial script used `frames[1]` and crashed on missing SEASON_ID column (CareerTotalsRegularSeason has no SEASON_ID). (2) Traded players have multiple rows per season — a TOT row aggregates plus individual team rows. Summing all rows double-counts.
**Learning:** For any script using `playercareerstats.PlayerCareerStats`: (a) postseason DataFrame is at `frames[2]`, not `frames[1]` — comment frame indices inline to prevent off-by-one; (b) per-season aggregation must prefer the TOT row when present (filter `TEAM_ABBREVIATION == "TOT"`), falling back to the single team row if no TOT exists. See Playoff_Track_Record.py `get_season_totals()` for the canonical pattern.
**Applies to:** all future scripts/.py files using nba_api's playercareerstats endpoint.
**Status:** Active
**Applications:** 2

---

## ENTRY FORMAT

See SELF-LEARNING-PROTOCOL.md for the canonical entry format. Each
active learning must include: ID, Date, Severity, Context, Learning,
Applies to, Status, Applications.

---

*Created Session 94. Empty scaffold.*
