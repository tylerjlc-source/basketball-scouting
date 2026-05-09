---
name: scout-ingest
description: "Maintain the wiki layer after a player evaluation completes. Reads the finished profile from output/ and the research packets from raw/, then creates or upgrades the player's wiki page, updates the archetype hub, recomputes tier-band neighbors and archetype peer lists, refreshes the index, and appends a log entry. Invoke automatically at Skill 5 completion, or manually as 'ingest [Player]' for catchup runs. This is always the final step — no scoring, no doc edits, just wiki sync."
---

# Skill 6 — Scout Ingest

**Job:** Sync the wiki layer to a freshly completed evaluation. One player per invocation.
**Position in chain:** Sixth and final. Receives the completed profile written by Skill 5.
**Output:** New or updated wiki pages, refreshed archetype hub, recomputed cascades, log entry.

---

## LOADING INSTRUCTIONS

Loads 2–7 below execute as a single parallel batch in Phase A — see I8.

Always load:
1. **This file (SKILL.md)** — ingest workflow, decision branches, diff-preview format

Surgical reads from larger files:
2. **wiki/WIKI-PROTOCOL.md** — read sections **PAGE TEMPLATES** and **RULES** only. Skip PURPOSE / FOLDER STRUCTURE / NON-GOALS (governance, not load-bearing for writes).
3. **docs/anchors/Tier_{N}.md** — read the per-tier file matching the profile's tier (from profile §1). Each tier file is small (~10–80 lines) and self-contained — read it in full. Pull the player's row and verbatim Notes from the table; pull any matching `## Session history` entry below the table if present. The cross-tier index `docs/ANCHOR-LIBRARY.md` is not needed for ingest — only the tier file holds the row.
4. **wiki/index.md** — `Read` only:
   - The `## Full-chain evaluated players` chronological list section — the only manually-maintained body section in the index. Skill 6 appends one line here per evaluation.
   ~20 lines instead of 235. Never load full-file. Group sections (GUARDS / WINGS / BIGS) and the `## Cross-references (by tier)` section are dataview-derived from player frontmatter (per W8 in WIKI-PROTOCOL) and need no read.

