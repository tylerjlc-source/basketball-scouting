---
name: scout-write
description: "Authors the initial `_public.md` draft from the Skill 5 _profile.md + Step 1.7/1.8 stat payloads. Loads PUBLIC-LANGUAGE-GUIDE + PUBLIC-VOICE-CALIBRATION + SIGNATURES in fresh editorial context; returns the full _public.md-shape draft text. Invoked by scout-publish at Step 3 via the Task tool; not directly user-invoked. Fact-checking + voice review run downstream (lint pre-flight + scout-review)."
---

# Skill — Scout Write (initial draft authoring)

**Job:** Author the initial `_public.md`-shape draft from the source `_profile.md` and stat payloads. Pure editorial assembly in fresh voice-craft context.
**Position in chain:** Sub-skill of Skill 7 (scout-publish). Invoked between Step 2 (lint_profile validate) and Step 3.4 (lint pre-flight). Not directly user-invoked.
**Output:** Full `_public.md`-shape draft text returned to scout-publish.

---

## LOADING INSTRUCTIONS

Loaded only when scout-publish invokes this skill. Loads execute as a single parallel batch.

Always load:
1. **This file (SKILL.md)** — write workflow, output template reference, voice spec discipline.
2. **docs/PUBLIC-LANGUAGE-GUIDE.md** — full transform spec (§§1–9, including §5.4 calibration sample).
3. **docs/validation/PUBLIC-VOICE-CALIBRATION.md** — voice exemplar samples + pitfalls + Ranked Voice Recommendation (§§1–10).
4. **docs/SIGNATURES.md** — sub-domain Signature roster + tier rules (mechanical derivation per §3–§4).
5. **docs/PUBLIC_MD_TEMPLATE.md** — canonical `_public.md` output shape.

Inputs received from scout-publish (the handoff contract):
6. **Absolute path to the source `_profile.md`** — scout-write reads §§1, 2, 3, 4, 5, 9, 10 (per scout-publish §4-A pull policy; §§6, 7, 8, 11 skipped).
7. **Step 1.7 career stats markdown** — text block ready to paste into the `## Career stats` section (markdown table format).
8. **Step 1.8 narrative stats markdown handoff** — text block organized by sub-domain with `current_season` / `prior_season` / `two_season_aggregate` views.
9. **Path to scripts/public_narrative_stats_output.json** — slim shape (post-Phase-C C2) for sub-domain rationale stat anchors.

**NOT loaded** (R1 enforcement):
- `docs/SCORING-RULES.md`, `docs/SUB-DOMAINS_v3.md`, `docs/POSITION_SCALE_*.md`, `docs/ANCHOR-LIBRARY.md`, `docs/ARCHETYPE-WEIGHTS-*.md`, `docs/DOMAIN-SCALE_v1.md`, `docs/DOMAIN-SCORE-ROLE-RELEVANCE.md` — scout-write is editorial-surface-only; upstream scoring scaffolding never enters the writer context. Numbers pass through byte-equal from the profile.
- `docs/PUBLIC-RUBRIC.md`, `docs/FACT-CHECK-RUBRIC.md` — review rubrics are loaded by scout-review's V context and by fact-audit's F context, not by the writer.
- The publish skill's orchestration state. Fresh-context writer per the writer/reviewer pattern.

---

## WRITE WORKFLOW

### Step 1 — Read inputs

Read the source `_profile.md` fully. Confirm §9 carries a `TENSE: [past / present / mixed]` token for NBA-vet projection (per scout-output.md §9; default `present` if legacy). Read the Step 1.8 markdown handoff block and the slim narrative-stats JSON for stat anchors.

### Step 2 — Apply pull policy + voice transform

Apply [PUBLIC-LANGUAGE-GUIDE §4-A](../docs/PUBLIC-LANGUAGE-GUIDE.md) pull policy: pull §§1, 2, 3, 4, 5, 9, 10 from the profile; skip §§6, 7, 8, 11.

Apply transforms in order:
- **§3 (strip)** — remove internal flag language (`CAPPED`, `SZ`, `structural zero`, `flagged`), R-code citations (`R12`, `R13`), sub-domain id refs (`#14`, `#26`), and ambiguity-flag prose. Synthesis, not plagiarism — never reproduce another scout's phrasing.
- **§4-B (rewrite)** — sub-domain rationale rewrites: synthesize from profile §4 + Step 1.8 payload; one publish-voice sentence per row.
- **§5 (Vecenie 4-paragraph narrative)** — Identity → Strength → Weakness → Projection-verdict.
  - **§5.1 — narrative posture: essence, not snapshot.** Target 0–2 stats per paragraph, prose-first. Surviving stats must be career-defining: championship/MVP counts, all-time records, career-span splits (`career 91.2%`), structural physical facts, two-season aggregates when the recent pattern is the essence. Single-season percentages relocate to the sub-domain rationale row that scores that skill — the table is where snapshot-in-time evidence belongs. Per [PUBLIC-LANGUAGE-GUIDE §5.1](../docs/PUBLIC-LANGUAGE-GUIDE.md) (post-pivot 2026-05-10).
  - §5.1 — paragraph structure (~3–6 sentences each, representative patterns over snapshot moments).
  - §5.3-P — citation-required percentage syntax. Every percentage carries a season anchor (`20YY-YY`), a paren-count anchor (`(N attempts` / `(N of`), an N-of-M aggregate (`N of M ... since 20YY`), OR a `career` qualifier within ~60 chars. Bare percentages are forbidden.
  - §5.3-G — acronym glossary. Each pinned acronym (DFGPOE, PPP, A:TO, FTR, OREB%, DREB%, TS%, USG, TOV/100, CAS 3PT%, PnR, DHO, ISO, DPOY, MVP, FMVP, 6MOTY) is expanded at first use per scan-standalone group.
  - §5.4 — calibration target. The Mitchell sample at PUBLIC-LANGUAGE-GUIDE §5.4 is the system-output target. Voice exemplars in PUBLIC-VOICE-CALIBRATION (Vecenie / Lowe / Schmitz) are reference inspiration only — match the §5.4 target, NOT the upstream writers (per S174-F02; Lowe-imitation by Claude failed across four iterations).
