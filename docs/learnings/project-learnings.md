# Project-Level Learnings

Active calibration learnings that span multiple skills or operate at
the architectural / operational layer. Loaded at session open alongside
SELF-LEARNING-PROTOCOL.md. Governed by SELF-LEARNING-PROTOCOL.md.

**Scope:** Category 3 findings that don't cleanly belong to a single
skill — cross-skill patterns, workflow refinements, architectural
observations not yet promoted to ARCHITECTURAL_PRINCIPLES.md.

---

## ACTIVE LEARNINGS

*Session 94 routing note: S94-F05 was demoted to a code comment in `scripts/Domain_5_Defense__Stats.py` per the Entry Threshold filter — applicability was too narrow (one file, one mode) for a standing learning. The ID gap between F04 and F06 is intentional.*

---

### S94-F01 — Validation expectations must be verified against real data, not roster memory
**Date:** 2026-04-21
**Severity:** Medium
**Context:** Two instances in Session 94. (a) Murray 2022-23: expected fragment, actual 65 GP at 32.8 MPG = healthy. (b) Irving 2025-26: expected healthy, actual 0 GP (March 2025 ACL tear). Both validation expectations were wrong based on recalled roster perception, not current data.
**Learning:** Before setting an expected classification in a validation test, pull the target player's actual GP/MPG for the test season(s) and classify per thresholds. Roster-memory assumptions about injury status, minutes, and availability drift and mislead.
**Applies to:** eval_window.py validation harness; any future script-level validation that asserts expected player state.
**Status:** Active
**Applications:** 2

---

### S94-F02 — Use ASCII dashes in script stdout, em-dashes only in markdown
**Date:** 2026-04-21
**Severity:** Low
**Context:** eval_window.py em-dashes (`—`) rendered as `�` on Windows cp1252 console. Fixed by replacing with `--` (ASCII double-dash) in output strings.
**Learning:** Any .py file that prints to stdout must use `--` in user-facing strings on Windows. Markdown docs and code comments can keep em-dashes — they render correctly in markdown viewers and are not sent to the console.
**Applies to:** all scripts in `scripts/`; any future script that outputs human-readable text.
**Status:** Active
**Applications:** 1

---

### S94-F03 — UTF-8 stdout reconfigure required on all domain scripts
**Date:** 2026-04-21
**Severity:** High
**Context:** Domain scripts crashed with `UnicodeEncodeError` on Windows cp1252 console when player names contained non-ASCII characters (e.g., Jokić, Dončić). Surfaced during Phase 2 validation on Jokić. Fixed by adding `sys.stdout.reconfigure(encoding='utf-8')` after `import sys` in all 7 domain scripts.
**Learning:** Any new domain-level script (or any script that may print player names fetched from nba_api) must include `sys.stdout.reconfigure(encoding='utf-8')` immediately after `import sys`. Without it, international player names crash the run on Windows.
**Applies to:** all scripts in `scripts/`; applied retroactively to Domain_1, 2, 3, 4, 5, 6, 8.
**Status:** Active
**Applications:** 7

---

### S94-F04 — R12_AGGREGATE mode has not been validated end-to-end
**Date:** 2026-04-21
**Severity:** Medium
**Context:** Phase 2 validation covered DEFAULT (SGA) and R12_ANCHOR (Irving natural, Wall with --current-season 2021-22). No validation player triggered R12_AGGREGATE. Math in Domain_5 and Domain_8 may produce slightly stale weights in that mode.
**Learning:** When the first real player triggers R12_AGGREGATE in production, run spot-validation on that domain's output: verify weighted values reflect proportional weights, not 0.60/0.40. Compare the script's computed weighted value to a manual calculation before trusting it.
**Applies to:** all 7 domain scripts when AGGREGATE mode fires.
**Status:** Proposed
**Applications:** 0

---

### S94-F06 — Domain scripts have heterogeneous code patterns; batch edits require per-script adaptation
**Date:** 2026-04-21
**Severity:** Medium
**Context:** Phase 2 wire-in initially assumed all 7 domain scripts shared Domain_1's structure. Reading them revealed 4 distinct patterns: A (Domain_1, Domain_2), B (Domain_3), C (Domain_5, Domain_6, Domain_8), D (Domain_4). Each required a slightly different edit shape.
**Learning:** Before proposing a batch edit across multiple domain scripts, read each one first and group by structural pattern. Do not assume uniformity. Plan per-pattern, not per-file.
**Applies to:** any future multi-script editing work across `scripts/`.
**Status:** Active
**Applications:** 1

