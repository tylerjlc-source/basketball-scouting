# Wiki Index

**Last updated:** 2026-05-02

> Page counts are dataview-derived — see `## Cross-references (by tier)` below.

## How to use this index

- Primary organization: **group → archetype → composite (descending)**
- Each player line: `[[Name]] — composite / tier` (★ marks full-chain evaluated)
- Full-chain evaluated players (have an `output/` profile) marked with ★
- Archetype wikilinks navigate to the hub page for that archetype

---

## GUARDS

### [[Jumbo Playmaker]]

```dataviewjs
const archetype = "Jumbo Playmaker"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Offensive Engine]]

```dataviewjs
const archetype = "Offensive Engine"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[All-Around Guard]]

```dataviewjs
const archetype = "All-Around Guard"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[3-and-D Guard]]

```dataviewjs
const archetype = "3-and-D Guard"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Pure Point Guard]]

```dataviewjs
const archetype = "Pure Point Guard"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Microwave Scorer]]

```dataviewjs
const archetype = "Microwave Scorer"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Slasher]]

```dataviewjs
const archetype = "Slasher"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Shooting Specialist (Guard)]]

```dataviewjs
const archetype = "Shooting Specialist (Guard)"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Defensive Specialist (Guard)]]

```dataviewjs
const archetype = "Defensive Specialist (Guard)"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Dribble Pass Shoot Guard]] — LEGACY
> Merged into [[Offensive Engine]] at S46; tags pending migration lint.

```dataviewjs
const archetype = "Dribble Pass Shoot Guard"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

---

## WINGS

### [[All-Around Wing]]

```dataviewjs
const archetype = "All-Around Wing"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Modern Four]]

```dataviewjs
const archetype = "Modern Four"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[3-and-D Wing]]

```dataviewjs
const archetype = "3-and-D Wing"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[3-and-some-D Wing]]

```dataviewjs
const archetype = "3-and-some-D Wing"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Dribble Pass Shoot Wing]]

```dataviewjs
const archetype = "Dribble Pass Shoot Wing"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Secondary Playmaker]]

```dataviewjs
const archetype = "Secondary Playmaker"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Score-First Wing]]

```dataviewjs
const archetype = "Score-First Wing"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Shooting Specialist (Wing)]]

```dataviewjs
const archetype = "Shooting Specialist (Wing)"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Defensive Specialist (Wing)]]

```dataviewjs
const archetype = "Defensive Specialist (Wing)"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Defensive-Engine Playmaker]]

```dataviewjs
const archetype = "Defensive-Engine Playmaker"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Energy Hustle Wing]] — LEGACY
> Merged into [[Defensive Specialist (Wing)]] at S47; tag pending migration lint.

```dataviewjs
const archetype = "Energy Hustle Wing"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

---

## BIGS

### [[All-Around Big]]

```dataviewjs
const archetype = "All-Around Big"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Switchable Big]]

```dataviewjs
const archetype = "Switchable Big"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Rim Protector]]

```dataviewjs
const archetype = "Rim Protector"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Stretch Big]]

```dataviewjs
const archetype = "Stretch Big"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Versatile Scoring Big]]

```dataviewjs
const archetype = "Versatile Scoring Big"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

### [[Energy Big]]

```dataviewjs
const archetype = "Energy Big"
const players = dv.pages('"wiki/players"').where(x => x.archetype === archetype).sort(x => -x.composite)
dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))
```

---

## Full-chain evaluated players (53)

