# scout-scoring — Learnings

Active calibration learnings for the scout-scoring skill. Loaded
just-in-time at skill invocation (P1). Governed by
SELF-LEARNING-PROTOCOL.md.

**Scope:** Category 3 findings scoped to this skill's execution.
Category 1 findings live in session logs. Category 2 findings live
in rule documents (see routing table in SELF-LEARNING-PROTOCOL.md).

---

## ACTIVE LEARNINGS

---

### S108-F01 — R9-spirit weighting choice when R12 doesn't formally fire (single-season-compromised + active proof-of-return)
**Date:** 2026-04-25
**Severity:** Medium
**Context:** Jayson Tatum S108 surfaced an evaluation-window weighting pattern not directly addressed by either R9 or R12. Eval window: 2025-26 (16 GP, 32.6 MPG — compromised post-Achilles recovery) + 2024-25 (72 GP, 36.4 MPG — healthy unanimous All-NBA First Team). R12 does NOT formally fire (only one season compromised; one healthy anchor available). R9 formally applies only to athleticism sub-domains (#21/#22/#15) — but Tatum's defensive/tracking numbers actually trend AT or ABOVE pre-injury baseline (DFGPOE −7.4% current vs +0.3% prior; DREB% career-high 27.4% in 2025-26; speed 3.82 mph current vs 3.65 prior). Where the recovery sample DOES drag is shooting/finishing rate stats (Rim FG% 71.9 → 61.3, CAS 3PT% 40.0 → 30.3, Mid-range 39.6 → 35.1 — clear ramp-up dips). The default 60/40 weighting puts 60% weight on a 16-GP recovery sample for these rate stats. R9 doesn't cover these sub-domains; R12 doesn't fire. Under-application: scoring weighted aggregates as primary signal under-credits Tatum's healthy ceiling. Over-application: ignoring the recovery sample over-credits the ceiling.
**Learning:** When R12 does not formally fire (one season healthy + one season compromised) but the post-injury sample is short (~15-25 GP) AND in active proof-of-return mode (positive trajectory, not multi-season persistence), apply R9 spirit to the weighting choice for shooting/finishing/skill rate stats: anchor sub-domain ceilings on the healthy season's data, treat the recovery sample as directional (consistent / inconsistent with anchor) but not as primary signal weighting. Document the choice explicitly in the Skill 2 Injury Temper Log with phrasing: "R9 considered, applied in spirit to weighting choice; R12 does not formally apply (one healthy anchor available); recovery sample treated as directional, healthy-anchor governs ceiling read." Distinct from formal R9 (athleticism sub-domains only) and formal R12 (both seasons compromised). The mechanic is a weighting-decision protocol, not a temper magnitude.
**Why:** Single-season-compromised + active-recovery is a real pattern that the formal R9/R12 framework does not cover cleanly. R9 is too narrow (athleticism only). R12 is too restrictive (both seasons compromised). Without explicit guidance, evaluators may either (a) over-weight the recovery sample as if it were a normal season or (b) ignore it entirely as if R12 fired. Neither is correct. The right protocol is to anchor on healthy data for sub-domain ceilings while treating recovery numbers as directional evidence — same pattern, different scope, than R9's healthy-baseline principle.
**How to apply:** During Skill 1 research, flag the weighting consideration in the packet's Injury History section. During Skill 2, apply the weighting choice per sub-domain: (1) for athleticism (#21/#22/#15) — formal R9 applies if conditions met; (2) for shooting/finishing rate stats (#1/#2/#4/#5/#6/#7) — anchor on healthy season's metrics, note recovery sample as ramp-up; (3) for tracking-based defense and rebounding (#15/#16/#20) — accept current sample if it's at or above prior (no temper needed; R9-spirit doesn't apply where the sample isn't dragging the score). Document each weighting decision in the rationale sentence. Do NOT formally invoke R9 or R12 unless their formal conditions are met — this is a procedural clarification, not a rule expansion.
**Applies to:** Skill 1 (research packet weighting flag) and Skill 2 (sub-domain weighting choice) for NBA-vet evaluations where the player is in active proof-of-return from a major injury, with one healthy season + one short-sample recovery season in the eval window. Does not apply when recovery has multi-season persistence (S96-F03 governs that case as recalibration). Does not apply to prospects (different evaluation framework).
**Status:** Active
**Applications:** 1 (Tatum S108 — R12 not fired, R9 applied in spirit to weighting choice; healthy-anchor 2024-25 used as primary signal for shooting/finishing rate stats; current 2025-26 16-GP sample used as directional ramp-up evidence; defensive/tracking numbers accepted at-current-sample because they trend at-or-above prior baseline)

---

### S96-F02 — R8 cross-reference caps and direct empirical measurement
**Status:** Superseded (promoted to SCORING-RULES.md R8 "Direct empirical measurement override" subsection, Session 102 2026-04-24)

Original entry archived at `docs/learnings/archive/S96-F02-archived.md`. Applied 11+ times across 4 NBA-vet evaluations (Morant S96; Mobley S102 ×4 strength caps on #15/#17/#18/#18; Sabonis S102 ×2 on #3/#20 strength caps; Bridges S102 ×4 on #6/#12/#15 caps plus one at-cap case). Pattern held cleanly across all applications — override never inflated composite outcome beyond anchor-library peer validation. Promoted to formal R8 rule subsection after empirical pattern held across session with 10+ applications in one sitting.

---

### S96-F03 — R9 temper disqualified by multi-season post-injury persistence
**Date:** 2026-04-22
**Severity:** Medium
**Context:** Ja Morant Skill 2 surfaced an R9 application ambiguity. All four R9 conditions formally met (named injury = right shoulder labrum tear Jan 2024, multi-source confirmation of injury-caused decline, pre-injury baseline exists in 2022-23, mechanism mapped to vertical/burst). But decline has persisted 2+ full seasons post-surgery with no meaningful athletic recovery — dunk rate halved and stayed halved, drive PPP dropped and stayed dropped, league evaluators began describing the athletic decline as permanent ("shell of his former athletic self," trajectory comp to D-Rose/J-Wall). Tyler approved not applying R9, treating decline as genuine recalibration.
**Learning:** R9's temper clause applies when injury suppression is "temporary and injury-related." When the decline persists across 2+ full seasons post-surgery with no meaningful recovery trend, treat as genuine recalibration of baseline — not temporary suppression. This is the contrast case R9 itself acknowledges: "Gradual multi-season decline with no documented injury is a genuine development concern, not R9." The S96-F03 extension: a documented injury that caused a decline WHICH HAS PERSISTED multi-season is effectively the same regression pattern — the injury explains the cause, but the persistence means the recovered baseline IS the current baseline. Note also: when R12 anchor selection has already given the injury benefit-of-doubt by selecting the most-recent pre-injury sample, adding R9 on top double-tempers. Log the call in the Injury Temper Log: "R9 considered, not applied — multi-season post-injury persistence treated as recalibration; R12 anchor already captured injury accommodation."
**Applies to:** Skill 2 scoring step — R9 injury temper application. Affects NBA-vet cases with documented injuries and multi-season post-surgery persistence. Interacts with R12: if R12 anchor is post-injury sample, R9 is typically already implicitly absorbed.
**Status:** Active
**Applications:** 2 (Ja Morant S96 — sub-domains #15, #21, #22; Joel Embiid S110 — sub-domains #21, #22, with derivative effect on #15 via cross-ref cap. Embiid is the inverse R12-pairing case from Morant: Embiid's R12 anchor was 2022-23 healthy MVP year (R9 would have double-tempered the post-injury sub-domains by suppressing scores from the healthy ceiling), so R9 was correctly NOT applied and the multi-season persistence drove athletic recalibration to current state directly per S96-F03 spirit. Pattern holds: when R12 has already given injury benefit-of-doubt, R9 on top double-tempers regardless of whether R12 anchor is pre- or post-injury sample.)

---

## ENTRY FORMAT

See SELF-LEARNING-PROTOCOL.md for the canonical entry format. Each
active learning must include: ID, Date, Severity, Context, Learning,
Applies to, Status, Applications.

---

*Created Session 94. Empty scaffold.*
