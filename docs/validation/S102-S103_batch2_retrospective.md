# Session 102–103 — Batch 2 Retrospective (Wing/Big Scale Validation Sweep)

**Scope:** Batch 2 of the position scale validation sweep. Planned as 4 player evaluations; split across S102 (3 players: Mobley, Sabonis, Bridges re-eval) and S103 (Barnes re-eval). Batch 2 now complete.

**Format:** Follows `S100_batch1_retrospective.md` precedent.

---

## Players Shipped (4)

| # | Player | Composite | Tier | Archetype | Library Status | Session |
|---|---|---|---|---|---|---|
| 1 | Evan Mobley | 8.67 | 5 middle | Switchable Big | **First Tier 5 Switchable Big anchor since initial library construction**; fills Bam 8.84 / JJJ 8.60 gap | S102 |
| 2 | Domantas Sabonis | 8.22 | 7 upper | Versatile Scoring Big | **First current-tag VSB anchor with credentialed Tier 6-level production; library's first NBA-vet anchor with active non-negotiable cap** (#17 Rim 4.7 fails C gate) | S102 |
| 3 | Mikal Bridges (re-eval) | 7.62 → **7.85** | 8 upper | 3-and-D Wing | **First library re-eval requiring multi-draft upward correction** (7.62 → 7.75 → 7.85 sequence) | S102 |
| 4 | Scottie Barnes (re-eval) | 8.40 → **8.55** | 6 upper | Modern Four → **Defensive-Engine Playmaker** | **Second Directional Rise R13 application in library** (after Mobley S102); archetype migration confirmed | S103 |

**Anchor library growth:** 100 → **102** (+2 additions; +2 revisions in-place). Library remains at 102 — batch 2 added less than batch 1 because 2 of 4 slots were re-evals.

**Knowledge-calibration budget used:** 2 of 4 slots (Bridges + Barnes) = 50% of batch, exceeding the 25%-of-sweep target for this specific batch. 2/2 hypotheses confirmed — both re-evals produced material corrections (Bridges +0.23 composite; Barnes +0.15 composite + archetype migration).

---

## Framework Validation — What Held Up

### Position Scale WINGS (S97-authored, continued validation)
- **Two additional archetypes scored cleanly** against POSITION_SCALE_WINGS_v1.md: 3-and-D Wing (Bridges re-eval) and Defensive-Engine Playmaker (Barnes re-eval).
- **No scale revisions required** from batch 2 wing evaluations.
- **Cumulative wing archetype validation (batch 1 + batch 2):** 3-and-some-D, Secondary Playmaker, Shooting Specialist, 3-and-D Wing, Defensive-Engine Playmaker — 5 of 10 wing archetypes scored cleanly. No scale revisions triggered across any of the 5.

### Position Scale BIGS (S97-authored, continued validation)
- **Two additional big archetypes scored cleanly** against POSITION_SCALE_BIGS_v1.md: Switchable Big (Mobley) and Versatile Scoring Big (Sabonis).
- **Efficiency-outlier observation surfaced at Sabonis:** 65.5% TS at 21.3% USG is anomalous for VSB archetype peers (both Vucevic 🔴 and Cousins 🔴 failed primary TS% tolerance). **Scale itself not revised**; anomaly flagged for monitoring if pattern repeats.
- **Cumulative big archetype validation (batch 1 + batch 2):** Rim Protector, Switchable Big, Versatile Scoring Big — 3 of 6 big archetypes. No scale revisions required.

### R8 Direct Empirical Measurement Override (S96-F02 promoted S102)
- **S102 promotion to SCORING-RULES.md R8 subsection validated across batch 2.**
- Application count: Mobley 4x + Sabonis 2x + Bridges 4x + **Barnes 5x** = **15 applications** across batch 2 alone.
- Barnes case is the **highest single-evaluation application count** to date — override fired on #6, #13, #15, #17, #20 (mid-range, pass execution, on-ball, rim protection, DREB all exceeded their cross-reference caps per direct empirical measurement). Pattern held cleanly; no over-application or composite inflation observed.

### S102-F03 Full Anchor-Library Cross-Reference Methodology (NEW, promoted during batch 2)
- Pattern **surfaced at Bridges S102** (three-draft correction 7.62 → 7.75 → 7.85 triggered by Tyler pushback on narrow Hauser-focused anchor set).
- **Applied cleanly at Barnes S103** as the calibration-slot re-eval methodology. Full Tier 5 + Tier 6 wing/big anchor sweep performed at pre-modifier stage; no hypothesis-anchor bias; pre-modifier 8.50 placement defensible against all in-band anchors with role-volume + team-context differentiation.
- **Validation count:** 2 applications (Bridges surfaced, Barnes confirmed). Pattern holds — methodology works as designed.

