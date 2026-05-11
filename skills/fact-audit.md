---
name: fact-audit
description: "User-invoked fact-check of a finished _public.md artifact. Spawns Subagent F (FACT-CHECK-RUBRIC) against the published draft + source profile + JSON payloads, then returns F's verdict + punch-list. Manual trigger: 'fact-audit [Player]'. Editorial-surface fact-check only — no scoring, no narrative authorship."
---

# Skill — Fact-Audit (on-demand fact-check)

**Job:** Run F (FACT-CHECK-RUBRIC) against a published `_public.md` artifact and return F's verdict + punch-list. Editorial-surface fact-check only.
**Position in chain:** Not part of the 7-skill scouting chain. User-invoked on demand against an already-published artifact (post-Skill 7).
**Output:** F verdict + critique returned in-conversation; no file written.

---

## LOADING INSTRUCTIONS

Always load (parallel batch):
1. **This file (SKILL.md)** — fact-audit workflow.
2. **docs/FACT-CHECK-RUBRIC.md** — F's binary rubric (§§F1–F7). Self-describing — its head section documents F's input contract.

Inputs (locate from the player name):
3. **output/[Player_Name]/[YYYY-MM-DD]_public.md** — the published artifact. Locate the latest by listing the directory and taking the lexicographically last `*_public.md` filename. Read fully.
4. **output/[Player_Name]/[YYYY-MM-DD]_profile.md** — the source profile (same date as the public artifact). F reads §§1, 3, 4, 9 (including the §9 `TENSE` token).
5. **scripts/public_career_stats_output.json** — career stats payload (must match the player; regenerate via Step 2 if stale or absent).
6. **scripts/public_narrative_stats_output.json** — narrative stats payload (must match the player; regenerate via Step 2 if stale or absent).

**NOT loaded** (R1 enforcement):
- `docs/SCORING-RULES.md`, `docs/SUB-DOMAINS_v3.md`, `docs/POSITION_SCALE_*.md`, `docs/ANCHOR-LIBRARY.md`, `docs/ARCHETYPE-WEIGHTS-*.md`, `docs/DOMAIN-SCALE_v1.md`, `docs/DOMAIN-SCORE-ROLE-RELEVANCE.md` — upstream scoring scaffolding never enters the F context.
- `docs/PUBLIC-LANGUAGE-GUIDE.md`, `docs/PUBLIC-RUBRIC.md`, `docs/validation/PUBLIC-VOICE-CALIBRATION.md` — fact-audit is fact-surface-only; voice scaffolding never loads here.
- The writer's reasoning. Fresh-context fact-check per the writer/reviewer pattern.

---

## WORKFLOW

### Step 1 — Locate the published artifact and its source profile

Confirm via parallel reads:
- `output/[Player_Name]/` directory exists with at least one dated `_public.md`.
- Latest public artifact = lexicographically last `*_public.md` filename in that directory.
- Source profile shares the same date stamp (`[YYYY-MM-DD]_profile.md`). If no matching `_profile.md`, stop and flag — fact-audit cannot run without the source.

### Step 2 — Confirm or regenerate the stats payloads

The stats JSONs at `scripts/public_career_stats_output.json` and `scripts/public_narrative_stats_output.json` are single-player files that get overwritten on each publish or fact-audit invocation. Confirm they match the current player by inspecting the top-level player name field.

If stale or absent, regenerate in parallel:
1. `python scripts/Public_Career_Stats.py "[Player]"`.
2. `python scripts/Public_Narrative_Stats.py "[Player]"`.

Routing fallthrough mirrors scout-publish Step 1.7 / 1.8: NBA path default; college fallback via the Skill 1 sub-agent on `ValueError: No player found`; HS / no-source omit the missing payload and surface in the final report.

### Step 3 — Spawn Subagent F

Spawn via the Task tool (`subagent_type=general-purpose`). F's inputs are documented in [FACT-CHECK-RUBRIC.md](../docs/FACT-CHECK-RUBRIC.md) "Inputs handed to F" section. Pass:
- The full `_public.md` artifact text.
- Absolute path to the source `_profile.md` (F reads §§1, 3, 4, 9 including the §9 `TENSE` token).
- Absolute paths to `scripts/public_career_stats_output.json` and `scripts/public_narrative_stats_output.json`.

F returns: structured critique per the rubric's output format (§§F1–F7) plus a binary VERDICT.

### Step 4 — Return F's verdict + punch-list

Surface F's return verbatim:

```
=== FACT-AUDIT RESULT — [Player Name] ===
Source: output/[Player_Name]/[YYYY-MM-DD]_public.md
Profile: output/[Player_Name]/[YYYY-MM-DD]_profile.md

[verbatim F output per FACT-CHECK-RUBRIC §§F1–F7 output format]

VERDICT: PASS / FAIL
```

Tyler reads. If F flags items, Tyler decides whether to edit the published artifact or amend the source profile. Fact-audit does not auto-revise — it surfaces findings only.

---

## RULES

**R1 — Fact-surface-only context.** Fact-audit never loads voice scaffolding (PUBLIC-LANGUAGE-GUIDE, PUBLIC-RUBRIC, PUBLIC-VOICE-CALIBRATION) or upstream scoring scaffolding (SCORING-RULES, SUB-DOMAINS_v3, POSITION_SCALE_*, ANCHOR-LIBRARY, ARCHETYPE-WEIGHTS-*, DOMAIN-SCALE_v1, DOMAIN-SCORE-ROLE-RELEVANCE). F's job is fact verification against the source profile + stat payloads; nothing else.

**R2 — Fresh F context.** F gets its own context via the Task tool. F does not see the writer's reasoning, V's critique (when applicable), or anything outside the rubric's documented input contract.

**R3 — User-invoked only.** Fact-audit fires only on Tyler's explicit `fact-audit [Player]` trigger. Not auto-chained from scout-publish; not invoked by scout-review. Per Phase C (2026-05-10), F was lifted out of the scout-publish flow to remove a fresh-context subagent cost from every publish — fact-audit is the on-demand replacement.

**R4 — Read-only.** Fact-audit does not write to `_public.md`, `_profile.md`, or any output file. It surfaces F's findings; Tyler chooses whether and how to amend the source artifacts.

**R5 — Single player per invocation.** Mirrors scout-publish P1. Multi-player audits are sequential invocations, each with its own F spawn.

---

*Created Phase C (2026-05-10) of the basketball-scouting super-user-practices plan as the user-invoked fact-checker. F was previously spawned in parallel with V at scout-review Step 1 (shadow-mode); per the Phase C cost-reduction plan, F's parallel firing was removed and replaced by this on-demand skill. See plan: `~/.claude/plans/we-need-to-examine-joyful-pearl.md`.*
