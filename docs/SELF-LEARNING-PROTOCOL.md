# SELF-LEARNING PROTOCOL

Operational governance for the project's self-learning system. Covers
finding capture, routing, offloading, and audit.

Anchored in P4 (Findings Feed Forward) from ARCHITECTURAL_PRINCIPLES.md.
This document carries the operational detail; ARCHITECTURAL_PRINCIPLES
carries the principle.

---

## FINDING CATEGORIES

Every finding surfaced during a session falls into one of three categories.
Category drives destination.

| Category | Definition | Destination |
|---|---|---|
| **1 — One-time fix** | Resolved once, no future governance needed | Session log only |
| **2 — Standing rule** | Governs all future cases of this type | Appropriate rule document |
| **3 — Calibration learning** | Refinement to a skill's execution; proven pattern still emerging | Skill-specific learnings file |

Category 3 is the self-learning system's primary domain. Categories 1
and 2 already have homes.

---

## FINDING ID FORMAT

`S{session}-F{number}` — e.g., S94-F01. Assigned at capture. Never reused.

---

## LEARNING ENTRY FORMAT
S94-F01 — Short descriptive title
Date: YYYY-MM-DD
Severity: Low / Medium / High
Context: What triggered the finding — specific case, data, observation.
Learning: The rule/pattern extracted. Written as an instruction.
Applies to: The specific skill step, script, or decision this governs.
Status: Proposed / Active / Superseded / Retired
Applications: Count of successful applications (for promotion tracking).

Status definitions:
- **Proposed** — captured, awaiting first real application
- **Active** — governing behavior, applications being counted
- **Superseded** — promoted to standing rule, entry moved to archive
- **Retired** — no longer relevant, entry moved to archive

---

## ENTRY THRESHOLD — WHAT DESERVES A CAT 3 ENTRY

Not every finding surfaced deserves a learnings-file entry. Signal beats volume.

A finding qualifies as Cat 3 only if **all three** tests pass:

1. **Applicability.** Does this apply across multiple future sessions, not just the one that surfaced it?
2. **Non-obviousness.** Would a fresh Claude instance without this context repeat the mistake or miss the pattern?
3. **Actionability.** Does it tell the next session what to do or avoid — or is it a bare observation?

A finding failing any test is Cat 1 (session log) or discarded. When in doubt, downgrade — it is easier to re-promote a missing learning than to retire noise that has accumulated unchallenged.

The filter runs BEFORE routing. Categorization assumes the finding earned its place.

---

## ROUTING DESTINATIONS (CATEGORY 2 & PROMOTIONS)

Promoted learnings go to the narrowest file that still governs every case
the learning covers.

| Governance type | Destination |
|---|---|
| Skill step execution | That skill's SKILL.md |
| Universal scoring rule | SCORING-RULES.md |
| Hard-stop / red-line rule | NON-NEGOTIABLES.md |
| Architectural pattern | ARCHITECTURAL_PRINCIPLES.md |
| Comp methodology | NBA-COMP-METHODOLOGY.md |
| Composite placement | COMPOSITE-SCALE-AND-TIERS.md |
| Anchor adjustments | ANCHOR-LIBRARY.md |
| Peer group / rank | SUB-DOMAINS_v3.md or position scale file |
| Archetype weight | ARCHETYPE-WEIGHTS-{POS}.md |
| Source / stat mapping | SUB-DOMAIN-SOURCE-MAP_v1.md |
| Script behavior | The relevant .py script |
| Operational / process | PRODUCT_DESIGN_DECISIONS or PROJECT_ROADMAP |
| Session governance | CLAUDE.md |

---

## SESSION-END ROUTING PROTOCOL

Executed at the end of every session — in chat when context is closing,
in VS Code on explicit "wrap session" trigger.

**Step 1 — Inventory.** List every finding surfaced during the session,
including any carried forward from prior sessions.

**Step 2 — Categorize.** For each finding, assign Category 1, 2, or 3.

