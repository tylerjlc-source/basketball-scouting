# ARCHITECTURAL PRINCIPLES

Project-level design rules. Five patterns that shape every architectural
decision on this project. Read at session open; consult whenever a new
document, skill, or process is being designed.

**Note on session open:** In VS Code / Claude Code, "session open" means
CLAUDE.md auto-load. In Claude.ai chat, "session open" means the opening
prompt. Same governance function, different mechanism.

---

## WHEN TO CONSULT

- Designing or splitting a reference document
- Designing or modifying a skill
- Editing a session opening prompt or CLAUDE.md
- Reviewing an existing process for drift
- Any moment where adding "just in case" feels tempting

---

## EXECUTION ENVIRONMENT

The four patterns apply across environments, but the binding constraint
and failure mode differ.

| Environment | Context | Session open | Primary P1 failure |
|---|---|---|---|
| Claude.ai chat | ~200K | Manual opening prompt + doc loads | Run out of context before work completes |
| VS Code / Claude Code | 1M | CLAUDE.md auto-loads standing governance | Signal diluted when irrelevant material loads |
| Production (future) | Per-call | API system prompt | Token cost + latency per call |

**Governance vs. reference distinction.** Lightweight governance (under
~150 lines of pure rules) loads at session open regardless of environment.
Heavy reference loads at the task that invokes it. Test: does this shape
every decision in the session, or only specific ones? If every, it's
governance — open load. If only some, it's reference — task load.

---

## P1 — LOAD JUST-IN-TIME, NOT JUST-IN-CASE

**Rule.** Load heavy reference documents only at the task that needs them.
Lightweight governance (this document) loads at session open because
architectural decisions can surface unpredictably during any skill run —
the catch is lost if the principles aren't already in context. Heavy
reference (anchor library, full skill files, position scales, script registry, NON-NEGOTIABLES) loads at the specific task that
invokes it.

**Why.** Context is finite in chat and signal-diluting in VS Code.
Front-loading burns budget on documents that may never be touched during
the session. A heavy opening prompt leaves less room for the actual work,
or buries the actual work in noise.

**Failure signature.**
- Session opening prompt or CLAUDE.md lists 5+ full documents as required reads
- A document is loaded but never cited in the session's output
- Context runs low before the primary task is complete (chat) or signal
  gets lost in noise (VS Code)
- Finding yourself re-reading the same file because earlier reads got pushed out

**Response when violated.** Audit the load list. Move heavy loads to the
task that needs them. Replace a load with a one-line pointer ("load
ANCHOR-LIBRARY.md at Task 1 start").

---

## P2 — SPLIT AT THE NATURAL SEAM

**Rule.** When a reference document exceeds ~300 lines or covers multiple
concerns, split it along the concern seam. Each resulting file holds one
concern and is loaded independently.

**Why.** A monolithic file forces you to load everything to use any part
of it. Splitting makes P1 possible. It also clarifies what the file is
for — if you can't name one concern the file covers, it covers too many.

**Failure signature.**
- Loading a file to use less than 25% of its contents
- A file whose name uses "AND" (two concerns fused)
- A file that different skills load for different reasons
- A file over 300 lines with no clear single purpose

**Response when violated.** Identify the seam. Split. Update every
reference that points into the old file. Archive the merged version with
a version note.

**Examples from this project.** ARCHETYPE-WEIGHTS split to Guards / Wings
/ Bigs (Session 90). ANCHOR-LIBRARY split out of COMPOSITE-SCALE-AND-TIERS
(Session 92). Both splits made just-in-time loading possible.

---

## P3 — ONE SKILL, ONE JOB

**Rule.** Each skill does one thing. Handoffs between skills are explicit
and use defined input/output formats. No skill makes decisions that belong
to another skill.

**Why.** A skill holding too many jobs means every run loads all their
contexts at once. Explicit handoffs let each skill stay lean and let the
chain be composed, paused, resumed, and swapped at each step.

**Failure signature.**
- A skill file exceeding the 200-line maximum
- One skill reaching into another skill's reference files
- A decision made in Skill N that Skill N+1 has to redo or override
- Output from a skill that doesn't match what the next skill expects as input

**Response when violated.** Name the single responsibility of each skill
in plain language. If you can't, the skill covers too much — split.
Define the handoff format (what goes in, what comes out). Document the
format in the skill file itself.

**Reference implementation.** The six-skill scouting chain (scout-research,
scout-scoring, scout-profile, scout-composite, scout-output, scout-ingest).
First validated end-to-end on Anfernee Simons, Session 94. Skill 7
(scout-publish) and its sub-skill scout-review are paired by an explicit
handoff contract — scout-publish writes + orchestrates, scout-review runs
the V/F parallel reviewer pass and revises against V — illustrating the
"split when one job grows two sub-responsibilities" pattern in practice
(Phase B.5, 2026-05-09).

---

## P4 — FINDINGS FEED FORWARD

**Rule.** Every calibration finding — error caught, rule refined, edge
case resolved — gets captured with an ID, scoped to the skill or document
it affects, and loaded on the next relevant run. Findings are consumed,
not just archived.

**Why.** Without a feedback loop, the system re-discovers the same
calibration principles every session. Tyler's time is spent fixing the
same mistakes instead of moving forward. Institutional memory is the
multiplier.

**Failure signature.**
- A finding is logged but never loaded by the skill it affects
- The same calibration error surfaces across multiple sessions
- A rule change lives in session transcripts but not in any project file
- Asking "did we decide this before?" and having no way to answer fast

**Response when violated.** Route the finding. Which skill does it belong
to? That skill's learnings file gets the entry. On next invocation, that
skill loads its learnings before execution. (See SELF-LEARNING-PROTOCOL.md
and `docs/learnings/`.)

---

## P5 — EARN EVERY LINE

**Rule.** Subtract before adding. A doc, rule, gate, or process step ships
only if removing it would produce a named, likely worse outcome.

**Why.** Context is the binding constraint (P1) and findings already feed
forward (P4) — extra layers aren't insurance, they're dilution. Every
unearned line burns budget that should go to evaluation work and creates
sync debt when the rule later changes.

**Failure signature.**
- Same rule restated in 2+ files (redundant codification)
- A check or gate whose failure mode is rare or whose value is marginal
  vs. its token cost
- Structure built for hypothetical future use cases
- Error handling or fallbacks for scenarios upstream guarantees can't occur
- Prose bloat around a load-bearing rule without adding signal
- A fix proposal with 2+ doc layers firing on the same trigger

**Response when violated.** Flag → confirm → cut. Per-flag confirmation
before editing. Pick the canonical home (usually the just-in-time skill
or rule doc that already owns the rule); replace restaters with one-line
cross-refs or delete.

**Reference implementation.** The 2026-05 subtractive audit
(`docs/validation/audit-plan.md`) — eight targets, ~940 lines cut from
active load with zero load-bearing claims lost. The failure-signature
bullets above are the audit categories, generalized to draft-time use.

---

## ENFORCEMENT

Every new document, skill, or process gets checked against P1–P4 before
it ships. When a pattern is violated:

1. Fix it, OR
2. Document the deliberate exception and why it's justified

Silent violations are the danger. A pattern drift caught and explained is
still alignment. A drift nobody named is how we end up with 1,171-line
reference files again.

---

*Created Session 94.*
