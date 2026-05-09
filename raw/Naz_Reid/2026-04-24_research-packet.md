# Research Packet — Naz Reid — 2026-04-24

=== RESEARCH PACKET ===
PLAYER: Naz Reid
POSITION: C / PF (listed C, plays both)
AGE: 26 (born 1999-08-26)
TEAM: Minnesota Timberwolves
COMPETITION LEVEL: NBA (7th pro season; undrafted 2019 out of LSU)
EVALUATION DATE: 2026-04-24

--- EVALUATION WINDOW ---
Mode: DEFAULT (2-season, no R12 trigger)
- 2025-26 (w=0.60): 77 GP, 26.1 MPG — healthy (shoulder injuries late season; see Injury History)
- 2024-25 (w=0.40): 80 GP, 27.5 MPG — full healthy season (eval_window.py mislabeled as "fragment" — S100-F01 family bug; 80 GP is unambiguously healthy per R12 eligibility floor ≥58 GP)
**Flags (S100-F01):**
- eval_window 2024-25 "fragment" label is incorrect (80 GP healthy season; ≥58 threshold clearly met)
- Domain 1 Synergy PostUp offense block not in output (sub-#3 stats gap)
- Domain 5 rim-specific endpoints (Opp FG% at rim, DFGPOE at rim) returned N/A
- Consistent with Vucevic-run S100-F01 bug family — scoring unaffected; qualitative compensation documented per sub-domain

--- PHYSICAL PROFILE ---
Height:         6'9.5" no shoes / 6'10" w/ shoes (2019 NBA Draft Combine)
Wingspan:       7'3.25" (+5" over-standing; very strong for C at his height)
Weight:         255.8 lbs at combine (14% body fat); current playing weight 249–260 (sources vary — Wolves lists 264)
Standing reach: Not published (typical C-range given height + wingspan)
Vertical:       Not published from combine
Lane agility:   Not published
Body type:      "Guard-like fluidity and pace with the size and skills of a stretch big" — quick-twitch athletic big, more mobility than Vucevic-type finesse; genuine PF/C positional flexibility; "great physical specimen"

--- DOMAIN 1 — FINISHING ---

**Statistical (weighted 2-season):**
- Rim FG%: 67.9% (69.8 cur / 65.9 prior); Non-Dunk Rim 65.5%
- Rim FGA volume: 186.4 weighted
- % Shots at Rim: 20.8% (LOW for C — stretch profile)
- Dunk Rate: 14.1% (moderate — more than 2× Vucevic's 6.6%; real but not elite vertical finisher)
- % Assisted at Rim: 73.7%
- FT%: 75.1% (73.2 cur / 77.6 prior); career 72.8%
- FTR: 0.147 (low but above Vucevic's 0.127)
- Drives/g: 4.04 (higher than Vucevic 3.04)
- Drive FG%: 48.9% (lower than Vucevic 53.2%)
- Drive PPP: 0.758 (higher than Vucevic 0.573 — more productive drives)
- Paint non-RA FG%: 47.5%

**Qualitative:**
- "Very good footwork on the perimeter and low block, with soft touch around the basket and shows some craft on his layups" (NBADraft.net / Peachtree Hoops 2019 draft profile — still accurate per current observation)
- "Punishing smaller mismatches in the low post with surgical footwork and hook shots" (SLAM cover story, 6MOTY context)
- "Used his guile and foot speed to make seven of eight shots from two-point territory, including a trio of layups in transition and a hook and a runner in the more structured half-court set" (Reid workout / MinnPost)
- "Post Hook Rating 82" (2K26 context — directional, not authoritative)
- Footwork: "fancy footwork... and-one score" (NBA.com highlight framing)
- Contact: not a foul-draw specialist; "self-molded, 'Little Big Man' hybrid through alternating steady bursts of three-point shooting and dribble penetrations"

**Data gaps:**
- Sub-#3 Post offense PPP: Synergy PostUp offense block absent from Domain 1 output (S100-F01). Qualitative language exists but no direct measurement. Medium confidence.
- Contact finishing quality in late-game / contested scenarios — thin specific evidence.

--- DOMAIN 2 — SHOOTING ---

**Statistical (weighted 2-season):**
- CAS 3PT%: 37.8% (38.1 cur / 37.3 prior) — strong for a big
- Corner 3%: 40.3% (stronger than Vucevic 32.6%)
- ATB 3%: 35.6%
- Total 3PA volume: 453.6 weighted
- Pull-Up 3PT%: 34.3% (30.2 cur / 41.2 prior) — real off-dribble shooting threat (unlike Vucevic at 20%)
- PU Zone 3PT%: 35.7%; PU Zone Mid%: 0.0% (doesn't shoot mid-range off dribble)
- ISO PPP: 0.823 (38.1 pctile) on 32 poss — functional
- Mid-Range FG%: 34.1% (30.0 cur / 42.9 prior) — current season materially worse (possible shoulder impact)
- Mid-Range FGA: 35.2 (low volume)
- FT%: 75.1% (73.2 cur / 77.6 prior); career 72.8%
- Clutch FT%: 71.9%
- TS%: 57.0% | eFG%: 55.2% | 3PT%: 36.9%

**Qualitative:**
- "Knockdown shooter and secondary creator" (Dunking with Wolves)
- "Cashing in corner threes" (SLAM)
- "Flexes the svelte brawn and finely-honed finesse... alternating steady bursts of three-point shooting and dribble penetrations"
- 2023-24: 41% from three on real volume
- Current-season dip flagged: "shooting struggles since beginning of March... clear he's dealing with an injury" (RotoWire — shoulder)
- "Late-season 2025-26 dip: 11.8 PPG, 40.5% FG since March 1 (18 games)" (multi-source)

**Data gaps:**
- Pull-up 3PT prior-vs-current split (30.2% vs 41.2%) shows meaningful drop in current season — confounded by shoulder injury. Healthy-baseline read is the 41.2% prior-season number.
- Mid-range volume too low (35 FGA weighted) to draw strong conclusions; 30.0 current vs 42.9 prior also confounded.

--- DOMAIN 3 — BALL SKILLS ---

**Statistical (weighted 2-season):**
- ISO PPP: 0.823 (38.1 pctile) on 32 poss — moderate volume, below-average efficiency
- PnR BH PPP: 0.788 (38.4 pctile) on 46 poss — **real secondary-handler sample** (unlike Vucevic's 0 poss)
- Handoff PPP: 1.055 on 42 poss — functional DHO contributor
- Touches/G: 49.0 (NOT a hub — lower than Vucevic's 61.5)
- Dribbles/Touch: 1.03 (twice Vucevic's 0.59 — more ball-handling volume per touch)
- Drives/G: 4.0 (slightly more than Vucevic 3.0)
- Drive FG%: 48.9% | Drive TOV%: 7.5% | Drive AST/G: 0.3
- USG%: 21.1%
- Floater FG% (4–14ft): 46.2% (47.5 cur / 44.0 prior) on 246 FGA (27.7% of total shots) — lower conversion than Vucevic (53.6%) but real volume
- Non-Dunk Rim FG%: 65.5%
- TOV per 100 Touches: 3.1 (2025-26: 3.3 / 2024-25: 2.9) — higher than Vucevic's 2.3
- Estimated TOV%: 9.6
- A:TO: 1.48 (materially weaker than Vucevic's 2.37)

**Qualitative:**
- "Handles well on the move for his size and can put the ball on the floor and shake his man" (NBADraft.net / Peachtree Hoops)
- "Guard-like fluidity and pace" (SLAM)
- "Good court vision and passing ability for a big man and can pass out of a drive"
- Pull-up threat + drive threat combo is genuine — unusual for a big

**Data gaps:**
- Live-dribble creation against NBA starters is limited-sample; most creation comes against backup bigs/wings in bench role.

--- DOMAIN 4 — PLAYMAKING ---

**Statistical (weighted 2-season):**
- Passes/G: 34.4 | Potential AST: 3.4 | Actual AST: 2.2 (much lower volume than Vucevic hub-role 45.2/5.7/3.4)
- Conv rate: 66.3% (higher than Vucevic's 59.3% — he converts his reads)
- Secondary AST: 0.3 | FT AST: 0.1
- Adjusted AST: 2.6 | Adjusted AST %: 7.7%
- AST Points Created: 5.8/g
- A:TO: 1.47
- Cut PPP: 1.122 (5-33 pctile, weak cutter) on 39 poss
- OffScreen PPP: 0.964 (40-64 pctile) on 100 poss
- Transition PPP: 1.146 (35-63 pctile) on 168 poss — moderate transition finisher
- Off speed: 4.49 mph (higher than Vucevic's 4.16)

**Qualitative:**
- "Secondary creator" role with Gobert/Edwards (Dunking with Wolves)
- "Development as a passer was significant, as he went from averaging 1.9 assists per 36 minutes in 2023-24 to 3.0 assists per 36 in 2024-25" (RotoWire)
- "Good court vision and passing ability for a big man and can pass out of a drive"
- Not an offensive hub — runs complementary / secondary playmaking role
- Plays next to Mike Conley / Anthony Edwards / Donte DiVincenzo who run primary creation

**Data gaps:**
- Decision quality specifically in pressure / high-leverage moments is thin-sourced qualitatively; regular-season clutch stats (Domain 8) imply weak performance.

--- DOMAIN 5 — DEFENSE ---

**Statistical (weighted 2-season):**
- #15 On-Ball Pressure:
  - Opp FG% (Overall): 46.0% | DFGPOE: −1.5% (better than Vucevic's −1.1%)
  - Deflections: 1.7/g | STL: 0.9/g | Contested shots: 5.9/g
  - PF/g: 2.5
  - ISO Defense PPP: 0.883 on 2.4 poss 2-season (tiny sample; no classification)
- #16 Help Defense:
  - DEF_RATING: 109.5 (109.9 cur / 108.8 prior) — **significantly better than Vucevic's 115.3** (Gobert-anchored team defense context)
  - Charges drawn: 0.05/g | Def loose balls: 0.29/g | Def box-outs: 0.80/g
  - BLK/g: 1.0
- #17 Rim Protection:
  - **Rim-specific endpoints returned N/A** — S100-F01 endpoint gap. BLK/g: 1.0 (cross-ref) is moderate; Contested 2PT/g: 3.6.
- #18 Post Defense:
  - PostUp Defense PPP: 1.436 on **0.7 poss/g 2-season total** — sample far too thin to be primary signal. Script percentile (1-28th) is driven by tiny sample variance.
  - Def box-outs/g: 0.80

**Qualitative:**
- Coach Chris Finch (Spring 2024): "Defensively, Naz has been outstanding. He has taken a lot of different matchups, and in his switching, Naz creates a lot of transition opportunities for us."
- "Reid shows how versatile he is as a player as he navigates around the screen on the perimeter and recovers to the driving James to get the block and rebound"
- "Reid has more often shown the ability to guard in space on the perimeter"
- "One strategy the Wolves could more often employ with Gobert off the court is switching one through five in pick-and-roll coverage as Reid has more often shown the ability to guard in space"
- "Great at rim protection; he's gotten a lot of blocked shots since we came back from the (All Star game) break"
- **Key caveat:** "Gobert's rim protection covers up for Randle and Reid, who have notably struggled (on defense) when Rudy is on the bench" (Canis Hoopus)
- Two-way signal: genuine switchability on perimeter + block-chasing instinct; but defensive results are Gobert-amplified — struggles without the anchor

**Data gaps:**
- Rim-specific DFGPOE endpoint N/A blocks direct rim-protection measurement. Qualitative + BLK/g (1.0) are the available signals.
- Post defense PPP at 0.7 poss/g is too thin to be meaningful — Gobert absorbs most post matchups.
- On-without-Gobert splits would be diagnostically useful but not pulled by script.

--- DOMAIN 6 — REBOUNDING ---

**Statistical (weighted 2-season):**
- REB/g: 6.12 | OREB/g: 1.2 | DREB/g: 4.96 (notably lower than Vucevic's 9.08)
- OREB%: 4.2% | DREB%: 18.1% | REB%: 11.3% (all meaningfully below Vucevic)
- Contested rate: 37.8% | DREB contested %: 33.2%
- Box-outs/g: 0.84–1.03 (much lower than Vucevic's 1.98–2.14)
- Avg REB distance: 5.3 ft

**Qualitative:**
- "Reid navigates around the screen on the perimeter and recovers to the driving James to get the block and rebound"
- Rebounding is not an archetype-defining strength — playing next to Gobert (elite rebounder) suppresses Reid's numbers, but per-minute rates also show Reid is a modest-volume big rebounder rather than a pursuit-driven one
- No explicit "crashes the glass" framing; no negative "doesn't rebound" framing either

**Data gaps:**
- On-without-Gobert rebounding splits would clarify opportunity-vs-skill, but not pulled.

--- DOMAIN 7 — ATHLETICISM ---

**Statistical (movement proxies, weighted 2-season):**
- Avg speed: 4.21 mph (faster than Vucevic's 3.96) | Off: 4.49 | Def: 3.94
- Distance/g: 1.94 mi
- Dunk Rate: 14.1% (moderate — 2× Vucevic's 6.6%)
- Drives/G: 4.0 at 48.9% FG — modest but real

**Qualitative:**
- "Guard-like fluidity and pace with the size and skills of a stretch big"
- "Good footwork... foot speed" — multi-source
- "Handles well on the move for his size"
- "Ability to guard in space on the perimeter" — defensive athleticism signal
- "Switching one through five" framing from coach
- Strength: 255+ lbs combine weight, plays both PF and C; per Canis Hoopus holds on interior defensively within Gobert system; no "gets backed down" language

**Data gaps:**
- No combine vertical / lane agility / shuttle published from 2019 Combine.
- Strength is inferred from weight + positional durability + no negative framing; no direct measured-strength data.

--- DOMAIN 8 — IQ / MOTOR ---

**Statistical (weighted 2-season):**
- Shot clock distribution: 2.3% 24-22 | 11.4% V.Early | 17.0% Early | 53.3% Average | 8.7% Late | 7.4% V.Late — healthy, average-heavy
- Defender distance: Very Tight 4.9% | Tight 37.7% | Open 23.9% | Wide Open 33.5% | Contested %: 42.6%
- **Clutch (2-season weighted, 57 GP): 0.6 PTS, 26.8% FG, 14.0% 3P, 60.8% FT, +/− −1.1, 0.0 AST, 0.1 TOV** — weak clutch production across 57 games sample
- Hustle: 1.7 deflections/g, 0.80 def box-outs/g, 0.29 loose balls/g, 0.05 charges/g

**Qualitative:**
- "His two-way game and high motor provide the Wolves optionality up front behind Gobert and Randle" (RotoWire)
- Contract extension 5yr/$125M June 2025 — team's confidence in him as core piece
- Undrafted-LSU-to-6MOTY arc — work ethic framing is multi-source positive
- **Recent negative motor signal (2025-26):** "Muted effort off bench" (CBS Sports 2025-26 headline, RotoWire echo)
- **Clutch paradox:** Coach Finch calls him "fourth-quarter hero" in specific playoff moments (2024 vs Nuggets Game 4, 2025 Round 1 Lakers series), BUT regular-season clutch stats show significant shrinkage (26.8% FG, 14.0% 3P on 57 GP sample) — the coach's narrative and the aggregate data diverge
- "Reid embodies the weirdness of being a bench player in the playoffs" (Zone Coverage 2025)
- 2025-26 late-season slide: "Critics noted that the Timberwolves will need more from Reid if they want to get past the first round"
- Basketball IQ: "reads the game well" per Finch; "good court vision and passing ability for a big man"

**Data gaps:**
- Competitive character in high-leverage moments is mixed-signal — needs careful interpretation (positive playoff spot-moments vs statistical clutch shrinkage).
- Whether the "muted effort" framing is shoulder-injury-related or genuine motor signal is ambiguous.

--- CHARACTER / PROJECTION SIGNALS ---

**Work ethic evidence:**
- Undrafted 2019 → 6MOTY 2023-24 → 5yr/$125M extension 2025 — trajectory reflects sustained development
- Multi-source respected-pro framing; "cult following" (SLAM)
- Coach endorsement consistent across 6+ years

**Competitive character evidence:**
- Coach Finch: "Naz shows up in the fourth quarter again" (playoff-specific)
- Playoff-specific highlight games exist — 2024 Round 1 vs Nuggets Game 4 fourth quarter; 2025 Round 1 Lakers series 5.4 4Q PPG at 9/11 FG, 6/6 from three
- 6MOTY voting beat Malik Monk by 10 points (competitive respect from voters)

**Negative signals:**
- Statistical clutch (regular-season last 5 min ±5): 26.8% FG, 14.0% 3P, +/− −1.1 across 57 GP — real negative pattern in non-playoff crunch time
- "Muted effort off bench" 2025-26 framing
- 2025-26 late-season scoring dip (11.8 PPG / 40.5% since March 1) likely injury-confounded but also productivity concern
- 2025-26 playoffs current: 3 GP, 7.0 PPG, TS 44.2% (−12.3 delta) — small sample; could be shoulder-impacted
- Critics: "Timberwolves will need more from Reid"

**Trajectory:**
- **Ascending through 2024-25** (14.2/6.0/2.3 career highs at 27.5 MPG)
- **Plateau/slight regression in 2025-26** (13.7/6.2/2.3 at 26.1 MPG; late-season 11.8 PPG; shoulder injury confound)
- Age 26 — still in ascending-to-peak window; not yet a decline signal
- New contract signals continuation of current role for 5 years

--- PLAYOFF / BIG-GAME TRACK RECORD (R13 applies) ---

**Sample:** Met (4 playoff seasons: 2022-23, 2023-24, 2024-25, 2025-26 [in progress])
**Recency status:** Active (currently in 2026 playoffs vs Nuggets; gap = 0)

**Statistical (matched-season basis, Playoff_Track_Record.py):**
- Playoff TS%: 59.0% (39 games / 4 seasons)
- Regular TS%: 58.0% (315 matched-season games)
- **Delta TS%: +1.0** (at strong-rise threshold boundary)
- Playoff PPG: 9.7 | Regular PPG: 12.4 | Delta: −2.7 (volume drops in playoffs, reserve role)
- Playoff FGA: 7.5/g | Regular FGA: 9.9/g

**Last 3 playoff runs:**
- 2025-26 (ongoing, MIN): 3 GP, TS% 44.2% (vs RS 56.5%, **−12.3**), 7.0 PPG — **small-sample collapse**, likely shoulder-impacted
- 2024-25 (MIN): 15 GP, TS% 64.5% (vs RS 57.7%, **+6.8**), 10.4 PPG — clear rise
- 2023-24 (MIN, WCF run): 16 GP, TS% 56.9% (vs RS 59.5%, −2.6), 11.1 PPG — mild shrink

**Qualitative:**
- Multi-source positive playoff-moment framing: "Naz shows up in the fourth quarter" (Finch), "stellar fourth quarter boosts Timberwolves' playoff aspirations" (BVM Sports 2024), "crucial shots for Timberwolves in Game 4's fourth quarter" (Star Tribune 2024)
- 2025 Round 1 Lakers: 5.4 4Q PPG at 9/11 FG, 6/6 from three — elite specific-moment efficiency
- Mixed signals: "Reid has faced inconsistencies in his playoff performance despite a strong regular season," "Timberwolves will need more from Reid if they want to get past the first round" (2025-26 current framing)
- No "disappears in big games" anchor language either

**Classification (manual, per R13):**
- Stat signal: Career matched delta +1.0 TS% = **strong statistical rise boundary** (script hint agrees); 2024-25 +6.8 is a real multi-game signal; 2023-24 mild shrink offsets; 2025-26 collapse confound is small-sample
- Qualitative signal: **mixed-positive** — multi-source playoff clutch-moment framing supports rise, but not dominant convergent rise narrative
- **R13 Stage 1 POT modifier classification: Moderate rise (+0.20)** — stat crosses strong-rise threshold but qualitative is mixed-positive rather than strongly convergent; R13 Moderate = "stat OR qualitative rise, ≥2 runs" fits cleanly
- **R13 Stage 2 composite modifier:** Strict convergence gate requires stat AND qualitative convergence — qualitative doesn't clearly converge on rise given the mixed 2025-26 signal. **Stage 2 does NOT fire** under strict-gate interpretation (per Mobley/Barnes precedent with Directional being the only sample-disciplined magnitude when signals mix).
- Alternative Stage 2 view: Directional Rise +0.05 is defensible IF evaluator interprets qualitative as leaning rise enough; leave for Skill 4 decision.

--- INJURY HISTORY ---

**2025-26 season (current eval window):**
- **Left shoulder soreness** mid-January 2026 — ruled out after 5 min vs San Antonio; returned soon after
- **Right shoulder injury** picked up March 2026 vs OKC — persisted through end of regular season; maintenance approach, missed final 2 regular-season games
- Shoulder cluster correlates with **late-season shooting slide** (11.8 PPG, 40.5% FG since March 1, 18 games)
- Cleared for Game 1 playoffs 2025-26 (not on injury report vs Nuggets)
- Right ankle twist vs Suns earlier in season — minor, returned same game

**R9 consideration:**
- Named injury: ✓ (right shoulder + left shoulder)
- Multi-source: ✓ (RotoWire, SI, Hoops Rumors, Dane Moore on X)
- Pre-injury baseline: ✓ (pre-March 2026 shooting was at career norms; 2024-25 was 80 GP healthy with 37.3% CAS 3PT)
- Mechanism: ✓ (shoulder → shooting decline is mechanism-consistent)
- **R9 applies narrowly to #4/#5/#6 shooting sub-domains, not athleticism** (R9 canonically covers #21/#22/#15). Given the shoulder mechanism affects shooting specifically, evaluator judgment at Skill 2: score from weighted data (already includes prior-season 40% healthy anchor) but note injury context in rationale — do NOT apply R9 formally since it's not an athleticism suppression case.

**R12 consideration:**
- 2025-26: 77 GP healthy baseline (even with shoulder dip late) = anchor-eligible
- 2024-25: 80 GP full healthy season = anchor-eligible
- **R12 NOT triggered.** Default 60/40 eval window stands.

**Career:**
- Broadly durable — consistent 70+ GP seasons
- No major surgeries or multi-week absences through 2024-25
- Minor ankle, shoulder soreness events in 2025-26

--- DATA GAP INVENTORY ---

**Strong support (3+ sources):**
- Physical profile (combine + multiple reports)
- Shooting stretch identity (CAS 3PT + scouting language + 6MOTY narrative)
- Switchable defense signal (Finch + Canis Hoopus + Dunking with Wolves + Zone Coverage)
- Post scoring / footwork (draft profiles + ongoing coverage)
- Secondary handling / drive threat (Peachtree + SLAM + stats)
- Rebounding baseline (stats + no negative framing)
- Character / work ethic (multiple pieces)
- Gobert-pairing defensive context (multi-source explicit)

**Moderate support (2 sources):**
- Hub-passing capability (secondary creator language, stats modest)
- Clutch signal — positive playoff-moment vs negative regular-season clutch stats (mixed)
- Shoulder injury impact on 2025-26 performance
- 6MOTY award context (multiple)

**Weak support (1 source or thin sample):**
- Post defense PPP (0.7 poss/g — too thin)
- ISO defense PPP (2.4 poss total — tiny)
- Pull-up 3PT prior-vs-current split interpretation (shoulder confound)

**No direct evidence:**
- Vertical leap / lane agility / bench press (2019 combine didn't publish or didn't test)
- Strength direct measurement (inferred from weight + positional durability)
- Rim-specific defensive splits (script endpoint N/A)

**Conflicting signals:**
- Clutch: Finch fourth-quarter-hero framing vs statistical clutch shrinkage (26.8% FG, 14.0% 3P on 57 GP) — both real signals
- 2025-26 trajectory: career-year peak in 2023-24/2024-25 vs plateau/slight regression in 2025-26 — confounded by shoulder injury
- R13: +1.0 matched delta (strong boundary) with +6.8 2024-25 rise vs −12.3 2025-26 small-sample collapse

**Script output bugs flagged (S100-F01 family):**
- eval_window.py: 2024-25 labeled "fragment" at 80 GP — incorrect (≥58 GP threshold clearly met); use as healthy anchor
- Domain 1 script: Synergy PostUp offense block absent — sub-#3 stats gap
- Domain 5 script: rim-specific endpoints (Opp FG% at rim, DFGPOE at rim) returned N/A — sub-#17 stats thin
- NBA_Comp_Stats.py (deferred to Skill 5): BLK%/STL% endpoint None likely to recur per Vucevic-run pattern

=== END RESEARCH PACKET ===