### R13 Stage 2 Playoff Modifier System
- **Full magnitude spectrum exercised across batch 2:**
  - Mobley: Directional Rise +0.05 (first Directional in library)
  - Sabonis: Historical-only + Strong Shrink Stage 2 skipped → Stage 1 POT −0.40 full magnitude
  - Bridges: Moderate Shrink −0.10
  - Barnes: Directional Rise +0.05 (second Directional in library)
- **Classification discipline held:** Barnes' +3.4 career TS% on 7 playoff games could have argued Moderate magnitude, but sample-size discipline (per Mobley precedent) kept it at Directional.
- **Stage 1/Stage 2 interaction confirmed:** Sabonis historical-only triggered Stage 2 skip + Stage 1 full magnitude (not tier-reduced); distinct from active cases where both stages fire at partial magnitude.
- **S99-F01 double-count protection** did not surface a false positive in batch 2 — the gate correctly suppressed Stage 2 on stat/qualitative divergence (none of the batch 2 cases presented that divergence).

### S102-F02 POT-Below-Composite for Post-Peak Vets (NEW, S102)
- **Surfaced at Sabonis** (POT 7.60 vs composite 8.22 — post-peak age-29 with documented injury + team rebuild + R13 shrink absorption).
- **Did not fire at Barnes** (ascending trajectory disqualifies the pattern — S102-F02 explicitly excludes "NBA vets still on ascending trajectory"). Pattern scope held cleanly.

### S96-F04 NBA-Vet Comp Adaptation (PROMOTED S101)
- **Applied on all 4 batch-2 evaluations** at Skill 5 Section 10.
- Age-comparable seasons used throughout: Bam age-24 + JJJ age-23 (Mobley); Vucevic age-28 + Cousins age-27 (Sabonis, both 🔴 — efficiency outlier); Anunoby age-28 + DFS age-28 (Bridges); **Iguodala age-24 + Draymond age-24 (Barnes)**.
- Formal-rule placement in NBA-COMP-METHODOLOGY.md + PROJECTION-OUTPUT-BLOCK.md held cleanly — no procedural surprises.

### Non-negotiables Gate
- **First NBA-vet anchor with active non-negotiable cap added at Sabonis** (S102). #17 Rim 4.7 fails C gate (5.0 threshold); cap binds composite to upper Tier 7 despite credential stack arguing Tier 6 floor.
- **Gate held as designed** — cap was not suspended (Sabonis is 29, past the 17-19 / 20-22 override age bands).
- Barnes cleared every frontcourt gate (SF + PF + C) with 4.5+ margin. Most gate-cleared anchor in batch 2.

---

## Bugs Surfaced

### S100-F01 Extended — NBA_Comp_Stats.py BLK%/STL% endpoint returns None (NEW S102 addition)
**Pattern:** Endpoint-wide issue, not player-specific. Appeared across all 6 comp candidates queried in S102 (Mobley + Bam + JJJ + Vucevic + Cousins + Sabonis) and both Barnes comps in S103 (Draymond + Iguodala).

**Total occurrences in batch 2:** 8+ cases (6 S102 + 2 S103).

**Impact:** Cosmetic — override at Skill 5 level (proceed with primary TS% + available secondaries per S100-F01 extension). Does NOT fail comps to 🔴 Rubric-only on endpoint quirk alone. Documented transparently in comp flags.

**Action:** Fix in scripts-maintenance session. Likely same endpoint-quirk family as existing STL% None cases; may be shared root cause.

### S100-F01 — eval_window.py GP aggregation + Playoff_Track_Record.py classification hint
**Status:** Both active from batch 1. Did not surface new cases in batch 2 (Barnes was single-team throughout eval window; other 3 batch-2 players also single-team in window).
- Mobley Playoff_Track_Record classification hint surfaced a thin-magnitude labeling case (+0.5 TS% → "moderate statistical rise" which should be Neutral). Confirms classification-hint logic still buggy. Bug application count now **2 confirmed cases** (Anderson batch 1 + Mobley batch 2).
- **Barnes Playoff_Track_Record hint was accurate** (+3.4 TS% → "strong statistical rise" — classification matched manual check). This shows the bug doesn't fire universally; it's a magnitude-based misclassification, not a wholesale failure. The threshold logic is the issue, not the basic direction.

