---
name: scout-composite
description: "Assign the composite score via tier placement. Runs the 6-step Tier Assignment Protocol against the anchor library. Compares profiles, checks awards, applies prospect gate, and positions within band. Invoke after scout-profile has produced a complete player profile — never assign composite without a profile first."
---

# Skill 4 — Scout Composite

**Job:** Assign the composite score. Read the profile, place the player in a tier band, and position within it.
**Position in chain:** Fourth. Receives complete profile from Skill 3.
**Hands off to:** Skill 5 (scout-output)

---

## LOADING INSTRUCTIONS

On every invocation, load:
1. **This file (SKILL.md)** — composite assignment workflow and output format
2. **BASKETBALL-BRAIN.md** — shapes how profile shape maps to tier placement
3. **COMPOSITE-SCALE-AND-TIERS.md** — tier table, Tier Assignment Protocol (Steps 1–6), awards cross-check table, prospect gate, and draft slot calibration table.
4. **ANCHOR-LIBRARY.md** (index — ~50 lines) — purpose, per-tier file index, loading policy, maintenance rules. The per-tier anchor data is **NOT** loaded here. See Step 3.5 below for the JIT load.
5. **learnings/scout-composite-learnings.md** — active calibration learnings for this skill. Apply before composite assignment.

These five load upfront. The per-tier anchor data loads after Step 3 identifies the candidate band — see Step 3.5.

**Input:** The player profile from Skill 3 provides archetype, gate results, domain scores, profile shape (strengths/liabilities/structural zeros, profile type), and flags. All scoring data traces back to Skill 2's score matrix.

---

## COMPOSITE ASSIGNMENT WORKFLOW

The composite is assigned, not calculated. No formula produces this number. The evaluator reads the profile, compares to anchors, and places the player.

The six steps below summarize the Tier Assignment Protocol. Full reference tables (tier table, awards cross-check table, draft slot calibration table) are in COMPOSITE-SCALE-AND-TIERS.md. The anchor library is in ANCHOR-LIBRARY.md.

---

### Step 1 — Profile inventory

Read all 26 sub-domain scores from Skill 3 and classify each:
- **Strengths** — sub-domains scoring ≥7.0
- **Liabilities** — sub-domains scoring ≤4.9 (non-structural)
- **Structural zeros** — sub-domains expected to score low by archetype design (e.g., rim protection for a Guard, post offense for a Shooting Specialist). Not liabilities; do not count against the player.

Record the count of each. Note active non-negotiable caps from Skill 3.

---

### Step 2 — Survivability check

- Did the player pass all non-negotiables for their position? A failed gate caps the composite ceiling regardless of strengths — apply the cap before assigning a band.
- Count non-structural liabilities only (structural zeros excluded). More than 3 genuine liabilities is a floor signal — pulls the candidate band down before anchor comparison.

---

### Step 3 — Candidate band identification

Map the strength/liability balance to a starting band:

| Profile shape | Candidate band |
|---|---|
| Elite across nearly all 26 sub-domains. Zero liabilities. | Tiers 1–3 (9.20–10.00) |
| Elite at primary sub-domains for archetype. 1 liability max. | Tiers 4–5 (8.60–9.19) |
| Above average across position-relevant sub-domains. No structural liabilities. | Tiers 6–7 (7.90–8.59) |
| Solid across most sub-domains. 2–3 liabilities acceptable. | Tier 8 (7.50–7.89) |
| Clear strengths in primary sub-domains. Noticeable gaps. | Tier 9 (6.80–7.49) |
| One or two real strengths. Significant gaps across most. | Tier 10 (5.80–6.79) |
| No transferable strengths at NBA level. | Tiers 11–13 (1.00–5.79) |

Starting point only — anchor comparison in Step 4 confirms or adjusts.

---

### Step 3.5 — JIT load anchor tier data

