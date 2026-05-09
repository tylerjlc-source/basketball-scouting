# EVALUATION WINDOW AUTOMATION
**Reference for R12 injury-evaluation-window detection in eval_window.py.**
**Load when:** auditing or modifying eval_window.py, debugging an R12 classification, or adjusting thresholds via a Calibration Finding.

---

## WHAT THIS DOES

eval_window.py is a shared utility imported by all 7 domain scripts. For any player, it decides which seasons to pull and how to weight them — overriding the default 0.60 / 0.40 two-season window when R12 triggers.

The module outputs a structured `=== EVALUATION WINDOW ===` block at the top of every script run. Skill 1 reads that block and pastes the flag text (with injury name filled in) into the research packet.

The module makes the quantitative call (which seasons). Skill 1 makes the qualitative call (which injury). Clean seam.

---

## WHEN THIS RUNS

Every domain script call. For the default case (both recent seasons healthy) the output is informational only — scoring behavior is byte-identical to pre-automation. R12 modes change which seasons the script fetches and how they're weighted.

Default window: current season weight 0.60, prior season weight 0.40. Per SCORING-RULES.md R12, this is overridden only when both recent seasons are compromised.

---

## CLASSIFICATION THRESHOLDS

Locked Session 94. Updated Session 96 — fragment-anchor-eligible band added per R12 S96 calibration (S96-F01).

| Classification | Games played | Minutes check | Anchor-eligible? |
|---|---|---|---|
| Healthy | ≥ 58 GP | MPG within 25% of career rotation average | Always |
| Fragment (anchor-eligible) | 40–57 GP | (no MPG check) | When most-recent pre-injury |
| Fragment (sample-only) | 25–39 GP | (no MPG check) | Never |
| Compromised | < 25 GP | (no MPG check) | Never |
| Rookie / not-yet-played | — | Special case, see Edge Cases | — |

**Career rotation average (MPG baseline).** Computed as the mean MPG across all prior career seasons where GP ≥ 40. This excludes rookie fragments and late-career scrap appearances, producing a stable "typical rotation minutes" baseline. For a first- or second-year player with fewer than two qualifying prior seasons, the MPG check is skipped and classification runs on GP alone.

**Why 58 GP:** ~70% of 82 games. Accounts for normal rest / load management without flagging genuine health. Kawhi-type healthy seasons at 55–65 GP clear via the MPG check when MPG is stable.

**Why 40 GP on the fragment-anchor-eligible floor (S96):** Roughly half a season. Below this threshold, sample is too thin to anchor a 26-sub-domain evaluation. At or above this threshold, rate-stat trends stabilize enough that a recent fragment is a cleaner read of current state than a walk-back to an older healthy season. See R12 "Anchor selection" clause in SCORING-RULES.md.

**Why 25 GP floor on fragment:** Below 25 games, sample size is insufficient to extract signal even for directional reads. Those seasons are compromised, not useful.

---

## DECISION TREE

Inputs: classification of current season (C) and prior season (P), plus earlier seasons as needed.

```
1. Is C the player's first career season?
   → Yes: ROOKIE mode. Current season only, no R12 evaluation.
   → No: continue.

2. Classify C and P.

3. Apply decision table:

   C = healthy, P = healthy     → DEFAULT (0.60 / 0.40)
   C = healthy, P = fragment    → DEFAULT (R9 may apply to P)
   C = healthy, P = compromised → DEFAULT (R9 may apply to P)
   C = fragment, P = healthy    → DEFAULT (R9 may apply to C)
   C = compromised, P = healthy → DEFAULT (R9 may apply to C)

   C = fragment or compromised, P = fragment or compromised
     → R12 TRIGGERED. Walk back to find anchor.

4. R12 anchor search (walk back P-1, P-2, P-3, P-4):
   Build candidate list of seasons meeting anchor eligibility floor:
     • Healthy (≥58 GP + MPG check), OR
     • Fragment-anchor-eligible (40–57 GP) — per S96 R12 fragment exception
   
   Select MOST RECENT candidate from the list as the R12 anchor at 100% weight.
     • If anchor is >3 seasons back: add age-concern flag.
     • If anchor is a fragment: add "fragment anchor (X GP)" note to output.
   
   → No candidates within 4 seasons back:
     • Check aggregate: do C + P combine to GP ≥ 50?
       - Yes: R12_AGGREGATE mode. Weight C and P proportionally to their GP.
       - No: INSUFFICIENT_DATA. Halt script; Skill 1 handles qualitatively.
```

---

## OUTPUT FORMAT

Every script run prints this block first, before any domain stats:

```
=== EVALUATION WINDOW ===
Mode: [DEFAULT | R12_ANCHOR | R12_AGGREGATE | ROOKIE | INSUFFICIENT_DATA]
Seasons used: [YYYY-YY (weight), YYYY-YY (weight)]
Detected: [YYYY-YY (GP, MPG — classification), ...]
[Mode-specific line: healthy anchor, aggregate breakdown, or insufficient-data reason]
Research packet flag template: "[template with [injury] placeholder]"
===
```

**Example — DEFAULT mode (no R12):**
```
=== EVALUATION WINDOW ===
Mode: DEFAULT
Seasons used: 2025-26 (0.60), 2024-25 (0.40)
Detected: 2025-26 (71 GP, 33.1 MPG — healthy), 2024-25 (78 GP, 34.0 MPG — healthy)
No R12 trigger.
Research packet flag template: (none required)
===
```

