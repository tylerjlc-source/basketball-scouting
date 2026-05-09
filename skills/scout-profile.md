---
name: scout-profile
description: "Assemble a complete player profile from sub-domain scores. Identifies archetype, runs non-negotiables gate, computes domain scores (excluding structurally irrelevant sub-domains), and produces profile shape analysis. Invoke after scout-scoring has produced a score matrix — never profile without scores first."
---

# Skill 3 — Scout Profile

**Job:** Take the 26 sub-domain scores and build the complete player profile — archetype, domain scores, gate checks, profile shape.
**Position in chain:** Third. Receives score matrix from Skill 2.
**Hands off to:** Skill 4 (scout-composite)

---

## LOADING INSTRUCTIONS

On every invocation, load:
1. **This file (SKILL.md)** — profile assembly protocol and output format
2. **BASKETBALL-BRAIN.md** — shapes archetype identification and profile interpretation
3. **The correct archetype weights file** — determined by the player's positional group (from Skill 2 handoff):
   - Guards → ARCHETYPE-WEIGHTS-GUARDS.md
   - Wings → ARCHETYPE-WEIGHTS-WINGS.md
   - Bigs → ARCHETYPE-WEIGHTS-BIGS.md
   Contains value driver descriptions, weight tables, and confirmed fits for all archetypes in the group. Used for archetype identification only (Step 1). Load one file only.
4. **DOMAIN-SCALE_v1.md** — load selectively: the preamble (top of file) + the Domain 1–7 sub-tables for the player's position group only (Guards / Wings / Bigs) + the Domain 8 universal table. Skip the other position groups' Domain 1–7 sub-tables. Per-domain "expression by position group" notes are short — keep all three position bullets for cross-position awareness. Drives Step 3 domain band assignment.
5. **DOMAIN-SCORE-ROLE-RELEVANCE.md** — full document. Archetype-by-archetype structural-zero context for Step 3 band-matching (excludes SZ sub-domains from the band-match read).
6. **NON-NEGOTIABLES.md** — full document. Required for gate check.
7. **learnings/scout-profile-learnings.md** — active calibration learnings for this skill. Apply before profile assembly.

All seven must be loaded before profile assembly begins.

**Input:** The score matrix from Skill 2 provides all 26 sub-domain scores, the peer group (Guard / Wing / Big), and any flags. The group is already determined — do not re-derive it.

---

## PROFILE ASSEMBLY PROTOCOL

Four steps, in order. Complete each before starting the next.

---

### Step 1 — Identify archetype

**Method — qualitative matching, not formula.** Read value drivers and confirmed fits; do not compute weighted sums.

**1a — Map the strength cluster.** Read all 26 sub-domain scores. Identify where the strengths concentrate (≥7.0). Which domains carry the profile? Where are the gaps?

**1b — Read value driver descriptions.** For each archetype in the player's group, read the value driver description in ARCHETYPE-WEIGHTS. Ask: does this player's strength cluster match what this archetype says drives value? The primary value-driver sub-domains for the archetype should align with the player's actual strengths.

**1c — Narrow to top 2–3 candidates.** Identify which archetypes best describe what this player does. Eliminate archetypes where the player is weak at the primary value drivers, even if they're strong elsewhere.

**1d — Validate against confirmed fits.** Compare the player's profile shape to the confirmed fits listed under the top candidate. The player should look structurally similar — not identical, but the same kind of player in where strengths and weaknesses fall.

**1e — Assign primary and runner-up.** Select the best-fit archetype with a 1–2 sentence rationale explaining why it was chosen over the runner-up. If two archetypes are very close, present both with a recommendation.

**Combo position note:** If the player's listed position straddles two groups (PG/SG, SG/SF), and the Skill 2 handoff flagged this, read archetypes from both adjacent groups and match against the player's actual strength cluster.

---

### Step 2 — Non-negotiables gate

Run the gate per NON-NEGOTIABLES.md for the player's listed position — not the archetype. Gates are position-specific.

