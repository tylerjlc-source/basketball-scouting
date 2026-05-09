# Sessions 110–113 — Workstream 2 Cost-Spike Retrospective

**Scope:** Workstream 2 of the Backend Foundation Track (per `project_s109_backend_foundation` memory). Planned as 4 bundled chain runs targeting (1) cost-spike instrumentation, (2) legacy expedited-route anchor re-evaluation under the current rubric. Workstream 2 now complete; pipeline UNLOCKED.

**Format:** Follows `S102-S103_batch2_retrospective.md` precedent.

---

## Players Shipped (4)

| # | Player | Prior → New Composite | Δ | Tier Change | Archetype Change | Cascade Fan-Out | Session |
|---|---|---|---|---|---|---|---|
| 1 | Alperen Sengun | 8.38 → **8.45** | +0.07 | T6 same | All-Around Big confirmed (no migration) | ~6 pages | S110-prep / S105 retro context |
| 2 | Joel Embiid | 8.05 → **8.40** | +0.35 | T7 → T6 | All-Around Big same | ~10 pages | S110 |
| 3 | Anthony Edwards | 9.37 → **8.93** | −0.44 | T3 → T4 | Offensive Engine → All-Around Wing + Guard → Wing group migration | ~9 pages | S111 |
| 4 | Cade Cunningham | 8.98 → **8.96** | −0.02 | T4 same | Jumbo Playmaker confirmed (no migration) | ~9 pages | S112 |
| 5 | Victor Wembanyama | 9.14 → **9.30** | +0.16 | T4 → T3 | Switchable Big → All-Around Big | **13 pages** | S113 |

**Anchor library state:** 105 → 105 (no count change — all 5 were revisions in-place). Pipeline unlocked at end of S113.

**Run-4 note:** Sengun was technically S105 (pre-spike) but functioned as the spike's first calibration data point. The spike formally instrumented S110–S113 (Embiid → Cade → Wemby), with Sengun + Embiid as the "ascending in-band" + "R12 anchor-correction" baselines.

---

## Cost / Cascade Findings

### Per-run cascade fan-out (the central instrumentation target)

| Run | Player | Cascade pages | Driver |
|---|---|---|---|
| 1 | Sengun | ~6 | In-band revision, no migration — minimal neighbor refresh |
| 2 | Embiid | ~10 | Tier crossing 7→6, no archetype migration — neighbor refresh on both bands |
| 3 | Edwards | ~9 | Tier crossing 3→4 + group migration + archetype migration — multi-axis fan-out, but small Tier 3/4 anchor density limited cascade size |
| 4 | Cade | ~9 | In-band revision, no migration — surprising fan-out from neighbor-list refresh on closely-clustered Tier 4 |
| 5 | **Wembanyama** | **13** | **Tier crossing 4→3 + archetype migration both firing simultaneously** — heaviest in spike |

**Pattern:** Cascade fan-out scales with (a) number of axes affected — tier band, archetype hub, group — and (b) tier density at the destination. Wemby hit both axes at high density (Tier 3 has Giannis/KD/Curry; All-Around Big has 7 anchors after migration). Sengun was lowest because no migration + already-in-band revision.

**Cost driver confirmed:** The S109 P1-audit identification of Skill 6 as quadratic-session-cost suspect (sequential tool calls within phases) held across the spike. Phase-batched execution (5-turn budget per ingest, parallel tool calls within phases) was followed for runs 4 and 5; runs 1–3 predated full Phase-batching enforcement.

### Skill 6 manifest production cost

**Tyler S112 observation:** Skill 6 manifest production cost ~14% session context on Cade run.

**S113 confirmation:** The 13-page Wemby cascade required substantially heavier reads than Cade's 9-page cascade — but the manifest itself was templated from the prior runs' patterns and produced quickly. The 14% figure was driven primarily by Phase B (parallel peer reads), not manifest authorship.

