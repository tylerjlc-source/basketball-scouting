# SIGNATURES — Public-Facing Sub-Domain Recognition System

Per-sub-domain skill recognition surfaced on the public profile. A Signature is awarded when a player's sub-domain score crosses 8.0; the tier (Proven → Generational) is set by the score band. Score-derived and deterministic — no editorial assignment.

**Status:** v1.0 — created 2026-05-08.

**Load scope:** Loaded by `skills/scout-publish.md` only. Not session-open. Not loaded by Skills 1–6. Single-skill consumer per [ARCHITECTURAL_PRINCIPLES.md](ARCHITECTURAL_PRINCIPLES.md) P1. Also referenced by `scripts/export_public_json.py` at JSON-export time for fail-loud reconciliation.

**Cross-references (do not duplicate):**
- Sub-domain definitions and "what it captures" content per [SUB-DOMAINS_v3.md](SUB-DOMAINS_v3.md). Descriptions in §2 are public-voice transforms of that content, not redefinitions.
- Numeric scores byte-equal between `_profile.md` and `_public.md` per [SCHEMA-SPEC.md §10-F](SCHEMA-SPEC.md). Signature tiers derive from those preserved numbers.
- Public voice rules (no R-codes, no rubric vocab, acronyms inline-translated) per [PUBLIC-LANGUAGE-GUIDE.md §5.3](PUBLIC-LANGUAGE-GUIDE.md).

---

## §1 — Purpose

The 4-paragraph Vecenie narrative + sub-domain rationale table communicates a player's profile, but does not quick-scan the question "what is this player elite at?". Signatures fill that gap with a per-sub-domain recognition layer surfaced as a column on the existing rationale table. Selectively awarded (only at 8.0+), they are signal-rich by design — a typical starter earns 1–4, a star earns 5–8, a generational player can carry 10+.

Signatures are deterministic from the score. They carry no editorial subjectivity at assignment time, and require no separate reasoning beyond what the sub-domain score already justifies. The reasoning lives upstream in the score matrix; the Signature is the public-facing label.

---

## §2 — The 24 Signatures