For each non-negotiable: check the score against the threshold. If it meets or exceeds → PASS.

If below threshold, apply the age-tiered override per NON-NEGOTIABLES.md *Projection Modifier Override*.

If suspended: add position risk note and flag for reassessment.
If cap applies: record the ceiling for Skill 4.

**Development note rule (suspended physical caps only):** When a physical non-negotiable (#22, #23) is suspended due to age and projectable frame, the output must state the **functional requirement** — not a specific weight target. Describe what the player needs to *do*: hold post position, absorb contact, box out at NBA level. If an NBA Comp is available, use the comp's functional strength profile as the reference point for what "enough" looks like for this archetype.

---

### Step 3 — Domain band assignment

**Method:** For each of the 8 domains, assign a domain score by matching the player's profile to a band on the position-group's domain scale in DOMAIN-SCALE_v1.md. Mechanic mirrors sub-domain scoring (R10): rank against the position peer group on the integrated capability the domain represents, then band-match against the descriptor. Domain scores are band-matched assignments, not arithmetic derivations from sub-domain scores.

**Domain composition (sub-domain inputs to read):**

| Domain | Sub-domains |
|---|---|
| 1 — Finishing | #1, #2, #3 |
| 2 — Shooting | #4, #5, #6, #7 |
| 3 — Ball Skills | #8, #9, #10 |
| 4 — Playmaking | #11, #12, #13, #14 |
| 5 — Defense | #15, #16, #17, #18 |
| 6 — Rebounding | #19, #20 |
| 7 — Athleticism | #21, #22, #23 |
| 8 — IQ / Motor | #24, #25, #26 |

**Per-domain protocol (run for each of the 8 domains):**

1. **Read role-relevant sub-domains.** Read the sub-domains in the table above, excluding archetype structural zeros per DOMAIN-SCORE-ROLE-RELEVANCE.md. Also read the qualitative narrative from Skill 1 / 2 — the rationales, not just the numbers.

2. **Rank against the peer group.** Among the player's archetype peer group (Guards / Wings / Bigs), where does this player rank at this *domain* — the integrated capability the domain represents? "Top 15–25 big defenders", "Above-average wing playmaker", etc. Domain 8 (IQ/Motor) is ranked against the full NBA population per the universal table.

3. **Band-match.** Open DOMAIN-SCALE_v1.md, find the row for this domain × position group (Domain 8 uses the universal table), identify the band whose descriptor matches the rank from step 2.

4. **Dial within band.** Same R14 precision discipline as sub-domain scoring: the descriptor anchors the band median (e.g. 8.7 for the 8.5–8.9 band). Score at floor when the player just meets the bar; dial toward ceiling when they exceed the descriptor and approach the next-tier descriptor. Domain scores reported X.X.

5. **All-SZ domain → "N/A"** with qualifier "(0 of M role-relevant)". No numeric fallback.

**Synthesis sentence per domain (mandatory):** One sentence naming the sub-domains that anchored the band-match AND the constraining sub-domain (if any) that pulled within the band. The lowest sub-domain remains visible alongside the band assignment — readers must see the integration logic, not just the number.

**Worked example — Jaren Jackson Jr. (Switchable Big), D5 Defense:**
- Role-relevant subs: #15=8.5, #16=8.0, #17=7.7, #18=5.7. No SZ.
- Rank: top 15–25 big defenders — DPOY pedigree, multi-axis switch / help / rim coverage, post defense capped by strength.
- Band-match: Bigs 8.5–8.9 floor — "All-Defensive caliber team anchor"; #18 weakness on a known archetype-driven cap pulls dial to floor.
- Score: 8.6.
- Synthesis: "All-Defensive caliber on the multi-axis defensive identity (#15, #16, #17), with post defense (#18) capped by the same strength shortfall the rebounding domain reflects."

---

### Step 4 — Profile shape analysis

Classify all 26 sub-domain scores:

- **Strengths** — sub-domains ≥ 7.0
- **Liabilities** — sub-domains ≤ 4.9 that are role-relevant for the archetype
- **Structural zeros** — sub-domains ≤ 4.9 that are structural zeros for the archetype per DOMAIN-SCORE-ROLE-RELEVANCE.md

For each liability, note severity based on role importance in the archetype weight table: primary value-driver (critical), supporting (moderate), or peripheral (minor) sub-domain.

**Profile type:**
- **Peaked** — 3 or fewer strengths, all ≥ 8.0, with noticeable gaps
- **Distributed** — 6+ strengths across multiple domains
- **Balanced** — 4–5 strengths with minimal liabilities

---

## OUTPUT — PLAYER PROFILE FORMAT

```
=== PLAYER PROFILE ===
PLAYER: [Name]
POSITION: [Listed position]
GROUP: [Guard / Wing / Big]
ARCHETYPE: [Primary]
RUNNER-UP: [Secondary]
ARCHETYPE RATIONALE: [1-2 sentences — why primary over runner-up]

--- NON-NEGOTIABLES GATE ---
Position: [PG / SG / SF / PF / C]
#[N] [Name]: [score] vs [threshold] → [PASS | CAP ACTIVE | CAP SUSPENDED]
[repeat for each non-negotiable]
[If CAP ACTIVE: ceiling note]
[If CAP SUSPENDED: risk note + reassessment flag]
[If position shift flagged: note]
Active caps: [list, or "None"]

--- DOMAIN SCORES ---
D1 Finishing:     [X.X] (N of 3 role-relevant)  incl: [#list] | excl: [#list (SZ)]  [synthesis]
D2 Shooting:      [X.X] (N of 4 role-relevant)  incl: [#list] | excl: [#list (SZ)]  [synthesis]
D3 Ball Skills:   [X.X] (N of 3 role-relevant)  incl: [#list] | excl: [#list (SZ)]  [synthesis]
D4 Playmaking:    [X.X] (N of 4 role-relevant)  incl: [#list] | excl: [#list (SZ)]  [synthesis]
D5 Defense:       [X.X] (N of 4 role-relevant)  incl: [#list] | excl: [#list (SZ)]  [synthesis]
D6 Rebounding:    [X.X] (N of 2 role-relevant)  incl: [#list] | excl: [#list (SZ)]  [synthesis]
D7 Athleticism:   [X.X] (N of 3 role-relevant)  incl: [#list] | excl: [#list (SZ)]  [synthesis]
D8 IQ / Motor:    [X.X] (N of 3 role-relevant)  incl: [#list] | excl: [#list (SZ)]  [synthesis]

(All-SZ domain → score is "N/A" with qualifier "(0 of M role-relevant)".)

--- PROFILE SHAPE ---
Strengths (≥7.0): [count]
  #[N] [Name]: [X.X] (role: [primary / supporting / peripheral])
  ...
Liabilities (≤4.9, non-structural): [count]
  #[N] [Name]: [X.X] (role: [primary / supporting / peripheral]) — [critical / moderate / minor]
  ...
Structural zeros (≤4.9, archetype SZ): [count]
  #[N] [Name]: [X.X]
  ...
Profile type: [Peaked / Distributed / Balanced]

--- FLAGS FOR SKILL 4 ---
[Active caps and ceiling implications]
[Position shift candidates]
[Primary value-driver liabilities]
[Scoring anomalies from Skill 2]
```

---

## RULES

**P1 — Profile shape feeds composite, not formula.** The shape analysis is qualitative input for tier assignment in Skill 4. It is not arithmetic.

**P2 — Low-ceiling archetypes do not suppress scores.** The rubric evaluates basketball reality as observed. A player who matches a low-ceiling archetype (Energy Big, Shooting Specialist, Defensive Specialist, etc.) still gets scored accurately on every sub-domain. The archetype ceiling affects the projection midpoint via the comp weighting system in Skill 5 — not the sub-domain scores or domain scores produced here.

---

*Skill 3 of 6 in the scouting chain. Built Session 91.*