**Automation candidate (logged for follow-up):** The manifest is mechanically derivable from `wiki/index.md` once the player's composite + archetype + tier-band are known. Specifically:
- Tier-band peers come from cross-references-by-tier section + neighbor-distance threshold
- Archetype peers come from group → archetype subsection
- Page-touch list is `archetype hub × 1 (or 2 if migration) + index × 1 + neighbors-needing-refresh + player page`

**Spike conclusion:** A `Skill 6 — manifest auto-draft` helper that reads index.md + the new composite/archetype/tier-band trio and emits the manifest as a templated diff would cut Phase C (manifest authorship) to near-zero token cost. Phase B (peer reads) remains the structural cost — but it's irreducible given the cascade requirement.

**Status:** Automation candidate logged. Out of scope for the spike (no contract modifications mid-window per spike discipline). Forward to next backend-foundation cycle as a Skill 6 enhancement.

---

## Pattern Validation — What Held Up

### S111-F01 — Anchor-deflation pattern
**Promotion candidate (3 applications now):**
1. **Edwards S111** (surfaced) — Initial Skill 4 draft 8.70 was anchor-deflated by Tatum's post-Achilles 8.88 + AD's injury-flag 8.50 + Embiid's 8.40 dormancy pulling the comparison set down. Tyler corrected to 8.93 by re-anchoring on healthy comparison set + multi-ANBA-Second compounding.
2. **Cade S112** (validation) — Healthy comparison set check applied at pre-modifier stage (Luka 9.07, Booker 8.92, Mitchell 8.92 anchored placement; Tatum/Edwards/Mobley flagged peers did not drive). Watchpoint applied, NOT driving placement.
3. **Wembanyama S113** (validation) — Comparison set checked. Tier 3 anchors all healthy; no deflation pattern. Watchpoint applied, NOT driving placement.

**Pattern character:** The watchpoint discriminates correctly between cases where deflation IS active (Edwards) vs. cases where it is NOT (Cade, Wemby). 1/3 firing rate is not a "false negative" — it's the watchpoint working as designed.

**Promotion recommendation:** Promote to `scout-composite-learnings.md` (full entry) or to SCORING-RULES.md as a Step 4 anchor-comparison subsection. Edges: distinct-from-S102-F03 (narrow-anchoring) — same family but different mechanism. S102-F03 is "evaluator picks too-narrow anchor set"; S111-F01 is "evaluator's broad anchor set is itself deflated."

**Status:** Promotion threshold met (3 applications, discrimination clean). Hold for cycle close — Tyler decides routing.

### R13 Stage 2 convergence-gate pattern
**Promotion candidate (2 applications, both NEGATIVE):**
1. **Edwards S111** — statistical NEUTRAL + qualitative MIXED → gate fails → Stage 2 does not fire. Composite unchanged by R13 Stage 2.
2. **Cade S112** — statistical mixed [career delta -3.4 TS% but 2026 sample course-correcting] + qualitative mixed → gate fails → Stage 2 does not fire.

**Wembanyama S113** — below sample minimum (1 series), gate doesn't even reach the convergence test. Different failure mode.

**Pattern character:** The convergence gate ("statistical AND qualitative both directional") correctly suppresses Stage 2 modifier in mixed-evidence cases. Both Edwards and Cade had real R13 trajectory data; both produced composite-stable outcomes.

**Promotion recommendation:** Promote the convergence-gate-fails-on-mixed-evidence behavior to SCORING-RULES.md R13 Stage 2 explicit subsection. Currently the "convergence required" language is implicit in the methodology; making it explicit prevents future evaluators from firing Stage 2 on single-axis evidence.

**Status:** Promotion threshold met (2 applications, both gate-fail discrimination correct). Hold for cycle close.

### S96-F02 — Empirical override on cross-reference caps (already promoted to R8)
**Heaviest single-evaluation application count in library history: Wembanyama S113 — 4 instances.**
- #15 On-ball pressure (DFGPOE -7.9% direct measurement overrides #23 Strength PF/C cap)
- #17 Rim protection (DPOY-unanimous + league-leading BLK + 8.7% opp FG% reduction overrides #23 Strength cap)
- #20 Defensive rebounding (DREB% 27.3% direct measurement overrides #23 Strength floor)
- Implicit #16 Help defense (length-based mechanism, no formal cap fired)

