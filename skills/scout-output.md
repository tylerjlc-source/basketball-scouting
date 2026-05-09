---
name: scout-output
description: "Generate the full player deliverable from the completed scouting chain. Assembles bio, scouting narrative, sub-domain rationales, domain summaries, profile shape, composite rationale, projection output block, and NBA comp into a single structured output. Invoke after scout-composite has assigned the composite score — this is always the final step."
---

# Skill 5 — Scout Output

**Job:** Assemble the final player deliverable. Everything from Skills 1–4 synthesized into one structured output.
**Position in chain:** Fifth and final. Receives everything from Skills 2–4.
**Output:** Complete player profile deliverable — the product.

---

## LOADING INSTRUCTIONS

On every invocation, load:
1. **This file (SKILL.md)** — output assembly protocol, section specs, quality checks
2. **Projection doc — load by route (required for Section 9):**
   - **NBA vet (≥25 NBA games):** load `NBA-PROJECTION-OUTPUT-BLOCK.md`. Anchor-based POT, asymmetric Min/Max, no Bust/Avg/Boom.
   - **Prospect or NBA player <25 games:** load `PROJECTION-OUTPUT-BLOCK.md`. Five-block prospect logic with sleeper criteria.
   Determine route from Skill 1 NBA games count.
3. **NBA-COMP-METHODOLOGY.md** — load surgically per Section 9 evaluation route. Determine route at Section 9 before this load.
   - **NBA vet (≥25 NBA games):** load only `§ B — NBA VET LINEAGE COMP` (~25 lines).
   - **States 1–3 (prospect):** load `§ A — PROSPECT NBA COMP` plus header/footer.
   Defer this load until Section 9 has resolved the route.
4. **SCRIPT-REGISTRY.md** — required for Section 10. Contains comp script location and usage.
5. **docs/ANCHOR-LIBRARY.md** — load at Section 11. Required to insert the new anchor entry. Heavy file — do not load earlier.
6. **learnings/scout-output-learnings.md** — active calibration learnings for this skill. Apply before output assembly.

Inputs required (produced by earlier skills):
7. **Research packet** (Skill 1) — physical profile, character signals, injury history
8. **Score matrix** (Skill 2) — 26 sub-domain scores with rationales and confidence tiers
9. **Player profile** (Skill 3) — archetype, gate results, domain scores, profile shape
10. **Composite assignment** (Skill 4) — composite, tier, placement rationale, anchor comparisons

All four upstream outputs must be available. If any is missing, stop and flag which skill needs to run first.

---

## DELIVERABLE SECTIONS

Build each section in order. Each has a source and a standard.

---

## Section 1 — Header

Markdown KV table with **bold field names** AND **bold Composite value**. Required fields (case-sensitive, exact spelling): `Player`, `Position`, `Group`, `Archetype`, `Composite`, `Tier`. Optional: `Team`, `Age`, `Evaluation Date`. `Position` value uses position codes only — `PG/SG/SF/PF/C`, optionally two joined by `/` (no parentheticals like `Forward (SF/PF)`). `Tier` value matches `N — label`. Drop variants: `Listed position` → `Position`; `Composite (OVR)` → `Composite`. No `Band` or `Placement` rows in §1 — that detail belongs in Section 8.

**Template:**

````
| Field | Value |
|---|---|
| **Player** | [Full Name] |
| **Position** | SG (or SG/SF, etc.) |
| **Group** | Guard / Wing / Big |
| **Archetype** | [exact archetype name] |
| **Composite** | **8.40** |
| **Tier** | 8 — NBA starter / rotation player |
````

Pulled from Skills 1, 3, and 4. No prose needed. The `Composite` value is the gate Skill 7 carves out around at calibration correction — keep it canonical and current.

---

## Section 2 — Physical profile

Height, wingspan, weight, standing reach, vertical, lane agility, body type. Pulled from Skill 1 research packet. Report what exists. Mark unknowns. Do not estimate missing measurements.

---

## Section 3 — Scouting narrative

3–5 paragraph synthesis. This is the section a reader will actually read. It must stand alone as a complete scouting report.

**Paragraph structure:**
1. **Identity.** What is this player? Archetype in plain language. Physical profile. What's the first thing you notice?
2. **Offensive profile.** Scoring, creation, shooting, playmaking. Lead with strengths. Be specific — not "good shooter" but what kind, from where, with what evidence. Name the gaps.
3. **Defensive profile.** What can this player guard? Is defense the value driver, functional, or a liability? Name the physical tools that support or limit it.
4. **Character and trajectory.** Motor, competitive fire, work ethic. Getting better or plateauing? Red flags stated directly.
5. **Bottom line.** (optional, for complex profiles) Projection, risk, what makes this player different from others in the same tier.

