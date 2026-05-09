# S111-F01 — Anchor-deflation pattern in comparison set compresses placement

**Status:** Superseded (promoted to COMPOSITE-SCALE-AND-TIERS.md Step 4 "Anchor-state correction" subsection, Session 114 2026-04-28)

**Original Date:** 2026-04-27
**Severity:** Medium
**Source file:** `docs/learnings/scout-composite-learnings.md`
**Applications before promotion:** 3 (Edwards S111 surfaced firing case + Cade S112 not-firing validation + Wembanyama S113 not-firing validation — discrimination clean across firing and not-firing cases per Workstream 2 retrospective)

---

**Context:** Edwards S111 re-eval initial Skill 4 draft landed 8.70 (upper Tier 5). Tyler pushback: (1) noted Tatum 8.88 sits below Tier 4 floor due to active Achilles recovery — anchored just under 8.90 to reflect post-injury uncertainty, NOT representative of healthy AAW ceiling; (2) two recent consecutive All-NBA Second selections compound to validate Tier 4 lower-third entry per "multiple awards compound" principle. Initial draft used Tatum 8.88 (deflated) and Brown 8.83 (Score-First Wing, archetype-adjacent not exact) as upper-Tier-5 ceiling anchors and compressed Edwards under them. Correct comparison set was Tier 4 lower-third cluster (Booker/Mitchell 8.92, Cade 8.98, Kawhi 8.90) — peer cluster with multiple ANBA selections + comparable PPG + similar drag profile. Final placement 8.93.

**Learning:** When the candidate-band comparison set includes anchors with active injury / recovery / dormancy flags, those anchors are typically deflated below their healthy-state ceiling. Using them as upper-band-or-tier ceiling references compresses the eval placement downward. Before applying the comparison, check each upper anchor's notes column for deflation flags (active recovery, injury flag, dormancy, load management). For each flagged anchor, reason about the healthy-state ceiling separately, and use the healthy ceiling — not the deflated current composite — as the comparison reference. Distinct from S102-F03 (hypothesis-text narrowing) — same family of "narrow-anchoring failure" but a different mechanism (anchor-state vs comparison-set scope).

**Why:** Injury-deflated anchors break the anchor library's calibration role for fresh evals — the deflation is a temporary discount, not a structural ceiling statement. Without the healthy-state correction, fresh evals systematically compress against the deflation and inherit it. The bigger the recent injury cohort in a tier band, the worse the compression. Tatum 8.88 (post-Achilles), Kawhi 8.90 (load-managed), Mobley 8.67 (left-calf) — Tier 4-5 alone has three deflated anchors actively pulling fresh evals downward.

**How to apply:** During Skill 4 Step 4, when listing comparison anchors in the candidate band, annotate each with deflation status from ANCHOR-LIBRARY Notes column. For each deflated anchor: reason about healthy-state ceiling explicitly in the walkthrough (e.g., "Tatum 8.88 currently / ~9.05 healthy per S108-F01 R9-spirit weighting"). Use healthy ceiling for comparison. Document the correction in the assignment walkthrough so the placement is auditable. Especially relevant when comparing against AAW (multiple injury-flagged anchors), Switchable Big (Mobley flag), Ball-handler injury cohorts.

**Applies to:** Skill 4 composite assignment — specifically the anchor comparison step (Step 4) for fresh evals or re-evals where the candidate band contains injury-flagged or dormancy-flagged anchors. Does not apply when no anchors in the comparison set carry deflation flags.

---

**Promotion record:** S111-F01 was surfaced during Edwards S111 re-eval as a firing case (Tyler corrected initial 8.70 → 8.93 by re-anchoring on healthy comparison set). Promotion criteria per SELF-LEARNING-PROTOCOL.md §139–149: 3 successful applications. Pattern held cleanly across the Workstream 2 spike:

- **Edwards S111** (firing) — Initial draft 8.70 anchored on Tatum 8.88 (post-Achilles) + Brown 8.83 (archetype-adjacent). Correction used Tier 4 lower-third cluster Booker/Mitchell/Cade/Kawhi instead. Final placement 8.93.
- **Cade S112** (not-firing validation) — Healthy comparison set check applied at pre-modifier stage. Luka 9.07, Booker 8.92, Mitchell 8.92 anchored placement; Tatum/Edwards/Mobley flagged peers did not drive. Watchpoint applied, NOT driving placement. Final placement 8.96.
- **Wembanyama S113** (not-firing validation) — Comparison set checked. Tier 3 anchors all healthy (Giannis, KD, Curry); no deflation pattern. Watchpoint applied, NOT driving placement. Final placement 9.30.

Discrimination character: 1/3 firing rate is the watchpoint working as designed — distinguishes correctly between cases where deflation IS active (Edwards) vs. cases where it is NOT (Cade, Wembanyama). Not a false-negative rate.

Promoted to COMPOSITE-SCALE-AND-TIERS.md Step 4 "Anchor-state correction" subsection. Operational guidance now governs every Skill 4 anchor comparison rather than loading just-in-time as a learning.
