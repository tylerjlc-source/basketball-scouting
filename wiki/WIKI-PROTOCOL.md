# WIKI PROTOCOL

Schema and maintenance rules for the basketball-scouting wiki layer.

**Load scope:** Task-loaded at wiki-related work only (P1). Not session-open governance.

---

## PURPOSE

The wiki is a persistent, LLM-maintained graph layer sitting between canonical project data and query/lint workflows. It does NOT replace any existing file — it aggregates and cross-references them.

| Layer | Owner | Purpose |
|---|---|---|
| `docs/` | Tyler | Canonical schema — rubric, scales, rules, anchor table |
| `skills/` | Tyler | 5-skill evaluation chain |
| `raw/` | Skill 1 | Immutable per-player research packets |
| `output/` | Skill 5 | Canonical finished profiles |
| `wiki/` | LLM | Derived graph — player pages, archetype hubs, index, log |

**Source of truth order:** `docs/` > `output/` > `raw/` > `wiki/`. If wiki contradicts upstream, upstream wins — wiki is corrected, not vice versa.

---

## FOLDER STRUCTURE

```
wiki/
├── WIKI-PROTOCOL.md    ← this file
├── index.md            ← catalog of pages, by group + archetype
├── log.md              ← append-only change history
├── players/            ← one page per anchor (evaluated or legacy)
└── archetypes/         ← one page per archetype hub
```

Filenames use spaces (Obsidian-native). Example: `wiki/players/Anfernee Simons.md`. This differs from `output/` which uses underscores. The difference is scoped per folder and does not leak.

---

## PAGE TEMPLATES

### Player page

All player pages use this template. `has_profile: true` for full-chain-evaluated players; `has_profile: false` for legacy anchors (ANCHOR-LIBRARY row only).

```markdown
---
player: [Full name]
group: [Guard | Wing | Big]
archetype: [Archetype name]
composite: [X.XX]
tier: [1-13]
tier_band: [X.XX–X.XX]
status: [Active | Retired | Injury flag | YYYY draft class]
competition_level: [NBA | College D1 | International | HS]
has_profile: [true | false]
profile_path: [output/First_Last/YYYY-MM-DD_profile.md | null]
scored_session: [N | null]
last_updated_session: [N | null]
rubric_version: [v3 | unknown]
pot: [X.XX | null]
# Scoring fields below are present only when has_profile: true (mirrored from profile Sections 4 + 5)
sd01_at_basket_finishing: [X.X | null]
sd02_contact_finishing: [X.X | null]
sd03_post_offense: [X.X | null]
sd04_catch_shoot_3pt: [X.X | null]
sd05_off_dribble_shooting: [X.X | null]
sd06_mid_range: [X.X | null]
sd07_free_throw: [X.X | null]
sd08_handling_creation: [X.X | null]
sd09_touch_feel: [X.X | null]
sd10_ball_security: [X.X | null]
sd11_court_vision: [X.X | null]
sd12_decision_making: [X.X | null]
sd13_passing_execution: [X.X | null]
sd14_off_ball_movement: [X.X | null]
sd15_on_ball_pressure: [X.X | null]
sd16_help_defense: [X.X | null]
sd17_rim_protection: [X.X | null]
sd18_post_defense: [X.X | null]
sd19_offensive_rebounding: [X.X | null]
sd20_defensive_rebounding: [X.X | null]
sd21_burst_explosion: [X.X | null]
sd22_lateral_quickness: [X.X | null]
sd23_strength: [X.X | null]
sd24_shot_selection: [X.X | null]
sd25_effort_motor: [X.X | null]
sd26_competitive_character: [X.X | null]
d1_finishing: [X.X | null]
d2_shooting: [X.X | null]
d3_ball_skills: [X.X | null]
d4_playmaking: [X.X | null]
d5_defense: [X.X | null]
d6_rebounding: [X.X | null]
d7_athleticism: [X.X | null]
d8_iq_motor: [X.X | null]
---

# [Full name]

**[[Archetype]]** [group] — composite **[X.XX]** (Tier [N]). [One-sentence identity.]

## Anchors in context

**Tier neighbors:**

```dataviewjs
const p = dv.current()
const peers = dv.pages('"wiki/players"')
  .where(x => x.tier === p.tier && x.player !== p.player)
  .map(x => ({player: x.player, composite: x.composite, delta: Math.abs(x.composite - p.composite)}))
  .array()
  .sort((a, b) => a.delta - b.delta || a.composite - b.composite || a.player.localeCompare(b.player))
  .slice(0, 4)
dv.list(peers.map(x => `[[${x.player}]] (${x.composite.toFixed(2)})`))
```

**Archetype peers:**

```dataviewjs
const p = dv.current()
const peers = dv.pages('"wiki/players"')
  .where(x => x.archetype === p.archetype && x.player !== p.player)
  .sort(x => -x.composite)