Each Signature maps to one sub-domain (or, in the Athleticism case, two combined). Free Throw (#7) is excluded — pure-isolation skill, not profile-defining. Burst (#21) and Lateral Quickness (#22) fold into a single Athleticism Signature per §4.

| # | Sub-domain | Signature | Description |
|---|---|---|---|
| 1 | At-basket finishing | **Rim Finisher** | Conversion at the basket through any means: rim finishes, touch finishes, floaters, fingerrolls, off-hand layups, and above-rim plays. |
| 2 | Contact finishing / foul drawing | **Contact Scorer** | Converting through contact and absorbing fouls. Uses body and footwork to initiate contact at the optimal moment and earn free throws. |
| 3 | Post offense | **Post Scorer** | Footwork, counters, and scoring with back to the basket. Includes post playmaking — collapsing the defense and finding cutters when doubled. |
| 4 | Catch-and-shoot 3PT | **Sniper** | Spot-up shooting off the catch from three. Footwork, release consistency, and range depth on attempts that arrive in rhythm. |
| 5 | Off-dribble shooting | **Pull-Up Shooter** | Creating own shot off the dribble. Pull-ups, step-backs, and self-generated separation moves with a clean release over a contest. |
| 6 | Mid-range | **Mid-Range Threat** | Pull-up and catch-and-shoot scoring from the elbow and baseline mid-range zones. A diminished but real weapon at the NBA level. |
| 8 | Handling / creation | **Shot Creator** | Dribble tightness, move variety, and live-dribble creation. Beats defenders with handle alone and generates scoring opportunities for self or teammates. |
| 9 | Touch / feel | **Soft Touch** | Fingertip control at the point of contact between hands and ball. Backboard finishes, fingerrolls, soft catches, and accurate pass delivery. |
| 10 | Ball security | **Sure-Handed** | Protecting possession in traffic. Two-hand securing, ball discipline on drives and in the post, and low live-ball turnover rate. |
| 11 | Court vision | **Floor General** | Reading the floor and seeing secondary options. Anticipates defensive rotations before they happen and identifies the pass that creates the open shot. |
| 12 | Decision-making | **High-IQ** | Executing the right play under pressure. Drive-kick timing, shot-versus-pass choice, late-clock decisions, and tempo management at game speed. |
| 13 | Passing execution | **Distributor** | Accuracy and touch on delivery. Threads passes through traffic, hits cutters in stride, and calibrates lob velocity and timing precisely. |
| 14 | Off-ball movement | **Off-Ball Threat** | Reading and using screens, cutting decisively, and creating space without the ball. Combines IQ with sustained motion in the half-court. |
| 15 | On-ball pressure | **Lockdown** | Guarding ball handlers with length, footwork, and intensity. Contests shots under control, stays attached through dribble moves, and forces difficult attempts. |
| 16 | Help defense | **Help Defender** | Rotations, weak-side positioning, and switching range. Reads the play before it happens and arrives at the help spot in time. |
| 17 | Rim protection | **Rim Protector** | Shot-blocking, shot-altering, and verticality at the basket. Deters drives early and changes what the offense even attempts. |
| 18 | Post defense | **Post Defender** | Holding ground in the post, denying deep catches, and contesting post finishes without fouling. Includes box-out strength after the contest. |
| 19 | Offensive rebounding | **Putback Threat** | Reading misses, evading box-outs, and creating second-chance points. Pursues offensive rebounds and converts the tip-in or putback. |
| 20 | Defensive rebounding | **Glass Cleaner** | Boxing out, securing the ball through contact, and ending opponent possessions. Locates the man before the ball and outlets cleanly. |
| 21+22 | Athleticism (combined) | **Athlete** | Burst and lateral quickness as one athletic profile. First-step explosion, vertical leap, hip mobility, and change of direction in space. |
| 23 | Strength | **Bruiser** | Functional basketball strength. Holds position, absorbs and initiates contact, sets displacing screens, and finishes through physicality at the rim. |
| 24 | Shot selection | **Shot IQ** | Taking the right shots — reading defenses, knowing when to shoot, pass, or attack. High true shooting earned through shot quality, not volume. |
| 25 | Effort / motor | **Hustle** | Relentless pursuit. Loose balls, transition sprints, deflections, and the second-effort plays that don't appear in the box score but change games. |
| 26 | Competitive character | **Competitor** | Physicality and intensity when the game is hard. Performance holds in close games, rivalry matchups, and elimination scenarios. Withstands adversity without withdrawing. |

Total: 24 Signatures.

---

## §3 — Tier System

Score thresholds are universal across sub-domains. Sub-domain scores already encode position-relative scaling (a guard's 8.2 in handling and a big's 8.2 in handling are both Proven Shot Creators — the underlying scale already does the position adjustment).

| Tier | Score range | Meaning |
|---|---|---|
| **Proven** | 8.0–8.4 | Reliable weapon; clearly above starter baseline. |
| **Elite** | 8.5–8.9 | All-Star caliber in this skill. |
| **Superstar** | 9.0–9.4 | Top 10–15 in the league at this skill. |
| **Iconic** | 9.5–9.9 | Top 5–10 active at this skill. |
| **Generational** | 10.0 | All-time elite. |

Sub-domain scores below 8.0 → no Signature awarded.

---

## §4 — Assignment Rules

**Standard rule.** For each sub-domain in the §2 table (excluding the combined Athleticism case), award the Signature when the sub-domain score is ≥ 8.0. Tier set by the score band per §3.

**Free Throw exception.** Sub-domain #7 (Free Throw) is excluded entirely. No Signature awarded regardless of score.

**Athleticism rule.** The combined Athleticism Signature is awarded when `average(#21 Burst, #22 Lateral) ≥ 8.0`. The tier is set by the average per §3.

- Example: #21 = 8.4, #22 = 7.6 → average 8.0 → **Proven Athlete**.
- Example: #21 = 9.0, #22 = 8.0 → average 8.5 → **Elite Athlete**.
- Example: #21 = 8.5, #22 = 7.0 → average 7.75 → **no Signature** (even though #21 alone is Elite).

A player earns at most one Athleticism Signature; the individual #21 and #22 scores never produce separate Signatures.

**Boundary inclusivity.** Tier ranges are inclusive on both ends within each band. A score of exactly 8.0 → Proven. Exactly 8.5 → Elite. Exactly 9.0 → Superstar. Exactly 9.5 → Iconic. Exactly 10.0 → Generational. A score of 7.9 → no Signature.

---

## §5 — Rendering

### §5.1 — Public profile (`_public.md`) sub-domain table

The sub-domain rationales table in `_public.md` carries a Signature column between Score and Public rationale. Format: `[Signature Name] ([Tier])`. No Signature → `—`.

```
| # | Sub-domain | Score | Signature | Public rationale |
|---|---|---|---|---|
| 1 | At-basket finishing  | 8.4 | Rim Finisher (Proven)        | ... |
| 4 | Catch-and-shoot 3PT  | 8.7 | Sniper (Elite)               | ... |
| 5 | Off-dribble shooting | 9.1 | Pull-Up Shooter (Superstar)  | ... |
| 6 | Mid-range            | 7.6 | —                            | ... |
| 7 | Free throw           | 8.5 | —                            | ... |
```

**Athleticism rendering.** Both #21 and #22 keep their own rows (preserves the 26-row count and parser invariants). When the average qualifies, the Athleticism Signature renders on row #21; row #22 reads `—`.

```
| 21 | Burst / explosion | 8.4 | Athlete (Proven) | ... |
| 22 | Lateral quickness | 7.6 | —                | ... |
```

Free throw row #7 always reads `—` in the Signature column.

### §5.2 — JSON export shape

Each `sub_domains[]` entry carries an optional `signature` object:

```json
{
  "id": 1,
  "name": "At-basket finishing",
  "score": 8.4,
  "rationale_public": "...",
  "signature": {
    "name": "Rim Finisher",
    "tier": "Proven",
    "description": "Conversion at the basket through any means: rim finishes, touch finishes, floaters, fingerrolls, off-hand layups, and above-rim plays."
  }
}
```

When no Signature is awarded: `"signature": null`. The `description` field is sourced from §2 verbatim — the public site renders it on hover/expand.

The Athleticism Signature is emitted on the entry for sub-domain #21 (Burst). Sub-domain #22 carries `"signature": null`.

### §5.3 — Reconciliation at export

`scripts/export_public_json.py` re-derives each Signature from the profile's sub-domain score using §3 + §4 rules and compares against the value parsed from `_public.md`. Mismatch is fail-loud, mirroring the existing score-byte-equality reconciliation pattern. The Signature in the public artifact is therefore not editorially asserted — it is mechanically validated.

---

## §6 — Voice rules for descriptions

Descriptions in §2 follow [PUBLIC-LANGUAGE-GUIDE.md §5.3](PUBLIC-LANGUAGE-GUIDE.md):

- ≤25 words.
- No R-codes, no session IDs, no rubric vocabulary.
- Acronyms expanded inline at first use within the description.
- No source attribution. No single-game references.
- Sourced from each sub-domain's "what it captures" content in [SUB-DOMAINS_v3.md](SUB-DOMAINS_v3.md), transformed for public voice. The Athlete description is authored fresh (combines Burst + Lateral as one profile).

Descriptions are static — they describe the skill the Signature represents, not the player who earned it. The description is identical whether the player is Proven or Generational at that skill.

---

*Created 2026-05-08 as part of the publishable-layer Signatures feature. Loaded by Skill 7 (`scout-publish.md`) at publish time and by `scripts/export_public_json.py` at export-time reconciliation.*