- **§6 (anchor cross-player comps)** — comp prose pulls from profile §10 only; never invent a comp.
- **§7 (domain one-line justifications)** — eight one-liners, one per domain band.

Stats anchor to Step 1.8 narrative payload + Step 1.7 career table — NEVER profile §3 weighted numbers (the 60/40 blend is the scoring substrate, not a publishable number; per [PUBLIC-LANGUAGE-GUIDE §8 QC7](../docs/PUBLIC-LANGUAGE-GUIDE.md)).

### Step 3 — Derive Signatures

For each sub-domain, derive the Signature column value per [docs/SIGNATURES.md](../docs/SIGNATURES.md) §3–§4 mechanical rules. Format: `[Name] (Tier)` with Tier ∈ {Proven, Elite, Superstar, Iconic, Generational}. Empty Signature cells use the em-dash `—` (U+2014).

Signature derivation is **mechanical, not editorial** — driven by the sub-domain score band. Reconciliation at JSON-export reconciliation is fail-loud (per [PUBLIC-LANGUAGE-GUIDE §4-B](../docs/PUBLIC-LANGUAGE-GUIDE.md)); deriving correctly here prevents downstream churn.

### Step 4 — Assemble draft

Render the full `_public.md` draft following [docs/PUBLIC_MD_TEMPLATE.md](../docs/PUBLIC_MD_TEMPLATE.md). Append the Step 1.7 career stats markdown as the final `## Career stats` section.

### Step 5 — Self-check before return

Quick mechanical sanity (the writer's own discipline; Step 3.4 lint + Step 3.5 scout-review reinforce defensively):
- Every percentage in narrative + sub-domain rationale has a season anchor / raw-count anchor / "since YYYY" frame (§5.3-P).
- Each pinned acronym expanded at first use per scan-standalone group (§5.3-G).
- No internal jargon: `R\d`, `S\d{2,3}`, `structural zero`, `CAPPED`, `flagged`, sub-domain id refs (`#N`).
- 4-paragraph narrative in Identity → Strength → Weakness → Projection-verdict order.
- Numbers byte-equal to profile: sub-domain scores (×26), domain bands (×8), composite, tier, projection POT/Min/Max/confidence.

Catch what you can here so downstream loops are cleaner.

### Step 6 — Return the draft

Return payload to the calling scout-publish skill:

```
=== SCOUT-WRITE RETURN ===
[Full _public.md-shape draft text, as a fenced code block or attached]
```

scout-publish consumes this draft at Step 3-T iteration entry (Tyler edits + redraft) or Step 3-C entry (accept as-is). Step 3.4 lint pre-flight runs on the final draft after iteration.

---

## RULES

**R1 — Editorial-surface-only context.** scout-write never loads upstream scoring scaffolding (SCORING-RULES, SUB-DOMAINS_v3, POSITION_SCALE_*, ANCHOR-LIBRARY, ARCHETYPE-WEIGHTS-*, DOMAIN-SCALE_v1, DOMAIN-SCORE-ROLE-RELEVANCE). Numbers pass through byte-equal from the source profile; voice + structure are the writer's surface.

**R2 — Fresh context.** scout-write gets its own context via the Task tool. The writer does not see the scout-publish orchestration state, the lint pre-flight, the scout-review V verdict, or the Phase B manifest. Clean voice context per the writer/reviewer pattern.

**R3 — Sub-skill, not user-invoked.** scout-write is invoked by scout-publish via the Task tool, not by Tyler directly. The `publish [Player]` trigger always enters at scout-publish Step 1; write is mid-Phase-A automation.

**R4 — Numbers byte-equal.** Sub-domain scores, domain bands, composite, tier, projection POT/Min/Max/confidence pass through byte-equal from the source profile. Stats in narrative + rationale anchor to Step 1.7 / 1.8 payloads, NOT profile §3 weighted numbers (per PUBLIC-LANGUAGE-GUIDE §8 QC7).

**R5 — Tyler approval is the canonical voice gate.** Per S174-F02, voice is judged by Tyler at scout-publish Phase B, not by scout-write or scout-review. scout-write's job is a quality first draft that minimizes Tyler's edit burden; Tyler's edit pass at Phase B is canonical.

**R6 — Calibration target is the §5.4 Mitchell sample.** Per S174-F02, upstream voice exemplars (Vecenie, Lowe, Schmitz) in PUBLIC-VOICE-CALIBRATION are reference inspiration only — match the §5.4 Mitchell sample as the system-output target. Lowe-imitation by Claude failed across four iterations during the Mitchell calibration sweep.

---

*Created Phase C C5 (2026-05-10) of the basketball-scouting super-user-practices plan by lifting Step 3 (narrative drafting + structured-field assembly) out of scout-publish.md into a dedicated craft skill. Motivation: written reports had been struggling under the orchestrator's mixed context; a fresh writer subagent with focused PUBLIC-LANGUAGE-GUIDE + PUBLIC-VOICE-CALIBRATION access addresses the quality gap. Cost: roughly neutral when Phase B/C orchestrator re-emission is accounted for (scout-publish's LOADING drops PUBLIC-LANGUAGE-GUIDE + PUBLIC-VOICE-CALIBRATION + SIGNATURES). See plan: `~/.claude/plans/we-need-to-examine-joyful-pearl.md`.*
