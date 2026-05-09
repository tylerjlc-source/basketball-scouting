# NBA PROJECTION OUTPUT BLOCK
**Loaded conditionally — used in place of PROJECTION-OUTPUT-BLOCK.md when subject is an NBA vet (≥25 NBA games played).**
**Part of Skill 5 (scout-output). Load alongside SKILL.md for NBA vet evaluations.**
**All values composite-scale (1.00–9.99). POT scale unified with composite scale Session 98.**

---

## OVERVIEW

The NBA Projection Output Block produces career-arc projection for an NBA vet — a player with ≥25 NBA games of observed evidence. It replaces the prospect projection logic, which is calibrated for players with no observed NBA data and produces inflated ceilings when applied to vets (S119 diagnosis: Maxey at composite 8.66 → prospect-path POT 9.30 vs. narrative-stated ceiling 8.70–8.92).

**Eligibility:** Subject must have played ≥25 NBA games (cumulative regular and postseason). Players below the 25-game threshold use PROJECTION-OUTPUT-BLOCK.md (prospect logic) regardless of NBA experience. Threshold gives ~1/3 of a season of observed sample — enough for trajectory and demonstrated-peak signals to form. Below it, draft-prior probabilities outperform thin observed data.

**Core discipline:** POT is anchored empirically to the realistic ceiling band named in the scouting narrative, not derived from `composite + modifier stack`. The evaluator names 2–3 ceiling anchors from the library, places POT inside that band, and justifies the position with career stage, trajectory, and skill-gap caps.

Five inputs in sequence:
1. Career stage assignment
2. Trajectory flag
3. POT placement (anchor-based)
4. Min / Max spread (asymmetric, age-compressed)
5. Output format

No Bust/Avg/Boom distribution — observed career data replaces probabilistic outcome modeling.

---

## STEP 1 — CAREER STAGE

Assign one stage based on age and NBA experience. Stage governs available POT growth and Min/Max spread shape.

| Stage | Age | NBA experience | Available growth |
|---|---|---|---|
| Pre-peak ascending | ≤24 | ≤3 seasons | Significant — composite is rising, peak not reached |
| Approaching peak | 24–27 | 3–7 seasons | Moderate — peak window opening, leap years possible |
| Peak | 27–30 | 5–10 seasons | Small — established level, marginal upside |
| Post-peak | 30–33 | 8–13 seasons | None to negative — POT ≤ demonstrated peak, decline likely |
| Late career | 33+ | 12+ seasons | Negative — POT typically ≤ current composite |

Tie-breaker: when age and experience suggest different stages, weight by the dominant signal. Bigs may peak slightly later (28–31) — apply judgment within ±2 years of band edges.

---

## STEP 2 — TRAJECTORY FLAG

Assign one flag based on observed trajectory in the last 1–2 seasons. The flag commits the evaluator to a direction and constrains POT placement within the anchor band.

| Flag | Definition | POT placement effect |
|---|---|---|
| Ascending | Leap year or sustained multi-year improvement; on track to exceed prior peak | Upper third of anchor band |
| Plateau | Established level; no meaningful trend either direction | Middle of anchor band |
| Declining | Observed regression in last 1–2 seasons against prior peak | Lower third of anchor band; at or below demonstrated peak |
| Recovering | Returning from major injury or off-court issue; trajectory provisional | At demonstrated peak; spread auto-Wide |

Trajectory must be supported by either statistical signal (composite or peak-stat trend) or qualitative signal (multi-source documentation of leap, plateau, or regression). Evidence cited inline in the trajectory note.

**Recovering-vs-Plateau distinguishing test.** When the current-window signal is dominated by injury cluster (chronic) or season-ending acute event, prefer Recovering. Distinguishing question: does the current-window signal read as recovery ramp or as skill regression / role decline? Recovery ramp → Recovering; skill regression → Plateau / Declining. Applies across Post-peak / Peak / Late career stages with active acute injury or chronic-injury-cluster events.

---

## STEP 3 — POT (anchor-based)

POT is the realistic career ceiling — the level the player most likely reaches at peak.

**Step 3.1 — Demonstrated peak floor.**
POT cannot fall below the player's best observed season composite (current or prior anchor-library entry, whichever is higher). For players whose peak season was not formally evaluated, estimate from accolades (aligned to composite tier table):