Players marked ★ above. Listed chronologically by evaluation session:
- S94–95: [[Anfernee Simons]] — first 5-skill chain profile
- S96: [[Ja Morant]]
- S99 (recalibration sweep): [[Jalen Williams]], [[Shai Gilgeous-Alexander]], [[Pascal Siakam]], [[Donovan Mitchell]], [[Jaylen Brown]], [[Amen Thompson]]
- S100: [[Bogdan Bogdanović]], [[Kyle Anderson]], [[Sam Hauser]]
- S101: [[Walker Kessler]]
- S102: [[Evan Mobley]], [[Domantas Sabonis]], [[Mikal Bridges]] (re-eval)
- S103: [[Scottie Barnes]] (re-eval, archetype migration)
- S104: [[Nikola Vučević]], [[Naz Reid]] (re-eval)
- S105: [[Alperen Sengun]] (re-eval)
- S106: [[Jalen Duren]] (re-eval)
- S107: [[Myles Turner]]
- S108: [[Jayson Tatum]]
- S110: [[Joel Embiid]] (re-eval, tier crossing 7→6)
- S111: [[Anthony Edwards]] (re-eval, tier crossing 3→4 + group migration Guard→Wing + archetype migration Offensive Engine→All-Around Wing)
- S112: [[Cade Cunningham]] (re-eval, no migration — minor calibration −0.02)
- S113: [[Victor Wembanyama]] (re-eval, tier crossing 4→3 + archetype migration Switchable Big→All-Around Big)
- S116: [[Giannis Antetokounmpo]] (Path D re-eval, archetype migration Modern Four→All-Around Big — first full profile; legacy peg 9.40 → 9.30)
- S119: [[Kevin Durant]] (re-eval upgrade, no migration — anchor-cluster recalibration drift 9.32 → 9.26 from S118 sweep; first full profile, prior was legacy)
- S120: [[Tyrese Haliburton]] (legacy upgrade — composite confirmed 9.11; first full chain run on existing anchor; R13 active-injury dormancy applied — Achilles 6/2025)
- S121: [[LeBron James]] (legacy upgrade with status correction — Path D recalibration; tier crossing 1→4 (largest in any anchor revision: 9.88 career-median Retired → 8.95 active current-level); first full chain run on existing anchor)
- S122: [[Nikola Jokic]] (Path D legacy upgrade — composite 9.58 → 9.64 (+0.06 credentialing accumulation); first full chain run on existing Tier 2 anchor; archetype All-Around Big canonical fit confirmed)
- S123: [[Stephen Curry]] (Path D legacy upgrade — composite confirmed 9.20 (held); first full chain run on existing Tier 3 anchor; archetype Offensive Engine confirmed-fit)
- S124: [[Luka Doncic]] (Path D legacy upgrade — composite confirmed 9.07 (held); first full chain run on existing Tier 4 anchor; archetype Jumbo Playmaker confirmed-fit; R13 active-injury dormancy applied — hamstring 4/2026)
- S125: [[Kawhi Leonard]] (Path D legacy upgrade — composite confirmed 8.90 (held); first full chain run on existing Tier 4 anchor; archetype migration All-Around Wing → Score-First Wing per S99-F02 — defensive recalibration to functional-not-elite eliminates AAW value-driver test)
- S126: [[Devin Booker]] (Path D legacy upgrade — composite confirmed 8.92 (held); first full chain run on existing Tier 4 anchor; archetype migration Offensive Engine → All-Around Guard per S99-F02 — canonical-confirmed-fit per ARCHETYPE-WEIGHTS-GUARDS.md governance triggered S125 carry-forward Cat 3 triage; user-instructed Step 1c skip)
- S127: [[Bam Adebayo]] (Path D legacy upgrade — composite 8.84 → 8.80 + archetype migration Switchable Big → All-Around Big per S99-F02 confirmed-fit governance; first full chain run on existing Tier 5 anchor; #17 rim-protection cap firing on 4.9 vs 5.0 razor-thin C threshold)
- S128: [[Kyrie Irving]] (Path D legacy upgrade — composite confirmed 8.78 (held); first full chain run on existing Tier 5 anchor; archetype Offensive Engine confirmed-fit; R12 single-season anchor 2024-25 fragment 50 GP per S96 exception; R13 active-injury dormancy applied — ACL March 2025; S102-F02 fires 2/3 conditions, POT 8.10 delta -0.68 mid-heavy)
- S129: [[Jamal Murray]] (Path D legacy upgrade — composite 8.65 → 8.68 [+0.03 from 2025-26 career-best regular season + first All-Star]; first full chain run on existing Tier 5 anchor; archetype Offensive Engine confirmed-fit; R13 Stage 2 convergence-gate fail per S111-S112 precedent — bifurcated playoff axis (peak 2020/2023 vs recent 2024/2026 MIN, McDaniels neutralization); S102-F02 1/3 conditions — pattern does NOT fire, standard no-slot path applies)
- S135: [[De'Aaron Fox]] (Path D legacy upgrade — composite 8.51 → 8.47 (-0.04) + archetype migration Slasher → Offensive Engine; first full chain run on existing Tier 6 anchor; 2025-26 evolution drivers (career-best CAS 3PT 37.6%, first playoff series win, 2nd All-Star, 4yr extension) offset by reduced-volume Spurs role and off-dribble 3PT 29.3% structural soft spot; R13 Stage 2 convergence-gate fail per S111-S112 precedent — stat moderate shrink (-4.7 TS% delta) vs qualitative mixed-positive)
- S130: [[Jalen Brunson]] (legacy upgrade — composite 8.64 → 8.70 [+0.06 from 2024-25 All-NBA 2nd Team + Kia Clutch POTY]; first full chain run on existing Tier 5 anchor; archetype Offensive Engine confirmed-fit per anchor-library reconciliation [Skill 3 initial AAG assignment overruled by Skill 4 anchor comparison; ARCHETYPE-WEIGHTS-GUARDS.md doc-fidelity drift surfaced for Tyler triage, not auto-fixed]; R13 Stage 2 convergence-gate fail per S99-F01 strict-gate (stat shrink Δ −3.0 vs qual rise Clutch POTY/ECF run); S102-F02 1/3 conditions — pattern does NOT fire, standard no-slot path applies)
- S131: [[Tyrese Maxey]] (Path D legacy upgrade — composite 8.62 → 8.66 [+0.04 from 2025-26 leap year — 2x All-Star starter (2nd-most votes East 2026), 76ers all-time 3PT record, defensive leap with Nurse coach endorsement, leadership emergence, 2026 playoffs Game 6 historic 30/0-TO PG playoff record]; first full chain run on existing Tier 5 anchor; archetype Offensive Engine confirmed-fit; R13 Stage 2 convergence-gate fail per S111-S112 precedent — statistical neutral (TS% delta -1.2) + qualitative moderate rise; S102-F02 0/3 conditions — pattern does NOT fire, standard no-slot path applies)
- S132: [[Deni Avdija]] (first full 5-skill chain evaluation — fresh eval, not Path D legacy upgrade; Tier 7 upper-third 8.24; Dribble Pass Shoot Wing archetype with All-Around Wing runner-up — defense profile 7.0/6.8 below AAW elite-two-way standard pushes to DPS; first All-Star + MIP finalist 3rd in 2025-26 career-arc leap; both SF and PF non-negotiable gates clear; 18-strength distributed profile / zero genuine liabilities; C4 ambiguity-resolves-downward applied at Tier 6/7 boundary, anchored between Ingram 8.32 and LaMelo 8.26; R13 Stage 2 not fired — below sample minimum [1 NBA playoff series]; back-recurrence durability flag)
- S133: [[Jaren Jackson Jr.]] (Path D legacy upgrade — composite 8.60 → 8.52 [tier crossing 5→6, -0.08]; first full chain run on existing Tier 5 anchor; archetype Switchable Big confirmed-fit per ARCHETYPE-WEIGHTS-BIGS canonical-fit list; 2025-26 fragmentation [48 GP — turf toe surgery + mid-season MEM→UTA trade + season-ending PVNS left-knee surgery 2/2026] + Ringer "Least Improved" framing + multi-year BLK rate recalibration 3.0→1.4 since DPOY peak drove the -0.08 drift; R13 Stage 2 not fired — convergence-gate fail [statistical strong shrink TS% delta -5.4 + qualitative moderate, no multi-source convergence] + active-injury dormancy clause applies; Stage 1 POT moderate shrink -0.20 absorbed at Skill 5; S102-F02 firing test 2/3 conditions [significant injury YES, R13 shrink absorption YES, flat trajectory borderline at age 26 — pre-2025-26 ascending arc held] — pattern does NOT fire per Tatum S108 / Doncic S124 negative-control precedents at younger age + active-recovery framing; POT 8.60 vs composite 8.52 delta +0.08 standard no-slot path output [band midpoint 9.50 - 0.40 injury - 0.20 R13 - 0.30 physical ceiling]; Min 7.30 / Max 9.40 Moderate confidence with Max tightened from base 9.60 because rebounding floor structurally caps All-NBA ceiling regardless of recovery; lineage comp Serge Ibaka peak years; eval_window.py reported 96 GP for 2025-26 — likely trade-year double-count artifact, operative GP = 48; finding logged for SCRIPT-MAINTENANCE-BACKLOG routing)
- S134: [[Karl-Anthony Towns]] (Path D legacy upgrade — composite 8.54 → 8.42 [-0.12, tier band held]; archetype migration All-Around Big → Stretch Big per ARCHETYPE-WEIGHTS-BIGS canonical-fit list; first full chain run on existing Tier 6 anchor; uninterrupted Skills 1-6 run per Tyler request, no human confirmation gates; both 2025-26 [75 GP] and 2024-25 [72 GP] healthy — DEFAULT 60/40 eval window, no R12; #17 Rim Protection 5.0 exactly at C threshold — PASS but hard ceiling drag; defense band all 4 sub-domains 5.0-6.0 weighted across 2024-25 negative ECF + 2025-26 D-LEBRON career-best improvement; R13 Stage 2 NOT fired — convergence-gate fail [statistical moderate shrink career TS% Δ-3.4 vs qualitative high-variance + recent strong R1 ATL +11.7 TS% counter-signal, no multi-source convergence]; R13 Stage 1 moderate shrink -0.20 absorbed at Skill 5 POT; POT 8.50 standard no-slot path [band midpoint 9.50 - 0.40 flat trajectory - 0.15 injury - 0.25 physical ceiling - 0.20 R13]; Min 7.70 / Max 9.00 Tight confidence; lineage comp Lauri Markkanen current-era Stretch Big peer; legacy-anchor independent-scoring protocol applied per memory feedback — divergence drivers: archetype reclassification, deeper defensive history documentation, 2025-26 down year on offensive volume, foul rate structural concern; counter-evidence [R1 ATL strong run, defensive trajectory positive, All-Star starter] held rating in Tier 6 rather than dropping)
- S136: [[Anthony Davis]] (Path D legacy upgrade — composite 8.50 → 8.75 [+0.25, tier crossing 6→5]; first full chain run on existing Tier 6 anchor; archetype All-Around Big confirmed-fit per ARCHETYPE-WEIGHTS-BIGS canonical-fit list (Jokic, Adebayo, Davis); R12 step-back applied (S120-F01) — eval window 2024-25 [51 GP] + 2023-24 [76 GP], 2025-26 [20 GP] compromised by bilateral Achilles tendinopathy + recurring calf + hand ligament damage; uninterrupted Skills 1-6 run per Tyler request, no human confirmation gates; legacy-anchor independent-scoring protocol applied — divergence driver: healthy-baseline read of 2023-24 All-NBA 2nd + All-Def 1st + 4th DPOY peak elevated existing 8.50 anchor that had reflected injury-flag deflation; 5x S96-F02 cross-reference cap overrides applied (#15/#17/#18/#20 strength-cap and #12 vision-cap — direct empirical NBA-vet measurement); R13 STRONG RISE classification (career playoff TS% +1.5 delta, 6 playoff seasons, 2020 ring as primary scorer + 2023 WCF dagger + 2024 one-armed playoff); R13 Stage 2 NOT fired — active-injury dormancy clause (multi-source documented hand ligament + bilateral Achilles ruling out 2025-26 playoff cycle); R13 Stage 1 strong rise +0.40 absorbed at Skill 5 POT; POT 8.55 standard no-slot path [band midpoint 9.50 - 0.60 injury - 0.60 declining trajectory - 0.40 senior near-ceiling + 0.40 R13]; Min 7.55 / Max 9.05 Tight confidence with -0.50 injury risk modifier on Min; anchor comparison set Bam 8.80 / Sengun 8.45 / Embiid 8.40 (anchor-state correction applied — Embiid healthy ceiling ~8.55-8.65, Davis-prior 8.50 deflated reference not used as upper-band ceiling); lineage comp Kevin Garnett — career-arc parallel of two-way All-Around Big with availability constraints in early 30s; awards cross-check (12x All-Star, 4x All-NBA, 1x Champion 2020) supports Tier 5; trajectory drag flag — 2025-26 fragment shows first credible production decline (PPG 20.4 / BPG 1.7) layered on bilateral Achilles + second mid-season trade)
- S137: [[James Harden]] (Path D legacy upgrade — composite 8.48 → 8.40 [-0.08, tier band held]; first full chain run on existing Tier 6 anchor; archetype Offensive Engine confirmed-fit per ARCHETYPE-WEIGHTS-GUARDS canonical-fit list (Curry, Lillard, SGA — Harden craft variant w/ burst at 5.0); uninterrupted Skills 1-6 run per Tyler request, no human confirmation gates; both 2024-25 [79 GP] and 2025-26 [70+ GP] healthy — DEFAULT 60/40 eval window, no R12, no R9 (multi-season age decline = recalibration per S96-F03); LAC→CLE mid-season trade 2026-02-04 for Garland + 2nd; 3x R8 cross-ref cap fires (#5 8.6→7.8 capped by #24 cognitive ceiling, #13 9.3→8.5 capped by #9 mechanical ceiling, #15 5.5→5.0 capped by #22 physical ceiling); legacy-anchor independent-scoring protocol applied — divergence driver: explicit R13 Stage 2 STRONG (-0.15) versus likely MODERATE assumption in legacy build, anchored by 2026 Cavs-TOR series confirmation (15 combined TOs Games 3-4, "self-inflicted" by Harden's own admission) + 13th 2-2 Game 7 statistic per Windhorst; R13 STRONG SHRINK classification — qualitative-driven (career TS% Δ -2.1 statistically neutral, but elimination subset is collapse-level: 2-11 last 13 elim on 39% FG, 12 of 26 elim under 20 PTS, NBA-record Game-7 losses across 4 distinct franchises HOU/BKN/PHI/LAC); R13 Stage 2 fired -0.15 (strong shrink, multi-run pattern reshaping league-wide view); R13 Stage 1 strong shrink -0.40 absorbed at Skill 5 POT; POT 8.40 standard no-slot path [band midpoint 9.50 - 0.60 declining trajectory - 0.10 physical ceiling - 0.40 R13 Stage 1]; Min 6.20 / Max 9.40 Moderate confidence with -1.20 risk modifier on Min (negative character R13 -0.60, injury history -0.20, declining trajectory -0.40); anchor comparison set Fox 8.47 / Brunson 8.70 / Maxey 8.66 — Harden compares unfavorably on Tier-5-OE value drivers (#21 burst, decision under elim pressure) confirming Tier 6 floor below Tier 5; lineage comp Chris Paul (post-Houston facilitator era) — craft-based lead guard arc of replacing burst with manipulation + multi-franchise late-career playoff narrative drag; awards cross-check (1x MVP outside window — does not anchor floor, 11x All-Star sustained, 2024-25 All-NBA Third Team in window = Tier 6 floor signal); profile shape Distributed with 15 strengths, 0 liabilities (non-structural), 4 soft-floor watchpoints at 5.0 [#15/#21/#22/#26] all role-relevant; 2025-26 thumb fracture Feb 2026 playing through, not in eval window)
- S138: [[Jalen Johnson]] (legacy upgrade — composite 8.40 → 8.45 [+0.05, tier band held] + archetype migration Dribble Pass Shoot Wing → All-Around Wing; first full chain run on existing Tier 6 anchor; uninterrupted Skills 1-6 run per Tyler request, no human confirmation gates; eval_window.py auto-fired R12_ANCHOR with 2023-24 healthy fragment-anchor and classified 2025-26 [72 GP, 35.2 MPG] as fragment — diagnosed as MPG-band false positive driven by qualifying-set rotation_mpg skew from low-MPG early-career years; manually overrode with --season-override 2025-26 across all 7 domain scripts and used 2025-26 as primary eval window; R9 not applied (Hawks medical clearance + 72-GP healthy 2025-26 sample); legacy-anchor independent-scoring protocol applied per memory feedback — divergence drivers: (1) 2025-26 first All-Star ascension + 7.9 APG primary creator role + 13 triple-double franchise record warrant +0.05 dial, (2) archetype reclassification — DPS H-weighted off-dribble shooting value driver (Johnson #5=5.7) is the clearest profile gap whereas All-Around Wing value drivers (multi-level scoring + multi-position defense + playmaking) align cleanly; profile shape DISTRIBUTED with 19 strengths, 0 liabilities, 0 structural zeros; 2x S96-F02 R8 cross-reference cap overrides applied (#13 passing execution 7.6 above #9 touch 7.2 cap; #20 DREB 9.0 well above #23 strength 7.1 cap — both direct empirical NBA-vet measurement); R13 below sample minimum (1 NBA playoff series 2025-26 vs NYK + 2022-23 Play-In) — Stage 1 and Stage 2 both skipped, POT absorbs directional G3 win + sustained G6 51-pt-blowout output as positive trajectory note only; PF non-negotiables all clean (#20=9.0 vs 4.0; #23=7.1 vs 4.0; #16=7.0 vs 4.0); anchor comparison set Pascal Siakam 8.70 (Modern Four — comparable size + ascending arc but multi-time All-Star + championship pedigree above Johnson) / Scottie Barnes 8.55 (DEP — closest profile-shape peer, Barnes has ROY + DPOY-runner-up career arc above Johnson) / Brandon Ingram 8.32 (Score-First Wing — Johnson clearly above on D + REB + AST) / Alperen Sengun 8.45 (parallel 1st-All-Star ascension calibrating Johnson at parallel mid-Tier 6); awards cross-check 1x All-Star + MIP top-4 candidate = Tier 7 floor minimum, not constraining at 8.45; POT 9.15 standard no-slot path [composite 8.45 → 8.0+ band 9.00–9.99 → starting POT 9.05 + 0.50 ascending multi-year trajectory - 0.40 significant injury history (2024-25 shoulder labrum surgery + 2021-22 knee + Duke foot)]; Min 8.25 / Max 9.65 Tight confidence with -0.40 injury risk modifier on Min; lineage comp Pascal Siakam — All-Around Wing/Modern Four hybrid mid-career primary-creator ascent maps onto Johnson's profile shape; durability watchpoint flagged — 2025-26 was first >70-GP season since HS junior year)
- S139: [[Paolo Banchero]] (first full chain run — fresh eval, new Tier 7 anchor at 8.28; archetype Modern Four confirmed-fit per ARCHETYPE-WEIGHTS-WINGS canonical-fit list (Carmelo, Randle, Z-Bo); Tyler confirmed Wing peer group at Skill 2 boundary + explicit composite confirmation at Skill 4 per "Composite confirmation must be explicit" memory; both 2024-25 [46 GP fragment, oblique 34-GP miss] and 2025-26 [72 GP healthy] — DEFAULT 60/40 eval window, no R12 trigger, no R9 (single-source post-injury claim doesn't meet multi-source standard); profile shape DISTRIBUTED with 11 strengths, 0 liabilities (non-structural), 0 structural zeros — Modern Four has none; PF non-negotiables all PASS clean (#20=7.9 vs 4.0; #23=8.3 vs 4.0; #16=6.0 vs 4.0); 3x R8 cross-reference cap fires at Skill 2 (#6 mid-range 5.7 → 5.5 capped by #24 shot selection; #13 passing execution 7.6 → 7.1 capped by #9 touch/feel; #15 on-ball pressure 6.3 → 5.8 capped by #22 lateral quickness with R8 direct-empirical override considered but not applied — DFGPOE -0.3% essentially neutral, not clearly above cap); R13 Stage 2 convergence-gate fail per S99/S111-S112 strict-gate (career playoff TS% Δ -3.0 moderate statistical shrink + qualitative MIXED — multi-source teammate "playoff riser" language [Carter/Suggs/Black] vs Game 6 vs DET 4-20/0-9-from-3 historic shooting collapse same series in blown 24-point lead); R13 Stage 1 moderate shrink -0.20 absorbed at Skill 5 POT; S102-F02 post-peak vet check meets ≤1/3 conditions (age 23 + within-season ascending + no Embiid/Curry-tier injury history) — pattern does NOT fire, standard ascending-vet path holds; S118-F01 anti-clustering fired — 9 anchors within ±0.10 of 8.28 (Ingram 8.32, Holmgren 8.31, LaMelo 8.26, Avdija 8.24, Herro/Morant/Sabonis cluster at 8.22, Amen Thompson 8.20, Bane 8.18); profile-driven dial documented per anchor with explicit differentiation signals; anchor-state correction applied for Zion (deflated 8.08 → healthy ~8.40+) and Sabonis (deflated 8.22 → healthy ~8.35); anchor comparison set Pascal Siakam 8.70 (Modern Four — clearly above, 1 ring + 3x All-Star + 2x All-NBA + 1x MIP credential basket vs Banchero 2x All-Star + 1x ROY + 0 All-NBA; 0.42 gap reflects championship + extra credentials), Jalen Johnson 8.45 (All-Around Wing — clearly above, younger physical profile + better defense + made 2026 All-Star Banchero missed), Brandon Ingram 8.32 (Score-First Wing — roughly equivalent; Ingram more polished mid-range vs Banchero younger + more recent All-Star + better playmaker); awards cross-check 2x All-Star reserve 2024+2025 + sustained-Tier-7+ rule confirms Tier 7 floor; missed 2026 All-Star is within-evaluation-window recency signal holding below Tier 6 floor; C4 ambiguity-resolves-downward applied at Tier 6/7 boundary; POT 8.70 standard no-slot path [band midpoint 9.50 - 0.60 documented physical ceiling (multi-source explicit "lack of athleticism is legit" + Combine opt-out + burst 6.2 + lateral 5.8 sub-elite) - 0.20 R13 Stage 1 moderate shrink]; no ascending modifier (mixed trajectory: Plateau discourse + missed 2026 All-Star + within-season post-break surge); no injury history modifier (oblique + groin both fully recovered); Min 8.00 / Max 9.20 Tight confidence with -0.20 mild physical ceiling on Min (asymmetric spread -0.70/+0.50); lineage comp Carmelo Anthony — same Modern Four typology (physical mid-range creator + post game + ISO bucket-getting + average defense + sustained All-Star without championship); Wing/Big peer-group borderline (S48 boundary): physical 6'10"/250 sits at Modern Four / All-Around Big line, confirmed Wing per Tyler; Game 7 vs DET (May 3) outside evaluation window through 2026-05-02)
- S140: [[Cooper Flagg]] (legacy upgrade — composite confirmed 7.95 (held); first full chain run on existing Tier 7 anchor; archetype All-Around Wing confirmed-fit per ARCHETYPE-WEIGHTS-WINGS canonical-fit list (Kawhi, Paul George, Jaylen Brown); rookie #1 pick + 2025-26 ROY winner on 26-56 Mavericks roster (no Kyrie ACL + mid-season AD trade + GM fired Nov 11); profile shape DISTRIBUTED with 14 strengths across 6 of 8 domains, 0 liabilities (non-structural), 0 structural zeros — All-Around Wing has none; archetype-anomalous shooting cluster (CAS 5.2 / off-dribble 5.7 / mid 5.7) is the load-bearing offensive weakness — sub-30% 3PT (28.2% on 244 3PA full-season; CAS-specific 25% on 16-of-64 through mid-Jan) cleared by R1 worst-observation rule despite late-season 43.6% uptick from Dec 21; SF non-negotiables all PASS clean (#15 6.7 / #16 8.0 / #22 6.7) with PF point-forward cross-check also clean (#20 7.7 / #23 6.5 / #16 8.0); 3x R8 cross-reference cap fires (#5 capped by #24, #15 capped by #22 lateral, #17 capped by #23 strength) with S96-F02 direct-empirical override considered NOT applied at #15 (DFGPOE -0.9% only slightly above league avg) and #17 (BPG 0.9 weakside swat is qualitative not empirical) but APPLIED at #20 (DREB% 15.1% on full-season tracking clearly validates above #23 strength cap, recorded at peer-ranking 7.7); R13 not applicable — Mavs missed playoffs (12-seed West, 26-56 record); R12/R9 not applicable — single-season rookie healthy 70 GP / 33.5 MPG; R11 prospect cap NOT in effect — NBA-vet branch (>25 GP threshold); legacy-anchor independent-scoring protocol applied per memory feedback — independent profile-signature dial confirmed existing 7.95 placement (between Draymond 8.00 ceiling and rookie peers Castle 7.92 / Knueppel 7.91 floor); S118-F01 anti-clustering check fired — differentiation from Reaves 7.95 documented (different archetype profile shapes producing comparable current value: Flagg = wing primary creator with shooting hole + ROY trajectory; Reaves = established 4-yr efficient combo guard); anchor-state correction applied for Tatum (deflated 8.88 → healthy ~9.05) and Zion (deflated 8.08 → healthy ~8.40+); POT 8.50 anchor-based ascending placement [Banchero 8.28 + Jaylen Brown 8.83 + Tatum healthy ~9.05 band, capped by +0.60 pre-peak ascending allowance from DEP 7.95 → 8.55 effective ceiling]; R13 Stage 1 N/A; Min 7.65 / Max 9.00 Moderate confidence — Min reflects shooting failure + motor compounding into role-player ceiling, Max reflects All-NBA-caliber two-way wing if shooting + handle compound + physical tools mature (Tatum-Brown trajectory); skill-gap caps named: CAS 3PT development (load-bearing), lateral quickness ceiling on #15, average physical separation rules out highest-athleticism wing ceilings, heavy floater reliance (38.4% of FGA) sustainability concern; lineage comp Paolo Banchero — recent #1 pick wing ROY parallel rookie-arc shape and likely growth trajectory; Skill 1 qualitative pull ran in Sonnet 4.6 sub-agent per S121 trial — sub-domain numbering errors in Domains 4-8 headers corrected in-place via 12 targeted Edits before Skill 2 handoff)
- S141: [[Scottie Barnes]] (re-eval — composite 8.55 → 8.57 [+0.02 calibration headroom increment per memory feedback_calibration_headroom_increments]; archetype Defensive-Engine Playmaker confirmed-fit (no migration); first full-chain re-eval since S103 with raw/ packet persistence + Sonnet 4.6 sub-agent dossier per S121 trial; D5 softening drivers (#17 9.0 → 8.0 from LWB rim metric backfilling script null on D_FGA endpoint + #15 9.0 → 8.5 from DFGPOE-neutral and Sam Mitchell / Raptors Republic multi-source "on-ball weakest area" critique) partially offset by R13 Stage 2 Moderate +0.10 magnitude calibrated to active-series qualitative reshape (Barnes the Raptors' best player vs roster anchored by Donovan Mitchell + James Harden in 7-game series; career playoff TS% delta +1.7 / 2025-26 series alone +2.8 / franchise-first 30-5-10 G3); pre-modifier 8.47 differentiated above Sengun/JJ Johnson 8.45 cluster per S118-F01 anti-clustering on density + 100/100 STL+BLK feat; Tyler corrections at Skill 5 finalization (3 fields): lineage comp shift Draymond → Scottie Pippen (Barnes' offensive toolkit — mid-range iso, primary handler — exceeds Draymond's career arc), 2x All-Star credential confirmed (sub-agent dossier didn't surface 25-26 All-Star, anchored on prior eval's "1x"), hand injury watchpoint cleared (career-high 80 GP healthy in 2025-26, "feeling a lot better" entering season; Min projection 8.25 → 8.37 dropping injury adjustment); two new feedback memories saved (calibration_headroom_increments + re_eval_carry_forward_inertia); POT 8.87 standard NBA POB anchor-band path (Mobley 8.67 / Siakam 8.70 / Bam 8.80 band, ascending upper-third placement, raw POT 8.96 capped at demo+0.30 per Approaching peak Validation Check #2); profile shape DISTRIBUTED with 21 strengths, 0 liabilities, 0 SZ-liabilities — densest in DEP archetype family; lint-candidate flagged: scout-research sub-agent dossier should query current-cycle award counts as standing protocol when researching active vets)
- S142: [[Jimmy Butler]] (first full chain run — fresh eval, new Tier 7 anchor at 8.21; archetype Dribble Pass Shoot Wing with All-Around Wing runner-up — historical AAW identity gives way to current-state DPS as multiple H-weight bars (#15 6.5, #21 6.5, #22 6.6, #25 6.4) sit below All-Around Wing expectation at age 36; legacy-anchor independent-scoring protocol applied per memory feedback_legacy_anchor_independent_scoring; explicit composite confirmation gate at Skill 4 boundary per memory feedback_composite_confirmation_explicit; eval window DEFAULT 60/40 [2025-26 38 GP fragment pre-ACL + 2024-25 55 GP MIA→GSW trade season] with eval_window.py 110-GP-healthy classification of 2024-25 diagnosed as TOT-row aggregation artifact per S95-F07; profile shape DISTRIBUTED with 17 strengths across all 8 domains, 0 liabilities, 0 structural-zero liabilities (#17 5.5 + #18 6.8 are SZ-excluded from D5 average but score above liability threshold); SF non-negotiables all PASS clean (#15 6.5 / #16 7.8 / #22 6.6 vs 4.0 threshold); 3x R8 cross-reference cap fires (#13 → #9 capped 8.0 → 7.8, #15 → #22 capped 6.8 → 6.5, #24 → #11 capped 8.3 → 8.2 — all S96-F02 direct-empirical override considered, none qualified for 0.1-0.2 differential below "clearly validates above cap" threshold); R13 sample easily met (9+ playoff seasons across multiple years CHI/MIN/PHI/MIA/GSW), recency active 2024-25 GSW playoffs; R13 Stage 2 NOT fired — active-injury dormancy clause (ACL Jan 19 2026 rules out 2025-26 + most of 2026-27 playoff cycles) AND independent convergence-gate fail (qualitative axis mixed within itself: 2020 Bubble Finals + 2023 ECF MVP + 2025 Rockets validation rise vs 2025 Wolves Game 4-5 shrink with Curry sidelined "no excuse for how I played"); Stage 1 POT moderate rise +0.20 halved to +0.10 per double-count guard (named ceiling anchors Brown/Tatum/Kawhi all FMVP-pedigree wings embedding playoff signal); R9 NOT applied — 38 GP played in 2025-26 were healthy pre-injury, ACL is forward-looking Skill 5 input not retroactive Skill 2 suppressor; R12 NOT applied — single-season-compromised + active-recovery is wrong scope (Butler has not yet returned, post-injury not in active proof-of-return); awards cross-check NOT triggering upward adjustment — career resume historically Tier 5 floor (6× All-Star, All-NBA 2nd 2017, multiple All-NBA 3rd, 5× All-D 2nd, 2020 FMVP runner-up, 2023 ECF MVP) but current cycle 2025-26 + 2024-25 carries no All-NBA / All-Star selection per recency rule; full Tier 6-7 wing-creator/scorer anchor sweep per S102-F03 completed (Avdija 8.24 DPS Wing direct match, Herro 8.22 cross-position DPS, Ingram 8.32, Banchero 8.28, Jalen Johnson 8.45, Bane 8.18, Amen 8.20, Draymond 8.00 teammate); S118-F01 anti-clustering check fired clean — 8.21 differentiates from all anchors within ±0.10 with explicit per-anchor differentiation signal documented; Section 9 NBA POB Late career stage + Recovering trajectory (season-ending acute event) triggers Step 3.6 cap-floor coincidence — POT pins at DEP 8.85 (estimated from accolades since no formal peak eval exists, top-of-band single-season All-NBA 2nd/3rd lifted by playoff resume); ceiling anchor band Jaylen Brown 8.83 / Tatum 8.88 healthy ~9.05 / Kawhi 8.90; Min 7.41 [current 8.21 - 0.40 Recovering - 0.30 significant active injury - 0.20 age-acceleration risk + 0.10 GSW environment-stability mitigator] / Max 8.90 / Confidence Wide; lineage comp Dwyane Wade late-career — declining-athleticism wing creator-scorer with elite foul-draw + secondary playmaking + championship pedigree + signature playoff performances + direct on-court lineage (Butler trained extensively with Wade); Playoff_Track_Record.py timed out twice on PlayerCareerStats endpoint — likely API rate-limit on Butler's 9+ playoff seasons, R13 manually compiled from web evidence; Domain 5 LeagueDashPtDefend partial endpoint timeouts (3PT defense, rim defense, >15ft defense all returned None) — sub-domain #17 confidence Medium driven down to band-floor placement per R14; Sonnet 4.6 sub-agent qualitative pull was 3rd build under S121 trial — trial threshold reached, formal evaluation pending Tyler triage)
- S151: [[Damian Lillard]] (first full chain run — fresh eval, new Tier 6 anchor at 8.55; archetype Offensive Engine confirmed-fit per ARCHETYPE-WEIGHTS-GUARDS canonical-fit list (Curry, Lillard, SGA); R12 step-back applied (S120-F01) — eval window 2024-25 [58 GP healthy] + 2023-24 [73 GP healthy], 2025-26 [0 GP] compromised by Achilles tear April 2025 + age-36 return target 2026-27; profile shape DISTRIBUTED with 18 strengths across 7 of 8 domains, 0 liabilities, 3 structural zeros (#3/#17/#18); PG non-negotiables all PASS clean (#10 7.7 / #11 8.1 / #12 7.8 vs thresholds 4/4/5); 4x R8 cross-reference cap fires with 4x S96-F02 direct-empirical override applied (#5 → #8 capped 8.6 PnR BH 89th pctile validates above; #5 → #24 capped 7.2 off-dribble shot-making validates above; #6 → #24 capped 7.2 mid-range 44.9% on 170 FGA validates above; #20 → #23 capped 7.1 DREB% 10.6% + 60.6% chance conv validates above); R9 NOT applied — both eval-window seasons healthy regular seasons, Achilles tear post-2024-25 RS closed (Game 4 vs IND 4/27/2025); R13 sample easily met (10 playoff seasons, 68 games), recency active-injury dormant (Achilles + 2025-26 missed + age-36 return rules out next playoff cycle); R13 Stage 2 NOT fired — convergence-gate fail (statistical neutral career matched TS% Δ -2.9 + qualitative mixed: legendary peaks vs 36.1% career playoff W%) AND active-injury dormancy clause; R13 Stage 1 neutral 0 absorbed at Skill 5 POT; Tyler-flagged candidate-band correction at Skill 4 from initial Tier 5 mid-band 8.69 to Tier 6 upper-third 8.55 — driven by Harden 8.40 anchor decisiveness (direct age-35 OE PG comparison: similar eval-window output but Harden has MVP credential + active 2025-26 + 24-25 All-NBA 3rd) + age-regime Achilles recovery base rate (Billups/Parker historical precedent at age-35 Achilles tear); Hali/Kyrie/Tatum dormancy precedents declined to transfer across age regimes (Hali 25 / Kyrie 32 / Tatum 27); awards cross-check (9x All-Star, 7x All-NBA — 1 First / 5 Second / 1 Third, ROY 2013, ASG MVP 2024, 3x 3-Pt Contest including 2026 mid-rehab, 2024-25 NBA Cup champion) anchors Tier 5 healthy peak; current-state placement at Tier 6 reflects demonstrated-vs-current divergence governed by R13 active-injury dormancy + age-regime base rate; S118-F01 anti-clustering check fired clean — 6 anchors within ±0.10 of 8.55 with explicit per-anchor differentiation signals documented (Harden +0.15 / Fox +0.08 / JJJ +0.03 / Trae +0.22 / Barnes -0.02 / Maxey-floor -0.11); Section 9 NBA POB Late career stage + Recovering trajectory (active acute Achilles event) triggers Step 3.6 cap-floor coincidence — POT pins at DEP 8.55 (current composite governs forward-projection floor over distant career-peak accolade ~9.00 estimate); ceiling anchor band Harden 8.40 / Lillard self 8.55 / Maxey 8.66; Min 7.45 [current 8.55 - 0.50 Recovering - 0.40 significant injury Achilles - 0.20 age-acceleration risk] / Max 8.66 / Confidence Wide (Recovering auto-Wide); lineage comp Chauncey Billups post-Achilles — direct age-of-injury + archetype identity match (5x All-Star/1x FMVP "Mr. Big Shot" deep-range scoring PG, Achilles Feb 2012 at age 35, returned 22 GP at age 36 role-player capacity, retired effectively at 37); Tony Parker post-Achilles runner-up (less archetype overlap, cleaner statistical trajectory); Sonnet 4.6 sub-agent qualitative pull was 5th build under S121 trial — trial threshold substantially exceeded, formal trial evaluation overdue per S143 lint-candidate)
- S143: [[Trae Young]] (first full chain run — fresh eval, new Tier 6 anchor at 8.33; archetype Offensive Engine confirmed-fit per ARCHETYPE-WEIGHTS-GUARDS canonical-fit list (Curry, Lillard, SGA) with Pure Point Guard runner-up; eval window DEFAULT 60/40 [2025-26 30 GP fragment with MCL+quad/back season-ending + 2024-25 76 GP healthy classification on script criteria but qualitative chronic Achilles tendonitis "virtually every game" per Peachtree Hoops Dec 2024]; no R12, R9 considered NOT applied per S96-F03 spirit (multi-source decline framing "Is this just who Trae Young is now?" + pre-injury 2018-2023 baseline showed identical physical limitations = recalibration not temporary suppression); S108-F01 R9-spirit weighting considered NOT applied — both seasons have injury overlay, no clean healthy anchor available, default 60/40 governs; profile shape DISTRIBUTED with 9 strengths spanning Shooting/Ball Skills/Playmaking/Finishing, 3 non-structural liabilities (#15 4.5, #22 4.5, #26 4.7), 3 structural zeros (#3 2.5, #17 2.0, #18 3.0); PG non-negotiables all PASS clean (#10 6.2, #11 9.1, #12 6.5 vs thresholds 4/4/5); 3x R8 cross-reference cap fires with 3x S96-F02 direct-empirical override applied (#5 capped by #24 — pull-up 3PT 34% on 200+ attempts validates above; #6 capped by #24 — mid-range 46.2% on 70+ FGA validates above; #20 capped by #23 — DREB% 6.9% on perimeter gather posture validates above) and 1x cap binds (#13 → #9 mechanical link binds at 8.1); Tyler-flagged candidate-band correction at Skill 4 from Tier 7 mid-band 8.13 to Tier 6 bottom-third 8.33 — initial draft diagnosed as one-off reasoning error (under-weighted offensive density: 9 strengths + elite peak #11 9.1 + 4 secondary peaks ≥8.5 at #2/#6/#7/#8 is offensively Tier 5-ceiling pulled down by liabilities, not Tier 7 starter pulled up by credentials) AND too-literal awards-out-of-window interpretation (career body of work differentiates against same-band peers Ingram/Holmgren even when individual credentials are out-of-window for floor anchoring); awards cross-check 4x All-Star + 1x All-Star Starter (2024) + assist title 2024-25 + 1x All-NBA 3rd 2021-22 (out-of-window, body-of-work differentiator); S118-F01 anti-clustering check fired clean — differentiation from Garland 8.05 (-0.28 playmaking volume + foul-draw + handle elite), Morant healthy 8.22 (-0.11 inverted from initial draft — career credentials roughly equal but in-window signal favors Trae via assist title vs Morant UCL out), Ingram 8.32 (+0.01 credential basket: 4x AS + assist title + 30/20/5 historic), Holmgren 8.31 (+0.02 fully-realized profile vs projected ceiling), Harden 8.40 (-0.07 Harden's MVP + recent All-NBA 3rd separates); R13 sample met (3 series across 3 different years 2021/2022/2023) classified STRONG SHRINK (career playoff TS Δ -5.6 statistical + multi-source qualitative — 2022 MIA collapse 31.9% FG / 7-of-38 from three / more TO than AST + 2023 BOS collapse 8-of-49 from three across last 7 playoff games); R13 Stage 2 NOT fired — historical-only skip case (last playoff 2022-23, gap 3 years; active-injury dormancy clause does not apply because Trae fails recency test first per Skill 4 reading); R13 Stage 1 strong shrink -0.40 absorbed at Skill 5 NBA POB but pinned by DEP floor 8.70 (All-NBA 3rd 2021-22 accolade-derived); Career stage Peak (age 27, 8 NBA seasons), trajectory Declining (multi-source mainstream framing shifted from injury-suppressed to permanent decline + underwhelming McCollum+Kispert trade return + Hawks 0-5 in his return games + multi-injury 2024-26 cluster), POT 8.70 pinned at DEP floor (Step 3.1 hard floor binds; modifier-stack output 8.30 muted to floor); Min 7.50 / Max 8.80 Wide confidence (recent ATL→WAS trade + injury cluster + role uncertainty triggers dramatic-role-change Wide); lineage comp Steve Nash — undersized lead guard whose vision and PnR negotiation make the offense run with defensive structure that the team must always work around; full-chain unique-player count 50 → 51; pre-ingest ANCHOR-LIBRARY header correction — anchor count stale at 108 / Session stamp 140, corrected to actual rows 115 + Session 143 — backfill audit candidate suggesting prior ingests may have skipped header bump; Sonnet 4.6 sub-agent qualitative pull was 4th build under S121 trial — trial threshold substantially exceeded, formal trial evaluation should precede next sub-agent invocation)
- S154: [[Brandon Ingram]] (legacy upgrade — composite 8.32 → 8.26 [tier crossing 6→7, -0.06]; first full chain run on existing legacy anchor; archetype Score-First Wing confirmed-fit per ARCHETYPE-WEIGHTS-WINGS canonical-fit list (DeRozan, Rudy Gay, Pierce, Tobias Harris) with Dribble Pass Shoot Wing runner-up — close call resolved by mid-range identity (#6 8.7 H-weighted on SFW vs M on DPSW) + multi-source 2026 playoff "offense slowed when on floor" pattern matching Score-First over DPSW's "secondary creator that initiates offense" identity; legacy-anchor independent-scoring protocol applied per memory feedback_legacy_anchor_independent_scoring; explicit composite confirmation gate at Skill 4 boundary per memory feedback_composite_confirmation_explicit; eval window DEFAULT 60/40 [2025-26 77 GP healthy bookend + 2024-25 18 GP compromised by high-grade ankle sprain Dec 7 2024]; no R12, no R9 (current is healthy bookend after compromised prior); profile shape DISTRIBUTED with 12 strengths concentrated offensively across D1-D4+#24, 0 liabilities (non-structural), 0 structural-zero liabilities (#17 5.0 + #18 5.0 are SZ-excluded from D5 average but score above 4.9 listing threshold); SF non-negotiables all PASS clean (#15 5.5 / #16 5.5 / #22 5.5 vs 4.0 threshold); 5x R8 cross-reference cap fires (#3 → #23, #5 → #24, #15 → #22, #17 → #23, #18 → #23) with 2x S96-F02 direct-empirical override applied (#6 mid-range 8.7 — 291 FGA at 46.9% direct measurement validates above #24 cap; #20 DREB 6.7 — DREB% 14.2% on full-season tracking validates above #23 cap); R13 sample met (3 NBA playoff series 2022 NOR / 2024 NOR / 2026 TOR), recency active (2025-26 cycle concluded 2026-05-03); R13 STRONG SHRINK classification — career matched TS% Δ -5.3 statistical + multi-source qualitative "M.I.A." / "offense slowed when on floor" / "future couldn't be clearer" with 2 consecutive recent shrink runs at -12.8 (2024 vs OKC) and -13.3 (2026 vs CLE); R13 Stage 2 fired -0.10 MODERATE (not Strong -0.15 — 3-series sample with 2022 NOR positive outlier counterweight, recent runs carry injury context including 2026 heel inflammation Game 5+, "league-wide reshape" threshold not yet met per S118 calibration-headroom principle preserving next-cycle dialing room); pre-modifier composite 8.36 lower-middle Tier 6 (between Banchero 8.38 and self-prior 8.32) → -0.10 Stage 2 → 8.26 Tier 7 upper-third; band crossed Tier 6 → Tier 7, anchor comparison re-run in Tier 7 per protocol; S118-F01 anti-clustering check fired clean — 4 anchors (Avdija 8.24, Herro 8.22, Morant deflated 8.22, Sabonis 8.22) within 0.04 of 8.26 with explicit per-anchor differentiation signals documented; S111-F01 anchor-state correction applied for Morant (deflated 8.22 → healthy ~8.40+ ceiling) and Butler (deflated 8.21 → healthy ~8.40+); R13 Stage 1 strong shrink -0.40 reduced to -0.20 moderate per double-count guard (Stage 2 already fired at composite step); awards cross-check 2x All-Star non-consecutive 6-yr gap (2020 + 2026 Curry replacement) + 1x MIP 2020 = Tier 7 floor minimum, supports lower-mid Tier 6 ceiling without pushing to Tier 5; Section 9 NBA POB Peak career stage (age 28, 10 NBA seasons) + Plateau trajectory; POT 8.40 pinned at DEP floor (estimated 8.40 from MIP + 2x All-Star reserve credentials, 2019-20 MIP year as peak season not formally library-evaluated); ceiling anchor band Banchero 8.38 / Jalen Johnson 8.45 → 8.38-8.45; skill-gap caps named — defense floor (5.0-5.5 cluster #15-#22-#23), pull-up 3 (29.6%) on real volume, playoff shrink pattern (3-series career delta -5.3), lean 190-lb frame at 28 with recurring soft-tissue injury history; Min 7.80 [current 8.26 - 0.30 Plateau - 0.20 injury history - 0.10 role/team fit risk - 0.05 age] / Max 8.55 [top of anchor band 8.45 + Peak stage buffer 0.10] Moderate confidence; lineage comp DeMar DeRozan — Score-First Wing structural twin (mid-range identity + primary scoring volume + modest secondary playmaking + lean-frame defensive limitations + earlier-career playoff shrink reshaping trade narratives before late-career carry-mode runs); 2026 All-Star credential added since prior anchor (Curry replacement Feb 2026); 2026 vs CLE first-round series exit injury watchpoint — heel inflammation acute Game 5 onward + walking boot Game 7 morning, multi-source confirmed; archetype tag preserved (Score-First Wing) — no migration despite confirmed-fit listing under Dribble Pass Shoot Wing because current basketball reality (mid-range volume primary + Toronto playoff narrative + structural twin DeRozan) better matches Score-First identity; Sonnet 4.6 sub-agent qualitative pull was 6th build under S121 trial — trial threshold substantially exceeded per S143/S151 lint-candidate, formal trial evaluation overdue)
- S155: [[Chet Holmgren]] (legacy upgrade — composite 8.31 → 8.48 [+0.17, tier band held]; first full chain run on existing legacy anchor; archetype Switchable Big confirmed-fit per ARCHETYPE-WEIGHTS-BIGS canonical-fit list (JJJ, Mobley, Aaron Gordon) with Rim Protector runner-up explicitly ruled out per archetype-file flag "elite shot-blocking AND legitimate floor spacing belongs in Stretch Big, not Rim Protector"; legacy-anchor independent-scoring protocol applied per memory feedback_legacy_anchor_independent_scoring; explicit composite confirmation gate at Skill 4 boundary per memory feedback_composite_confirmation_explicit; eval window DEFAULT 60/40 [2025-26 69 GP / 28.9 MPG healthy + 2024-25 32 GP fragment compromised by iliac wing fracture Nov 11 2024]; no R12 (only one season compromised), no R9 (current is healthy — no athleticism suppression to model); divergence drivers from prior 8.31: 2025-26 cleanest healthy sample with career-best PPG (18.4) / FG% (56.1%) / TS% (63.1%), first All-Star 2026, 2024-25 NBA Champion + Finals Game 7 record blocks (most blocks in any Finals G7 ever, eclipsing Webster 1978 / Garnett 2010), Loud City-documented mechanical handle correction (wide-stance flaw resolved), Hartenstein-corroborated strength gain, 2026 R2 G1 career-high 24/12/3; profile shape DISTRIBUTED with 20 strengths across all 8 domains, 0 liabilities (non-structural), 0 structural zeros (Switchable Big has none); 4x peaks at 8.5+ (#7 8.5 / #16 8.5 / #25 8.6 / #17 8.9 — third all-time at-rim opp FG%) on lean-frame profile with two PVD soft-floors at 5.7 (#18 post defense + #23 strength); C non-negotiables all PASS clean (#17 8.9 vs 5.0 / #20 7.2 vs 5.0 / #23 5.7 vs 4.0); PF gate also clean (#20/#23/#16 all clear); 4x R8 cross-reference cap fires with 3x S96-F02 direct-empirical override applied (#15 → #23 — perimeter-D ISO PPP 0.809/62 pctile validates above strength cap; #17 → #23 — career 46.4% opp at-rim FG% 3rd all-time on full-season tracking validates above; #20 → #23 — DREB% 0.216 on full-season tracking validates above; #18 → #23 cap binds — post-up def PPP 0.820 on thin 1.1 poss/g sample fails "clearly above cap" condition); R13 sample met (3 playoff seasons 2023-24 / 2024-25 / 2025-26 in progress, 38 GP), recency active; R13 MODERATE SHRINK classification on offense (career playoff TS% Δ -4.7 statistical + Finals 3PT 15.8% qualitative shrink, 2024-25 sample post-injury-confounded per Holmgren self-acknowledgment "didn't have my pop"); R13 Stage 2 NOT fired — convergence-gate fail (qualitative axis MIXED: Game 7 closeout + 2026 R1 sweep + R2 G1 career-high = rise; pre-G7 Finals 3PT + persistent forced volume = shrink; defense never shrinks); R13 Stage 1 moderate shrink -0.20 absorbed at Skill 5 NBA POB, halved to -0.10 per double-count guard (named ceiling anchors Mobley DPOY 2024-25 + AD 2020 ring + JJJ DPOY 2023 already embody recent playoff/award credentials); S118-F01 anti-clustering check fired clean — 8 anchors within ±0.10 of 8.48 with explicit per-anchor differentiation signals documented (JJJ 8.52 healthy / Sengun 8.45 / Jalen Johnson 8.45 / KAT 8.42 / Duren 8.40 / Embiid dormant 8.40 / Harden 8.40 / Banchero 8.38); anchor-state correction applied for JJJ (out 2025-26 PVNS knee but 8.52 reflects healthy ceiling — no further correction needed) and Embiid (dormant 8.40 → healthy ceiling Tier 5 minimum, used as upper-bound reference only); awards cross-check 1x All-Star reserve 2026 + NBA Champion 2024-25 + Finals Game 7 record — Tier 7 floor minimum cleared, Tier 6 placement profile-driven not credential-driven; Section 9 NBA POB Pre-peak ascending stage (age 24, 3 active NBA seasons) + Ascending trajectory; POT 8.60 anchor-based upper-third placement [JJJ 8.52 / Mobley 8.67 / AD 8.75 band 8.52–8.75, dialed down from band top 8.75 by skill caps (strength + post-D + 51% career availability) → pre-modifier 8.70, R13 Stage 1 -0.10 → 8.60]; Min 7.98 [current 8.48 - 0.20 Ascending leap-doesn't-hold - 0.30 significant injury history (Lisfranc + iliac wing fracture, 51% career availability)] / Max 9.00 [top of anchor band 8.75 + Pre-peak ascending stage buffer 0.25] Moderate confidence with asymmetric spread reflecting durability tax on Min and Tier 4 floor entry plausibility on Max; skill-gap caps named — #23 strength structural ceiling (lean frame, mass differential vs 250+ bigs), #18 post defense vs heavy bigs (Jokic/Embiid bully concern), 51% career availability (Lisfranc 2022 + iliac wing fracture 2024); lineage comp Anthony Davis (early-prime arc) — defensive anchor skill big with championship pedigree, lean-frame ascending phase, frame development ahead; Sonnet 4.6 sub-agent qualitative pull was 7th build under S121 trial — trial threshold substantially exceeded per S143/S151/S154 lint-candidate, formal trial evaluation overdue)

---

## Sources

- **Canonical anchor table:** [docs/ANCHOR-LIBRARY.md](../docs/ANCHOR-LIBRARY.md)
- **Rubric & rules:** [docs/SCORING-RULES.md](../docs/SCORING-RULES.md), [docs/SUB-DOMAINS_v3.md](../docs/SUB-DOMAINS_v3.md), [docs/NON-NEGOTIABLES.md](../docs/NON-NEGOTIABLES.md)
- **Position scales:** [docs/POSITION_SCALE_GUARDS_v1.md](../docs/POSITION_SCALE_GUARDS_v1.md), [docs/POSITION_SCALE_WINGS_v1.md](../docs/POSITION_SCALE_WINGS_v1.md), [docs/POSITION_SCALE_BIGS_v1.md](../docs/POSITION_SCALE_BIGS_v1.md)
- **Archetype definitions:** [docs/ARCHETYPE-WEIGHTS-GUARDS.md](../docs/ARCHETYPE-WEIGHTS-GUARDS.md), [docs/ARCHETYPE-WEIGHTS-WINGS.md](../docs/ARCHETYPE-WEIGHTS-WINGS.md), [docs/ARCHETYPE-WEIGHTS-BIGS.md](../docs/ARCHETYPE-WEIGHTS-BIGS.md)
- **Full profiles:** [output/](../output/)
- **Research packets:** [raw/](../raw/) (7 player folders as of 2026-04-28 — Sengun, Duren, Turner, Naz Reid, Vučević, Tatum, Wembanyama)

## Cross-references (by tier)

```dataviewjs
const players = dv.pages('"wiki/players"').where(x => x.tier !== null).sort(x => -x.composite)
const grouped = players.groupBy(x => x.tier).sort(g => g.key)
const lines = grouped.map(g => {
  const band = g.rows[0].tier_band || "?"
  const names = g.rows.map(p => p.player).join(", ")
  return `**T${g.key}** (${band}): ${g.rows.length} — ${names}`
}).array()
lines.push(`**Total:** ${players.length}`)
dv.list(lines)
```
