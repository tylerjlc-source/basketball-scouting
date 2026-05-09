# POT RECALCULATION PROCEDURE

**Scope:** One-time sweep procedure for bringing the existing /output NBA-vet profiles into compliance with NBA-PROJECTION-OUTPUT-BLOCK.md (S119). Codifies the workflow validated on Scottie Barnes 2026-05-03.

**Load scope:** Task-loaded at the start of any recalc session. Not session-open governance, not loaded by Skill 5 in regular runs.

**Lifecycle:** Live until the sweep is complete. Archive with retrospective when all in-scope profiles carry `pot: X.XX` in wiki frontmatter (no remaining `pot: null` for any /output player).

---

## SCOPE

- **In:** All NBA-vet profiles in `/output` (48 as of 2026-05-03). All have ≥25 NBA games — every /output entry qualifies for the new NBA POB.
- **Done:** Scottie Barnes (2026-05-03 pilot).
- **Remaining:** 47 profiles.
- **Out:** Prospects (States 1–3 — not currently in /output; if added later, route through prospect POB, not this procedure). Profiles for players who lose NBA-vet eligibility (none currently exist; flagged here for completeness).

---

## WORKFLOW PER PLAYER

For each player, one full pass per session. **One player at a time** — do not batch confirmations.

### Step 0 — Pre-load
1. Read existing profile: `output/[Player_Name]/[YYYY-MM-DD]_profile.md`
2. Confirm composite, sub-domain scores, archetype, tier from Section 1 — these stay unchanged through the recompute.
3. Verify NBA games count (≥25). If a profile is borderline, surface to Tyler.

### Step 1 — Career stage (NBA POB STEP 1)
Assign one stage from age + NBA seasons:

| Stage | Age | NBA experience |
|---|---|---|
| Pre-peak ascending | ≤24 | ≤3 seasons |
| Approaching peak | 24–27 | 3–7 seasons |
| Peak | 27–30 | 5–10 seasons |
| Post-peak | 30–33 | 8–13 seasons |
| Late career | 33+ | 12+ seasons |

Tie-breaker: weight by dominant signal. Bigs may peak later (28–31) — apply judgment within ±2 years of band edges.

### Step 2 — Trajectory flag (NBA POB STEP 2)
Assign from existing profile narrative + last-season trend:

| Flag | POT placement effect |
|---|---|
| Ascending | Upper third of anchor band |
| Plateau | Middle of anchor band |
| Declining | Lower third; at or below demonstrated peak |
| Recovering | At demonstrated peak; spread auto-Wide |

Cite evidence inline (statistical or qualitative). For profiles older than ~30 days where current-season trajectory has materially shifted, refresh from public stats (basketball-reference) before assigning.

### Step 3 — POT (NBA POB STEP 3, anchor-based)

- **3.1 Demonstrated peak floor:** best observed season composite (current or prior anchor entry, whichever is higher). For unevaluated peak seasons, estimate from accolades per NBA POB Step 3.1 table.
- **3.2 Ceiling anchor band:** name 2–3 anchors from `docs/ANCHOR-LIBRARY.md`. Same archetype, or same group at minimum. Realistic peak outcomes (not aspirational reaches). Narrative must support the band.
- **3.3 Place in band:** per Step 2 trajectory placement rule.
- **3.4 Skill-gap caps:** name structural ceiling bounds from existing narrative (e.g. "no twitch off-dribble", "sub-33% CAS"). Caps prevent drift to top of band.
- **3.5 R13 Stage 1 modifier:** apply per existing R13 cite in profile Sec 4 #26 / Sec 8.

  | Signal | Modifier |
  |---|---|
  | Strong rise | +0.40 |
  | Moderate rise | +0.20 |
  | Moderate shrink | −0.20 |
  | Strong shrink | −0.40 |

  **Double-count guard:** if named ceiling anchors already embody playoff signal (champions, FMVP-pedigree, deep-run vets), justify why R13 isn't already baked in OR reduce magnitude (typically halve to +0.20 / −0.20).