| Accolade level | Composite |
|---|---|
| Perennial All-NBA 1st (MVP territory) | 9.20+ |
| Multi-time All-NBA (any team) | 8.90–9.19 |
| Single-season All-NBA 1st | 8.85–9.05 |
| Single-season All-NBA 2nd / 3rd | 8.70–8.89 |
| Perennial All-Star starter | 8.60–8.79 |
| All-Star starter (single season) | 8.50–8.69 |
| All-Star reserve | 8.30–8.49 |
| All-Rookie / quality starter | 7.50–8.29 |

**Step 3.2 — Ceiling anchor band.**
Name 2–3 anchors from ANCHOR-LIBRARY.md that define the realistic ceiling band. Anchors must:
- Share archetype, or share group at minimum
- Represent realistic peak career outcomes the player could plausibly reach (not aspirational reaches — generational outliers are not valid ceiling anchors for a non-generational profile)
- Be supported by the scouting narrative — narrative names the ceiling neighborhood, anchors instantiate it

Ceiling anchors are distinct from composite anchors: composite anchors place the player at *current* level (Section 8); ceiling anchors define *where the player can go*. The two sets may overlap but serve different purposes.

The anchor band runs from the lowest to the highest of the named anchors. Example: Brunson 8.70 / Mitchell 8.92 / Booker 8.92 → band 8.70–8.92.

**Step 3.3 — Place POT in band.**
Position within the anchor band per the Step 2 trajectory flag. Skill-gap caps (Step 3.4) constrain upward drift.