**Writing rules:**
- **Synthesize, don't plagiarize.** Scouting language from reports is research input — not copy material. Take what scouts observed, process it through the profile, and write it in our own words. Never reproduce another scout's phrasing.
- **No source attribution.** This is synthesis, not a research summary. Do not write "scouts report that" or "according to ESPN." Write with authority.
- **Specific over general.** "Gets to his spots in the mid-range using a hesitation dribble and long stride" beats "good mid-range scorer."
- **Name the weakness.** Do not bury it. Do not soften it.
- **No scores in the narrative.** Numbers live in the sub-domain section. The narrative paints the picture.
- **No single-game references (R15).** Sample size too small. Use season-long patterns. Narrow exception: clutch moments in championship-deciding games only.

**Source:** Synthesized from Skills 1, 2, and 3.

---

## Section 4 — Sub-domain scores

All 26 scores organized by domain. Each score with its confidence tier and rationale (1–2 sentences). Format for readability — group by domain with domain headers.

**Source:** Skill 2 score matrix — direct transfer. Do not alter scores or rationales. If a rationale is missing, flag it.

---

## Section 5 — Domain summaries

8 domain scores with included/excluded sub-domain lists and one-sentence synthesis per domain.

Prepend the deliverable's Section 5 with a single italic reader's note above the table:

> *Domain scores average only the sub-domains that drive value for this archetype; sub-domains structurally outside the role appear in the Excluded column and do not affect the average.*

**Source:** Skill 3 player profile — direct transfer.

---

## Section 6 — Profile shape

Strengths, liabilities (with severity), structural zeros, counts, profile type.

**Source:** Skill 3 player profile — direct transfer.

---

## Section 7 — Non-negotiables gate

Gate results per non-negotiable. PASS, CAP ACTIVE, or CAP SUSPENDED with detail. Active caps listed.

**Source:** Skill 3 player profile — direct transfer.

---

## Section 8 — Composite rationale

Composite, tier, band, placement. Condensed assignment walkthrough — candidate band, anchor comparisons (which anchors, how the player compared at value-driver sub-domains), awards cross-check result, prospect gate result, ambiguity flags. Include the key decision points, not every sub-step.

**Source:** Skill 4 composite assignment — condensed.

---

## Section 9 — Projection Output Block

Built fresh from the routed projection doc (loading instruction 2). Not a transfer from an earlier skill.

**Before running, confirm:**
- Composite score (Skill 4)
- NBA games count (Skill 1) — determines which projection doc applies
- For prospects: consensus draft position and declaration state (Skill 1 research or current mock draft data)
- For NBA vets: career stage inputs (age, NBA seasons), trajectory evidence, ceiling anchors from anchor library
- NBA Comp (identified during research or scoring)

Follow the routed doc exactly. Do not improvise percentages or POT values.

**Format spec.** Fenced code block with `KEY: VALUE` lines. Required keys (case-insensitive): `POT`, `MIN`, `MAX`, `CONFIDENCE` ∈ {tight, moderate, wide}. Prospect track (States 1–3) adds `BUST`, `AVG`, `BOOM` (each as `NN%`). Numeric values one- or two-decimal precision, ≤ 9.99 for POT.

**NBA-vet template:**

````
--- NBA PROJECTION OUTPUT BLOCK ---
CAREER STAGE:           [stage]
TRAJECTORY:             [Plateau / Ascending / Recovering / etc.]
DEMONSTRATED PEAK:      [d.dd]
CEILING ANCHORS:        [anchor citations]
SKILL-GAP CAPS:         [caps]
R13 STAGE 1:            [+0.00 modifier or NA]

CURRENT (composite):    [d.dd]
POT:                    [d.dd]
Min:                    [d.dd]
Max:                    [d.dd]

Confidence:             [Tight / Moderate / Wide]
Spread note:            [≤2 sentences]
Trajectory note:        [≤2 sentences]
````

**Prospect template (States 1–3):**

````
POT:           [d.dd]
Min:           [d.dd]
Max:           [d.dd]
Confidence:    [tight / moderate / wide]
Bust:          [NN]%
Avg:           [NN]%
Boom:          [NN]%
````

Bust + Avg + Boom must sum to 100. Min ≤ POT ≤ Max enforced at QC4.

---

## Section 10 — NBA Comp

