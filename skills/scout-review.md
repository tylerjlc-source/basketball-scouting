---
name: scout-review
description: "Fresh-context review pass for a Skill 7 _public.md draft. Spawns Subagent V (Voice / PUBLIC-RUBRIC) and Subagent F (Fact-checker / FACT-CHECK-RUBRIC) in parallel against the draft, then revises against V's critique (the PASS gate). Returns the revised draft plus V verdict + F shadow report. Invoked automatically by scout-publish at Step 3.5; not directly user-invoked."
---

# Skill 7.5 — Scout Review

**Job:** Run V (PUBLIC-RUBRIC) and F (FACT-CHECK-RUBRIC) in parallel against a Phase A draft, then revise against V's critique. Return the revised draft plus both verdicts.
**Position in chain:** Sub-skill of Skill 7 (`scout-publish`). Invoked between Step 3.4 (lint pre-flight) and Step 4 (manifest preview). Not directly user-invoked — `scout-publish` handles the trigger via the Task tool.
**Output:** Revised draft text; V verdict + critique; F shadow verdict + punch-list.

---

## LOADING INSTRUCTIONS

Loaded only when `scout-publish` invokes this skill. Loads execute as a single parallel batch — see R5.

Always load:
1. **This file (SKILL.md)** — review workflow, the V + F parallel pattern, revise-against-V protocol.
2. **docs/PUBLIC-RUBRIC.md** — Subagent V's binary rubric (§§1–13). Self-describing — its head section documents V's input contract.
3. **docs/FACT-CHECK-RUBRIC.md** — Subagent F's binary rubric (§§F1–F7). Self-describing — its head section documents F's input contract.
4. **docs/validation/PUBLIC-VOICE-CALIBRATION.md** — voice spec; loaded inside Subagent V's context per V's input contract.
5. **docs/PUBLIC-LANGUAGE-GUIDE.md** §5.4 calibration sample — system-output target; loaded inside Subagent V's context.

Inputs received from `scout-publish` (the handoff contract):
6. **Draft text** — full `_public.md` draft from Step 3-C output, OR the structured-fields slice when Step 3-T is active.
7. **Absolute path to the source `_profile.md`** — V reads §§1, 2, 3; F reads §§1, 3, 4, 9 (including the §9 `TENSE` token from B1).
8. **Path to `scripts/public_career_stats_output.json`** — Step 1.7 payload; F input.
9. **Path to `scripts/public_narrative_stats_output.json`** — Step 1.8 payload; F input.

**NOT loaded** (R1 enforcement):
- `docs/SCORING-RULES.md`, `docs/SUB-DOMAINS_v3.md`, `docs/POSITION_SCALE_*.md`, `docs/ANCHOR-LIBRARY.md`, `docs/ARCHETYPE-WEIGHTS-*.md`, `docs/DOMAIN-SCALE_v1.md`, `docs/DOMAIN-SCORE-ROLE-RELEVANCE.md` — review is editorial-surface-only; upstream scoring scaffolding never enters the review context.
- The writer's reasoning. Fresh-context review per the writer/reviewer pattern (Anthropic's best-of-N pattern applied to prose).

---

## REVIEW WORKFLOW

### Step 1 — Spawn V + F in parallel

Two subagents run **in parallel** in a single response. Spawn both via the Task tool (`subagent_type=general-purpose`) so they execute concurrently. Each subagent has its own fresh context; they do not see each other's inputs or outputs.

**Subagent V — Voice (PASS gate).** Inputs are documented in [PUBLIC-RUBRIC.md](../docs/PUBLIC-RUBRIC.md) "Inputs handed to V" section. V returns: structured critique per the rubric's output format (§§1–13) plus a binary VERDICT (PASS / FAIL). PUBLIC-RUBRIC PASS does NOT guarantee Tyler approval — the rubric tests surface markers; Tyler approval at scout-publish Phase B is the gate. **V remains the PASS gate** during shadow-mode rollout.

**Subagent F — Fact-checker (shadow-mode).** Inputs are documented in [FACT-CHECK-RUBRIC.md](../docs/FACT-CHECK-RUBRIC.md) "Inputs handed to F" section. F returns: structured critique per the rubric's output format (§§F1–F7) plus a binary VERDICT. **Shadow-mode** — F's punch-list and verdict are surfaced in the scout-publish Phase B manifest as informational only; they do not auto-trigger Step 2 revision and do not gate publish. After 3 publishes, evaluate F's signal-to-noise; promote to PASS-required (and optionally strip V §8 / §12 to remove redundancy at that point — see [FACT-CHECK-RUBRIC.md](../docs/FACT-CHECK-RUBRIC.md)). Promotion is a documented learnings entry, not a silent flip.