**Action:** All three S100-F01 bugs remain open for a scripts-maintenance session. Consolidated fix-list now spans eval_window.py (GP aggregation), Playoff_Track_Record.py (classification threshold), NBA_Comp_Stats.py (BLK%/STL% endpoint nulls).

---

## Methodology Learnings Promoted Through Batch 2

### S102 rule-doc updates (formalized during batch 2)
1. **SCORING-RULES.md R8 — Direct empirical measurement override subsection added** (S96-F02 promoted). Applied 15 times across batch 2. Pattern held.
2. **Archive:** `docs/learnings/archive/S96-F02-archived.md` created.

### S102 learnings promoted to active scope
1. **S102-F02** (scout-output-learnings.md) — POT below composite for post-peak NBA vets.
2. **S102-F03** (scout-composite-learnings.md) — Full anchor-library cross-reference at pre-modifier stage for calibration-slot re-evals.

Both validated in batch 2:
- S102-F02 did not falsely fire on Barnes (ascending trajectory correctly disqualified).
- S102-F03 applied cleanly at Barnes S103 re-eval.

---

## Knowledge-Calibration Hypothesis Tracking (NEW OBSERVATION)

**Pattern across batch 2:** 2/2 Tyler-flagged knowledge-calibration re-evals confirmed their hypothesis text and produced material corrections.

| Re-eval | Hypothesis text | Confirmed? | Correction |
|---|---|---|---|
| Bridges (S102) | "Bridges > Hauser; 7.62 too low" | YES | +0.23 composite (7.62 → 7.85); exposed narrow-comparison bias, produced S102-F03 methodology |
| Barnes (S103) | "Modern Four vs DEP archetype migration question" | YES | +0.15 composite (8.40 → 8.55) + archetype migration Modern Four → DEP |

**Implication:** Knowledge-calibration budget is well-spent. Batch 2's 2/2 accuracy rate plus the compounding cost of pure-expansion-only sweeps (delays correcting known library errors while the subject pool is still tight) supports dropping the 25%-of-sweep cap. Re-evals and fresh expansion mix at batch-prep time based on what's live — no hard ratio. Expansion remains the long-term engine; over-indexing on re-evals stays a drift risk and is self-correcting via batch-prep review.

**Rule change (S104):** 25%-of-sweep cap on knowledge-calibration re-evals dropped. Allocation set per-batch based on active hypotheses and library state.

---

## DEP Archetype — Structural Observation

Barnes' DEP evaluation surfaced a **same-archetype comp-thinning issue:** ARCHETYPE-WEIGHTS-WINGS.md lists 3 confirmed DEP fits (Draymond, Iguodala, Barnes). With Barnes as the subject, only 2 external comps available. No third same-archetype comp option.

**Resolution in-session:** Two-comp set accepted (Iguodala 🟢 Full + Draymond 🟡 Partial). Section 10 spec allows 2-3 comps (2 is minimum). Noted in deliverable that the archetype has only 2 non-subject confirmed fits.

**Future implication:** The next DEP evaluation (if one occurs) will face the same 2-comp constraint. The archetype note already states "Historically rare archetype — 3 validation players reflects reality, not a research gap" — so comp-thinning is expected. No action required, but worth noting for future DEP evaluations.

---

## Carry-forward for Next Batch (Batch 3)

Batch 3 kickoff framing (from S103 session opener):

### Sweep status after batch 2
- **Wings evaluated: 5** (Bogdanović, Anderson, Hauser, Bridges, Barnes — 3-and-some-D, Secondary Playmaker, Shooting Specialist, 3-and-D Wing, Defensive-Engine Playmaker)
- **Wings remaining to hit 10–15 target: 5–10**
- **Bigs evaluated: 3** (Kessler, Mobley, Sabonis — Rim Protector, Switchable Big, Versatile Scoring Big)
- **Bigs remaining to hit 10–15 target: 7–12**
- **Anchor library: 102**

### Wing archetype coverage state (post-batch-2)
- 3-and-some-D Wing: Bogdan (anchor)
- Secondary Playmaker: Anderson (anchor)
- Shooting Specialist (Wing): Hauser (2nd active vet)
- 3-and-D Wing: Bridges re-evaluated (primary anchor)
- Defensive-Engine Playmaker: Barnes re-evaluated (2nd DEP anchor alongside Draymond)
- **Remaining wing archetype gaps:** All-Around Wing (beyond Leonard/PG/Brown — beyond-current-anchors coverage), Score-First Wing (beyond Ingram/Brown), Dribble Pass Shoot Wing (beyond JJohnson/Ingram), Modern Four (beyond Siakam/Zion; Barnes now DEP not Modern Four), Defensive Specialist (beyond Thompson/Okogie)