Branch by Section 9 route. Loading instruction item 3 above governs which section of NBA-COMP-METHODOLOGY.md to load. The two branches produce different §10 shapes — do not mix.

### States 1–3 — Prospect NBA Comp

Assign 2–3 NBA Comps per NBA-COMP-METHODOLOGY.md § A. Identify candidates from Skill 1 / Skill 2 (same group, same archetype bucket), run NBA_Comp_Stats.py per candidate, then apply tolerances and assign comp tier per § A.2–A.3.

**Non-NBA prospects:** The prospect side of the comparison uses projected stats inferred from the 26 sub-domain profile — not pulled from any database. The comp script runs only for the NBA comp candidates.

The comp is not aspirational. It describes who the player looks like now — similar strengths, similar weaknesses, similar archetype. If no strong comp exists, say so and describe the profile shape in functional terms.

**Template:**

````
### Comp 1: [Player Name]
- **Tier:** 🟢 Full (or 🟡 Partial / 🔴 None)
- **Similarity:** [≤2 sentences]

### Comp 2: [Player Name]
- **Tier:** 🟡 Partial
- **Similarity:** [≤2 sentences]
````

H3 form `### Comp N: Player` (no `NBA ` prefix). Each block carries a `**Tier:**` bullet with one of 🟢 Full / 🟡 Partial / 🔴 None. Two to three comps total.

### NBA Vet — Lineage Comp

Assign one lineage comp per NBA-COMP-METHODOLOGY.md § B. Qualitative-only per § B.4 — single callout line. Universal for NBA vet evaluations: every active-NBA-vet profile carries one.

**Template:**

````
**LINEAGE COMP: [Player Name] ([era])** — [prose, ≤100 words].
````