---

### S94-F07 — Tyler reviews markdown/prose, not Python code
**Date:** 2026-04-21
**Severity:** High
**Context:** Tyler stated mid-Phase-2: "I don't know enough about python script to review your edits. The most important thing is that we don't break any of the scripts." Shifted communication pattern for the rest of Phase 2.
**Learning:** When editing Python scripts: (a) communicate outcomes and intent in plain English, not diffs; (b) rely on post-change validation runs as the safety check, not Tyler's code review; (c) show code only if Tyler explicitly asks. For markdown docs and conversation: normal draft-review-approve flow still applies.
**Applies to:** any session involving script work — scout-research (script-driven data collection), all script-registry operations, all domain-script maintenance, eval_window.py maintenance.
**Status:** Active
**Applications:** 1

---

### S95-F04 — P1 test for skill loads: inline summary vs full rule text
**Date:** 2026-04-22
**Severity:** Medium
**Context:** When adding R13 to Skills 4 and 5, initial instinct was to add SCORING-RULES.md to their LOADING INSTRUCTIONS so the skills could reference the full rule. Re-examination found that inlining gate conditions + magnitude tables in the target files (PROJECTION-OUTPUT-BLOCK.md for Stage 1, scout-composite.md Step 5.75 for Stage 2) covered the skills' needs without loading 265 lines of rule text. The default "load the authoritative doc" instinct would have violated P1 ("just in case" loads).
**Learning:** When deciding whether a skill should load a full rule doc, apply the test: "does the skill need the full rule text, or just a mechanical summary?" If summary suffices, inline it in the skill's existing load targets and use a one-line back-reference. Reserve full-doc loads for cases where the skill reasons across multiple rule clauses or needs prose explanations.
**Applies to:** every "should Skill N load Doc X?" decision during skill or rule authoring.
**Status:** Active
**Applications:** 2

---

