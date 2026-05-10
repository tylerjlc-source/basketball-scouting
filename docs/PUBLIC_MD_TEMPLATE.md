# PUBLIC_MD TEMPLATE — `_public.md` output shape

Canonical spec for the `_public.md` artifact produced by Skill 7 (`scout-publish`). Headings are case-sensitive H2 form.

**Status.** Phase B.5 extraction (2026-05-09). Content moved verbatim from `skills/scout-publish.md`'s `## TEMPLATE — _public.md output shape` block. This file is now the canonical spec; the `PUBLIC_MD_TEMPLATE` Python string literal in [scripts/export_public_json.py](../scripts/export_public_json.py) is the implementation echo and must be kept in sync with this file. The Phase 4 export pipeline cross-checks the produced artifact against this shape at stage 1; deviations fail loud.

---

## Template

````
# [Player Name] — Public Profile

## Identity
[Vecenie paragraph 1 — Identity. Plain language: archetype, physical profile, headline credentials.]

## Strength
[Vecenie paragraph 2 — Strength evidence. Value drivers anchored to numbers and observed pattern.]

## Weakness
[Vecenie paragraph 3 — Weakness evidence. Gaps named directly.]

## Projection-verdict
[Vecenie paragraph 4 — Realistic floor, realistic ceiling, what they will and will not become.]

## Sub-domain rationales

| # | Sub-domain | Score | Signature | Public rationale |
|---|---|---|---|---|
| 1 | At-basket finishing | [score, byte-equal from profile §4] | [Signature Name] ([Tier]) when score ≥ 8.0; `—` otherwise. Athleticism Signature renders on row #21 only; #22 always `—`. Free throw row #7 always `—`. Per [docs/SIGNATURES.md](SIGNATURES.md) §3–§5. | [≤30 words, numbers in word form per PUBLIC-LANGUAGE-GUIDE §5.3] |
| ... | ... (26 rows total — all sub-domains, including structural zeros) | ... | ... | ... |

## Domain one-lines

| # | Domain | One-line |
|---|---|---|
| 1 | Finishing | [≤25 words per PUBLIC-LANGUAGE-GUIDE §7] |
| ... | ... (8 rows) | ... |

## Projection (public)

[≤2 sentences. POT/Min/Max preserved byte-equal, written in prose form. Confidence label included.]

## NBA Comp(s)

| Comp player | Comp tier | Similarity |
|---|---|---|
| [Player] | Full \| Partial \| None \| Lineage | [≤2 sentences per comp] |

## Career stats

### Regular Season

| Season | Team | GP | GS | MIN | PTS | REB | AST | STL | BLK | TOV | FG% | 3P% | FT% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [season_id] | [team] | [int] | [int] | [n.n] | [n.n] | [n.n] | [n.n] | [n.n] | [n.n] | [n.n] | .XXX | .XXX | .XXX |
| ... | ... |
| **Career** |  | **[int]** | **[int]** | **[n.n]** | **[n.n]** | **[n.n]** | **[n.n]** | **[n.n]** | **[n.n]** | **[n.n]** | **.XXX** | **.XXX** | **.XXX** |

### Playoffs

[Same shape as Regular Season. Omit this sub-section when CareerTotalsPostSeason is empty.]
````

---

## Variants and conditional sections

NBA-vet profiles with a single `**LINEAGE COMP:` in profile §10 emit one row in the `## NBA Comp(s)` table with `Lineage` in the Comp tier column (qualitative-only, no glyph). Prospect profiles emit 2–3 rows with Full / Partial / None.

**Career stats appendix shape variants** (per [PUBLIC-LANGUAGE-GUIDE](PUBLIC-LANGUAGE-GUIDE.md) §9):
- **NBA vet:** `### Regular Season` always; `### Playoffs` only when present.
- **College prospect:** `### College career` replaces both NBA sub-sections (single table; school name in Team column).
- **HS / web-fallback failure:** Entire `## Career stats` section omitted — no heading, no empty placeholder.

---

*Phase B.5 (2026-05-09): extracted from skills/scout-publish.md to bring the parent skill within the P3 200-line ceiling. The template content is unchanged from its post-Phase-B form. The `PUBLIC_MD_TEMPLATE` constant in scripts/export_public_json.py continues to echo this file. See plan: `~/.claude/plans/we-need-to-examine-joyful-pearl.md`.*
