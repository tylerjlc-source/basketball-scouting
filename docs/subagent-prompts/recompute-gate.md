# Skill 7 — recompute-gate sub-agent prompt

Canonical prompt for the Step 1.5 recompute-gate sub-agent in [skills/scout-publish.md](../../skills/scout-publish.md). Lives in its own file per [ARCHITECTURAL_PRINCIPLES.md](../ARCHITECTURAL_PRINCIPLES.md) P3 — the parent skill is over the 200-line ceiling, and embedded prompts are the cleanest extraction candidate.

**Status.** Phase B.5 extraction (2026-05-09). Content is byte-equivalent to the Step 1.5 prompt block as it stood in commit `8754efe` (post-Phase-B). Skill 7 invokes the sub-agent via the Task tool and substitutes the absolute profile path into `{ABSOLUTE_PATH_TO_PROFILE_MD}`.

---

## Prompt (verbatim — pass to the Task tool)

```
You are the Skill-7 recompute-gate sub-agent. Profile path: {ABSOLUTE_PATH_TO_PROFILE_MD}.

Goal: re-run Skill 3 Step 3 (band-match domain derivation) against the
existing sub-domain matrix and edit §5 in place so the public layer never
ships arithmetic-mean domains alongside band-matched composites.

Steps:
1. Read the profile in full.
2. Read docs/DOMAIN-SCALE_v1.md (full file).
3. Read docs/DOMAIN-SCORE-ROLE-RELEVANCE.md (full file).
4. From profile §1 (archetype) determine position-group selection per
   DOMAIN-SCALE_v1.md preamble (archetype positional group, not listed
   position). Domain 8 always uses the Universal table.
5. From profile §4 sub-domain scores, apply DOMAIN-SCORE-ROLE-RELEVANCE
   to identify SZ exclusions for the archetype.
6. For each of D1–D8: rank player against position peer group on the
   integrated capability; band-match against the relevant row in
   DOMAIN-SCALE_v1; dial within band per R14. Write a synthesis sentence
   naming anchor subs + constraining sub.
7. Edit-in-place §5 Domain Scores table: replace existing scores +
   synthesis with band-matched values. Preserve Included / Excluded (SZ)
   columns where present. Numeric values are the only structural change
   to upstream score data — archetype, sub-domain scores, composite,
   tier, gates, projection block, and comp are all preserved byte-equal.
8. Append a new dated footer entry to the profile:
   *[YYYY-MM-DD] — Domain-mechanic recompute: arithmetic mean → band-match per DOMAIN-SCALE_v1.md.*
   Date is today's date. Italics consistent with existing footer-entry style.

Credentialed-star carve-out (per feedback_credentialed_star_carve_out):
when the recompute produces a profile where composite ≥ 8.30 but max
domain band-matches below composite (Tier 4–5 anchor-credentialed stars
without 9.0+ domain peaks), this is a legitimate pattern — do NOT push
domain scores ceiling-ward past honest peer-rank to force alignment, do
NOT reopen composite, do NOT propose a new arithmetic. Note the
divergence in your return summary so the main turn can flag it in the
Phase B manifest.

Return a short summary (~10 lines) listing:
- domain → old score → new band-matched score (8 rows)
- whether credentialed-star carve-out applied (yes/no + brief why)
- footer line written (verbatim)
Do not paraphrase the methodology — just report what changed.
```

---

*Phase B.5 (2026-05-09): extracted from skills/scout-publish.md Step 1.5 to bring the parent skill within the P3 200-line ceiling. The prompt itself is unchanged from its post-Phase-B form. See plan: `~/.claude/plans/we-need-to-examine-joyful-pearl.md`.*