### S95-F05 — Entry Threshold has an implicit P1 sub-test
**Date:** 2026-04-22
**Severity:** Medium
**Context:** Task 4 (historical mining) surfaced two candidate Cat 3 entries (S82 Precision Principle, S84-F01 Expert-Driven Stat Selection) that passed the three-test Entry Threshold (applicability / non-obvious / actionable). On P1 review, both only apply during source-map construction; routing to project-learnings.md (loads every session) would violate "load just-in-time" for principles that fire in a small fraction of sessions. Both were downgraded to Cat 1 pending a narrower destination (SUB-DOMAIN-SOURCE-MAP Construction Methodology header at S97).
**Learning:** Entry Threshold is necessary but not sufficient for Cat 3 promotion. After a finding passes the three tests, apply a P1 check: "does the destination load mechanism match this finding's applicability scope?" If destination loads every session but finding applies only in N% of sessions, route to a narrower location (sub-domain source map, specific skill's learnings file, or a future load-gated doc). Promotion candidate for SELF-LEARNING-PROTOCOL.md as a fourth Entry Threshold test after ≥3 applications.
**Applies to:** every Cat 3 routing decision during session-end protocol.
**Status:** Active
**Applications:** 2

---

### S97-F01 — Weight terminology belongs in the weights files, not in authored documents
**Date:** 2026-04-22
**Severity:** Medium
**Context:** Wings scale v1 was drafted with weight-letter references (H-weighted, L or N-weighted, etc.) in multiple Notes to describe archetype priorities. Tyler corrected during bigs worked-example review: archetype weights are deprecated in scoring (weights files serve only to identify archetypes, not to feed scoring), so weight-letter terminology misleads by implying active use. Wings file carries a cleanup-candidate flag; bigs file was authored without the error.
**Learning:** When authoring reference documents (position scales, rubrics, Notes, sub-domain descriptions), never use weight terminology — H-weighted, M-weighted, L-weighted, N-weighted, or parenthetical (H-), (M-), (L-), (N-). Describe archetype priorities using identity / role / value-driver / primary-evaluation-dimension language. Example: "Rim Protector archetype is built around this skill — interior deterrence is the archetype's primary value driver" not "(H-weighted for Rim Protector)".
**Applies to:** all reference document authoring — position scales, SCORING-RULES.md edits, SUB-DOMAINS_v3.md edits, skill file edits, any doc that references archetype priorities.
**Status:** Proposed
**Applications:** 1

---

### S97-F02 — No player names in position scale documents (applies to Notes, not just bands)
**Date:** 2026-04-22
**Severity:** Medium
**Context:** During wings QC, names were found in band descriptions across 4 Notes; removed per Tyler's rule ("keep it out — that's what our anchor library is for"). During bigs authoring, names slipped into Notes again (#6 historical mid-range tradition; #11 elite court vision anchors) despite the rule being established. Both instances required explicit QC catch and re-approval.
**Learning:** When authoring or editing position scale documents, no player names appear anywhere — not in band descriptions, not in Notes, not in peer-group framing. Historical and tradition references use abstract language ("the interior-scoring tradition", "the high-post passing tradition") rather than canonical players. The anchor library is the single source for "who sits where"; duplicating names in scales creates maintenance surface and conflates scoring axes (Skill 2 scores skills abstractly; Skill 4 compares to composite anchors). Requires draft-time discipline, not just QC-time catch.
**Applies to:** all position scale authoring and editing; extends to any document that describes sub-domain bands abstractly.
**Status:** Proposed
**Applications:** 2

---

### S97-F03 — Anchor library is canonical for per-player archetype tags
**Date:** 2026-04-22
**Severity:** Medium
**Context:** S97 wings and bigs authoring surfaced multiple anchor-library-vs-weights-file archetype-tag divergences (Jaylen Brown Score-First Wing vs weights-file All-Around Wing; Giannis Modern Four vs S48 All-Around Big; Valanciunas Post Scoring Big vs merged Versatile Scoring Big). Tyler ruled "anchor library is truth" when the two sources disagree on a specific player's archetype. The weights file "confirmed fits" lists are historical reference from S47–S48 and have not been actively maintained; the anchor library shows active maintenance (S89, S95, S96 edits).
**Learning:** When a per-player archetype assignment conflicts between ANCHOR-LIBRARY.md and a weights file's "Confirmed fits" list, the anchor library tag wins. Weights-file confirmed-fits are historical and may be stale post-merger. For any scoring chain step that asks "what archetype is player X?": check anchor library first; fall back to weights file only if not listed; if the weights-file tag references a merged/renamed archetype, apply the merger rule (Post Scoring Big → Versatile Scoring Big per S48; Energy/Hustle Wing → Defensive Specialist per S47).
**Applies to:** Skill 3 (archetype identification), Skill 4 (composite placement via anchor comparison), Skill 5 (comp assignment), scale authoring that pulls per-archetype rosters.
**Status:** Proposed
**Applications:** 1

---

### S97-F04 — Anchor library archetype tags can drift post-merger; flag legacy tags during maintenance
**Date:** 2026-04-22
**Severity:** Low
**Context:** During S97 anchor roster synthesis, three legacy-tag drifts were identified. Leonard Miller tagged "Energy/Hustle Wing" — that archetype was merged into Defensive Specialist S47. Jonas Valanciunas tagged "Post Scoring Big" — merged into Versatile Scoring Big S48. Giannis tagged "Modern Four" under Big group — per S48 physical-gate resolution, a physically-big player with wing skills is All-Around Big. None updated in the anchor library despite the taxonomy changes.
**Learning:** When touching ANCHOR-LIBRARY.md, verify each anchor's archetype tag against the current canonical archetype roster in the weights file. Legacy tags (Energy/Hustle Wing, Post Scoring Big, Rebounding Specialist) indicate drift from pre-S48-merger taxonomy. Flag drift to Tyler for reclassification authorization — do not edit silently. For scale authoring that pulls per-archetype rosters, apply the merger rule during synthesis and flag the source drift separately.
**Applies to:** any session that reads or edits ANCHOR-LIBRARY.md; scale authoring that uses anchor rosters.
**Status:** Proposed
**Applications:** 1

---

### S97-F05 — Precision over brevity in reference document authoring
**Date:** 2026-04-22
**Severity:** Medium
**Context:** During wings worked-example review, framing a Note-length question as "acceptable, or tighten?" invited a brevity-biased answer. Tyler corrected: "We need to be accurate. We can't sacrifice precision for brevity." Reference documents load just-in-time at the task that consumes them (P1), so the usual "don't dilute signal across a long session" argument doesn't apply — the loader specifically needs the content. Cutting a load-bearing clause to hit a shorter word count is a P1 violation in the precision direction (insufficient-load failure mode, mirror of overload failure mode).
**Learning:** When drafting or reviewing reference document content, apply the load-bearing test to every clause: does this clause do a distinct job the loader needs? If yes, keep regardless of length. If no, cut regardless of length. Do not frame review questions as "acceptable, or tighten?" — that biases toward trimming. Frame as "does each clause do load-bearing work?" Brevity is secondary in reference/governance documents; precision, completeness, and load-correctness are primary. Does NOT apply to chat-level communication — ordinary terseness guidance holds there.
**Applies to:** all reference document authoring — position scales, SCORING-RULES.md, SUB-DOMAINS_v3.md, skill file edits, architectural documents.
**Status:** Proposed
**Applications:** 1

---

### S98-F01 — Layer discipline between scoring rules and projection outputs
**Date:** 2026-04-23
**Severity:** Medium
**Context:** During POT scale unification (Session 98), the question arose whether the 7.89 prospect composite cap should propagate from Skill 4 into Skill 5's Projection Midpoint under the 1-minimal formulation (Midpoint = composite). The answer depended on intent: the cap exists to bound evaluation uncertainty at Skill 4 assignment, not to bound projected Year-1 production at Skill 5. Under OVR the composite→OVR scaffold imposed the cap indirectly anyway (prospect at composite 7.89 mapped to rubric_OVR ~78–79, below Path A's top-pick trigger of 81). Option A preserved this inherited behavior; Option B would have added a Skill 4 projection_composite emit to unlock top-pick Path A. Tyler chose Option A.
**Learning:** When refactoring a rule, value, or cap that crosses skill boundaries, explicitly identify which skill's intent owns it before deciding whether to propagate, strip, or re-layer. Evaluation caps, uncertainty gates, and assignment rules typically belong to the scoring layer (Skill 2–4). Projection outputs (Skill 5) should inherit numeric values but not necessarily the intent behind them. Check whether the "inherited" behavior was ever desirable, or whether it was a side-effect of the prior representation — then make the propagation choice explicit.
**Applies to:** Any cross-skill refactor — currently queued: domain rating calibration (S99+), position scale validation (S99+). Also governs future unification-style work.
**Status:** Active
**Applications:** 1

