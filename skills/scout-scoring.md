---
name: scout-scoring
description: "Score 26 sub-domains from a research packet. Applies the 1–10 scale against position-specific peer groups using three-signal rating (statistical anchor, qualitative signal, rubric framework). Produces a score matrix with rationales and confidence tiers. Invoke after scout-research has produced a research packet — never score without research first."
---

# Skill 2 — Scout Scoring

**Job:** Score all 26 sub-domains from the research packet. Every score needs evidence and a confidence tier.
**Position in chain:** Second. Receives research packet from Skill 1.
**Hands off to:** Skill 3 (scout-profile)

---

## LOADING INSTRUCTIONS

On every invocation, load:
1. **This file (SKILL.md)** — scoring protocol and output format
2. **BASKETBALL-BRAIN.md** — foundational domain knowledge. Shapes how to interpret evidence.
3. **SUB-DOMAINS_v3.md** — all 26 sub-domain definitions with observable dimensions, proxy signals, and negative balance anchors. Load once and keep active throughout.
4. **The correct POSITION_SCALE file** — determined by player's archetype positional group:
   - Guard archetypes → POSITION_SCALE_GUARDS_v1.md
   - Wing archetypes → POSITION_SCALE_WINGS_v1.md
   - Big archetypes → POSITION_SCALE_BIGS_v1.md

   Each peer-scale file's preamble defines scale structure (band/precision rule) and the four universal sub-domains. Scoring against the position-specific scale plus the universal-scale file below.