After Step 3 identifies the candidate band (Tier `N`), load the relevant tier files **before** Step 4 anchor comparison:
- `docs/anchors/Tier_N.md` — the candidate band
- `docs/anchors/Tier_(N-1).md` — neighbor above (skip if N=1)
- `docs/anchors/Tier_(N+1).md` — neighbor below (skip if N=10 or higher; tiers 11–13 currently empty)

Up to three files, ~10–80 lines each. The anchor library is the single load-bearing reference for Steps 4–5; do not load tiers outside the ±1 window unless Step 4 surfaces a clear cross-band comparison need (rare; flag if it happens).

---

### Step 4 — Anchor comparison and awards cross-check

Select 2–3 anchors from the candidate band that match the player's archetype and profile shape. Compare directly at the sub-domains that matter most for the archetype:
- Compares favorably to most anchors → confirm band or move one band up.
- Compares unfavorably → move one band down.
- No populated anchors in band → hold Step 3 placement, flag for review.

**Anchor-state correction (apply before comparison).** When a candidate-band anchor carries an active deflation flag in ANCHOR-LIBRARY Notes (active recovery, injury flag, dormancy, load management), use the healthy-state ceiling — not the deflated current composite — as the comparison reference. Document in walkthrough (e.g., "Tatum 8.88 currently / ~9.05 healthy per S108-F01"). Distinct from anchor-set scope errors (S102-F03) — run both checks.

**Awards cross-check (NBA only — recheck trigger, not override).** If credentials suggest higher placement than the sub-domain profile is producing, recheck drag sub-domains before locking. Awards outside the evaluation window do not anchor current rating. Full table in COMPOSITE-SCALE-AND-TIERS § Step 4.

Key tier-floor signals: MVP → Tier 4 floor; All-NBA First Team → Tier 5 floor; All-NBA Third Team / All-Defensive First / DPOY → Tier 6 floor; All-Star starter → upper Tier 7 minimum; All-Star reserve → Tier 7 floor.

---

### Step 5 — Position within the band

| Position | Criteria |
|---|---|
| Upper third | Profile clearly stronger than most anchors in band; approaches floor of band above |
| Middle | Profile roughly equivalent to central anchors in band |
| Lower third | Profile clears band floor but does not compare favorably to most anchors |

**Strength cluster density** determines final decimal placement: more strengths at archetype-relevant sub-domains → top of sub-range; fewer → floor. Express to two decimal places.

---

### Step 5.5 — Prospect gate (non-NBA players only)

| Band | Requirement |
|---|---|
| 7.50–7.89 | Default range for highly touted prospects at peak. No additional justification. |
| 7.90–8.29 | Not appropriate for any pre-NBA player. Requires confirmed NBA performance. |
| 8.30+ | Not appropriate without ironclad multi-season evidence at elite competition level. Apply Step 6 ambiguity rule — assign lower band. |

Hard ceiling: 7.89 for any pre-NBA player. No override path. Pull to 7.89 or below if exceeded. Does not apply to NBA players rated at current level.

---

### Step 5.75 — R13 Stage 2 playoff modifier (NBA players with ≥2 playoff series)

Apply after Step 5 decimal placement. Both conditions required:
1. **Strong validation** — multi-source statistical AND qualitative convergence on playoff rise/shrink
2. **Recency** — playoff activity in at least one of the last two playoff cycles

When both met, apply the magnitude table:

| Tier | Magnitude | Threshold |
|---|---|---|
| Defining | ±0.20 | Career-defining playoff signal. Finals MVP or equivalent. Once-per-generation. |
| Strong | ±0.15 | Multi-run rise/shrink that meaningfully reshapes how the player is viewed league-wide. |
| Moderate | ±0.10 | Clear rise/shrink across multiple series, not career-defining. |
| Directional | ±0.05 | Suggestion of rise/shrink. Single series or mixed evidence. Use sparingly. |