**Example — R12_ANCHOR mode:**
```
=== EVALUATION WINDOW ===
Mode: R12_ANCHOR
Seasons used: 2022-23 (1.00)
Detected: 2025-26 (28 GP, 14.2 MPG — compromised), 2024-25 (31 GP, 18.1 MPG — compromised), 2023-24 (18 GP — compromised), 2022-23 (71 GP, 34.5 MPG — healthy)
Healthy anchor: 2022-23 (2 seasons back, no age-concern flag).
Research packet flag template: "Evaluation window: 2022-23 applied as primary per R12 — 2025-26 and 2024-25 compromised by [injury]."
===
```

**Example — INSUFFICIENT_DATA mode:**
```
=== EVALUATION WINDOW ===
Mode: INSUFFICIENT_DATA
Seasons used: (none — script halted)
Detected: 2025-26 (22 GP — compromised), 2024-25 (19 GP — compromised), 2023-24 (34 GP, fragment), 2022-23 (28 GP, fragment)
No healthy anchor within 4 seasons back. Aggregate GP insufficient (2025-26 + 2024-25 = 41 GP < 50).
Research packet flag template: "R12 triggered but insufficient data — qualitative-only evaluation required."
===
```

---

## OVERRIDE MECHANISM

Every domain script accepts `--season-override YYYY-YY` as an optional CLI flag. When set, eval_window.py skips its own decision tree and uses the named season at 100% weight.

**When to use:**
- Load-management seasons misclassified as injury (script can't distinguish rest from injury).
- Qualitative research contradicts the script's classification.
- Testing / debugging.

**Usage:**
```bash
python scripts/Domain_1_Finishing__Stats.py 'Kawhi Leonard' --season-override 2019-20
```

Override output:
```
=== EVALUATION WINDOW ===
Mode: OVERRIDE
Seasons used: 2019-20 (1.00)
Override reason: manual (--season-override flag)
Research packet flag template: "Evaluation window manually set to 2019-20 — reason required in packet."
===
```

The research packet must document the override reason manually (script doesn't know why).

---

## EDGE CASES

1. **Rookie / first career season.** Detected via nba_api career log length = 1. Skip R12 logic entirely. ROOKIE mode uses current season only, matches existing pre-automation behavior.

2. **Mid-career trade-season / waiver-season.** Low GP, not injury. Script cannot distinguish from compromised. Handle via `--season-override` once qualitative research confirms.

3. **Load-management seasons** (Kawhi '19, late-career stars). GP may fall below 58 but MPG check clears if minutes stable. If both GP and MPG fall, misclassified as compromised — override manually.

4. **Mid-season evaluation.** Current season GP still accumulating. v1 behavior: classify on raw current GP without projection. A season tracking healthy may misclassify as fragment until ~game 58. Skill 1 overrides with `--season-override` if needed. Formal season-completion projection is a v2 enhancement.

5. **Playoff games missed** (regular-season healthy but missed playoffs). Script uses regular-season GP only. Playoff games don't factor into classification.

6. **Healthy anchor >3 years old.** R12_ANCHOR still fires, with age-concern flag. The flag surfaces in script output and research packet; Skill 1 or Tyler decides whether the anchor is still representative or the player should be flagged for aging concern.

---

## RELATION TO R9 AND R12

**R9 (Injury Temper)** — suppresses athleticism sub-domain (#21, #22, #15) scores to healthy baseline when documented injury is active within a normal evaluation window. R9 applies per-sub-domain. Scripts do not implement R9 — it's a Skill 2 scoring rule.

**R12 (Injury Evaluation Window)** — overrides the two-season weighting when both recent seasons are compromised. R12 applies at the window level. eval_window.py implements R12 detection.

**Coexistence:** In R12_ANCHOR mode, the anchor season's athleticism scores are already from a healthy period (no R9 needed). In R12_AGGREGATE mode, R9 still applies to athleticism sub-domains because the aggregated fragment seasons are mid-injury. Skill 2 handles R9 regardless of which window mode is active.

---

## INTEGRATION WITH DOMAIN SCRIPTS

**Phase 1 (current): classification-only.** eval_window.py prints the header block. Domain scripts still fetch current/prior seasons using hardcoded weights. Validates the classification logic without risk to existing output.

**Phase 2 (post-validation): wired in.** Each domain script replaces its hardcoded season fetch with a call to `determine_evaluation_window()`. Scoring math runs against the returned season list and weights.

Backward compatibility: DEFAULT mode produces identical stats output to pre-automation (with a new evaluation-window header block prepended).

---

## CALIBRATION FINDINGS

Findings for eval_window.py and its integration now live in `docs/learnings/project-learnings.md` per SELF-LEARNING-PROTOCOL.md. Historical entries EW-F01, EW-F02, and EW-F04 migrated to S94-F01, S94-F02, and S94-F03 respectively. EW-F03 was Cat 1 (one-time doc-wording correction) and required no migration.

**S96-F01 — R12 fragment-anchor exception.** Locked Session 96 via Ja Morant production-run calibration. Fragment seasons in the 40–57 GP band are now anchor-eligible when most-recent pre-injury, preserving the strict healthy definition (≥58 GP) but closing the walk-back hole that caused the eval_window to skip a recent 50-GP sample in favor of an older 61-GP healthy season. Implemented as Cat 2 standing rule — lives in SCORING-RULES.md R12 + this document's Classification Thresholds and Decision Tree. Threshold (40 GP) chosen as midpoint of Tyler's proposed 35–45 GP range; revisit if future cases expose edge conditions.

---

*Created Session 94. Thresholds and decision tree locked via architectural-principles review in same session. Session 96: fragment-anchor-eligible band added to Classification Thresholds; Decision Tree Step 4 updated to build candidate list from healthy + fragment-eligible seasons and select by recency.*