**Step 3.4 — Skill-gap cap check.**
Name the structural ceiling bounds the narrative identifies (e.g., Maxey's half-court pull-up, conservative passing, 6'2" defensive structure). When skill caps bound the realistic outcome, POT does not drift to the top of the anchor band — it lands where the cap allows. List skill caps explicitly in the output.

**Step 3.5 — R13 Stage 1 playoff modifier.**

| Signal | POT modifier |
|---|---|
| Strong playoff rise | +0.40 |
| Moderate playoff rise | +0.20 |
| Moderate playoff shrink | −0.20 |
| Strong playoff shrink | −0.40 |

Per SCORING-RULES.md R13. R13 stacks on top of anchor placement. **Double-count guard:** if the named ceiling anchors already embody the playoff signal (e.g., Brunson is a Clutch POTY winner; an anchor band of FMVP-pedigree wings), evaluator must justify why R13 isn't already baked into the anchor selection — or reduce the modifier accordingly. **Default operationalization is to halve the magnitude (±0.40 → ±0.20, ±0.20 → ±0.10) — applies to both positive and negative R13.**

**Hard cap: POT ≤ 9.99.**

**Step 3.6 — Cap-floor coincidence (Post-peak / Late career).**
When career stage has Validation Check #2 cap = DEP + 0 (Post-peak / Late career), the cap (from above) and the Step 3.1 floor (from below) converge at exactly DEP. POT collapses to DEP regardless of trajectory placement OR R13 sign. Trajectory and R13 walkthrough still surface evidence cites but do not move the number.

Recovering trajectory adds a third pin: F9 Recovering rule directly pins POT at DEP via "at demonstrated peak." Triple convergence (cap + floor + Recovering rule) confirms POT = DEP.

**No-anchor fallback:**
When no library anchor cleanly bounds the ceiling, default to demonstrated peak + career-stage modifier:

| Stage | Modifier on demonstrated peak |
|---|---|
| Pre-peak ascending | +0.30 to +0.60 |
| Approaching peak | +0.10 to +0.30 |
| Peak | 0 to +0.10 |
| Post-peak | −0.10 to −0.30 |
| Late career | −0.20 to −0.50 |

**Firing conditions (any one suffices):**
1. **Generational outlier** — same-archetype peers above current are all generational-tier (Wemby/Jokić/Kareem-class); not aspirational ceilings for non-generational profiles
2. **Skill-separation lacks** — same-archetype peers above carry skill or structural separation the target lacks (defensive identity, playmaking shape, primary-handler primacy)
3. **Younger-active exclusion** — for Late career vets, same-archetype peers above are younger-ascending and the target structurally cannot out-ascend them
4. **Library exhausted above DEP** — at top-of-active-library altitudes, only retired era-defining outliers exist above DEP (Tier 2 / top-of-library cases)

---

## STEP 4 — MIN / MAX SPREAD

Min and Max anchor separately. Asymmetric anchoring reflects that vet uncertainty is directional: ascending vets carry upside without symmetric downside; declining vets carry downside without symmetric upside.

**Max — ceiling outcome (everything breaks right):**

Max = top of anchor band + stage buffer:

| Stage | Max buffer above top of anchor band |
|---|---|
| Pre-peak ascending | +0.20 to +0.40 |
| Approaching peak | +0.10 to +0.30 |
| Peak | +0.05 to +0.15 |
| Post-peak | 0 to +0.10 |
| Late career | 0 |

**Hard cap:** Max cannot cross into a composite tier the scouting narrative explicitly rules out (e.g., "never an MVP" → Max < 9.20).

**Min — floor outcome (trajectory fails):**

Min = current composite − trajectory adjustment − risk modifiers:

| Trajectory | Trajectory adjustment |
|---|---|
| Ascending | −0.10 to −0.30 (leap doesn't hold, regression to prior level) |
| Plateau | −0.20 to −0.40 |
| Declining | −0.40 to −0.60 |
| Recovering | −0.30 to −0.50 (spread auto-Wide) |

**Risk modifiers (pull Min only):**

| Driver | Min adjustment |
|---|---|
| Significant injury history (chronic or active) | −0.20 to −0.40 |
| Age-related decline acceleration risk | −0.10 to −0.30 |
| Off-court / multi-source character risk | −0.20 to −0.40 |
| Role / team fit risk (specific situational) | −0.10 to −0.20 |

**Confidence tier:**
- **Tight** — established profile, multi-source confirmation, peak or post-peak vet
- **Moderate** — pre-peak vet still consolidating, or established vet with one ambiguous signal
- **Wide** — Recovering trajectory, dramatic role change, or recent trade to incompatible system

Confidence widens trajectory adjustment and Max buffer by one tier when applicable.

---

## STEP 5 — OUTPUT FORMAT

```
--- NBA PROJECTION OUTPUT BLOCK ---
CAREER STAGE:           [Pre-peak ascending | Approaching peak | Peak | Post-peak | Late career]
TRAJECTORY:             [Ascending | Plateau | Declining | Recovering] — one line evidence cite

DEMONSTRATED PEAK:      [X.XX (composite) | qualitative — e.g. "All-NBA 2nd 2024-25"]
CEILING ANCHORS:        [Anchor 1 (X.XX), Anchor 2 (X.XX), Anchor 3 (X.XX)] — band X.XX–X.XX
SKILL-GAP CAPS:         [list named structural ceiling bounds, or "none identified"]
R13 STAGE 1:            [+0.40 | +0.20 | 0 | −0.20 | −0.40] — playoff signal cite

CURRENT (composite):    [X.XX]
POT:                    [X.XX]
Min:                    [X.XX]
Max:                    [X.XX]

Confidence:             [tight | moderate | wide]
Spread note:            [one line — what Min and Max represent for this vet]
Trajectory note:        [one line — what the trajectory flag commits to and the evidence behind it]
```

---

## INTERACTION WITH PROJECTION-OUTPUT-BLOCK.md

This doc replaces State 4 (NBA vet) handling in PROJECTION-OUTPUT-BLOCK.md. The existing doc retains prospect logic (States 1–3) only.

When the subject is an NBA vet (≥25 NBA games played):
- Skill 5 loads NBA-PROJECTION-OUTPUT-BLOCK.md instead of PROJECTION-OUTPUT-BLOCK.md
- The existing doc's State 4 references and no-slot path remove

CLAUDE.md routing and skills/scout-output.md loading instructions update in step.

---

## VALIDATION CHECK

Before finalizing the output, confirm:

1. **POT lands inside the named anchor band** — if outside, justify in the trajectory note (typically only ascending pre-peak with no skill caps, or post-peak with declining trajectory pulling below band)
2. **POT does not exceed demonstrated peak by more than the career-stage allowance** — pre-peak ascending +0.60 max; approaching peak +0.30 max; peak +0.10 max; post-peak/late should not exceed at all
3. **Min < POT < Max**
4. **Min ≤ current composite for ascending or recovering trajectories** — Min cannot rise above current observed level when the trajectory implies upside (downside = trajectory fails)
5. **Max does not cross narrative-stated tier exclusions** — e.g., "never an MVP" caps Max < 9.20
6. **Skill-gap caps named in output match those in Section 3 narrative and Section 8 composite rationale** — no new caps invented at projection step

---

*NBA Projection Output Block designed Session 119. Purpose: replace inflated prospect-arc POT logic with empirical anchor-based projection for NBA vets. Core discipline: POT anchored to realistic ceiling band named in narrative, modulated by career stage and trajectory flag, capped by skill-gap bounds.*
