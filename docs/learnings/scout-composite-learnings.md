# scout-composite — Learnings

Active calibration learnings for the scout-composite skill. Loaded
just-in-time at skill invocation (P1). Governed by
SELF-LEARNING-PROTOCOL.md.

**Scope:** Category 3 findings scoped to this skill's execution.
Category 1 findings live in session logs. Category 2 findings live
in rule documents (see routing table in SELF-LEARNING-PROTOCOL.md).

---

## ACTIVE LEARNINGS

---

### S118-F01 — Composite anchor-clustering anti-pattern in sequential top-tier evaluations
**Date:** 2026-04-29
**Severity:** HIGH (system-integrity threatening)
**Context:** Three sequential top-tier evaluations clustered at 9.30 — Wemby S113, Giannis S116, KD S118 (draft). Each placement was reasoned relative to the previous comparator, producing anchoring drift toward the same value rather than independent placement against the full Tier 3 spread (9.20–9.49). The two-decimal composite scale exists specifically to differentiate similar players — clustering wastes that precision and threatens the rating system's signal value. Tyler caught the pattern at S118; required full recalibration to 9.34 / 9.30 / 9.26 for Wemby / Giannis / KD.
**Learning:** At Step 5 decimal placement, dial composite to profile signature INDEPENDENTLY before checking against adjacent anchors. The sequence matters — profile-driven dial first, spread check second. C4 ("ambiguity resolves downward") is a between-band rule; do NOT apply it within-band, where the goal is decimal precision, not band selection. Within-band ambiguity is resolved by digging deeper into profile signature, not by snapping to the nearest existing anchor.
**Mandatory checks before locking composite:**
1. Enumerate all anchors within ±0.10 of the proposed composite.
2. If proposed value matches an existing anchor exactly: redial with explicit differentiation signal (one specific profile dimension justifying same-value-or-different).
3. If 3+ anchors cluster within 0.05: flag for cross-cluster redial — distribution density should reflect actual profile differences, not anchoring inertia.
4. State the differentiating signal from each adjacent anchor in the walkthrough (one sentence per anchor, not generic "comparable" framing).
**Why:** Anchor-clustering (a) wastes the two-decimal precision the scale delivers, (b) signals lazy calibration to consumers of ratings, and (c) compounds across sessions because each new evaluation anchors on the cluster. System integrity requires each placement be earned by specific profile data, not inherited from a recent comparator's value.
**How to apply:** During Skill 4 Step 5: (1) read profile signature — strength count, peak density, domain edges, trajectory, credentials, current-cycle health; (2) draft decimal placement from profile alone, NOT relative to a specific anchor; (3) THEN list all Tier-band anchors and check spread; (4) if clustering detected, redial with explicit differentiating signal documented in walkthrough.
**Applies to:** Skill 4 Step 5 decimal placement for all NBA-level evaluations. Critical for Tier 3–5 where active anchor density is highest, and for sequential evaluations of comparable-tier players.
**Status:** Active
**Applications:** 5 (S118 — Wemby/Giannis/KD full recalibration sweep producing 9.34 / 9.30 / 9.26 spread; S120 Haliburton — Tier 4 same-band re-confirmation case: anti-clustering check fired on existing 9.11 anchor vs Luka 9.07 in candidate band; differentiation signal documented [cleaner cognitive profile + elite ball security + 1 liability vs Luka's 2-3]; placement held at 9.11; check ran cleanly on a same-band re-confirmation case, distinct from S118's clustering-pattern case; S122 Jokić — Tier 2 anchor recalibration case: anti-clustering check fired on +0.06 revision to 9.64 vs only SGA 9.62 within ±0.10 in candidate band; differentiation signal documented [heavier credential basket 3× MVP + FMVP + ring vs SGA's 1× MVP balanced against SGA's age-27-ascending edge; +0.02 above SGA reflects resume edge dialed against profile density]; placement set at 9.64 with single-anchor differentiation — first sparse-band Tier 2 application of the protocol. **S124 backfill — entry was missing from S122 wrap; surfaced and routed at S124 wrap.**; S123 Curry — Tier 3 same-band re-confirmation case: anti-clustering check fired on existing 9.20 anchor vs KD 9.26 within ±0.10 (+0.06 above) and Hali 9.11 Tier-4-floor within ±0.10 (−0.09 below); differentiation signals documented per anchor [vs KD: KD 24 strengths + 7.2 defense + 7.2 athleticism + size > Curry 13 strengths + record-holding shooting + 4 rings + active recency; vs Hali: Curry 4 rings + 2 MVPs + FMVP > Hali no rings + healthy-state trajectory edge]; placement held at 9.20; check ran cleanly on a Tier 3 same-band re-confirmation, distinct from S118's clustering-pattern case. **S124 backfill — entry was missing from S123 wrap; surfaced and routed at S124 wrap.**; S124 Doncic — Tier 4 same-band re-confirmation case: anti-clustering check fired on existing 9.07 anchor vs only Hali 9.11 within ±0.10 in candidate band; differentiation signal documented [Hali's cleaner cognitive profile + elite ball security trumps Luka's denser overall strength count]; placement held at 9.07; check ran cleanly on third consecutive same-band re-confirmation case across Tier 2/3/4, validating S118-F01 protocol on Path D legacy-anchor refresh sequence)

---

### S111-F01 — Anchor-deflation pattern in comparison set compresses placement
**Status:** Superseded (promoted to COMPOSITE-SCALE-AND-TIERS.md Step 4 "Anchor-state correction" subsection, Session 114 2026-04-28)

Original entry archived at `docs/learnings/archive/S111-F01-archived.md`. Applied 3 times across S111-S113 — Edwards S111 firing case (composite correction 8.70 → 8.93), Cade S112 not-firing validation (deflation check applied, did not drive placement), Wembanyama S113 not-firing validation (Tier 3 anchors all healthy, deflation check non-firing). Discrimination clean across firing and not-firing cases; promotion threshold met per Workstream 2 retrospective.

---

### S102-F03 — Calibration-slot re-evals require full anchor-library cross-reference at pre-modifier stage
**Date:** 2026-04-24
**Severity:** Medium
**Context:** Bridges re-eval (S102) required three drafts to land correctly (7.62 → 7.75 → 7.85). The first draft validated the existing 7.62 anchor after a Hauser-focused comparison (Tyler's calibration hypothesis text was "Bridges > Hauser; 7.62 too low," which anchored my initial comparison set on Hauser 7.55 and Eason 7.58). This produced pre-modifier 7.72 and final 7.62 post-R13. Tyler pushed back: "do you really think Bridges is .30 below Smart? below Pritchard, Caruso, Jones?" — surfacing that my narrow comparison set had missed anchors in the Tier 8 middle band (Pritchard 7.72, Caruso 7.68, Jones 7.68, Claxton 7.68). Bridges's role-volume (82 GP starter on conference finalist, iron-man NBA minutes leader) objectively exceeded those specialist/bench peers. Second draft corrected to 7.75, third to 7.85 after fully weighing role volume + team context at pre-modifier stage.
**Learning:** For calibration-slot re-evals, run a **FULL anchor-library cross-reference sweep at the pre-modifier stage** before applying R13 Stage 2 or any composite modifiers. Specifically: identify the player's role-archetype profile (starter-on-contender / bench / specialist / primary-creator / secondary) and cross-reference against ALL anchors in the candidate tier band, not just archetype-peers or hypothesis-anchor. Role volume + team context is a legitimate pre-modifier differentiator that narrow comparisons can miss. If the hypothesis framing anchors on a specific player (e.g., "X > Y"), treat that as ONE reference point and expand the comparison set immediately.
**Why:** The hypothesis text in calibration-slot re-evals can bias the evaluator's comparison set anchoring. "Bridges > Hauser" naturally focused my comparison on Hauser-adjacent anchors, obscuring that Bridges's starter-on-contender role objectively exceeded the Tier 8 lower-middle specialist cluster. The full-sweep methodology prevents narrow-framing errors.
**How to apply:** At Skill 4 Step 4 for any calibration-slot re-eval: (1) list ALL anchors in the candidate tier band; (2) explicitly compare role-volume + team-context dimensions, not just archetype-peer comparisons; (3) position the player against the FULL distribution before applying Stage 2 modifier; (4) document the comparison in the walkthrough, including which anchors rank above/below and why.
**Applies to:** Skill 4 Step 4 anchor comparison, especially for calibration-slot re-evaluations where a hypothesis text frames the comparison. Does not apply to fresh evaluations (no hypothesis-anchor bias) or prospect evaluations (different comparison framework).
**Status:** Active
**Applications:** 2 (Bridges S102 — three-draft correction sequence 7.62 → 7.75 → 7.85; initial Hauser-focused comparison produced under-valued placement; full anchor-sweep produced correct placement. Embiid S110 — full Tier 6 cluster sweep from prior anchor 8.05; compared against AAB peers AD/KAT/Sengun + cross-archetype credential peer Harden + Tier 7 ceiling check Sabonis 8.22; full-sweep methodology produced 8.40 placement on first draft with no correction needed. Tyler endorsed: "precisely where I would have placed him." Pattern held — full sweep prevents under-anchoring on archetype-only comparison set.)

---

### S99-F02 — Archetype-migration drift is a distinct correction category from composite drift during anchor recalibration sweeps
**Date:** 2026-04-23
**Severity:** Medium
**Context:** S99 anchor recalibration sweep re-scored 6 anchors. Two of six required archetype migration: Jalen Williams (Offensive Engine → All-Around Guard, based on current value delivery as defense-plus-IQ two-way guard rather than primary scorer) and Amen Thompson (Dribble Pass Shoot Wing → Defensive Specialist Wing, based on non-shooter identity that the DPS tag requires). The initial drift-shortlist methodology used three filters (awards credential mismatch, trajectory divergence, R13 retrofit) — archetype-fit staleness was not in the filter set, yet it drove 2 of 6 material corrections. Without explicit archetype-fit check, these migrations would have been missed and the re-scored composites would have remained tagged with stale archetypes.
**Learning:** Anchor library drift sweep methodology must include an explicit archetype-fit check alongside composite-drift filters. For each drift-candidate anchor, ask: does the archetype tag still match current value delivery? Archetype staleness can be driven by (a) player role evolution (handle of ball, scoring pattern, defensive role all shift as players age or change teams) or (b) framework evolution (archetype definitions refine over time). Archetype migration corrections can be independent of composite movement — a player may stay at the same composite level with a better-fitting archetype, or shift composite AND archetype together. Neither should be assumed; both should be evaluated. Evidence from S99-F01 companion work: archetype migrations in S99 did not correlate one-to-one with composite moves (Jalen Williams moved both composite and archetype; Amen Thompson moved composite modestly but archetype materially).
**Applies to:** Skill 4 composite assignment workflow — specifically the drift-sweep methodology used during anchor library maintenance. Also relevant to any Skill 3 archetype identification step when re-scoring an existing anchor. **Scope extension (S102):** Also applies to expansion-slot candidate screening at batch-prep time — archetype-fit check before evaluation commits catches archetype misclassifications early. Validated on the Aaron Gordon case (S102 batch 2 prep): initial prep flagged Gordon as "Switchable Big" candidate but archetype-fit check surfaced that Gordon's profile (6'8", 235 lbs, defends 2-4 not 1-5) is Modern Four shape, not Switchable Big. Correction happened before any evaluation cycles burned.
**Status:** Active
**Applications:** 2 (S99 anchor recalibration sweep — 2 of 6 anchors had archetype migration: Jalen Williams, Amen Thompson; S102 batch prep — 1 case: Aaron Gordon misclassification caught pre-evaluation)

---

### S99-F01 — R13 Stage 2 is additive on credential-driven placement; strict convergence gate is protective against double-counting
**Status:** Superseded (promoted to SCORING-RULES.md R13 "Stage 2 application note — double-count protection" subsection, Session 99 2026-04-23)

Original entry archived at `docs/learnings/archive/S99-F01-archived.md`. Applied 6 times during S99 anchor recalibration sweep — Stage 2 did not fire in any case, validating the protective interpretation. Promoted to formal rule clarification after empirical pattern held across the sweep.

---

## ENTRY FORMAT

See SELF-LEARNING-PROTOCOL.md for the canonical entry format. Each
active learning must include: ID, Date, Severity, Context, Learning,
Applies to, Status, Applications.

---

*Created Session 94. Empty scaffold.*