### Big archetype coverage state (post-batch-2)
- Rim Protector: Kessler 7.87 (first current-era mid-tier)
- Switchable Big: Mobley 8.67 (first Tier 5 since initial construction)
- Versatile Scoring Big: Sabonis 8.22 (first current-tag; Valanciunas 7.05 migrated in from Post Scoring Big at S101)
- **Remaining big archetype gaps:** Stretch Big (Markkanen recheck vs Naz Reid comparison), All-Around Big (Sengun deep dive + possibly Vucevic as fresh current-tag VSB), Energy Big (Duren recheck or fresh candidate)

### Batch 3 candidate order (set at S104 open)
- Vucevic (fresh — Versatile Scoring Big, current-tag expansion)
- Naz Reid (fresh — Stretch Big, fills Markkanen comparison gap)
- Sengun (re-eval — All-Around Big, rising credentials deep-dive)
- Wings TBD after Bigs trio

### Knowledge-calibration / expansion allocation
25%-cap rule dropped at S104. Allocation set per-batch based on active hypotheses and library state. Default remains expansion-weighted; re-evals surface when Tyler flags a hypothesis worth testing.

---

## Open Items Carried Forward to Future Sessions

1. **Script maintenance backlog (S100-F01 family):**
   - eval_window.py GP aggregation (traded-player row filtering)
   - Playoff_Track_Record.py classification-hint threshold logic
   - NBA_Comp_Stats.py BLK%/STL% endpoint None handling
   All three cosmetic; all three documented; all three require maintenance session.

2. **Task 3 P4 scaffold** — ARCHITECTURAL_PRINCIPLES.md P4 line "Task 3 — not yet built" still open. Dedicated session required.

3. **VSB archetype efficiency-outlier monitoring** — Sabonis's 2024-25 profile was anomalous for VSB peers. If another modern VSB surfaces with similar outlier efficiency, might warrant finer archetype distinction (currently scoped as monitoring note only).

4. **Remaining wing/big archetype coverage** — 5 wing archetypes + 3 big archetypes still need validation for full position scale validation.

---

## Memory Artifacts Updated (Batches 2 Cumulative)

### During S102:
- `docs/SCORING-RULES.md` — R8 Direct empirical measurement override subsection added
- `docs/learnings/archive/S96-F02-archived.md` — NEW archive
- `docs/learnings/scout-scoring-learnings.md` — S96-F02 marked superseded with pointer
- `docs/learnings/scout-output-learnings.md` — S102-F02 added (POT below composite)
- `docs/learnings/scout-composite-learnings.md` — S102-F03 added (full anchor sweep)
- `docs/learnings/scout-research-learnings.md` — S100-F01 extended (NBA_Comp_Stats BLK%)
- `ANCHOR-LIBRARY.md` — 2 entries added (Mobley, Sabonis) + 1 revision (Bridges); session history appended for each

### During S103:
- `ANCHOR-LIBRARY.md` — 1 revision (Barnes 8.40 → 8.55, Modern Four → DEP); session history appended; stamp updated to Session 103
- No learning-file updates triggered (all methodology patterns already formalized in S102)
- No memory file updates triggered (no new durable user/feedback/project findings)

### Batch 2 formal-rule-document changes (total)
- SCORING-RULES.md: 1 subsection added (R8)
- Archive: 1 file created (S96-F02)
- Skill-learnings files: 3 updated (S102-F02, S102-F03, S100-F01 extended)

---

## Session Close Notes

**S102 close (batch 2 partial):** Mobley + Sabonis + Bridges shipped. S96-F02 promoted to R8 formal subsection. Barnes re-eval deferred to S103.

**S103 close (batch 2 completion):**
- Barnes re-eval completed cleanly with archetype migration.
- S102-F03 methodology applied successfully at second test case.
- Library at 102 anchors, no additions.
- No rule documents modified; only anchor library.
- All session-end routing completed (see `MEMORY.md` index for any new entries).

**Batch 2 overall:** 4 of 4 slots filled. 5 of 10 wing archetypes validated, 3 of 6 big archetypes validated. Position scale documents hold as designed — no revisions required. Knowledge-calibration hypothesis accuracy 2/2 (ROI strong).

---

*Authored at S103 close. Follows S100 batch 1 retrospective format. Batch 3 prep artifact to be authored at next session start.*