**Double-count guard:** When Stage 2 fires, Stage 1 POT modifier (Skill 5) is reduced by one tier. Composite has already absorbed part of the demonstrated track record; POT reflects residual ceiling movement.

**Strict convergence:** Stat side must independently support qualitative direction. Divergence (stat shrink + qualitative rise, or vice versa) fails the gate regardless of credentials. Finals MVP alone does not fire Stage 2 if TS% career-matched delta indicates shrink — already credited via awards cross-check.

**Skip cases (composite unchanged; POT in Skill 5 absorbs track record):**
- Below sample minimum (≥2 series different years) → neither Stage 1 nor Stage 2 fires; narrative only.
- Historical-only evidence (last playoff ≥3 years ago, no intervening activity) → Stage 1 POT absorbs and re-evaluates downward; composite unchanged.
- Active-injury dormancy — recent playoff activity but documented injury rules player out of next playoff cycle → dormant for composite. Stage 1 still fires.
- Convergence-gate fail — either axis neutral / mixed / divergent → Stage 2 = 0; Stage 1 still fires per its thresholds.
- Prospects → does not apply.

**If the modifier crosses a band boundary, re-run Step 4 anchor comparison in the new band.**

Record the modifier (or "No modifier — [reason]") in the assignment walkthrough.

---

### Step 6 — Ambiguity resolution

If the profile sits between two adjacent bands after Steps 4 and 5: assign the lower band and flag for review. Do not assign to the upper band without a clear anchor match that supports it.

---

### Draft slot calibration check (prospects only)

After composite assignment, cross-check against the Draft Slot Calibration Table in COMPOSITE-SCALE-AND-TIERS. Validation input only. Inside the credible range → passes. Outside → trigger profile review before finalizing.

---

## OUTPUT — COMPOSITE ASSIGNMENT FORMAT

```
=== COMPOSITE ASSIGNMENT ===
PLAYER: [Name]
POSITION: [Listed position]
GROUP: [Guard / Wing / Big]
ARCHETYPE: [Archetype]

COMPOSITE: [X.XX]
TIER: [N] — [Tier label]
BAND: [X.XX–X.XX]
PLACEMENT: [Upper / Middle / Lower third]

--- ASSIGNMENT WALKTHROUGH ---
Step 1 — Profile inventory:
  Strengths: [N] | Liabilities: [N] | Structural zeros: [N]
  Active caps: [list, or "None"]

Step 2 — Survivability:
  Gate: [All passed | Cap active on #N — ceiling at X.XX]
  Liability count: [N] [floor signal note if >3]

Step 3 — Candidate band: Tier [N] ([X.XX–X.XX])

Step 4 — Anchor comparison:
  [Anchor]: [X.XX] ([Archetype]) — [comparison at value-driver sub-domains]
  [Anchor]: [X.XX] ([Archetype]) — [comparison]
  [Anchor]: [X.XX] ([Archetype]) — [comparison]
  Band adjustment: [Confirmed | Moved to Tier N]
  Awards cross-check: [N/A | result]

Step 5 — Placement: [Upper / Middle / Lower] third
  [Strength cluster density note]

Step 5.5 — Prospect gate: [N/A | Passed | Pulled to X.XX]

Step 5.75 — R13 Stage 2 playoff modifier (NBA only): [N/A (prospect or below sample) | No modifier — [reason] | Applied [±X.XX] for [defining/strong/moderate/directional] [rise/shrink] — composite shifted from X.XX to X.XX]

Step 6 — Ambiguity: [None | Flagged — assigned lower band]

Draft slot check: [N/A | Pick range X–X | AVG X.XX | Range X.XX–X.XX | Pass / Review]

--- FLAGS FOR SKILL 5 ---
[Ambiguity flags]
[Prospect gate adjustments]
[Draft slot divergence — potential sleeper or bust-risk signal]
[Non-negotiable caps constraining projection ceiling]
```

---

*Skill 4 of 6 in the scouting chain.*