Inputs required (must already exist):
5. **output/[Player_Name]/[YYYY-MM-DD]_profile.md** — the completed Skill 5 deliverable (BRANCH layout per SCHEMA-SPEC §10-A; dated file under per-player directory). Locate the latest by listing the directory and taking the lexicographically last filename. Read fully — it's load-bearing for every step.
6. **raw/[Player_Name]/** — confirm the folder exists via `Glob` or `ls`. Do **not** read packet contents — only the folder path is needed for the player page's Sources section.

Conditional reads (only when relevant):
7. **wiki/players/[Player Name].md** — `Read` only if it exists (legacy or prior-eval upgrade case). Branch in Step 3.

The archetype hub (`wiki/archetypes/[Archetype].md`) is no longer read or written by Skill 6. Hub roster tables are dataview-derived from player frontmatter; once the player page reflects the new archetype, the hub auto-renders. If the hub doesn't exist for the player's archetype, the Step 4 edge-case flag catches it.

If the profile or research packet folder is missing, stop and flag — do not synthesize from memory.

---

## EXECUTION PATTERN — PHASE-BATCHED (load-bearing)

The workflow steps below cluster into **3 execution phases. Each phase runs in a single turn with parallel tool calls** — see I8 for the rationale.

| Phase | Steps | Turn shape |
|---|---|---|
| A | 1–3 (Locate, Format-validate, Branch) | One turn, ~4–5 parallel reads: profile, WIKI-PROTOCOL surgical, the matching `docs/anchors/Tier_{N}.md` file, index.md surgical (chronological list section), existing player page (if any). Steps 2–3 run as analysis after the reads return. |
| B | 4 (Diff preview) | One turn, no tools — assemble manifest, present to Tyler. |
| — | (Approval gate) | Tyler confirms. |
| C | 5–8 (Batch write, sanity check, ledger, log, confirmation) | One turn — all writes in parallel (~3–4 Edit/Write calls: player page, index chronological-list append, `evaluations.jsonl` append, `log.md` append). Sanity check runs as in-memory analysis. Confirmation output in the same response. |

**Three turns total per ingest is the budget.**

---

## INGEST WORKFLOW

### Step 1 — Locate inputs (Phase A entry)

**This step initiates Phase A — issue all loads from LOADING INSTRUCTIONS items 1–7 in parallel within a single response.**

Confirm via the Phase A reads:
- `output/[Player_Name]/` directory exists with at least one dated profile (`[YYYY-MM-DD]_profile.md`). Latest = lexicographically last filename
- `raw/[Player_Name]/` exists with at least one dated packet
- Player name resolves consistently across folders per W5 (underscores in `output/` and `raw/`, spaces in `wiki/players/`)

After all Phase A reads return, pull from the profile header (Section 1): full name, group, archetype, composite, tier. Pull from `docs/anchors/Tier_{N}.md` table: the player's row (added by Skill 5) and the verbatim Notes column.

### Step 2 — Format-validate the profile (fail-loud)

Before any wiki write, verify the profile parses against expected structure:
- 11 sections present (Section 1 — Header through Section 11 — Anchor Library Entry)
- Each section heading uses H2 form: `## Section N — Title` (current practice; see WIKI-PROTOCOL log [2026-04-25] re: spec-vs-practice drift)
- Section 1 contains: name, group, archetype, composite, tier
- Section 8 composite matches Section 1 composite (cross-check)

If any check fails: **stop**. Report the drift back to the user and recommend a Skill 5 format-fix pass before re-invoking ingest. Do not proceed to writes with a malformed profile — wiki contamination is harder to clean up than a one-time profile fix.

### Step 3 — Branch: upgrade or create

Check `wiki/players/[Player Name].md`:

| State | Path |
|---|---|
| Page does not exist | **Create** — populate the player template fresh |
| Exists with `has_profile: false` | **Upgrade legacy** — flip `has_profile` to true, set `profile_path`, set `scored_session` and `last_updated_session`, set `rubric_version: v3`, refresh frontmatter from new composite/archetype/tier, replace Library History with the verbatim Notes from the matching tier file (`docs/anchors/Tier_{N}.md`), add raw/ packet path to Sources |
| Exists with `has_profile: true` | **Re-eval update** — update composite, tier, tier_band, last_updated_session in frontmatter; refresh Library History; append new raw/ packet path to Sources (do not remove prior packets) |

The page body always uses the current player template from WIKI-PROTOCOL.md. No content sections beyond the template.

### Step 4 — Diff preview and approval gate (Phase B)

Before writing anything, present an enumerated operation manifest:

```
=== INGEST PLAN — [Player Name] ===
Mode: [CREATE | UPGRADE legacy → has_profile | RE-EVAL UPDATE]
Composite: X.XX (Tier T<n>)
Archetype: [Archetype]

Files touched:
  [CREATE|UPDATE]  wiki/players/[Player Name].md
  APPEND           wiki/index.md (chronological list, session N entry)
  APPEND           wiki/evaluations.jsonl (one JSON row per SCHEMA-SPEC §14)
  APPEND           wiki/log.md ([YYYY-MM-DD] ingest | [Player Name])

Total files touched: 4
```

Edge cases to flag in the manifest:
- **New archetype with no existing hub:** Skill 6 does not auto-create hubs — that's a rare event involving Tyler-authored definition text from ARCHETYPE-WEIGHTS-*.md.
- **Wikilinks in player page body to non-existent pages:** caught by Step 6 sanity check.

Wait for explicit Tyler approval before any write. Approval applies to the manifest as drafted — if Tyler edits scope, regenerate the manifest and re-confirm.

### Step 5 — Batch write (Phase C)

Issue every Edit / Write tool call together in one response. Each tool call still targets one file (no merging multi-file changes into a single Edit), but the calls run in parallel.

Typical Phase C write batch (3–4 calls):
- Write or Edit `wiki/players/[Player Name].md` (frontmatter + body per the player template in WIKI-PROTOCOL.md)
- Edit `wiki/index.md` (append player line to the chronological list under the right session header)
- Append to `wiki/evaluations.jsonl` (one JSON row per SCHEMA-SPEC §14 — see Step 7)
- Append to `wiki/log.md` (the ingest entry — see Step 8)

### Step 6 — Post-write sanity check (Phase C analysis)

After all writes, verify:
- New/updated player page has all required frontmatter fields (per W6 — none omitted, `null` or `unknown` if not applicable)
- The chronological-list line in `wiki/index.md` was added under the right session header

If any check fails, fix in place. This is a narrow per-player check, not a full wiki lint.

### Step 7 — Append evaluation ledger row

Append one JSON object (single line) to `wiki/evaluations.jsonl` per SCHEMA-SPEC §14. This is the authoritative longitudinal record of evaluations — load-bearing for the public ratings DB. If the file does not exist, create it.

**Required fields** (all must be present; use `null` for inapplicable):

```json
{"player": "First Last", "session": N, "eval_date": "YYYY-MM-DD", "composite": X.XX, "pre_modifier_composite": X.XX|null, "pot": X.XX|null, "tier": N, "archetype": "Name", "group": "Guard|Wing|Big", "position": "PG|SG|SF|PF|C", "rubric_version": "v3", "prior_composite": X.XX|null, "prior_archetype": "Name"|null, "profile_path": "output/First_Last/YYYY-MM-DD_profile.md", "research_packet_path": "raw/First_Last/YYYY-MM-DD_research-packet.md"}
```

**Field sources:**
- `player`, `composite`, `tier`, `archetype`, `group`, `position` — from profile §1 header
- `eval_date` — from profile §1 evaluation_date or filename
- `session` — from profile footnote or session context
- `pre_modifier_composite` — from profile §8 (R13 Stage 2 walkthrough). Null if no Stage 2 modifier fired
- `pot` — from profile §9 POT line (NBA POB STEP 3 for vets, prospect POB BLOCK 2 for States 1–3). `null` for profiles not yet recomputed under the current schema. Min/Max excluded by design — see WIKI-PROTOCOL W9
- `prior_composite`, `prior_archetype` — from prior ledger row for this player (`null` if first evaluation)
- `rubric_version` — `v3` for current-system evaluations
- `profile_path`, `research_packet_path` — derive from filename conventions

**Append-only invariant:** Never modify or remove a prior row. A correction is a new row. Never re-write the file — open in append mode (or read + rewrite with the new row appended last).

### Step 8 — Append log entry

Append to `wiki/log.md`:

```
## [YYYY-MM-DD] ingest | [Player Name]
Composite: X.XX | Archetype: [Name] | Session: N | Mode: [create | upgrade | re-eval]
Pages touched: [list, comma-separated]
```

If the ingest revealed any wiki-relevant findings (orphan wikilink candidate, format drift in another profile, missing legacy page for a referenced player), append a separate `## [YYYY-MM-DD] lint-candidate | ...` entry per WIKI-PROTOCOL log conventions. Do not silently fix; flag for Tyler.

---

## OUTPUT — INGEST CONFIRMATION

After Step 8, report back:

```
=== INGEST COMPLETE — [Player Name] ===
Mode: [create | upgrade | re-eval]
Pages written: N
Log entry: appended

Open items: [list any lint-candidate findings, or "None"]
```

---

## RULES

**I1 — One player per invocation.** Skill 6 ingests exactly one evaluation. Catchup of multiple stale evals = multiple sequential invocations, each with its own approval gate.

**I2 — Wiki-only writes.** Never modify `docs/`, `output/`, or `raw/`. Per W1, upstream is canonical; if the wiki disagrees with upstream, the wiki is wrong. Skill 5 owns the per-tier anchor files (`docs/anchors/Tier_*.md`) and the index (`docs/ANCHOR-LIBRARY.md`) — Skill 6 reads from them.

**I3 — Format drift fails loud.** A malformed profile blocks ingest. Do not warn-and-proceed; the wiki is the wrong place to absorb upstream defects.

**I4 — Approval gate is mandatory.** No writes before Tyler confirms the operation manifest. Cascade fan-out is the reason — silent multi-file edits compound errors.

**I5 — Wiki body content is dataview-derived, not authored.** Per WIKI-PROTOCOL W8, peer lists, archetype hub rosters, and index.md group/tier sections render live from frontmatter via dataviewjs blocks. Skill 6 edits frontmatter and the chronological-list section only — never authors peer content directly. Direct edits to dataview-rendered bodies revert on next render while leaving the source frontmatter stale.

**I6 — Verbatim Library History.** Per W2, the player page's `## Library history` section reproduces the matching tier file's Notes column verbatim. No summarization, no synthesis from memory.

**I7 — Surgical reads, not full-file loads.** WIKI-PROTOCOL.md and wiki/index.md are large and growing — full-file loads on every ingest are direct P1 violations. The per-tier anchor files are small enough to read whole; the cross-tier index is read only when the workflow specifically needs it. Always grep / section-read per the LOADING INSTRUCTIONS. If a future workflow change tempts you to "just load the whole file" or "just read all the player pages," fix the workflow instead.

**I8 — Phase-batched execution is mandatory.** Skill 6 runs in 3 turns: Phase A (parallel reads of all docs + profile + existing player page if any), Phase B (manifest preview, no tools), approval gate, Phase C (parallel writes + ledger append + log append + sanity check + confirmation). Sequential tool calls within a phase trigger quadratic session-usage cost — same mechanic as [[token-compounding]] applied at the tool-call layer. If you find yourself doing one Read, then a second Read, then a third Read across separate turns within a phase, halt and re-batch.

---

*Skill 6 of 6 in the scouting chain. Built S108. Current shape per S115 dataview pivot — see WIKI-PROTOCOL W8.*