### Step 2 — Revise against V's critique

**Runs only on Claude-only output** (Step 3-C narrative or Step 3-T structured fields). **The Tyler-iterated narrative is not auto-revised** — Tyler's edit pass is the canonical voice gate; the reviewer rubric is defense-in-depth only and runs only on structured fields when Step 3-T is active.

Apply V's critique (PASS gate during shadow-mode):
- Cut every cosmetic stat (§3).
- Rewrite every hedged line (§2).
- Replace every AI-tell occurrence (§6).
- Where §4 flags <1 specific moment in a paragraph, rewrite that paragraph against the source profile §3 narrative for concrete anchors.
- Where §5 = N, rewrite the close as archetype-projection.
- Where §7 flags em dashes, replace with commas / semicolons / periods.
- Where §8 flags fact-check mismatches, fix the claim against the source profile or remove it.
- Where §9 flags overclaiming, soften the team-state attribution to the individual claim.
- Where §10 flags repetition, remove the repeated mention outside Identity.
- Where §11 flags clichés, rewrite the construction.
- Where §12 / §13 flag acronym or signature-format issues, fix in place.
- Where §1 worst-line reason names a pattern not yet covered above, address it.

**F's punch-list (shadow-mode)** is read but not auto-revised. Surface F's findings + verdict in the return payload under the labeled `[F shadow]` block so `scout-publish` can include it in the Phase B manifest. If Tyler edits in response at Phase B, those edits flow back into a rerun of Step 2's revise pass on the next iteration. On promotion to PASS-required, F-flagged items merge into the auto-revise list above (one item per F-rubric §F1–§F7, with the same fix-or-remove default).

If V FAILs and the writer cannot revise to PASS without losing source fidelity, do not silently ship a FAIL — surface the un-revisable failure in the return payload as a flag for `scout-publish` to forward into the Phase B manifest.

### Step 3 — Return to scout-publish

Return payload to the calling `scout-publish` skill:

```
=== SCOUT-REVIEW RETURN ===
Revised draft:
[revised _public.md text — full, as a fenced code block or attached]

V verdict: PASS / FAIL
V critique:
[verbatim V output per PUBLIC-RUBRIC §§1–13 output format]

[F shadow]
F verdict: PASS / FAIL
F critique:
[verbatim F output per FACT-CHECK-RUBRIC §§F1–F7 output format]

Un-revisable flags (if any):
[V failures the writer could not fix without source-fidelity loss]
```

`scout-publish` consumes this payload at its Step 3.5 return point: revised draft replaces the in-context draft for Step 4 manifest assembly; V/F verdicts and any flags are folded into the manifest under labeled blocks.

---

## RULES

**R1 — Editorial-surface-only context.** Review never loads upstream scoring scaffolding (SCORING-RULES, SUB-DOMAINS_v3, POSITION_SCALE_*, ANCHOR-LIBRARY, ARCHETYPE-WEIGHTS-*, DOMAIN-SCALE_v1). Voice + fact + structure are the review surface; scoring is not.

**R2 — Fresh contexts.** V and F each get their own context. Neither sees the writer's reasoning, the other's inputs, or the other's outputs. Cross-pollination defeats the writer/reviewer pattern.

**R3 — V is the PASS gate; F is shadow-mode.** During the first 3 publishes after Phase B ships, V's verdict gates Step 2 revision and Tyler's manifest sees F's punch-list as informational only. Promotion to PASS-required happens on a documented learnings entry after 3 publishes if F's signal-to-noise holds.

**R4 — Tyler approval supersedes V PASS.** Per S174-F02, V PASS does NOT guarantee Tyler approval. The rubric tests surface markers; Tyler's edit pass at scout-publish Phase B is the canonical voice gate.

**R5 — Parallel-batch execution.** V + F spawn in a single response so they run concurrently. Sequential spawn doubles the wall-clock cost of the review pass.

**R6 — Sub-skill, not user-invoked.** `scout-review` is invoked by `scout-publish` via the Task tool, not by Tyler directly. The `publish [Player]` trigger always enters at `scout-publish` Step 1; review is mid-Phase-A automation.

---

*Skill 7.5 of the scouting chain. Created Phase B.5 (2026-05-09) by lifting Steps 3.5 + 3.6 out of `scout-publish.md` to bring the parent skill within ARCHITECTURAL_PRINCIPLES.md P3's 200-line ceiling. The writer/reviewer split that S175 introduced is now an explicit two-skill handoff: scout-publish writes + orchestrates, scout-review reviews + revises. See plan: `~/.claude/plans/we-need-to-examine-joyful-pearl.md`. Phase B's V/F parallel split is preserved verbatim; only the file the skill lives in changed.*