dv.list(peers.map(x => `[[${x.player}]] (${x.composite.toFixed(2)})`))
```

## Library history
[Verbatim Notes column from ANCHOR-LIBRARY.md. If blank: "No update history recorded."]

## Sources
- Full profile: [output/First_Last/YYYY-MM-DD_profile.md](...) | (legacy — no profile)
- Research packets: [list raw/... paths | none]
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
```

### Archetype hub

```markdown
---
archetype: [Name]
group: [Guard | Wing | Big]
---

# [Archetype name]

[1–2 sentence definition from ARCHETYPE-WEIGHTS-*.md]

## Anchor roster (by composite, descending)

```dataviewjs
const archetype = dv.current().archetype
const roster = dv.pages('"wiki/players"')
  .where(x => x.archetype === archetype)
  .sort(x => -x.composite)
dv.table(
  ["Composite", "Tier", "Player", "Status"],
  roster.map(x => [x.composite.toFixed(2), `T${x.tier}`, x.file.link, x.status ?? ""])
)
```

## Source documents
- Definition: [docs/ARCHETYPE-WEIGHTS-*.md](...)
- Structural-zero tables: [docs/DOMAIN-SCORE-ROLE-RELEVANCE.md](../../docs/DOMAIN-SCORE-ROLE-RELEVANCE.md)
```

---

## RULES

**W1 — docs/ and output/ are never modified by wiki operations.** The wiki reads from them; upstream writes govern. If wiki and upstream disagree, upstream wins.

**W2 — Verbatim preservation of library history.** Notes column in ANCHOR-LIBRARY.md contains load-bearing calibration history (drift corrections, R13 firings, archetype migrations). Wiki pages preserve Notes verbatim — no summarization.

**W3 — No hallucinated summaries for legacy anchors.** If a player has no full profile, do not synthesize a summary from memory. State "Legacy anchor — no full profile" and show metadata only.

**W4 — Wikilinks resolve or don't exist.** Do not wikilink to a player who doesn't have a wiki page. Either create the page or use plain text.

**W5 — Filenames: spaces in wiki/, underscores in output/ and raw/ — do not cross.** `wiki/players/Anfernee Simons.md`, `output/Anfernee_Simons/YYYY-MM-DD_profile.md`, and `raw/Anfernee_Simons/YYYY-MM-DD_research-packet.md` are all correct for their folders. Do not rename across folders.

**W6 — Frontmatter is load-bearing.** All fields in the template must be present. If unknown, use `null` or `unknown` — never omit.

**W7 — Score frontmatter mirrors profile, sourced from Sections 4 + 5.** When `has_profile: true`, the 26 sub-domain (`sd01_*..sd26_*`) and 8 domain (`d1_*..d8_*`) score fields are populated from the profile's Section 4 (sub-domain table Score column) and Section 5 (domain summary Score column). These power Obsidian radar/spider plots via dataviewjs. Profile is the source of truth — wiki scores are mirrored, not authored. When a domain has no role-relevant inputs (all sub-domains SZ for the archetype), domain score = mean of the SZ sub-domains as fallback so every domain has a numeric value (radar plots cannot render N/A). `has_profile: false` pages omit all score fields.

**W8 — Body content is dataview-derived; only frontmatter is hand-maintained.** Player pages, archetype hubs, and index.md group/tier sections all use `dataviewjs` blocks that read frontmatter at render time (peer lists, archetype rosters, tier groupings, cross-references-by-tier). Edits target frontmatter only — bodies auto-refresh on render. Direct edits to dataview-rendered content are anti-patterns: the next render reverts them while the source frontmatter stays stale. Manual narrative sections (Library History, Sources, the chronological evaluated-players list in index.md) are explicit exceptions — they capture per-player history and per-evaluation annotations that aren't derivable from frontmatter.

**W9 — POT exposed in frontmatter; Min/Max intentionally excluded.** The `pot` field mirrors the central projection (POT) from profile Section 9 (NBA POB) or Section 9 Block 2 (prospect POB) and powers Obsidian dataview queries + the public ratings DB ceiling-search surface. The Min/Max range is deliberately not exposed in frontmatter — the public-facing rating surface should expose ceiling level (POT), not the full uncertainty band. Min/Max remain in the profile narrative (Section 9) for evaluator review and longitudinal audit; they are not queryable. When a profile has not been recomputed under the new schema (or has no profile), `pot: null`. Adding `pot_min` / `pot_max` fields is an anti-pattern — surface the question to Tyler before touching this rule.

---

## NON-GOALS

- The wiki is not a substitute for ANCHOR-LIBRARY.md. The canonical anchor table stays in docs/.
- The wiki does not score players. All scoring happens in Skills 1–5.
- The wiki is not public-facing. Product 2's rating site would be a presentation layer built on top.

---

*Created 2026-04-24. Schema for the wiki layer, Step 2 of the Karpathy wiki buildout (see `project_karpathy_wiki_buildout` memory).*
