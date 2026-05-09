# SESSION OPENING TEMPLATE

Governance document for session-start prompts. Source file for every new session's opening message.

**How to use:**
1. Copy the TEMPLATE BODY section below into the new session's first message.
2. Replace placeholders: `{NN}` with session number, `{YYYY-MM-DD}` with date, `{ACTIVE LEARNINGS SUMMARY}` with current state of `project-learnings.md`, `{SESSION FOCUS}` with the work for this session, `{UPCOMING SESSIONS}` with forward-planning notes (optional).
3. Paste, start session.

**Maintenance:**
At Session-End Routing Protocol Step 6, update the ACTIVE LEARNINGS block in this template to reflect learnings routed during the session. Source of truth is `docs/learnings/project-learnings.md`; this template mirrors the summary for prompt use. When a learning is Superseded or Retired, remove its summary line here. When a new learning is Active, add it.

---

## TEMPLATE BODY (copy from here down, replacing placeholders)

# Session {NN} Opening

**Date:** {YYYY-MM-DD}
**Environment:** VS Code / Claude Code (1M context)

## Auto-loaded via CLAUDE.md

- `docs/ARCHITECTURAL_PRINCIPLES.md` — P1–P4 project design rules
- `docs/SELF-LEARNING-PROTOCOL.md` — finding capture, routing, Entry Threshold
- `docs/BASKETBALL-BRAIN.md` — domain foundation
- `docs/SCORING-RULES.md` — R1–R13
- `docs/learnings/project-learnings.md` — active project-level learnings

Skills load their own learnings files just-in-time at invocation.

## Active learnings — apply throughout this session

{ACTIVE LEARNINGS SUMMARY}

Full entries in `docs/learnings/project-learnings.md`.

## This session's work

{SESSION FOCUS}

{UPCOMING SESSIONS — optional: one- or two-line notes on what follows this session}

## Process reminders (standing)

- No document modified without explicit confirmation.
- Apply Entry Threshold (applicability / non-obvious / actionable) before any Cat 3 routing.
- Session-end: run full Session-End Routing Protocol per SELF-LEARNING-PROTOCOL.md.
- Workflow-critical learnings appear in the Active learnings block above and govern communication mode.

---

*Created Session 94. Template governance — update ACTIVE LEARNINGS block at each session-end per Step 6 of SELF-LEARNING-PROTOCOL.md.*