- **Apply Validation Check #2 cap:** POT ≤ demonstrated peak + career-stage allowance.

  | Stage | Cap above demonstrated peak |
  |---|---|
  | Pre-peak ascending | +0.60 |
  | Approaching peak | +0.30 |
  | Peak | +0.10 |
  | Post-peak / Late career | 0 (POT ≤ demonstrated peak) |

### Step 4 — Min/Max spread (NBA POB STEP 4, asymmetric)

- **Max** = top of anchor band + stage buffer (Pre-peak +0.20–0.40 down to Late career 0). Hard cap: narrative-stated tier exclusions (e.g. "never an MVP" → Max < 9.20).
- **Min** = current composite − trajectory adjustment − risk modifiers (injury, age-decline, character, role-fit). Per NBA POB Step 4 table.
- **Confidence:** Tight (multi-source established vet) | Moderate (consolidating or one ambiguous signal) | Wide (Recovering trajectory, dramatic role change, recent trade to incompatible system).

### Step 5 — Confirmation gates

Surface to Tyler **before** any file edits:

1. **Ceiling anchor band selection** — especially when no archetype peer exists above current composite (cross-archetype substitution requires explicit confirmation per Barnes pilot precedent).
2. **R13 magnitude** — if discounted via double-count guard (state the discount + justification).
3. **Career stage** — for borderline cases (boundary years, big-vs-wing peak-age judgment).
4. **Final POT / Min / Max** — explicit composite-scale values, not just an approval of the walkthrough.

Per memory feedback "Composite confirmation must be explicit": never infer POT approval from approval of an adjacent decision (anchor band, modifier, etc.). Every recompute requires explicit POT/Min/Max approval as a final gate.

---

## EDIT-IN-PLACE RULE

Per memory feedback "BRANCH layout scope — calibration corrections edit in-place":

- This is a calibration correction, NOT a new evaluation
- **Edit Section 9 + QC4 + footer in place** on the existing dated profile
- **Do NOT create a new dated file** — composite, sub-domain scores, archetype, tier are unchanged; new dated file would imply new findings
- Footer should append a recompute log line noting the prior POT/Min/Max → new POT/Min/Max for audit

---

## FILES TO UPDATE PER PLAYER

After Tyler confirms POT/Min/Max:

1. `output/[Player_Name]/[YYYY-MM-DD]_profile.md`
   - Section 9 — replace prior block with new NBA POB output format (per NBA-PROJECTION-OUTPUT-BLOCK.md Step 5). The output block carries embedded cites for career stage, trajectory, DEP, ceiling anchors, skill-gap caps, R13 magnitude, and confidence — no separate "Recompute walkthrough" sub-block needed (post-pilot finding: walkthrough restated the block in step-labeled form, pure redundancy).
   - QC4 — update to NBA POB validation language IF the profile structure includes a QC block. Many post-S96 profiles do not; hold scope per BRANCH layout rule when absent (Edwards / Davis / Cade / Fox precedent).
   - Footer — append one-line recompute log entry: `[YYYY-MM-DD] — NBA POB recompute (S119 sweep). Prior POT/Min/Max → new POT/Min/Max / Confidence.`
2. `wiki/players/[Player Name].md`
   - Frontmatter `pot:` value (currently `null`)
3. `wiki/evaluations.jsonl`
   - Update player's row (currently `"pot": null`)
4. `wiki/log.md`
   - Append minimal entry — header + one line of files touched with before/after deltas + sweep counter:
     ```
     ## [YYYY-MM-DD] recompute-projection | [Player Name]
     POT [old] → [new] | Min [old] → [new] | Max [old] → [new] | Conf [old] → [new]. Files: profile §9 + footer; wiki frontmatter; jsonl row. X of 47 remaining.
     ```
     **Do not restate recompute reasoning** — it lives in the profile Section 9 block (canonical home).