5. **POSITION_SCALE_UNIVERSAL.md** — the four universal sub-domains (#12, #24, #25, #26) scored against the full NBA population regardless of peer group.
6. **SCORING-RULES.md** — full text of rules R1–R15. Load before scoring begins.
7. **learnings/scout-scoring-learnings.md** — active calibration learnings for this skill. Apply before scoring begins.

Do not score any sub-domain without SUB-DOMAINS_v3.md and the correct position-specific scale loaded.

---

## THE 1–10 SCALE

Sub-domain scores use the 1–10 scale defined in the POSITION_SCALE_{GUARDS,WINGS,BIGS}_v1.md and POSITION_SCALE_UNIVERSAL.md files.

**Banded structure.** Each row in the scale defines a band of 5 valid scores (e.g., 8.5–8.9). The descriptor anchors the band median. Score at the band median when the player matches the descriptor exactly. Score at the band floor when the player just meets the bar. Dial toward the band ceiling when the player exceeds the descriptor and approaches the next-tier descriptor.

**Peer-relative.** Scores are assigned against the player's archetype peer group (guard / wing / big), except for the four universal sub-domains (#12, #24, #25, #26) which are scored against the full NBA population.

**R14 precision discipline.** High and Medium confidence sub-domains use full .1 resolution within the band. Low and Very-Low confidence sub-domains land at the band floor only (.0 or .5). Unjustified clustering at .0/.5 — round numbers chosen because the analysis was not pushed far enough — is the defect R14 catches.

---

## SCORING PROTOCOL

For each sub-domain, follow this sequence:

### Step 1 — Mandatory peer ranking (R10)

Before matching any descriptor, answer: "Among active players in this peer group, where does this player rank at this specific skill?"

Integrate both signal types:
- **Quantitative** — statistics, efficiency, volume, consistency over time
- **Qualitative** — league-wide consensus, scouting reports, credible analyst and coach assessments

No single statistic determines the rank. If only one stat is driving the placement, identify at least one additional signal before scoring.

**Evaluation window rule:**
- Active player → rank current ability
- Retired player → rank at career median
- Injured player → rank based on last active season

The scale descriptor is the confirmation check, not the input. The peer ranking is the input. If rank and descriptor conflict, the rank wins.

### Step 2 — Apply the three-signal rating
Rate using all available evidence from the research packet:

| Signal | Role | Weight |
|---|---|---|
| Statistical anchor | Where available, stats set the baseline range | Primary when available |
| Qualitative signal | Scouting language refines placement within range | Primary for skill sub-domains without stats |
| Rubric framework | SUB-DOMAINS_v3.md definitions govern what each score level means | Always active — the anchor |

**How to interpret the three signals together.** When statistical anchor and qualitative signal converge in the same direction, score within the converged range — confidence is High by R4. When they diverge, the rubric framework arbitrates: re-read the SUB-DOMAINS_v3.md observable dimensions for the sub-domain and ask which signal source carries more weight given the data architecture (stats lead for measurable production sub-domains; qualitative leads for skill sub-domains without direct stats per the SUB-DOMAIN-SOURCE-MAP). Document the divergence in the rationale.

### Step 3 — Apply rules
Check all applicable rules (R1–R15) against the score. Full text in SCORING-RULES.md (auto-loaded).

### Step 4 — Assign confidence tier (R4)

| Signal count and quality | Confidence tier | Interval |
|---|---|---|
| 3+ independent sources | High | ±0.5 |
| 2 sources | Medium | ±1.0 |
| 1 source | Low | ±1.5 |
| Inferred / no direct evidence | Very low | ±2.0 |

### Step 5 — Write the rationale
One sentence per sub-domain. Must state: (1) primary evidence driving the score, (2) key negative balance anchor if one applies, (3) any cross-reference cap or flag triggered. A score without a rationale is incomplete.

---

## OUTPUT — SCORE MATRIX FORMAT

The score matrix is the handoff to Skill 3 (scout-profile).

```
=== SCORE MATRIX ===
PLAYER: [Name]
POSITION: [Listed position]
PEER GROUP: [Guard / Wing / Big]
SCALE DOCUMENT USED: [POSITION_SCALE_GUARDS/WINGS/BIGS_v1.md]

--- SCORES ---
#1  At-basket finishing              X.X  [confidence: tier — rationale]
#2  Contact finishing / foul draw    X.X  [confidence: tier — rationale]
#3  Post offense                     X.X  [confidence: tier — rationale]
#4  Catch-and-shoot 3PT              X.X  [confidence: tier — rationale]
#5  Off-dribble shooting             X.X  [confidence: tier — rationale]
#6  Mid-range                        X.X  [confidence: tier — rationale]
#7  Free throw                       X.X  [confidence: tier — rationale]
#8  Handling / creation              X.X  [confidence: tier — rationale]
#9  Touch / feel                     X.X  [confidence: tier — rationale]
#10 Ball security                    X.X  [confidence: tier — rationale]
#11 Court vision                     X.X  [confidence: tier — rationale]
#12 Decision-making                  X.X  [confidence: tier — rationale]
#13 Passing execution                X.X  [confidence: tier — rationale]
#14 Off-ball movement                X.X  [confidence: tier — rationale]
#15 On-ball pressure                 X.X  [confidence: tier — rationale]
#16 Help defense                     X.X  [confidence: tier — rationale]
#17 Rim protection                   X.X  [confidence: tier — rationale]
#18 Post defense                     X.X  [confidence: tier — rationale]
#19 Offensive rebounding             X.X  [confidence: tier — rationale]
#20 Defensive rebounding             X.X  [confidence: tier — rationale]
#21 Burst / explosion                X.X  [confidence: tier — rationale; burst type: vertical | horizontal | balanced]
#22 Lateral quickness                X.X  [confidence: tier — rationale]
#23 Strength                         X.X  [confidence: tier — rationale]
#24 Shot selection                   X.X  [confidence: tier — rationale]
#25 Effort / motor                   X.X  [confidence: tier — rationale]
#26 Competitive character            X.X  [confidence: tier — rationale]

--- CROSS-REFERENCE LOG ---
[List any cross-references that fired, which sub-domain was capped, and by how much]

--- PROSPECT TRANSLATION LOG ---
[If R11 applied: list sub-domains capped at 7.5 and any overrides with justification]

--- INJURY TEMPER LOG ---
[If R9 applied: list sub-domains scored from healthy baseline with evidence]

--- FLAGS FOR SKILL 3 ---
[Any scoring anomalies, conflicting signals, or unusual patterns for profile review]
```

---

*Skill 2 of 6 in the scouting chain.*