**Step 3 — Draft routing.** For each finding, propose destination and
draft content (rule language, learning entry, or log-only marker).

**Step 4 — Tyler review.** Tyler reviews the draft and marks each finding:
  - **Keep as drafted** — approved, proceed to write
  - **Modify** — edits content before write
  - **Downgrade** — reassign to lower category (e.g., Cat 2 → Cat 3)
  - **Reject** — finding is not worth logging, discard

**Step 5 — Execute.** Write approved entries to their destinations. No
silent writes. No bundled writes — each file edit is its own step.

**Step 6 — Update opening prompt.** Source the next session's opening
prompt from `SESSION-OPENING-TEMPLATE.md`. Update the ACTIVE LEARNINGS
block in the template to reflect any learnings routed this session
(promote Active, remove Superseded/Retired). Then populate
`{SESSION FOCUS}` with the next session's work and paste at session open.

---

## VS CODE SESSION SEMANTICS

Claude.ai chat sessions end when context runs out. VS Code / Claude Code
sessions with 1M context don't end on their own — they end explicitly.

| Trigger | Response |
|---|---|
| Tyler says "wrap session" (or similar) | Run Session-End Routing Protocol |
| Tyler completes a defined task list | Prompt: "Wrap session and route findings?" |
| Tyler starts fundamentally new work | Prompt: "Close current session first?" |
| No explicit trigger | Findings accumulate in buffer; no write |

**Finding buffer.** During a VS Code session, findings surface into an
in-session buffer. They are not written to learnings files until the
session closes and Tyler approves the routing draft.

---

## PROMOTION — CATEGORY 3 → CATEGORY 2

A Category 3 learning becomes a candidate for promotion when it has been
Active and successfully applied in ≥3 independent cases.

**Promotion flow:**
1. Trigger: application count reaches 3
2. Draft rule language for the destination file (per routing table)
3. Tyler approves or defers
4. On approval: write the rule to its destination, mark original entry
   Superseded, move entry to archive

**Deferrals are valid.** Not every 3x-applied learning needs to become
a rule. Some are better left as skill-specific learnings.

---

## OFFLOADING — KEEPING LEARNINGS FILES LEAN

Three mechanisms keep active learnings files from growing unbounded.

**1. Promotion.** Superseded learnings leave the active file and move to
`docs/learnings/archive/`.

**2. Retirement.** Learnings that no longer apply (methodology changed,
edge case eliminated) move to archive with a retirement note.

**3. P2 splits.** When a learnings file approaches ~300 lines, split at
the natural seam — typically by domain, sub-domain group, or rule area.
Example: `scout-scoring-learnings.md` may split into
`scout-scoring-finishing-learnings.md`, `scout-scoring-shooting-learnings.md`,
etc.

---

## QUARTERLY AUDIT

Every ~90 days, audit each active learnings file against the
governance-rate metric:

**Governance rate = (learnings that governed a decision in the last 10
sessions) ÷ (total active learnings in file)**

| Rate | Interpretation | Action |
|---|---|---|
| ≥80% | File is working | No action |
| 50–79% | Drift accumulating | Review candidates for retirement |
| <50% | File is noise-heavy | Full pass: retire stale, promote mature, split if needed |

Audit output: short report per file (governance rate, retired count,
promoted count, split decisions). Archived with date.

---

## DIRECTORY STRUCTURE
docs/
├── SELF-LEARNING-PROTOCOL.md       ← this file (governance)
└── learnings/
├── scout-research-learnings.md
├── scout-scoring-learnings.md
├── scout-profile-learnings.md
├── scout-composite-learnings.md
├── scout-output-learnings.md
├── project-learnings.md
└── archive/
└── {superseded and retired entries}

Per-skill learnings files load just-in-time at that skill's invocation,
not at session open (P1). This protocol file loads at session open
because it governs every session (governance, not reference).

---

*Operational companion to ARCHITECTURAL_PRINCIPLES.md P4.*