---

### S98-F02 — Calibrated band tables need draft-time flexibility language
**Date:** 2026-04-23
**Severity:** Low
**Context:** During POT scale unification, Tyler flagged (on approving the derived POT anchor bands) that the tables need to remain adaptive to generational outliers and weak draft classes — not read as hard gates. The POB now carries flexibility notes on Block 1 (pick-implied composite) and Block 2 (POT anchor) explaining the modal-class calibration and when outliers should be flagged in the divergence field. Without the note, a future reader is more likely to treat the bands as bounds than as centroids.
**Learning:** When authoring any calibrated band table (pick-range, tier, position-scale, archetype-weight), include a one-line flexibility note covering: (a) what the calibration population represents (modal class, current anchor library, etc.), (b) that generational or weak-class outliers may stretch the bands, and (c) where to record range-exceptions (divergence flag field, notes column, or explicit flag). Bare tables with bands but no flexibility note read as hard gates — reviewers apply them too rigidly.
**Applies to:** Any new band-table authoring. Currently relevant to S99+ domain rating calibration (new band tables expected) and position scale validation (wing/big anchor expansion may surface outliers that test current scales).
**Status:** Active
**Applications:** 1

---

## ENTRY FORMAT

See SELF-LEARNING-PROTOCOL.md for the canonical entry format. Each
active learning must include: ID, Date, Severity, Context, Learning,
Applies to, Status, Applications.

---

*Created Session 94. Active.*