5. `docs/validation/POT-RECALC-FINDINGS.md`
   - **Only when a new sweep pattern fires or an existing pattern recurs.** New pattern → new entry. Recurrence → one-line append to that entry's Cases list. Do not duplicate per-player narrative — that lives in the profile.

Min/Max NOT exposed in wiki frontmatter or jsonl per WIKI-PROTOCOL W9 — they remain in profile narrative only.

---

## SPECIAL HANDLING

### Profiles without raw research packet
~16 of 47 (Amen Thompson, Anfernee Simons, Bogdan Bogdanović, Domantas Sabonis, Donovan Mitchell, Evan Mobley, Ja Morant, Jalen Williams, Jaylen Brown, Kyle Anderson, Mikal Bridges, Pascal Siakam, Sam Hauser, Shai Gilgeous-Alexander, Walker Kessler — confirmed missing /raw at 2026-05-03 audit).

Recomputable from existing profile narrative + age + anchor library. /raw is not required. If narrative is too thin to support trajectory or ceiling-band derivation, flag and surface to Tyler before forcing — do not invent ceiling anchors not supported by existing narrative.

### Drift since profile date
For trajectory-sensitive recomputes on profiles >30 days old, refresh trajectory evidence from public stats (basketball-reference) before assigning. Career stage and demonstrated peak generally don't drift on monthly timescales; trajectory does.

### Re-eval territory
If during recompute the existing profile's underlying scoring (sub-domains, archetype, tier) appears stale enough to warrant a full re-evaluation, **stop the recompute** and flag — re-eval is a different operation (full Skill 1–5 chain, new dated profile, anchor library revision). The recompute procedure does not silently morph into re-eval.

---

## SEQUENCING GUIDANCE

Tyler-driven. Suggested batching (none mandatory):

- **By tier** — start with lower-tier vets (Tier 7–8) where ceiling decisions are simpler; build calibration before high-stakes Tier 4–5 names
- **By group** — guards / wings / bigs sequentially keeps anchor-library mental cache warm
- **By trajectory similarity** — group ascending vets, then plateau, then post-peak — modifiers and validation checks pattern-match within each group

Pilot pattern: one player at a time, full confirmation cycle, then move to next. Do not batch the actual confirmations — every POT/Min/Max requires its own explicit approval.

---

## RELATIONSHIP TO OTHER DOCS

| Doc | When loaded |
|---|---|
| `docs/NBA-PROJECTION-OUTPUT-BLOCK.md` | Always — the methodology this procedure applies |
| `docs/ANCHOR-LIBRARY.md` | At Step 3.2 for ceiling-anchor selection |
| `docs/SCORING-RULES.md` R13 | At Step 3.5 if R13 cite needs verification |
| `wiki/WIKI-PROTOCOL.md` | If uncertain about wiki write path or W9 (Min/Max exclusion) |
| `docs/SCHEMA-SPEC.md` §8b | For the full NBA-vet projection block schema |

This procedure is **not** loaded by Skill 5 in regular runs. Skill 5 loads NBA POB directly.

---

## RETIREMENT

Procedure is complete when all 48 /output profiles carry `pot: X.XX` in wiki frontmatter (no `pot: null` for any /output player). At that point:

1. Append a final retrospective summarizing patterns observed across the sweep (anchor-band reuse patterns, R13 double-count guard frequency, validation check #2 cap firings, ceiling-band cross-archetype frequency).
2. Move this doc to `docs/validation/archive/POT-RECALC-PROCEDURE-archived.md` with a header noting completion date.
3. Remove the load instruction from any session opener that referenced it.

---

*Created 2026-05-03. Codifies the Scottie Barnes pilot recompute (2026-05-03) workflow for the broader 47-profile sweep. Pilot validated full cycle: career stage → trajectory → ceiling band (cross-archetype with no DEP peer above) → R13 double-count guard discount → Validation Check #2 cap fired (POT capped at demonstrated peak + 0.30 Approaching peak allowance) → Min/Max spread → wiki frontmatter + jsonl propagation.*
