# PROJECTION OUTPUT BLOCK
**Prospect projection only (States 1–3). NBA vets with ≥25 NBA games route to NBA-PROJECTION-OUTPUT-BLOCK.md.**
**Loaded conditionally — after dimensional profile and NBA Comp assignment are complete.**
**Part of Skill 5 (scout-output). Load alongside SKILL.md when projection output is required.**
**All values composite-scale (1.00–9.99). POT scale unified with composite scale Session 98.**

---

## OVERVIEW

The Projection Output Block is the final step before output assembly. It takes the completed dimensional profile (composite score, confidence tier, projection modifiers, NBA comp validation) and produces the full projection output.

Five blocks in sequence:
1. Projection Midpoint — current composite estimate
2. POT — career ceiling projection
3. Min / Max — development range
4. Bust% / Avg% / Boom% — outcome probability distribution
5. Output format

Plus: Sleeper criteria — divergence flag system.

All projection values are expressed in composite scale (1.00–9.99, two decimal places).

---

## DECLARATION AND CONSENSUS STATES

Assign one of four states before running any block. The state determines the calculation path.

| State | Description | POT path | Flag |
|---|---|---|---|
| 1 | Consensus + Declared | Full two-input model | None |
| 2 | Consensus + Undeclared | Full two-input model | "Pre-declaration — consensus slot applied" |
| 3 | No consensus + Undeclared | Composite-only | "Pre-consensus — composite estimate only" |

**Consensus threshold:** Player appears in 2+ credible mock drafts within the same pick range tier. Credible sources: ESPN, The Athletic, NBADraft.net, Bleacher Report, CBS Sports, and established outlets. Scales with mock draft availability — no hard source count required.

**Key rule:** Consensus is independent of declaration status. A player with an established consensus position uses it regardless of whether they have declared.

**Consensus confidence by pick range:**

| Pick range | Consensus confidence |
|---|---|
| 1–3 | Near-certain |
| 4–14 | High |
| 15–30 | Moderate |
| 31–45 | Low |
| 46–60 | Very low |

---

## BLOCK 1 — PROJECTION MIDPOINT

The Projection Midpoint is the current composite estimate — what the player projects to produce entering the league.

**Formula:**
```
Midpoint = composite
```

The rubric composite anchors the midpoint directly. The NBA Comp operates as a validation cross-check rather than a weighted numeric input. See NBA-COMP-METHODOLOGY.md § A.4 for tier→strength mapping and the validation flag rule. Divergence does not shift the Midpoint — the comp is a check, not a weight.

