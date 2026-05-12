---
name: scout-review
description: "Fresh-context review pass for a Skill 7 _public.md draft. Spawns Subagent V (Voice / PUBLIC-RUBRIC) against the draft, then revises against V's critique (the PASS gate). Returns the revised draft plus V verdict. Invoked automatically by scout-publish at Step 3.5; not directly user-invoked. Fact-checking (F / FACT-CHECK-RUBRIC) lives in the user-invoked fact-audit skill — not part of scout-review."
---

# Skill 7.5 — Scout Review

**Job:** Run V (PUBLIC-RUBRIC) against a Phase A draft, then revise against V's critique. Return the revised draft plus V's verdict.
**Position in chain:** Sub-skill of Skill 7 (`scout-publish`). Invoked between Step 3.4 (lint pre-flight) and Step 4 (manifest preview). Not directly user-invoked — `scout-publish` handles the trigger via the Task tool.
**Output:** Revised draft text; V verdict + critique.

---

## LOADING INSTRUCTIONS

Loaded only when `scout-publish` invokes this skill.

Always load:
1. **This file (SKILL.md)** — review workflow, V invocation, revise-against-V protocol.
2. **docs/PUBLIC-RUBRIC.md** — Subagent V's binary rubric (LLM-required §§: §1, §3, §4, §5, §8, §9, §11; mechanical §§ 2, 6, 7, 10, 12, 13 are caught by `lint_public.py` upstream). Self-describing — its head section documents V's input contract.
3. **docs/validation/PUBLIC-VOICE-CALIBRATION.md** — voice spec; loaded inside Subagent V's context per V's input contract.
4. **docs/PUBLIC-LANGUAGE-GUIDE.md** §5.4 calibration sample — system-output target; loaded inside Subagent V's context.

Inputs received from `scout-publish` (the handoff contract):
5. **Draft text** — full `_public.md` draft from Step 3-C output, OR the structured-fields slice when Step 3-T is active.
6. **Absolute path to the source `_profile.md`** — V reads §§1, 2, 3.

**NOT loaded** (R1 enforcement):
- `docs/SCORING-RULES.md`, `docs/SUB-DOMAINS_v3.md`, `docs/POSITION_SCALE_*.md`, `docs/ANCHOR-LIBRARY.md`, `docs/ARCHETYPE-WEIGHTS-*.md`, `docs/DOMAIN-SCALE_v1.md`, `docs/DOMAIN-SCORE-ROLE-RELEVANCE.md` — review is editorial-surface-only; upstream scoring scaffolding never enters the review context.
- The writer's reasoning. Fresh-context review per the writer/reviewer pattern (Anthropic's best-of-N pattern applied to prose).

---

## REVIEW WORKFLOW

### Step 1 — Spawn Subagent V

Spawn V via the Task tool (`subagent_type=general-purpose`) — fresh context. V is the editorial PASS gate during the review pass; Tyler approval at scout-publish Phase B remains the canonical voice gate.

**Subagent V — Voice (PASS gate).** Inputs are documented in [PUBLIC-RUBRIC.md](../docs/PUBLIC-RUBRIC.md) "Inputs handed to V" section. V returns: structured critique per the rubric's output format (LLM-required §§ enumerated in PUBLIC-RUBRIC.md) plus a binary VERDICT (PASS / FAIL). PUBLIC-RUBRIC PASS does NOT guarantee Tyler approval — the rubric tests surface markers; Tyler approval at scout-publish Phase B is the canonical gate.

**Fact-checking note.** Subagent F (FACT-CHECK-RUBRIC) is not part of this flow. Tyler runs the user-invoked [skills/fact-audit.md](fact-audit.md) skill on demand against the final `_public.md` artifact for factual coverage.

### Step 2 — Revise against V's critique

**Runs only on Claude-only output** (Step 3-C narrative or Step 3-T structured fields). **The Tyler-iterated narrative is not auto-revised** — Tyler's edit pass is the canonical voice gate; the reviewer rubric is defense-in-depth only and runs only on structured fields when Step 3-T is active.

Apply V's critique (PASS gate). Mechanical checks (§2 hedges, §6 AI-tells, §7 em-dashes, §10 height/weight/wingspan repetition, §12 acronym scan, §13 signature format) are caught upstream by the Step 3.4 lint pre-flight; V no longer reports them, so they are not in this revise list.
- Cut every cosmetic stat (§3).
- Where §4 flags <1 representative pattern in a paragraph, rewrite that paragraph against the source profile §3 narrative for career-spanning anchors (recurring matchup motif, multi-year trait, career-credential class, structural physical fact).
- Where §5 = N, rewrite the close as archetype-projection.
- Where §8 flags fact-check mismatches, fix the claim against the source profile or remove it.
- Where §9 flags overclaiming, soften the team-state attribution to the individual claim.
- Where §11 flags clichés, rewrite the construction.
- Where §1 worst-line reason names a pattern not yet covered above, address it.

If V FAILs and the writer cannot revise to PASS without losing source fidelity, do not silently ship a FAIL — surface the un-revisable failure in the return payload as a flag for `scout-publish` to forward into the Phase B manifest.

### Step 3 — Return to scout-publish

Return payload to the calling `scout-publish` skill:

```
=== SCOUT-REVIEW RETURN ===
Revised draft:
[revised _public.md text — full, as a fenced code block or attached]

V verdict: PASS / FAIL
V critique:
[verbatim V output per PUBLIC-RUBRIC output format]

Un-revisable flags (if any):
[V failures the writer could not fix without source-fidelity loss]
```

`scout-publish` consumes this payload at its Step 3.5 return point: revised draft replaces the in-context draft for Step 4 manifest assembly; V's verdict and any flags are folded into the manifest under labeled blocks.

---

## RULES

**R1 — Editorial-surface-only context.** Review never loads upstream scoring scaffolding (SCORING-RULES, SUB-DOMAINS_v3, POSITION_SCALE_*, ANCHOR-LIBRARY, ARCHETYPE-WEIGHTS-*, DOMAIN-SCALE_v1). Voice + fact + structure are the review surface; scoring is not.

**R2 — Fresh context.** V gets its own context via the Task tool. V does not see the writer's reasoning or anything outside the rubric's documented input contract. Fresh-context review per the writer/reviewer pattern.

**R3 — V is the PASS gate.** V's verdict gates Step 2 revision. Tyler approval at scout-publish Phase B is the canonical voice gate (R4). Fact-checking lives in the user-invoked [fact-audit](fact-audit.md) skill, not in scout-review.

**R4 — Tyler approval supersedes V PASS.** V PASS does NOT guarantee Tyler approval. The rubric tests surface markers; Tyler's edit pass at scout-publish Phase B is the canonical voice gate.

**R5 — Sub-skill, not user-invoked.** `scout-review` is invoked by `scout-publish` via the Task tool, not by Tyler directly. The `publish [Player]` trigger always enters at `scout-publish` Step 1; review is mid-Phase-A automation.

---

*Sub-skill of scout-publish. V-only fresh-context review pass; revises against V's critique and returns the revised draft + verdict.*
