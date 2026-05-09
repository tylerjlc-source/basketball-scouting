# DOMAIN-SCORE-ROLE-RELEVANCE.md — Archetype Exclusion Tables

**Purpose:** Feeds scout-profile.md Step 3 (domain band assignment). Identifies, per archetype, which sub-domains are structurally irrelevant to the archetype's value delivery. SZ sub-domains are excluded from the band-match read — the evaluator integrates only the role-relevant subs when ranking against the position peer group on that domain.

**Scope:** Domain scores are band-matched assignments per DOMAIN-SCALE_v1.md, not arithmetic derivations. This document governs the role-relevance filter that feeds the band-match. The "worst observation anchors the score" principle continues to govern at the sub-domain and composite levels.

**Relationship to ARCHETYPE-WEIGHTS-\* files:** Those files hold archetype identity, value drivers, and confirmed fits, and remain the source of truth for archetype identification (Skill 3 Step 1). They play no scoring role. This file informs band-match context for domain scoring; archetype identity continues to live in the weights files.

**Convention:** Each archetype lists its **structural zeros** by sub-domain number and name. Every other sub-domain is role-relevant. Archetypes with no structural zeros have all 26 sub-domains role-relevant.

---

## GUARDS

### Jumbo Playmaker
**Structural zeros:** #17 Rim protection, #18 Post defense
Guard-listed position; interior defense is not part of the archetype's value delivery regardless of size.

### Offensive Engine
**Structural zeros:** #3 Post offense, #17 Rim protection, #18 Post defense, #19 Offensive rebounding
Primary perimeter shot creator; value is perimeter creation and not interior operations or offensive-glass work.

### All-Around Guard
**Structural zeros:** #3 Post offense, #17 Rim protection, #18 Post defense, #19 Offensive rebounding
Balanced two-way guard; interior offense, interior defense, and offensive rebounding are outside the role.

### 3-and-D Guard
**Structural zeros:** #3 Post offense, #17 Rim protection, #18 Post defense, #19 Offensive rebounding
Role is catch-and-shoot plus perimeter defense; no interior value expectation on either end.

### Pure Point Guard
**Structural zeros:** #3 Post offense, #17 Rim protection, #18 Post defense, #19 Offensive rebounding, #20 Defensive rebounding
Smallest-footprint guard role; rebounding on either glass is not part of the value delivery.

### Microwave Scorer
**Structural zeros:** #3 Post offense, #17 Rim protection, #18 Post defense, #19 Offensive rebounding, #20 Defensive rebounding
Instant offense role only; rebounding and interior defense sit outside the archetype.

### Slasher
**Structural zeros:** #3 Post offense, #17 Rim protection, #18 Post defense
Downhill perimeter attacker; some glass work is expected at the guard level, but interior offense and interior defense are outside the role.

### Shooting Specialist (Guard)
**Structural zeros:** #3 Post offense, #8 Handling / creation, #11 Court vision, #13 Passing execution, #17 Rim protection, #18 Post defense, #19 Offensive rebounding, #20 Defensive rebounding, #23 Strength
Catch-and-shoot offensive weapon; self-creation handle, advanced playmaking, interior defense, rebounding, and physical contribution are outside the role. Off-dribble shooting and mid-range remain role-relevant — the archetype is defined by shooting identity and cannot be structurally indifferent to shooting sub-domains.

### Defensive Specialist (Guard)
**Structural zeros:** #3 Post offense, #5 Off-dribble shooting, #6 Mid-range, #17 Rim protection, #18 Post defense
Defense-and-effort role; self-creation scoring and interior defense sit outside the archetype. Passing execution remains role-relevant — a guard who cannot pass at a functional level will not hold minutes even in a defensive role.

---

## WINGS

### All-Around Wing
**Structural zeros:** none — all 26 sub-domains role-relevant
Elite two-way archetype; no dimension is outside the role.

### Modern Four
**Structural zeros:** none — all 26 sub-domains role-relevant
Size-skill hybrid operating inside and out; every sub-domain contributes to the profile.

### 3-and-D Wing
**Structural zeros:** #3 Post offense, #19 Offensive rebounding
Perimeter-only role on both ends of the floor.

### 3-and-some-D Wing
**Structural zeros:** #3 Post offense, #19 Offensive rebounding
Same offensive identity as 3-and-D Wing with a lower defensive ceiling; structural zeros match.

### Dribble Pass Shoot Wing
**Structural zeros:** #17 Rim protection, #18 Post defense
Wing creator; interior defense is outside the role. Post offense and other dimensions are real contributors.

### Secondary Playmaker
**Structural zeros:** #3 Post offense, #5 Off-dribble shooting, #6 Mid-range, #17 Rim protection, #18 Post defense, #19 Offensive rebounding
Low-usage ball mover; self-creation scoring, interior defense, and offensive glass are outside the role.

### Score-First Wing
**Structural zeros:** #17 Rim protection, #18 Post defense
Volume scorer who may post up; only interior defense is structurally outside the role.

### Shooting Specialist (Wing)
**Structural zeros:** #2 Contact finishing / foul draw, #3 Post offense, #8 Handling / creation, #11 Court vision, #13 Passing execution, #17 Rim protection, #18 Post defense, #19 Offensive rebounding, #20 Defensive rebounding, #23 Strength
Catch-and-shoot offensive weapon at wing size; self-creation handle, advanced playmaking, contact finishing, interior defense, rebounding, and physical contribution are outside the role. Off-dribble shooting and mid-range remain role-relevant — the archetype is defined by shooting identity and cannot be structurally indifferent to shooting sub-domains.

### Defensive Specialist (Wing)
**Structural zeros:** #3 Post offense
Wing defenders are expected to contribute at the rim, in post defense, and on the glass — only post offense is structurally outside the role.

### Defensive-Engine Playmaker
**Structural zeros:** #4 Catch-and-shoot 3PT, #5 Off-dribble shooting, #6 Mid-range
Near-zero scoring threat by archetype design; all jump-shooting sub-domains are outside the value profile. Post offense and every defensive/playmaking dimension remain role-relevant.

---

## BIGS

### All-Around Big
**Structural zeros:** none — all 26 sub-domains role-relevant
Modern franchise big; the entire board contributes.

### Switchable Big
**Structural zeros:** none — all 26 sub-domains role-relevant
Defensive-first big with offensive functionality across the board; no dimension is outside the role.

### Rim Protector
**Structural zeros:** #4 Catch-and-shoot 3PT, #5 Off-dribble shooting, #6 Mid-range, #8 Handling / creation, #13 Passing execution
Interior-only offense; perimeter shooting, self-creation, and advanced passing are outside the role.

### Stretch Big
**Structural zeros:** #3 Post offense
Floor-spacing is the identity; post offense is structurally outside the archetype. Floor-spacing bigs with a real post game are typically All-Around Big or Versatile Scoring Big instead.

### Versatile Scoring Big
**Structural zeros:** none — all 26 sub-domains role-relevant
Scoring big with weak but genuine defensive contribution; defensive dimensions are low-ceiling, not structurally irrelevant.

### Energy Big
**Structural zeros:** #4 Catch-and-shoot 3PT, #5 Off-dribble shooting, #6 Mid-range, #8 Handling / creation, #11 Court vision, #13 Passing execution
Finishing and rebounding role through effort and athleticism; perimeter shooting, self-creation, and advanced playmaking are outside the archetype.

---

*Authored Session 99. Replaces the scoring role previously served by the H/M/L/N weight gradient in ARCHETYPE-WEIGHTS-\* files. Archetype identity, value drivers, and confirmed fits continue to live in the weights files.*
