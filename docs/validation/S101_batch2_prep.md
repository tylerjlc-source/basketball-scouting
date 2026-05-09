# Session 101 → Batch 2 Prep (Wing/Big Scale Validation Sweep)

**Purpose:** Transition notes from batch 1 (complete at Kessler, S101) to batch 2. Authored at S101 close while batch 1 insights are fresh. Load at batch 2 session opener.

**Companion doc:** `docs/validation/S100_batch1_retrospective.md` (full batch 1 record).

---

## Sweep Status Entering Batch 2

| Group | Evaluated | Target | Remaining |
|---|---|---|---|
| Wings | 3 | 10–15 | 7–12 |
| Bigs | 1 | 10–15 | 9–14 |
| **Total batch-1 added** | **4** | | |

**Anchor library:** 100 (library milestone reached at Kessler S101).

---

## Batch 2 Candidate Shortlist

Session opener candidates, grouped by coverage priority.

### Bigs (priority — library has most gaps)

**Switchable Big** (currently in library: Wemby 9.14, Bam 8.84, JJJ 8.60, Holmgren 8.31, PJ Washington 7.62)
- **Aaron Gordon** — active switchable 4 on Denver contender; demonstrated playoff track record
- **Daniel Gafford** — younger switchable profile on Dallas

**Versatile Scoring Big** (currently in library: Valanciunas 7.05 as first current-tag VSB anchor post-S101 migration)
- **Domantas Sabonis** — high-usage scoring/passing big on Sacramento
- **Nikola Vučević** — shooting-adjacent veteran scoring big
- Valanciunas now clean-tagged (S101 migration) — usable as mid-tier VSB anchor reference in batch 2 comparisons

**Stretch Big** (currently in library: Markkanen 8.02, KAT 8.54 [All-Around], Naz Reid 7.65, Bobby Portis 7.62, Luke Kornet 6.90)
- Reasonable coverage; low priority unless a specific anchor gap surfaces

**Energy Big** (currently in library: Duren 8.30, Looney 7.10, Hayes 6.95, Achiuwa 6.88, Tshiebwe 5.85)
- Already well-populated; low priority

**All-Around Big** (currently in library: Jokic 9.58, KAT 8.54, Sengun 8.38, Embiid 8.05, AD 8.50)
- Mid-to-upper tier well-populated; batch 2 could add a mid-tier reference if one surfaces

**Rim Protector** (currently in library: Gobert 7.98, Kessler 7.87 NEW, Claxton 7.68, Mo Bamba 5.95, Moses Brown 5.88)
- Kessler filled the current-era mid-tier gap
- Lower priority for batch 2 unless a specific anchor gap surfaces

### Wings

**3-and-D Wing** (currently: Bridges 7.62, Anunoby 8.15, Eason 7.58 — Batum 6.85 migrated out to Secondary Playmaker S101)
- **Mikal Bridges re-eval** — Tyler S100 flag: "Bridges is superior to Hauser; if both anchor near 7.62, Bridges is underranked." Knowledge-calibration re-eval candidate.

**Modern Four** (currently: Giannis 9.40, Siakam 8.70, Barnes 8.40, Zion 8.08)
- **Scottie Barnes re-eval** — deferred from batch 1; archetype migration question (Modern Four / Defensive-Engine Playmaker / ?). Knowledge-calibration re-eval candidate.

**Dribble Pass Shoot Wing** (currently: Jalen Johnson 8.40 only)
- Expansion needed. No specific candidate flagged yet.

**Score-First Wing** (currently: Brown 8.83, Ingram 8.32)
- Tobias Harris, Rudy Gay mentioned at session opener as candidates.

**Defensive-Engine Playmaker** (currently: Draymond 8.00 only)
- Expansion needed. Thin archetype population limits re-eval comparison surface area.

### Knowledge-Calibration Budget (25% of sweep)

Reserved slots (2 confirmed):
1. **Scottie Barnes** — archetype migration question
2. **Mikal Bridges** — rank-too-low hypothesis

Neither runs in the same batch as a fresh first-time evaluation of the same archetype (avoid context bleed). Both are wing re-evals, compatible with mixed-composition batch 2.

---

## Recommended Priority Ordering for Batch 2 (non-prescriptive)

Reasoning: batch 1 was 3 wings + 1 big (Kessler). Batch 2 should emphasize Bigs (least-populated group) with room for the two flagged wing re-evals.

