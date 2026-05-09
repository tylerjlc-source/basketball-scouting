# S120-F01 — Archived

**Original location:** `docs/learnings/scout-research-learnings.md`
**Status:** Superseded (promoted to SCORING-RULES.md R12 "Single-season step-back" subsection + eval_window.py `determine_evaluation_window()` patch, Session 120 2026-04-30)
**Promotion rationale:** Tyler accelerated promotion on first application — finding had a clear single-clause rule expansion + bounded script patch path; both layers shipped together rather than waiting for 3-application threshold.

---

## Original entry (verbatim)

### S120-F01 — eval_window.py R12 trigger does not fire when only current season is compromised
**Date:** 2026-04-30
**Severity:** Medium
**Context:** Tyrese Haliburton S120 (Achilles rehab — entire 2025-26 missed, 0 GP, prior 2024-25 healthy 73 GP / 33.6 MPG) surfaced an eval_window.py spec gap. The `classify()` function correctly tags 2025-26 as `compromised` (gp < FRAGMENT_GP_MIN = 25). But the R12 anchor trigger requires both current AND prior to be compromised — `if not (c_ko and p_ko): return _build_default(c, p, all_seasons)`. With prior healthy, the trigger fails and the script returns `DEFAULT` mode with `seasons_used = [(2025-26, 0.60), (2024-25, 0.40)]` — placing 60% weight on a 0-GP synthesized season. Structurally wrong: weighting a 0-GP season cannot produce meaningful aggregates. Tyler's spec clarification (S120 chat): "If one of the previous 2 seasons is insufficient we default to the most recent season until we find a season with sufficient GP" — i.e., step back when *either* season is compromised, not only when both are. Manual override `--current-season 2024-25` used in S120 as procedural workaround; produced correct window 2024-25 (0.60) + 2023-24 (0.40).
**Learning:** When current season is 0-GP-compromised (entire-season miss — Achilles, ACL, suspension) and prior season is healthy, eval_window.py should auto-step-back the window one position to (most-recent-healthy + previous-healthy) at default 0.60/0.40 weighting. The existing R12 trigger guards the both-compromised case (R12 anchor mode = single-season anchor); an additional clause should handle the current-only-compromised case where stepping back yields a clean two-season window without invoking R12 anchor mode. The proposed clause: if `c.classification == "compromised"` AND `p.classification == "healthy"` AND a `before-prior` healthy season exists, return `DEFAULT` mode with seasons_used = [(p.season, 0.60), (before_prior.season, 0.40)] and a flag template documenting the step-back.
**Why:** R12's anchor mode applies when the player has no clean two-season window available. When current is missed entirely but prior + before-prior are both healthy, a clean two-season window IS available — just one position back. R12 anchor mode (single-season anchor at 1.00 weight) is heavier than necessary for this case and discards a valid second healthy season worth of data. The S120 manual override produced exactly the right window; the script should reach the same answer automatically.
**How to apply:** Until the script is patched, evaluators must manually pass `--current-season {prior_healthy_season}` when the auto-detection produces a 0-GP weighting. Documentation: surface the override + reason in the research packet header EVAL WINDOW field.
**Applies to:** scripts/eval_window.py `determine_evaluation_window()` function. Affects any NBA-vet evaluation where the current season has 0 GP (entire-season miss) with a healthy prior season. Distinct from R12 (both compromised — anchor mode) and S96 fragment-anchor (recent fragment season ≥40 GP). Possible promotion targets: (a) SCORING-RULES.md R12 expansion to cover the current-only-compromised case, or (b) eval_window.py auto-stepback subroutine, or (c) both. Tyler triage required.
**Status:** Active — proposed fix surfaced; pending Tyler triage.
**Applications:** 1 (Tyrese Haliburton S120 — 2025-26 0 GP Achilles / 2024-25 73 GP healthy → manual `--current-season 2024-25` override applied; produced correct window 2024-25 (0.60) + 2023-24 (0.40); both seasons fully healthy.)

---

## Promotion outcome

- **Rule destination:** SCORING-RULES.md R12 — new "Single-season step-back" subsection inserted between "Application:" block and "Anchor selection (S96 — R12 fragment exception):" block.
- **Script destination:** eval_window.py — new branch in `determine_evaluation_window()` after rookie check, before existing R12 trigger; `_build_stepback()` builder function added; one new validation case (Tyrese Haliburton 2025-26 → DEFAULT mode with step-back flag).
- **Operator impact:** Manual `--current-season` override no longer required for current-season-compromised + prior-season-healthy NBA-vet evaluations. The script auto-handles the step-back case.
