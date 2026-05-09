# Basketball Scouting System — Claude Code Workspace

## WHAT THIS PROJECT IS

A proprietary basketball player evaluation system. Two products:

1. **Scouting Tool** — evaluates players using a 26 sub-domain rubric scored 1–10 against position-specific peer group scales. Covers NBA, college, and high school players.
2. **Ratings Database** — public-facing, built on the same rubric. Longitudinal tracking from high school through the NBA.

The system answers one question: how good is a player at basketball. Not role-relative or archetype-relative — absolute basketball ability, scored transparently with evidence at every layer.

## WORKSPACE STRUCTURE

```
basketball-scouting/
├── CLAUDE.md              ← You are here.
├── docs/                  ← Project knowledge files (rubric, scales, anchors, rules)
├── scripts/               ← Python statistical pipeline (nba_api)
├── skills/                ← 7-skill scouting chain (research → scoring → profile → composite → output → ingest → publish)
├── raw/                   ← Per-player research packets, dated, immutable (Skill 1 persistence layer)
├── output/                ← Finished player profiles, dated, immutable (Skill 5 persistence layer; per-player directories)
├── wiki/                  ← Derived graph layer: player pages, archetype hubs, evaluations.jsonl ledger (Skill 6)
```

## THE SCOUTING CHAIN

Six sequential skills produce the canonical profile; one manual-trigger editorial skill (Skill 7) transforms a finished profile for public consumption. Never skip a step within Skills 1–6.

| Step | Skill | File | Job |
|------|-------|------|-----|
| 1 | scout-research | skills/scout-research.md | Gather all data. Run scripts for NBA players. Search for scouting reports, biometrics, character. Produce research packet. |
| 2 | scout-scoring | skills/scout-scoring.md | Score 26 sub-domains from the research packet. Three-signal rating: stats, qualitative, rubric. Produce score matrix. |
| 3 | scout-profile | skills/scout-profile.md | Identify archetype, run non-negotiables gate, assign domain band scores, analyze profile shape. Produce player profile. |
| 4 | scout-composite | skills/scout-composite.md | Assign composite score via tier placement against anchor library. Produce composite assignment. |
| 5 | scout-output | skills/scout-output.md | Assemble final deliverable: narrative, scores, profile, projection, NBA comp. Save to output/. |
| 6 | scout-ingest | skills/scout-ingest.md | Sync the wiki layer to the new evaluation. Auto-runs after Skill 5; manual fallback "ingest [Player]". |
| 7 | scout-publish | skills/scout-publish.md | Editorial transform from internal profile to public artifact. Manual trigger only ("publish [Player]"). Output: `output/[Player]/[YYYY-MM-DD]_public.md`. Feeds the JSON export pipeline. |

**Before running any skill:** Read the skill file and every document it lists under LOADING INSTRUCTIONS.

## STATISTICAL PIPELINE

**NBA players only.** Python scripts in `scripts/` — 7 domain scripts at Skill 1, comp script at Skill 5, Playoff_Track_Record.py at Skill 1 when ≥2 playoff series across different years (per R13). College, international, and HS players skip scripts entirely — data via web search at Skill 1.

See `docs/SCRIPT-REGISTRY.md` for the script list, `pip install nba_api` setup, and the 2-season evaluation window (60/40 current/prior weighting).

## DOCUMENT MAP

### Always load for any evaluation:
- `docs/BASKETBALL-BRAIN.md` — foundational domain knowledge

### Load when modifying skills, docs, or architecture:
- `docs/ARCHITECTURAL_PRINCIPLES.md` — P1–P5 project design rules. Load before editing CLAUDE.md, any doc in `docs/`, any skill file, or any structural process.

### Load at session-end / finding-routing:
- `docs/SELF-LEARNING-PROTOCOL.md` — operational governance for finding capture, routing, and offloading (companion to P4). Load on "wrap session", "route findings", or when a finding surfaces that needs categorization.
- `docs/learnings/project-learnings.md` — active project-level cross-skill and architectural learnings. Load alongside SELF-LEARNING-PROTOCOL at session-end.