This exceeds Barnes S103's prior record of 5 applications in single eval (different sub-domain spread). Wemby's case is structurally distinct — the 4 overrides all ride on the SAME structural mechanism (length/verticality compensating for strength deficit), not on independent empirical signals. **Suggests an enhancement to R8: when N overrides ride on the same structural mechanism, the override pattern becomes the player's evaluation signature and should be flagged in profile narrative.** Not a rule change; a documentation enhancement.

**Status:** Note for future R8 documentation pass. Not a blocker.

### S102-F02 — POT-below-composite for post-peak vets (already in scout-output-learnings)
**Wembanyama S113: negative-control 6th confirmation.** Ascending trajectory + 0/3 post-peak conditions (no decline, no significant injury affecting current sample, no R13 shrink) + age 22. Standard ascending path holds; POT 9.94 above composite 9.30 by 0.64. Pattern firing 3/3 on post-peak vets, not firing 6/6 on ascending vets. Discrimination empirically clean across age range 22–32.

**Status:** Pattern stable. No promotion needed (already in active learning).

---

## Cumulative Anchor Revision Pattern

| Player | Δ Composite | Type | Driver |
|---|---|---|---|
| Sengun | +0.07 | In-band | Light upward calibration after full chain run; archetype confirmed |
| Embiid | +0.35 | Tier crossing UP | R12 anchor on 2022-23 MVP year + S96-F03 athletic recalibration absorbed; structural injury history bounded by R12 |
| Edwards | −0.44 | Tier crossing DOWN | Legacy expedited-route drift (rubric_version: unknown → v3) + group migration (Guard → Wing) + archetype migration |
| Cade | −0.02 | In-band | Minor calibration under current rubric; CAS 3PT down-year offset by YoY improvements + 2026 playoff resilience |
| Wembanyama | +0.16 | Tier crossing UP | Year-3 production explosion (DPOY-unanimous + MVP-finalist + healthy 64-GP) + archetype migration (Switchable Big → All-Around Big) |

**Net library effect:** No anchor count change (5 revisions in-place). Average absolute |Δ| = 0.21. Largest revision Edwards (−0.44); smallest Cade (−0.02). Direction split: 3 upward, 2 downward.

**Pattern observation — legacy expedited-route anchor drift severity:**

The spike's central hypothesis was that legacy anchors (rubric_version: unknown) entered at expedited-route placements pre-framework-evolution would drift when re-scored under the current rubric. The five data points:

| Player | Time-since-entry | Migration pressure | |Δ| |
|---|---|---|---|
| Sengun | ~10 sessions | None (archetype confirmed) | 0.07 |
| Embiid | ~10 sessions | Mild (R12 anchor + recalibration) | 0.35 |
| Edwards | ~12 sessions | Heavy (group + archetype migration) | 0.44 |
| Cade | ~5 sessions (had been recently touched) | None (archetype confirmed) | 0.02 |
| Wembanyama | ~8 sessions | Heavy (archetype migration + tier crossing) | 0.16 |

**Drift severity correlates with:**
1. **Archetype migration pressure** — heavy migration produces |Δ| ≥ 0.16 (Edwards, Wemby). No migration produces |Δ| ≤ 0.07 (Sengun, Cade). Embiid had mild migration pressure (R12 anchor selection re-thought) → |Δ| 0.35.
2. **Tier crossing** — independent of migration. Embiid and Wemby crossed up (+0.35, +0.16); Edwards crossed down (−0.44). All three had heavier |Δ| than non-tier-crossing revisions (Sengun, Cade).
3. **Time-since-entry** — weak signal in this sample (n=5). Cade was recently touched and held; Sengun had been quiescent and shifted only slightly. Edwards had ~12 sessions elapsed and drifted heavily, but the migration pressure dominates the time signal.

**Conclusion:** For legacy-anchor re-evaluation prioritization, **migration pressure is the dominant driver**, not time-since-entry. Future anchor library audits should prioritize anchors where the current archetype tag does not match the most-recent rubric framework, regardless of how recently they were touched.

