# scripts/

Index of every Python script in this folder. The production statistical pipeline (Domain_1–Domain_8, NBA_Comp_Stats, Playoff_Track_Record, Public_Career_Stats, Public_Narrative_Stats, export_public_json) is documented in detail in [docs/SCRIPT-REGISTRY.md](../docs/SCRIPT-REGISTRY.md) — start there for endpoint mappings, sub-domain coverage, and CLI usage. This file lists what's here and which skill calls it; the registry is the source of truth for *how* each one runs.

Known issues: [docs/SCRIPT-MAINTENANCE-BACKLOG.md](../docs/SCRIPT-MAINTENANCE-BACKLOG.md).

## Domain stat scripts (Skill 1: scout-research)

| Script | Domain | Detail |
|---|---|---|
| `Domain_1_Finishing__Stats.py` | At-basket + contact finishing | [SCRIPT-REGISTRY](../docs/SCRIPT-REGISTRY.md) |
| `Domain_2_Shooting__Stats.py` | CAS 3PT, off-dribble, mid-range, FT | [SCRIPT-REGISTRY](../docs/SCRIPT-REGISTRY.md) |
| `Domain_3_Ball_Skills__Stats.py` | Handling, touch, ball security | [SCRIPT-REGISTRY](../docs/SCRIPT-REGISTRY.md) |
| `Domain_4_Playmaking__Stats.py` | Court vision, decision-making, passing, off-ball | [SCRIPT-REGISTRY](../docs/SCRIPT-REGISTRY.md) |
| `Domain_5_Defense__Stats.py` | On-ball, help, rim protection, post defense | [SCRIPT-REGISTRY](../docs/SCRIPT-REGISTRY.md) |
| `Domain_6_Rebounding__Stats.py` | OREB, DREB | [SCRIPT-REGISTRY](../docs/SCRIPT-REGISTRY.md) |
| `Domain_8_IQ_Motor__Stats.py` | Shot selection, motor, competitive character | [SCRIPT-REGISTRY](../docs/SCRIPT-REGISTRY.md) |

There is no Domain_7 script — Domain 7 (Athleticism) is sourced from biometrics + scouting reports, not API stats.

## Other production scripts

| Script | Called by | Purpose |
|---|---|---|
| `NBA_Comp_Stats.py` | Skill 5 (scout-output) | Statistical similarity data for prospect NBA Comp matching. Per-position TS%/USG% etc. |
| `Playoff_Track_Record.py` | Skill 1 (scout-research) | R13 playoff-vs-regular-season delta summary for players with ≥2 qualifying playoff runs. |
| `Public_Career_Stats.py` | Skill 7 (scout-publish) | Career per-game tables (RS + Playoffs) for `_public.md` appendix. |
| `Public_Narrative_Stats.py` | Skill 7 (scout-publish) | Narrative-section stats (e.g. zone splits, drive volume) for the public profile body. |
| `export_public_json.py` | Skill 7 (scout-publish) | Final transform: `_public.md` → `published/[Player].json`. Entry point for the public ratings DB. |

## Helpers (imported by other scripts; not run directly)

| Script | Purpose |
|---|---|
| `eval_window.py` | Resolves the 2-season evaluation window (current + prior season weights). Imported by every Domain script + comp/playoff scripts. R12 injury-window override logic lives here. See [docs/EVAL-WINDOW-AUTOMATION.md](../docs/EVAL-WINDOW-AUTOMATION.md). |
| `shared_math.py` | Single source of truth for the weighting math (`volume_weighted_pct`, `simple_weighted`, `stat_block`) and safe-coercion helpers (`safe_int`, `safe_float`, `safe_round`, `safe_div`, `safe_get`). Replaces the duplicated copies that previously lived in each Domain script. |

## Lint / QC

Run after a profile is written; not part of the live evaluation chain. Each one reports what's wrong; doesn't auto-fix.

| Script | Checks |
|---|---|
| `lint_profile.py` | Internal `_profile.md` files: section completeness, score consistency, frontmatter integrity. Skill 5 QC6. |
| `lint_public.py` | Public `_public.md` files: editorial-voice rules, omitted internals, section completeness. Skill 7 QC. |
| `qc_profile.py` | Cross-section consistency for finished profiles (sub-domain → domain → composite alignment). |
| `audit_player_frontmatter.py` | `wiki/players/*.md` frontmatter audit (composite, archetype, evaluation-date format). Skill 6 housekeeping. |

## One-off migrations (kept for reference)

These were used once to migrate the wiki to a new layout. Not part of any active workflow.

| Script | Done |
|---|---|
| `migrate_to_dataview.py` | Original migration to Dataview-rendered wiki pages. |
| `migrate_hubs_to_dataview.py` | Archetype-hub conversion. |
| `migrate_index_groups_to_dataview.py` | Index-page grouping conversion. |

## Subfolder

`experiments/` — research-tooling experiments. **Not production.** Currently holds Firecrawl test packets relocated out of `raw/` per the rule that `raw/` is production-only. See `experiments/firecrawl/README.md` for context.