### Load per skill (see each skill file for specifics):
- `docs/SCORING-RULES.md` — rules R1–R15 governing all scoring (Skill 2; Skills 1 and 4 reference R12/R13 inline as flag-and-defer pointers and do not need the full text)
- `docs/SUB-DOMAINS_v3.md` — 26 sub-domain definitions (Skill 2)
- `docs/POSITION_SCALE_GUARDS_v1.md` — guard peer group scale (Skill 2, guards only)
- `docs/POSITION_SCALE_WINGS_v1.md` — wing peer group scale (Skill 2, wings only)
- `docs/POSITION_SCALE_BIGS_v1.md` — big peer group scale (Skill 2, bigs only)
- `docs/POSITION_SCALE_UNIVERSAL.md` — universal sub-domain scale for #12, #24, #25, #26 (Skill 2, every evaluation)
- `docs/ARCHETYPE-WEIGHTS-GUARDS.md` — guard archetype roster (Skill 3, guards only; weights deprecated — used for archetype identification only)
- `docs/ARCHETYPE-WEIGHTS-WINGS.md` — wing archetype roster (Skill 3, wings only; weights deprecated — used for archetype identification only)
- `docs/ARCHETYPE-WEIGHTS-BIGS.md` — big archetype roster (Skill 3, bigs only; weights deprecated — used for archetype identification only)
- `docs/DOMAIN-SCALE_v1.md` — master 8×3 domain band scale (Domains × Guards/Wings/Bigs); Skill 3, every evaluation. Load selectively: preamble + only the player's position-group sub-tables for D1–D7 + the universal D8 table.
- `docs/DOMAIN-SCORE-ROLE-RELEVANCE.md` — archetype structural-zero context for domain band-matching (Skill 3)
- `docs/NON-NEGOTIABLES.md` — position gate thresholds (Skill 3)
- `docs/COMPOSITE-SCALE-AND-TIERS.md` — tier table, assignment protocol (Skill 4)
- `docs/ANCHOR-LIBRARY.md` — 96 confirmed anchor players (Skill 4)
- `docs/PROJECTION-OUTPUT-BLOCK.md` — prospect projection methodology, States 1–3 (Skill 5)
- `docs/NBA-PROJECTION-OUTPUT-BLOCK.md` — NBA vet projection methodology, ≥25 NBA games (Skill 5)
- `docs/NBA-COMP-METHODOLOGY.md` — comp assignment rules (Skill 5)
- `docs/SCRIPT-REGISTRY.md` — script-to-subdomain mapping (Skill 1)
- `docs/PUBLIC-LANGUAGE-GUIDE.md` — public editorial transform spec (Skill 7 only)
- `docs/SIGNATURES.md` — sub-domain Signature roster, tiers, descriptions, and assignment rules (Skill 7 only; also consumed by `scripts/export_public_json.py` at JSON-export reconciliation)

### Reference (load when needed):
- `docs/SUB-DOMAIN-SOURCE-MAP_v1.md` — detailed data source mapping per sub-domain
- `docs/GUARD_VALIDATION_SCORES_v1.md` — guard validation data
- `docs/PRODUCT_DESIGN_DECISIONS_v9.md` — product design history
- `docs/SCRIPT-MAINTENANCE-BACKLOG.md` — active bug tracker for the Python statistical pipeline (load on-demand when a script run produces unexpected output, or during maintenance sessions)

## CORE PRINCIPLES — NON-NEGOTIABLE

**Composite is assigned, not calculated.** Anchor library comparisons govern placement. No formula produces the composite.

**Negative Balance Rule.** For every positive attribute found, actively search for negative evidence on the same skill.

**Scoring precision.** Use the full decimal range (.0–.9 for sub-domains, .00–.99 for composites). Never default to .5 or .50 without justification.

**Qualitative validation is mandatory.** Every score needs a justifying sentence. Most critical for prospects where play-type data doesn't exist.

**Prospect ceiling.** 7.89 is the hard ceiling for pre-NBA player composites. No override path.

**Synthesis, not plagiarism.** Take what scouts observed, process through the profile, write in the system's own words.

**No document modified without Tyler confirming.** No section of any core document is modified without explicit confirmation.

## HOW TO EVALUATE A PLAYER

When Tyler says "scout [Player Name]" or "evaluate [Player Name]":

1. Confirm with Tyler at key decision points: archetype assignment, composite placement, flag review
2. Save the final deliverable to `output/[Player_Name]/[YYYY-MM-DD]_profile.md` (per-player directory, dated file — see SCHEMA-SPEC.md §10-A)

## OUTPUT STANDARD

Every finished profile saved to `output/` must pass five quality checks (QC1–QC5 in scout-output.md):
- Completeness — all 10 sections, no placeholders
- Consistency — scores match across sections
- Narrative integrity — narrative doesn't contradict scores
- Projection coherence — percentages sum correctly
- Source fidelity — no scores altered between skills

**File output discipline:** Skill 5 owns the canonical profile write to `output/`. Each evaluation produces one new dated file under a per-player directory: `output/[Player_Name]/[YYYY-MM-DD]_profile.md` (BRANCH layout per SCHEMA-SPEC.md §10-A — re-evals create new dated files; prior profiles remain immutable). Skill 7 (scout-publish) additionally writes the public editorial artifact to `output/[Player_Name]/[YYYY-MM-DD]_public.md` when invoked manually — same per-player directory, dated to match the source profile, never overwritten. Skill 1 additionally persists the research packet to `raw/[Player_Name]/[YYYY-MM-DD]_research-packet.md` — an immutable longitudinal record, not a deliverable. Skill 6 (scout-ingest) writes the structured evaluation ledger row to `wiki/evaluations.jsonl` (per SCHEMA-SPEC §14 — authoritative longitudinal series for the public ratings DB). Skills 2–4 outputs (score matrix, player profile, composite assignment) remain in-session handoffs — assembled in conversation, not persisted as separate files. Project artifacts (validation-sweep retrospectives, batch prep notes, calibration logs) live in `docs/validation/`, not `output/`.

## OBSIDIAN VAULT

Project opens as an Obsidian vault. Use `[[wikilinks]]` where the target file or heading exists; don't force them onto table-row references like ANCHOR-LIBRARY entries.
