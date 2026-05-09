# ANCHOR LIBRARY — Confirmed Composite Anchors (Index)

---

## PURPOSE

Anchor examples are confirmed players whose composite scores have been assigned. They define what a composite in that tier band looks like in practice. Every tier band should have at least one confirmed anchor before the system is used for prospect evaluation at that tier.

Current players are rated at current level. Retired players are rated at career median. Archetype is noted alongside each anchor to guide comparison — a player being evaluated should be compared primarily to anchors of the same or similar archetype.

**Anchor count:** 116 confirmed players across tiers 1–10 (as of Session 158).

---

## ORGANIZATION

The library is split into per-tier files for context-efficient just-in-time loading. Skills load only the candidate's tier file plus one neighbor on each side, not the full library.

| Tier | Band | Label | File | Anchors |
|---|---|---|---|---|
| 1 | 9.80–10.00 | All-time top 3 | [docs/anchors/Tier_1.md](anchors/Tier_1.md) | 2 |
| 2 | 9.50–9.79 | All-time top 5–10 | [docs/anchors/Tier_2.md](anchors/Tier_2.md) | 4 |
| 3 | 9.20–9.49 | Perennial All-NBA First Team | [docs/anchors/Tier_3.md](anchors/Tier_3.md) | 4 |
| 4 | 8.90–9.19 | All-NBA caliber | [docs/anchors/Tier_4.md](anchors/Tier_4.md) | 8 |
| 5 | 8.60–8.89 | Perennial All-Star | [docs/anchors/Tier_5.md](anchors/Tier_5.md) | 11 |
| 6 | 8.30–8.59 | Genuine team star | [docs/anchors/Tier_6.md](anchors/Tier_6.md) | 13 |
| 7 | 7.90–8.29 | Quality starter | [docs/anchors/Tier_7.md](anchors/Tier_7.md) | 22 |
| 8 | 7.50–7.89 | NBA starter / rotation player | [docs/anchors/Tier_8.md](anchors/Tier_8.md) | 25 |
| 9 | 6.80–7.49 | Fringe rotation | [docs/anchors/Tier_9.md](anchors/Tier_9.md) | 17 |
| 10 | 5.80–6.79 | G-League starter | [docs/anchors/Tier_10.md](anchors/Tier_10.md) | 10 |
| 11 | 4.30–5.79 | G-League rotation | *no anchors yet* | 0 |
| 12 | 3.00–4.29 | Early development | *no anchors yet* | 0 |
| 13 | 1.00–2.99 | No pathway | *no anchors yet* | 0 |

When a tier-11/12/13 anchor is added, create the corresponding `docs/anchors/Tier_{N}.md` file using the same template as the existing tier files and update this index row.

---

## LOADING POLICY

Skills read only the candidate's tier file plus one neighbor on each side (e.g., a Tier-5 candidate loads Tier_4 + Tier_5 + Tier_6). The candidate band is identified before anchor data is loaded — see [skills/scout-composite.md](../skills/scout-composite.md) Step 3.

Skip neighbor files outside the 1–10 range. If the candidate band has no anchors yet (Tiers 11–13), hold the Step 3 placement and flag for review.

For tools that need the full library as a single text blob (e.g. fact-checking in `scripts/export_public_json.py`), concatenate all `docs/anchors/Tier_*.md` files at read time. Do not reintroduce a monolithic file.

---

## MAINTENANCE

New anchors are added by Skill 5 ([skills/scout-output.md](../skills/scout-output.md) Section 11) as the final step of every scouting chain run — any player who completes the chain becomes an anchor. Each anchor is written to its tier file only; this index file changes only when the anchor count or per-tier count needs refreshing, or when a new tier file is created.

Revisions to existing anchors follow the Davion Mitchell precedent — update in place, note the prior value in the Notes column, keep the strict 10-word Notes limit.

**Tier crossings.** If a revision moves a composite across a tier band, move the row from the prior tier file to the new tier file at the correct sorted position. Composite must equal §1 Composite (linter cross-check) and the inline §11 row in the profile.

**Notes column policy** (10-word strict limit): allowed content is active injury/surgery flags, rookie/draft-class status, active non-negotiable caps, band markers, durable credential shorthand. Forbidden: session walkthroughs, methodology references (R13/R8/S96-F02 IDs), comp-tier details, profile-shape descriptions, batch-sweep references, "first X anchor" library-history notes. Detailed history lives in the per-player profile, learnings files, and git history of the tier file — never in Notes.

---

## SESSION HISTORY

When a session produces calibration sweeps, retro corrections, or batch revisions across multiple anchors, append a dated entry to the appropriate tier file's bottom under a `## Session history` section. Tier-file-local history keeps the cross-tier index lean and lets per-tier git diffs surface session changes cleanly.