**Pick-implied composite reference (derived from the Draft Slot Calibration Table in COMPOSITE-SCALE-AND-TIERS.md, grouped into POB's pick tiers):**

| Pick range | Composite range | Pick-implied midpoint |
|---|---|---|
| 1–3 | 7.30–7.89* | 7.60 |
| 4–14 | 6.95–7.80 | 7.30 |
| 15–30 | 6.70–7.55 | 7.10 |
| 31–45 | 6.15–6.85 | 6.50 |
| 46–60 | 5.40–6.20 | 5.80 |

*Capped at the prospect ceiling (7.89) per Step 5.5 in COMPOSITE-SCALE-AND-TIERS.md.

*These ranges are calibrated baselines, not hard gates. Draft class strength and generational outliers can stretch them in either direction — a weaker top of the draft pulls the 1–3 midpoint down; a generational #1 pushes it up. When a range is exceeded, note the reason explicitly in the divergence flag field. **Maintain sync with the Draft Slot Calibration Table — if that table revises, this table revises in step.***

**Divergence flag rule:** When the Projection Midpoint diverges significantly from the pick-implied midpoint, flag in the output. Upward divergence = sleeper candidate. Downward divergence = bust-risk signal. Thresholds defined in the Sleeper Criteria section.

---

## BLOCK 2 — POT

POT is the career ceiling projection — what the player most likely becomes at their best.

**Step 1 — Draft slot anchor (States 1 and 2):**

| Pick range | Consensus confidence | POT anchor |
|---|---|---|
| 1–3 | Near-certain | 9.00–9.99 |
| 4–14 | High | 8.30–9.50 |
| 15–30 | Moderate | 7.60–8.80 |
| 31–45 | Low | 7.00–8.00 |
| 46–60 | Very low | 6.50–7.50 |
| Undrafted | Very low | 6.00–7.00 |

Start at midpoint of anchor range. Composite modifier (Step 2) moves it.

*Ranges intentionally overlap. Draft position anchors the starting point. Composite score and modifiers determine where within — and whether a player breaks through — the range.*

*These bands are calibrated against the modal draft class and derived from the anchor library. Weaker top-of-draft classes pull the 1–3 band down; generational talent (profiling above 9.99-implied ceiling) pushes it up. Pick-range breakouts that land above-band — Brunson at pick 33 landing at 8.70 composite — are the sleeper system's job, not the POT band's job. Flag range exceptions in the divergence flag field.*

**Step 2 — Composite score modifier:**

| Composite vs. expected for pick range | POT modifier |
|---|---|
| Significantly above expected | +0.60 to +1.20 |
| Modestly above expected | +0.20 to +0.60 |
| Aligns with expected | 0 |
| Modestly below expected | −0.20 to −0.60 |
| Significantly below expected | −0.60 to −1.20 |

*"Expected" is defined by the pick-implied composite reference (Block 1). Validate in Task 4 before tightening modifier thresholds (T4-FLAG-03).*

**Step 3 — Projection modifiers (stack on Steps 1 and 2):**

| Modifier | Direction | Magnitude |
|---|---|---|
| Ascending multi-year trajectory | Up | +0.40 to +0.80 |
| Elite competitive character (multi-source) | Up | +0.40 |
| Elite physical ceiling for position | Up | +0.40 |
| Flat trajectory | Down | −0.40 to −0.60 |
| Declining trajectory | Down | −0.60 to −1.00 |
| Senior / multi-year college (near ceiling) | Down | −0.40 to −0.80 |
| Significant injury history | Down | −0.40 to −0.80 |
| Documented physical ceiling | Down | −0.40 to −0.80 |
| Confirmed negative character (multi-source) | Down | −0.60 to −1.20 |

**Playoff modifier (per R13 Stage 1):**

| Signal | POT modifier |
|---|---|
| Strong playoff rise — per R13 Stage 1 (statistical strong rise AND qualitative, ≥2 runs) | +0.40 |
| Moderate playoff rise — per R13 Stage 1 (statistical OR qualitative rise, ≥2 runs) | +0.20 |
| Moderate playoff shrink — per R13 Stage 1 (statistical OR qualitative shrink, ≥2 runs) | −0.20 |
| Strong playoff shrink — per R13 Stage 1 (statistical strong shrink AND qualitative, ≥2 runs) | −0.40 |

Statistical thresholds are baseline-relative (playoff TS% efficiency drops ~2 pts from regular season for star-level players). Full threshold table, sample minimums, and special cases (historical-only evidence, active-injury dormancy, double-count guard) in SCORING-RULES.md R13.

Hard cap: POT cannot exceed 9.99.

**No-slot path (State 3):**

| Composite | POT estimate |
|---|---|
| 8.0–10.0 | 9.00–9.99 |
| 7.0–7.9 | 8.20–9.00 |
| 6.0–6.9 | 7.40–8.20 |
| 5.0–5.9 | 6.80–7.40 |
| Below 5.0 | Below 6.80 |

Apply projection modifiers normally. No composite modifier step — no anchor to adjust from. Min/Max widens by one confidence tier to reflect absence of consensus.

---

## BLOCK 3 — MIN / MAX SPREAD

**Framework:** Min < POT < Max. The spread is symmetric around POT at the base level. Risk modifiers pull Min down only — they do not affect Max.

- **Min** = the floor outcome — what the player looks like if things go wrong
- **POT** = the expected/average outcome — what the player most likely becomes
- **Max** = the ceiling outcome — what the player looks like if everything goes right

**Base spread by confidence tier (symmetric around POT):**

| Confidence tier | Min | Max |
|---|---|---|
| Tight | POT − 0.40 to 0.60 | POT + 0.40 to 0.60 |
| Moderate | POT − 0.80 to 1.20 | POT + 0.80 to 1.20 |
| Wide | POT − 1.20 to 1.80 | POT + 1.20 to 1.80 |

**Risk modifiers — pull Min down only (additive):**

| Driver | Min adjustment |
|---|---|
| Negative character (multi-source confirmed) | −0.60 to −1.00 |
| Negative character (single source) | −0.20 to −0.40 |
| Significant injury history | −0.40 to −0.60 |
| Declining trajectory | −0.40 to −0.80 |
| Documented physical ceiling | −0.20 to −0.40 |
| Senior / near-ceiling profile | −0.20 to −0.40 |
| No-slot player (State 3) | Widen one confidence tier |

---

## BLOCK 4 — BUST% / AVG% / BOOM% DISTRIBUTION

*Activates for all three states (1, 2, 3).*

**Framework:**
- **Bust%** = probability the player lands at or near Min outcome
- **Avg%** = probability the player lands at or near POT outcome
- **Boom%** = probability the player lands at or near Max outcome
- **Avg% = 100% − Bust% − Boom%. Always the residual. Never set independently.**

**Hard constraints:**
- Bust% floor: 3%
- Boom% floor: 3%
- Avg% minimum: 20%
- Bust + Avg + Boom = 100% — no exceptions

### Outcome Tier Scale

All outcomes are relative to the player's POT-implied expected outcome — not a universal standard.

| Tier | Description |
|---|---|
| 1 | Generational / GOAT-tier |
| 2 | MVP / Franchise cornerstone |
| 3 | All-NBA First Team regular |
| 4 | All-NBA (any team) |
| 5 | All-Star regular |
| 6 | Occasional All-Star / quality starter |
| 7 | Solid starter |
| 8 | Reliable rotation contributor |
| 9 | End-of-bench / developmental |
| 10 | Roster fringe / G-League level |
| 11 | Doesn't stick in the league |

Bust = falls meaningfully short of POT-implied tier. Boom = meaningfully exceeds it. Avg = lands at or near the POT-implied tier.

### POT-Based Expected Outcome Anchor

| POT range | Expected outcome (Avg% anchor) |
|---|---|
| 9.20–9.99 | MVP / Franchise cornerstone |
| 8.80–9.19 | All-NBA regular |
| 8.30–8.79 | All-Star candidate / occasional All-Star |
| 7.90–8.29 | Solid starter |
| 7.50–7.89 | Reliable rotation contributor |
| 6.80–7.49 | End-of-bench / developmental |
| Below 6.80 | Roster fringe |

*Mapping aligns with the Composite Tier Table (COMPOSITE-SCALE-AND-TIERS.md). This anchor appears explicitly in the output block so the reader knows what Avg% means for this specific player.*

### Bust% Baseline by Pick Range

| Pick range | Bust% baseline |
|---|---|
| 1–3 | 5–10% |
| 4–6 | 12–18% |
| 7–10 | 18–25% |
| 11–14 | 22–28% |
| 15–30 | 20–28% |
| 31–45 | 24–32% |
| 46–60 | 28–35% |
| Undrafted | 33–42% |

**Bust% modifiers (additive):**

| Driver | Addition |
|---|---|
| Confirmed negative character (multi-source) | +15 to +20% |
| Confirmed negative character (single source) | +8 to +10% |
| Flat trajectory | +5 to +8% |
| Declining trajectory | +8 to +15% |
| Documented physical ceiling | +5 to +10% |
| Significant injury history | +5 to +10% |
| Anomalous data gap for peer group | +5 to +8% |
| Senior player (near-ceiling profile) | +8 to +12% |

### Boom% Baseline by Pick Range

| Pick range | Boom% baseline |
|---|---|
| 1–3 | 35–75% |
| 4–14 | 22–45% |
| 15–30 | 12–32% |
| 31–45 | 8–22% |
| 46–60 | 4–15% |
| Undrafted | 3–8% |

**Boom% modifiers (additive):**

| Driver | Addition |
|---|---|
| Ascending multi-year trajectory | +5 to +10% |
| Elite competitive character (multi-source) | +5% |
| Youth premium (HS senior or intl 17–19) | +5 to +8% |
| Full-tier NBA Comp with high-ceiling archetype | +3 to +5% |

### Internal Consistency Checks

Run both checks before finalizing. Flag and review any contradiction before the output is accepted.

**Check 1 — Boom% too high for POT:** If POT implies "rotation contributor" but Boom% looks like a lottery-upside profile, flag and review.

**Check 2 — Boom% too low for POT:** If the Max outcome (POT + spread) implies "All-Star ceiling" but Boom% is below 15%, flag and review.

---

## BLOCK 5 — OUTPUT FORMAT

```
--- PROJECTION OUTPUT BLOCK ---
STATUS:                 [State 1: Consensus+Declared | State 2: Pre-declaration | State 3: Pre-consensus]
CONSENSUS CONFIDENCE:   [Near-certain | High | Moderate | Low | Very low | N/A]
SLOT SOURCE:            [X of X mocks — pick range: XX–XX | N/A]

PROJECTION MIDPOINT:    [X.XX]  [comp tier: 🟢/🟡/🔴]  [comp validation: aligned | flagged]
POT:                    [X.XX]
Min:                    [X.XX]
Max:                    [X.XX]

Avg% anchor:            [POT-implied expected outcome — e.g. "Reliable rotation contributor"]
Bust%:                  [XX%]  [drivers: list confirmed drivers, or "baseline only"]
Avg%:                   [XX%]
Boom%:                  [XX%]  [drivers: list confirmed drivers, or "baseline only"]

Confidence:             [tight | moderate | wide]
Spread note:            [one line — data sparsity, profile risk, or both?]
Divergence flag:        [none | sleeper candidate | bust-risk signal] + one line explanation
```

---

## SLEEPER CRITERIA

A sleeper is a player whose rubric evaluation (composite or POT) is meaningfully higher than what their draft position implies. The divergence is flagged — not silently resolved. This is where the system earns its value by disagreeing with consensus transparently.

**Pick-implied composite reference:** see Block 1 table. Pick-implied midpoint = midpoint of that band; reference value for all Path A divergence calculations. No other reference point is used.

**POT-implied consensus reference:** Use the midpoint of the POT anchor range for the player's pick tier (Block 2, Step 1).

**Pre-consensus rule:** The sleeper flag only activates when the player has a confirmed consensus position (States 1 or 2). State 3 players (no consensus) already surface their high composite via the Pre-consensus flag. There is no reliable pick-implied composite to diverge from for State 3 players.

---

### Path A — Composite-Led (direct trigger, no gates required)

| Consensus tier | Pick range | Sleeper flag triggers at |
|---|---|---|
| Near-certain | 1–3 | Composite +0.60 above pick-implied* |
| High | 4–14 | Composite +0.80 above pick-implied* |
| Moderate | 15–30 | Composite +1.00 above pick-implied* |
| Low | 31–45 | Composite +1.20 above pick-implied |
| Very low | 46–60 | Composite +1.40 above pick-implied |

Path A triggers directly. Threshold met → flag fires.

*\*Structural note for pick bands 1–30: the 7.89 prospect ceiling (per Step 5.5 in COMPOSITE-SCALE-AND-TIERS.md) bounds pre-NBA composite below these triggers. Path A is therefore structurally unachievable for top pre-NBA prospects — this matches pre-unification behavior under the OVR system, where the composite→OVR scaffold imposed the same ceiling indirectly. Sleeper signal for top-pick prospects routes through Path B (POT-led) or Path C (combined), which operate in the uncapped POT space.*

---

### Path B — POT-Led (requires all three validation gates)

| Consensus tier | Pick range | Sleeper flag triggers at |
|---|---|---|
| Near-certain | 1–3 | POT +1.00 above consensus midpoint |
| High | 4–14 | POT +1.20 above consensus midpoint |
| Moderate | 15–30 | POT +1.40 above consensus midpoint |
| Low | 31–45 | POT +1.60 above consensus midpoint |
| Very low | 46–60 | POT +1.80 above consensus midpoint |

**Validation gates — all three must pass:**

**Gate 1 — Bust% ceiling (primary gate):** Bust% must be below 20%. If Gate 1 fails, the flag is suppressed regardless of Gates 2 and 3. A high-POT player with high bust risk is a gamble, not a sleeper.

**Gate 2 — Max spread (ceiling legitimacy):** Max must be at least POT + 0.80. If Max barely clears POT, the ceiling is not compelling enough to flag.

**Gate 3 — Min floor (downside containment):** Min must not fall more than 1.60 below POT (Min ≥ POT − 1.60). *Exception: Wide confidence profiles with no active risk modifiers may extend to POT − 1.80. A Wide profile fails Gate 3 only when risk modifiers have pulled Min beyond the base Wide spread — indicating genuine downside risk, not data uncertainty.*

---

### Path C — Combined Composite + POT (requires all three validation gates)

Triggers when neither composite nor POT alone crosses its threshold, but the compound signal is strong enough.

| Consensus tier | Pick range | Combined trigger (composite divergence + POT divergence) |
|---|---|---|
| Near-certain | 1–3 | ≥ +1.40 |
| High | 4–14 | ≥ +1.80 |
| Moderate | 15–30 | ≥ +2.20 |
| Low | 31–45 | ≥ +2.60 |
| Very low | 46–60 | ≥ +3.00 |

*Combined = simple addition of composite divergence and POT divergence. Composite weighting (×1.5) deferred to T4-FLAG-01 testing.*

Path C requires all three validation gates (same as Path B).

---

### Downward Divergence — Bust-Risk Flag

When the Projection Midpoint falls significantly below the pick-implied composite, flag as bust-risk signal. Uses the same threshold table as Path A in reverse — the divergence thresholds and consensus-tier scaling are identical.

---

## TESTING FLAGS

**T4-FLAG-01** — Test Path C sleeper criteria: simple addition vs composite-weighted (×1.5) combined threshold. Run against full 2027 GT class once composite scores are validated. Stop after ~5 calls.

**T4-FLAG-02** — Validate the pick-implied composite reference table (Block 1) and POT anchor ranges (Block 2, Step 1) against GT composite scores as the anchor library grows. Current bands are derived from the current 96-anchor library and the Draft Slot Calibration Table (COMPOSITE-SCALE-AND-TIERS.md) — both are in calibration.

**T4-FLAG-03** — Validate composite modifier reference thresholds (Block 2, Step 2). Quantify boundaries for "significantly above expected" and "modestly above expected" once GT composites are available.

**T4-FLAG-04** — Test Block 3 Min/Max spread against GT class. Verify Wide tier ceiling (−1.80/+1.80) is sufficient for highly uncertain freshman profiles, or whether extension is needed.

---

*Projection Output Block fully designed Session 24. Revised and locked Session 25. Unified with composite scale Session 98: POT/Min/Max/Midpoint all express in composite-scale (1.00–9.99); OVR scaffolding and 2K Layer 2 bifurcation removed; NBA Comp weighting simplified to validation cross-check (1-minimal); Path A retains picks-1–30 structural ceiling inherited from OVR behavior; POT anchors re-derived from anchor library; all modifier magnitudes mechanically rescaled at 1 OVR = 0.20 composite. S119: scope narrowed to prospect-only (States 1–3); NBA vet logic separated to NBA-PROJECTION-OUTPUT-BLOCK.md per S119 diagnosis (prospect-arc POT inflation on NBA vets). Stored as external reference file — loaded conditionally after dimensional profile is complete.*