No tier glyph (lineage is qualitative-only per § B.4; the schema's `comp_tier` enum reserves `Lineage` for this branch). One line, single comp. Do not append a Secondary or Rubric-only comp — flag-comp notes (e.g., post-injury cautionary parallel) belong in ≤2 sentences of trailing prose, not a separate `### Comp 2:` block.

**Source:** Comp candidates identified during Skill 1 research or Skill 2 scoring. Statistical matching applies to prospect track only (States 1–3).

---

## Section 11 — Anchor Library Entry

Final step of Skill 5. After Sections 1–10 are complete and QC1–5 have passed, record the player in `docs/ANCHOR-LIBRARY.md` AND emit the same row inline in the profile §11. The inline row is the canonical fingerprint the linter and JSON pipeline cross-check against §1 Composite.

**Inline §11 template (mandatory on every evaluation):**

````
## Section 11 — Anchor Library Entry

**Action:** [New entry / Update in place / Tier crossing — one short clause].

````
| {composite} | {Player Name} | {Status} | {Group} | {Archetype} | {Notes} |
````

[Optional ≤2 sentences: prior-value note for revisions, tier-crossing rationale, or `(N words in Notes — within 10-word strict limit.)`]
````

The inline row is byte-equal to the row written into `docs/ANCHOR-LIBRARY.md`. Composite must equal §1 Composite (linter cross-check). Do not omit §11 — the linter blocks delivery and Skill 7 publish on a missing or malformed §11.

**Anchor library insertion process:**

1. Load `docs/ANCHOR-LIBRARY.md`.
2. Locate the tier sub-table matching the composite. Tier sections are H3 headings with format: `### Tier N — {band} — {label}` (e.g., `### Tier 8 — 7.50–7.89 — NBA starter / rotation player`).
3. Insert the player row into that tier's sub-table, sorted by composite descending. In case of tie, insert after existing same-value entries.
4. Row format (per-tier sub-tables — no Tier or band column; tier is in the section heading):
   ```
   | {composite} | {Player Name} | {Status} | {Group} | {Archetype} | {Notes} |
   ```
   - **Status:** Active / Retired / `{Year} draft class`
   - **Group:** Guard / Wing / Big
   - **Archetype:** exact name from the relevant ARCHETYPE-WEIGHTS-{POS}.md
   - **Notes:** strict 10-word maximum. Leave blank if no current state flag applies. The library is a fast-lookup reference scaling to hundreds of anchors — Notes column space is finite. Allowed content: active injury / surgery flags ("Injury flag", "Labrum surgery 2025-26", "Elbow UCL — out 2025-26"), rookie/draft-class status ("Rookie"), active non-negotiable caps ("C #17 cap active"), band markers ("Top of band", "Bottom of band"), durable credential shorthand ("1x All-Star; 6MOTY", "6MOTY 2023-24"). Forbidden content: session walkthroughs ("Updated Session N — was X"), methodology references (R13/R8/S96-F02/S100-F01/S96-F04 and similar IDs), comp tier details, profile shape descriptions, batch-sweep references, "first X anchor" library-history notes. Detailed history lives in SESSION HISTORY (bottom of file), per-player profile (output/[Player]_profile.md), and learnings files — never the Notes column.

5. **Insertion ordering:** sort rows within a tier sub-table by composite descending; tied entries append. After insert/update, verify the row sits between its neighbors and re-sort if needed.
6. **Tier crossing:** if a revision moves a composite across a tier band, move the row to the new tier sub-table at the correct sorted position.
7. Update the anchor count line near the top of the file: increment by 1, update the "as of Session X" stamp.

**Revisions (not new entries):** If the composite is a revision to an existing anchor, update the row in place. Do not duplicate. The detailed revision rationale (prior value, drift drivers, modifier applications) lives in SESSION HISTORY at the bottom of the file — NOT in the Notes column. The Notes column follows the same strict 10-word policy for revisions as for new entries.

**Source:** All required fields are present in Section 1 (header) and Section 8 (composite rationale). No additional research needed.

---

## QUALITY CHECKS

Run all six before delivering. If any fails, fix it.

**QC1 — Completeness.** All 10 sections present. No placeholders. No "[TBD]."

**QC2 — Consistency.** Composite in header matches Section 8. Sub-domain scores in Section 4 match domain scores in Section 5. Gate results in Section 7 match cap references in Section 8. Archetype in header matches weight references throughout.

**QC3 — Narrative integrity.** Section 3 does not contradict Section 4 scores. "Elite shooter" requires a sub-domain ≥ 8.0. "Defensive liability" requires a sub-domain ≤ 4.9.

**QC4 — Projection coherence.** Min < POT < Max. POT ≤ 9.99. For prospects: Bust% + Avg% + Boom% = 100%, divergence flag logic matches PROJECTION-OUTPUT-BLOCK thresholds. For NBA vets: validation checks per NBA-PROJECTION-OUTPUT-BLOCK.md (Min ≤ current composite for ascending/recovering trajectories; Max within narrative tier exclusions; POT inside named anchor band).

**QC5 — Source fidelity.** No scores altered between Skill 2 and Section 4. No domain scores altered between Skill 3 and Section 5. No composite altered between Skill 4 and Section 8.

**QC6 — Lint pass.** Run `python scripts/lint_profile.py output/[Player_Name]/[YYYY-MM-DD]_profile.md`. Linter validates §1 / §4 / §5 / §9 / §10 / §11 against the canonical templates above and cross-checks §1 ↔ §8 ↔ §11 composite equality. Exit 0 = clean; exit 1 = drift (fix in place before declaring delivery complete); exit 2 = fatal parse error. Do not ship a profile that fails the linter.

---

## RULES

**O1 — The deliverable is the product.** Every section must be clear, complete, and internally consistent.

**O2 — Scores are sacred.** Do not round, adjust, or editorialize. If a score looks wrong in context, flag it — do not fix it.

**O3 — The narrative is synthesis, not summary.** Written from understanding. Reads like a professional scouting report — authoritative, specific, honest.

**O4 — Projection is mechanical.** Follow PROJECTION-OUTPUT-BLOCK.md tables and modifiers exactly.

**O5 — Flag don't fix.** If something is inconsistent between upstream skills, surface it. Do not silently resolve contradictions.

**O6 — One dated file per evaluation.** Only Skill 5 writes to `output/`. One new dated file per evaluation at `output/[Player_Name]/[YYYY-MM-DD]_profile.md` (SCHEMA-SPEC §10-A). Never overwrite. Skills 1–4 outputs are in-session handoffs, not files.

---

*Skill 5 of 5 in the scouting chain. Built Session 91. Comp script workflow added Session 92. Section 11 (anchor library entry) added Session 95. S98: QC4 POT cap updated to 9.99 per composite-scale unification. S109: write path changed to `output/[Player_Name]/[YYYY-MM-DD]_profile.md` per SCHEMA-SPEC §10-A BRANCH resolution. S119: NBA-vet projection routed to NBA-PROJECTION-OUTPUT-BLOCK.md when ≥25 NBA games; prospect doc retains States 1–3. 2026-05-03: "State 4" terminology retired across active routing — replaced with "NBA vet" / "≥25 NBA games" routing per S119 NBA POB design.*