Suggested batch 2 composition (4 players):
1. **Switchable Big** — Aaron Gordon OR Daniel Gafford (validate Switchable Big scale + expand archetype population)
2. **Versatile Scoring Big** — Sabonis OR Vučević (validate Versatile Scoring Big scale + first current-tag anchor)
3. **Mikal Bridges re-eval** — knowledge-calibration slot 1 (test the rank-too-low hypothesis)
4. **Scottie Barnes re-eval** — knowledge-calibration slot 2 (resolve archetype migration question)

Alternative compositions are fine — Tyler to confirm at batch 2 session opener.

---

## Carryover Learnings (active for batch 2)

### From batch 1 (S100 + S101)
- **feedback_precision_full_range** — avoid .0/.5 defaults in sub-domain and composite scoring; use full .01-.09 range. Applied cleanly across all batch 1 players. Continue.
- **S96-F02** — R8 cross-reference cap override via direct empirical measurement. ~10 applications across batch 1; pattern robust. Continue.
- **S96-F04** — NBA-vet Comp + Projection adaptation. **Now formalized** at `NBA-COMP-METHODOLOGY.md § NBA-Vet Adaptation` and `PROJECTION-OUTPUT-BLOCK.md § State 4 Procedure`. Load from those docs at Skill 5, not from learnings.
- **S99-F02** — Anchor library drift sweeps include archetype-fit check. Relevant to Barnes and Bridges re-evals.
- **S100-F01** — eval_window GP aggregation bug + Playoff_Track_Record classification hint bug. Both trigger on specific cases (traded players; negative-delta playoff classification). Apply override discipline in research packet.

### Framework watchpoints for batch 2
- **POSITION_SCALE_BIGS_v1.md** — Kessler (Rim Protector) is the only big evaluated so far. Batch 2 tests Switchable Big, Versatile Scoring Big, and possibly others. Watch for:
  - Archetype Notes accuracy at cluster placements
  - Structural zero exclusion behavior per archetype (DOMAIN-SCORE-ROLE-RELEVANCE.md)
  - Any band language that surfaces as unclear or miscalibrated
- **S99 Shooting Specialist D2 watchpoint (from MEMORY.md):** Off-dribble and mid-range stay role-relevant for Shooting Specialists. Applies to wing Shooting Specialist archetype, not relevant unless a Shooting Specialist Wing is re-eval'd.
- **R13 Stage 2 strict-gate interpretation** — continue applying S99-F01 (now part of SCORING-RULES.md R13). Kessler didn't fire (below sample); batch 2 may surface new Stage 2 cases if players have active playoff resumes.

---

## Open Items to Resolve (not blocking batch 2, but worth clearing)

### Script maintenance session (independent of sweep)
1. **eval_window.py GP aggregation bug** — ~10 lines in script. Fix when a maintenance session is scheduled.
2. **Playoff_Track_Record.py classification hint** — negative delta should label "shrink"; sub-moderate magnitude should label "Neutral."

### Anchor library housekeeping
3. ~~Nicolas Batum archetype migration~~ — **CLOSED S101.** Migrated 3-and-D Wing → Secondary Playmaker per Davion Mitchell tag-only precedent. Composite 6.85 unchanged.
4. ~~Jonas Valanciunas archetype migration~~ — **CLOSED S101.** Migrated Post Scoring Big → Versatile Scoring Big per S48 merger rule. Composite 7.05 unchanged. Clears stale legacy tag before batch 2 VSB evaluations.

### Task 3 (P4 scaffold)
5. `docs/ARCHITECTURAL_PRINCIPLES.md` P4 ends with "Task 3 — not yet built." No change this session; awaiting a future session for dedicated build.

---

## What Batch 2 Should NOT Do

Guardrails to prevent scope creep:
- **Don't re-author position scales based on a single batch-2 player.** Scale revisions require multiple-player evidence convergence (per S97 build discipline).
- **Don't silently migrate anchor archetypes.** S97-F04 learning: flag drift for Tyler, don't edit silently.
- **Don't skip checkpoints.** S100 precedent: archetype confirmation, non-negotiables gate, composite placement, Skill 5 QC → Tyler eyes at each before proceeding.
- **Don't inflate composites.** Batch 1 discipline held (Hauser 7.55, Bogdan 6.85 both stayed honest despite archetype-first-anchor pressure). Continue.

---

*Authored S101 close. Load at batch 2 session opener for context carryover.*