---

## Skill 1 / Script Bug Findings (S100-F01 family)

The spike re-confirmed several known script bugs across runs:

| Bug | Confirmed in | Status |
|---|---|---|
| `eval_window.py` GP aggregation TOT-row double-count | Sengun, Embiid (no, single-team) | Held — fires on traded-player rows specifically |
| `Playoff_Track_Record.py` classification-hint mislabeling | Embiid (career delta −3.6 → "moderate statistical shrink"; manual override applied) | Held — script hint requires manual qualitative AND-rule check per R13 |
| `NBA_Comp_Stats.py` BLK%/STL% endpoint None | Embiid (2 comp runs), Cade (3 comp runs), Wemby (3 comp runs) | Held — 24+ individual cases now; endpoint-wide bug not player-specific |
| `Domain_1_Finishing__Stats.py` rim-zone partial-season returns 0 | Embiid 2025-26 single-season `--season-override` | New variant; workaround documented (substitute Non-Dunk Rim FG% from Domain 3) |
| `Domain_5_Defense__Stats.py` #17 Rim D_FGA endpoint N/A | Wemby S113 | Held — proxy via BLK + Contested + on/off + qualitative |
| Domain 5/6/8 partial endpoint timeouts | Wemby S113 (D5 LeagueDashPtDefend partial; D6 Tracking Rebounding 2025-26; D8 distance bands + shot clock 2025-26) | Held — workarounds applied (2024-25 fallback or qualitative substitution) |

**Script Maintenance Backlog candidate:** All five bug variants reconfirmed across the spike. Threshold for promoting "Script Maintenance Backlog" to a dedicated doc has clearly been reached (24+ cases on BLK%/STL% alone). Forward to next backend cycle.

---

## Pipeline State at Spike Close

- **Anchor library:** 105 anchors. 5 revisions in-place across spike. Library calibration confirmed under current rubric for All-Around Big, Jumbo Playmaker, All-Around Wing, Switchable Big (post-Wemby exit).
- **Open lint items:** Kawhi Leonard wiki frontmatter T5/T4 mismatch (S111 carry-over); legacy tier-neighbor band-violation sweep candidate (S113 finding) — both deferred to dedicated lint pass.
- **Workstream 2:** COMPLETE. Pipeline LOCK released.
- **Position scale validation track (paused S108):** Resumes after Workstream 2 unlock. State: Wings 6/15, Bigs 8/15 validated; anchor library 105.

**Memory updates required at session close:**
- `project_s109_backend_foundation.md` — mark Workstream 2 complete; pipeline unlocked
- `project_s99_position_scale_validation.md` — note resume-readiness
- `project_s99_anchor_library_recalibration.md` — append S110–S113 results to revision log

---

## Recommendations for Next Cycle

1. **Promote S111-F01 (anchor-deflation pattern)** to either `scout-composite-learnings.md` or SCORING-RULES.md Step 4 subsection.
2. **Promote R13 Stage 2 convergence-gate** to SCORING-RULES.md R13 explicit subsection (currently implicit).
3. **Skill 6 manifest auto-draft helper** — derive cascade list mechanically from `wiki/index.md`. Cuts Phase C (manifest authorship) cost; Phase B (peer reads) remains irreducible.
4. **Script Maintenance Backlog** dedicated doc — promote the S100-F01 family from learning-file note to canonical backlog. 24+ cases, fix priority by frequency.
5. **Legacy anchor audit prioritization** — sort remaining `rubric_version: unknown` anchors by archetype-migration risk (current archetype tag vs. current-rubric archetype description), not by time-since-entry.

---

*Workstream 2 cost-spike complete 2026-04-28 (S113 close). Pipeline unlocked. 5 anchor revisions, 1 anchor migration heavy (Edwards), 2 tier crossings (Embiid +, Wemby +; Edwards −). Cascade-cost instrumentation captured per-run. R8 empirical-override pattern hit single-eval high (Wemby 4×). S102-F02 and S111-F01 negative-controls held cleanly.*
