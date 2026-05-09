# SUB-DOMAIN SOURCE MAP — Layer 1 Scouting Rubric Data Reference
**Defines where data comes from, how to access it, and how much to trust it for each sub-domain.**
**Companion to SUB-DOMAINS_v3.md — that file defines WHAT to evaluate. This file defines WHERE to get the data.**
**Governed by SCORING-RULES.md R2 (signal hierarchy), R3 (competition temper), R4 (confidence tiers).**

## DATA SOURCE REGISTRY

| Source | Coverage | Cost | Access type | API available? |
|---|---|---|---|---|
| NBA.com (nba_api) | NBA | Free | 🟢 Automated | Yes — Python package |
| Basketball-Reference | NBA + College | Free | 🟢 Scrapeable | No official API |
| Hoop-Math | College D1 | Free | 🟢 Scrapeable | No official API — scraper build required |
| CBBpy (ESPN PBP) | College D1 | Free | 🟢 Automated | Yes — Python package |
| Cleaning the Glass | NBA | ~$5/mo | 🟡 Manual lookup | No API |
| EvanMiya | College D1 | ~$30/mo or $180/yr | 🟡 Manual lookup | Unknown — inquiry pending |
| Synergy/Sportradar | NBA + College + Intl | Unavailable | 🔴 Requires B2B | Yes but requires org relationship |
| FIBA box scores | International | Free | 🟡 Manual per player | No |

## CONFIRMED INFRASTRUCTURE BUILDS REQUIRED
1. Hoop-Math scraper (college rim FG%, shot distribution, % assisted)
2. CBBpy integration (college PBP parsing for shot type classification — dunks, layups)
3. NBA.com pipeline via nba_api (restricted area FG%, play type, player tracking data)

## FUTURE ACCESS — PARTNERSHIP INQUIRIES (post-proof-of-concept)
- EvanMiya: API or data export? Licensing?
- Cleaning the Glass: Bulk access or licensing?
- Synergy/Sportradar: Re-evaluate if org structure changes

---

## EVALUATION WINDOW — 2-SEASON DEFAULT (S83 Decision)

**NBA-level evaluation uses a 2-season window with 60/40 recency weighting.**

- Current season weight: 0.60
- Prior season weight: 0.40
- Method: Volume-weighted for percentages (FG%, FT%, etc.). Simple weighted average for rate stats (FTR, ISO PPP, drive rate).
- Rationale: Single-season splits are noisy, especially for traded players or players with partial seasons. A 2-season window smooths variance while reflecting current ability. Established S83-F05.
- Exception: Rookies or players who missed the entire prior season use current season only.
- Pipeline implementation: Both seasons queried independently with explicit season parameters. Weighted composite computed in Python.

---

## Domain 1: Finishing

---

### #1 — At-Basket Finishing

**Block A — Primary Statistical Input (co-primary: efficiency + volume)**

*Updated Session 82: Volume elevated to co-primary alongside rim FG%. Finding S82-F01 — rim FG% alone fails to discriminate among guards (2.4pp spread across four dramatically different finishers). Volume context is essential.*

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | Restricted Area FG% (0-4 ft) | NBA.com via nba_api | 🟢 Automated | Efficiency (co-primary) |
| NBA | % of shots at rim + raw rim FGA | NBA.com via nba_api | 🟢 Automated | Volume (co-primary) |
| College | FG% at Rim (layups + dunks + tips) | Hoop-Math | 🟢 Scraper build required | Efficiency (co-primary) |
| College | % of FGA at rim | Hoop-Math | 🟢 Scraper build required | Volume (co-primary) |
| College (corroboration) | Opponent-adjusted 2PT% | EvanMiya | 🟡 Manual lookup — blends rim with non-rim twos, use as corroboration not primary | Corroboration only |
| International | Points in the paint per game, normalized for usage | FIBA box scores via web search | 🟡 Manual per player | Combined proxy |

**Why co-primary (updated Session 82):** FG% at the rim measures conversion quality. But the four-guard validation test (Irving 67.6%, Fox 65.8%, Smart 65.4%, Hield 65.2%) showed only 2.4 percentage points of spread across players who should be dramatically different finishers. Volume — how often the player actually goes to the rim — is the discriminator. Smart's 26 rim attempts across a full season at 21 MPG is not data sparsity; it's definitive evidence that he's not a finisher (S82-F03). Rim FG% and volume must be read together as co-primary stats. High rim FG% on low volume scores near baseline. Low volume at real minutes IS the signal.

**Block B — Secondary Statistical Inputs**

*Updated Session 82: % of shots at rim elevated to co-primary (Block A). % assisted at rim and finish rate against shot blockers confirmed as essential — prioritized for script build.*

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | % assisted at rim | Hoop-Math (college) / nba_api (NBA) | 🟢 Both buildable | Separates self-creators from catch-and-finish players. A center finishing lobs at 70% is a different profile than a guard finishing self-created drives at 60%. Feeds archetype assignment. Essential at scale for wings/bigs; confirms for guards. |
| 2 | Dunk rate (dunks as share of rim attempts) | CBBpy PBP parsing (college) / nba_api (NBA) | 🟢 Both buildable — college requires PBP shot type classification | Separates athletic finishers from craft finishers (S82-F02). Irving 0.5% dunk rate vs Fox 8.6% — non-dunk rim FG% reveals true touch (Irving 67.4% vs Fox 62.6%). Style descriptor, not quality ranking — dunk rate should NOT penalize legitimately athletic finishers. |
| 3 | FT% | Basketball-Reference (both levels) | 🟢 Scrapeable | Mechanical proxy for touch. When rim FG% data is sparse or unavailable, 85%+ FT% signals soft hands. Sub-65% caps the finishing ceiling. Most useful for international prospects where rim-specific data doesn't exist. |
| 4 | Finish rate against shot blockers | nba_api matchup data (NBA only) | 🟢 NBA only / 🔴 College | Best discriminator between college finishers and NBA-translatable finishers. Confirmed as potential score-mover (Session 82). Doesn't exist at college level. Prioritized for script build. |
| 5 | Left/right hand splits | nba_api player tracking (NBA only) | 🟢 NBA only / 🔴 College | Single-hand dependency is a negative balance anchor per SUB-DOMAINS. At college level, this is qualitative-only — no statistical source exists. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports (NBADraft.net, 247Sports, On3, The Ringer, ESPN) | 6 | 🟢 Web search during player research | Independent multi-source. Convergence across three reports is a real signal. Synergy percentile rankings regularly cited in these reports — capture those when found. |
| Single-source scouting report | 7 | 🟢 Web search | Directional only. Midpoint rule applies to all positive language per R1. |
| Recruiting-context coach quotes | 8 | 🟢 Web search | Directional only. Never primary justification. Coaches in recruiting mode inflate finishing language. |

**Key language triggers from SUB-DOMAINS:**

Positive (midpoint rule): "soft hands around the rim," "creative finisher," "uses the glass"

Negative (anchoring — caps the score): "struggles against length," "gets his shot blocked at the rim," single-hand dependency language

**Synergy data note:** Play-type efficiency (e.g., "97th percentile finishing at rim per Synergy," "1.15 PPP on cuts") regularly appears in published scouting reports and prospect write-ups. Capture and log these during web search research. They function as high-quality secondary signals even though we can't query Synergy directly.

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Max vertical leap | NBA Combine / Pro Day results | 🟢 Web search — combine results are publicly published | Sets ceiling for above-rim finishing. Elite vertical (36"+) expands the finishing toolkit. Below-average vertical narrows the finishing profile but doesn't kill the score — craft finishers exist. |
| Wingspan | NBA Combine / Pro Day / FIBA testing | 🟢 Web search | Longer wingspan extends finishing angles. +4" differential creates structural advantage against rim protectors. |
| Standing reach | NBA Combine / Pro Day | 🟢 Web search | Combined with vertical, defines the player's finishing plane relative to the rim. |

N/A for NBA-level evaluation — physical profile is already known and integrated into career performance data.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Rim FG% primary (Hoop-Math or nba_api) + at least two of: % shots at rim, % assisted, dunk rate, FT% as proxy | ±0.5 |
| Medium | Rim FG% primary + one secondary stat OR opponent-adjusted 2PT% (EvanMiya) + two independent qualitative sources converging | ±1.0 |
| Low | Single stat (overall 2PT% only, no rim split) OR single qualitative source | ±1.5 |
| Very Low | Inferred from physical profile and role only — no finishing data available | ±2.0 |

Practical note: For college prospects with a Hoop-Math profile + EvanMiya 2PT% + one qualitative source, the default is Medium confidence. High requires the secondary splits (assisted %, dunk rate) which are buildable from Hoop-Math + CBBpy. For international prospects without Hoop-Math coverage, default is Low unless FIBA box score data + multiple qualitative sources push it to Medium.

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 9.0+ | — | — | — | *Populate when elite finisher profiles are built (e.g., Kyrie Irving)* |
| 7.0–8.5 | Zion Williamson (confirmed) | 68.0% at rim (career) | nba_api | Above-rim dominant. Power finishing profile. |
| 5.0–6.5 | — | — | — | *Populate as mid-tier profiles are built* |
| 3.0–4.5 | — | — | — | *Populate as limited finisher profiles are built* |

---

### #2 — Contact Finishing / Foul Drawing

**Block A — Primary Statistical Input**

| Level | Stat | Source | Access |
|---|---|---|---|
| NBA | Free throw rate (FTA/FGA) | Basketball-Reference via scraping OR nba_api | 🟢 Automated |
| College | Free throw rate (FTA/FGA) | Hoop-Math (listed as FTA/FGA) | 🟢 Scraper build required |
| College (enhanced) | Opponent-adjusted FTR | EvanMiya | 🟡 Manual lookup — better version, adjusts for opponent and usage |
| International | FTA per game relative to positional peers | FIBA box scores via web search | 🟡 Manual per player |

**Why FTR is the primary:** This is confirmed by the research. FTR is universally available at every level of competition, directly measures how often a player earns trips to the line, and is the consensus stat for contact-seeking behavior across analytics communities. The enhanced version (SFLD% from Cleaning the Glass — how often a player draws fouls specifically on shot attempts) is a better isolation of the skill, but it only exists at the NBA level behind a manual lookup.

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Free throw percentage | Basketball-Reference (both levels) | 🟢 Scrapeable | Drawing the foul is worthless if the player can't convert. Sub-65% FT is a negative balance anchor per SUB-DOMAINS. FTR and FT% together tell the complete contact-finishing story. |
| 2 | SFLD% (shooting fouled percentage) | Cleaning the Glass (NBA only) | 🟡 Manual lookup, $5/mo | Isolates foul-drawing on shot attempts from floor fouls and loose-ball situations. The purest version of the primary stat. NBA-level only. |
| 3 | AND1% (and-one conversion rate) | Cleaning the Glass (NBA only) | 🟡 Manual lookup | Finishing *through* contact on made baskets. The single purest contact finishing signal. NBA-level only. |
| 4 | Drive rate + paint FG% | nba_api Player Tracking (NBA) / EvanMiya partial (college) | 🟢 NBA / 🟡 College manual | High drive rate combined with high paint FG% signals conversion through contact, not around it. At college level, EvanMiya's scoring volume and 2PT% together approximate this. |
| 5 | FTR trend across competition levels | Cross-source — HS to college to NBA where available | 🟡 Manual aggregation | Declining FTR as competition rises is a negative balance anchor — the skill doesn't translate. Requires stitching data from multiple sources manually. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | Convergence on contact language is meaningful. "Gets to the line" from three independent sources is a real signal. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule on positive language. |
| Recruiting-context coach quotes | 8 | 🟢 Web search | Directional only. |

**Key language triggers from SUB-DOMAINS:**

Positive (midpoint rule): "gets to the line," "draws contact," "uses his body well," "hard to stop without fouling"

Negative (anchoring): "soft," "avoids contact," "goes around defenders rather than through them," foul-drawing via shot-fake manipulation rather than physical contact-seeking

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Weight relative to position | NBA Combine / Pro Day / FIBA testing | 🟢 Web search | Heavier players absorb contact more effectively. Below-position-average weight is a structural flag — cross-reference #23 strength. |
| Body composition | Combine medical / visual from film / scouting reports | 🟢 Web search for combine data; qualitative otherwise | Functional weight matters more than scale weight. 210 with documented muscle ≠ 210 with poor composition. |

N/A for NBA-level evaluation.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | FTR primary + FT% + at least one of: SFLD% (CtG), drive rate, FTR trend, AND1% | ±0.5 |
| Medium | FTR primary + FT% OR FTR + one qualitative convergence | ±1.0 |
| Low | FTR alone (no FT% context) OR single qualitative source | ±1.5 |
| Very Low | Inferred from physical profile and role only | ±2.0 |

Practical note: Any college prospect with Hoop-Math FTR + Basketball-Reference FT% + one qualitative source reaches Medium. Adding EvanMiya's opponent-adjusted version can push toward High if there's also a qualitative convergence. SFLD% and AND1% are NBA-only enrichments via Cleaning the Glass manual lookup.

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 9.0+ | — | — | — | *Populate with elite foul-drawers (e.g., Harden, Embiid)* |
| 7.0–8.5 | Zion Williamson (confirmed) | 10.4 FTA/36 career | Basketball-Reference | Elite contact-seeking. Power-based, not craft-based. |
| 5.0–6.5 | — | — | — | *Populate as mid-tier profiles are built* |
| 3.0–4.5 | Rudy Gobert (confirmed) | Low FTR relative to paint touches | Basketball-Reference | Scores on lobs and putbacks — doesn't seek contact as a skill. |

---

### #3 — Post Offense

**Block A — Primary Statistical Input**

| Level | Stat | Source | Access |
|---|---|---|---|
| NBA | Points per post-up possession (PPP) | NBA.com Play Type page (Synergy) / scouting reports | 🟡 Manual — public web lookup. Domain 1 script does not currently capture this; see [SCRIPT-MAINTENANCE-BACKLOG.md](SCRIPT-MAINTENANCE-BACKLOG.md) B10. |
| College | Post-up PPP / post-up percentile | Synergy data cited in scouting reports | 🟡 Manual — capture from published prospect write-ups during web search |
| College (fallback) | Usage profile + assist rate from non-guard | EvanMiya (role metric, assist rate) | 🟡 Manual lookup |
| International | Post touch frequency from FIBA PBP where available | FIBA box scores via web search | 🟡 Manual per player |

**Why post-up PPP is primary and why college access is the hardest problem in Domain 1:** Post offense is the most play-type-dependent sub-domain. You can't derive post-up efficiency from box score stats — it requires possession-level tracking. At the NBA level, nba_api gives this to us cleanly. At the college level, it's locked behind Synergy. Our workaround: Synergy percentile data is regularly cited in published scouting reports ("71% at the rim in the half court per Synergy," "93rd percentile in post-ups per Synergy"). We capture that during player research. It's not systematic, but for the 20-60 players per draft class who get serious scouting coverage, it's functional.

**Absence is itself a signal:** Per SUB-DOMAINS, no documented post role at any level scores at or near position baseline. If web search turns up zero post-up data or post-up language for a player, that *is* the data — the score is near baseline.

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Post touch frequency | NBA.com Play Type page (Synergy) — post-up possessions | 🟡 NBA manual / 🔴 College | Establishes whether the player has a post role at all. Without touches, efficiency is meaningless. Domain 1 script does not currently capture this — public-web lookup until script implementation lands (see [SCRIPT-MAINTENANCE-BACKLOG.md](SCRIPT-MAINTENANCE-BACKLOG.md) B10). At college, inferred from scouting language and role description. |
| 2 | Assist rate in half-court settings | EvanMiya assist rate + role metric (college) / nba_api (NBA) | 🟢 NBA / 🟡 College manual | High assist rate from a non-guard in half-court settings is a proxy for post playmaking — the Jokić/Draymond dimension. EvanMiya's role metric (1-5 creator/receiver scale) helps calibrate this. |
| 3 | EvanMiya BPR / OBPR | EvanMiya | 🟡 Manual lookup | Overall offensive value as cross-validation. A player with high OBPR and no documented post role is contributing from somewhere other than the post — helps confirm baseline score. |
| 4 | Footwork variety / counter usage | Scouting reports only | 🟢 Web search | How many distinct post moves does the player show? Drop step, up-and-under, jump hook, spin — each counter expands the scoring envelope. No stat captures this. Always qualitative. |

**Cross-reference gate:** #3 → #23. Post offense without physical capacity has a hard ceiling. A player below 220 lbs at C/PF with no documented post role has a structural ceiling regardless of skill language. Weight data is publicly available from combine/pro day results.

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | Post offense is the most film-dependent sub-domain. Convergence on footwork language is high-value. Synergy data cited in reports is the best college-level signal available. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule. |
| Recruiting-context coach quotes | 8 | 🟢 Web search | Directional only. "Back to the basket threat" in a recruiting context can mean almost anything. |

**Key language triggers from SUB-DOMAINS:**

Positive (midpoint rule): documented post role, footwork variety language, "finds the open man from the post," doubling response language

Negative (anchoring): "no counter," "only goes right," "predictable footwork," no documented post role at any level, single-move dependency, poor catch radius, low assist rate from post situations

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Weight | NBA Combine / Pro Day / FIBA testing | 🟢 Web search | Below 220 lbs at C/PF is a structural ceiling per SUB-DOMAINS. Weight is a prerequisite, not a skill signal. |
| Strength profile (relative) | Cross-reference #23 score | Internal — scored in same evaluation | #23 is the physical gate. A low strength score hard-caps post offense regardless of footwork or touch. |

N/A for NBA-level evaluation.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Post-up PPP from nba_api (aspirational — once Domain 1 implements SynergyPlayTypes post-up; see [SCRIPT-MAINTENANCE-BACKLOG.md](SCRIPT-MAINTENANCE-BACKLOG.md) B10) OR Synergy percentile from published source + post touch frequency + at least one of: assist rate from post, footwork variety from qualitative | ±0.5 |
| Medium | Synergy percentile from published report + one secondary OR EvanMiya role/assist data + converging qualitative sources | ±1.0 |
| Low | Single qualitative source describing post role OR inferred from EvanMiya role metric only | ±1.5 |
| Very Low | Inferred from physical profile only — no post usage documented at any level | ±2.0 |

Practical note: High confidence on #3 at the college level requires finding Synergy data cited in a published scouting report. Without that, Medium is the ceiling. This is the sub-domain where college confidence will most frequently cap at Medium or Low. For international prospects, Low is the default unless FIBA-level post usage data + multiple qualitative sources push it up.

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 9.0+ | Nikola Jokić (confirmed) | 1.09 PPP on post-ups (career) | nba_api | The full model — scoring + playmaking from the post. Elite footwork, elite passing out of doubles. |
| 7.0–8.5 | — | — | — | *Populate with strong post scorers / playmakers* |
| 5.0–6.5 | Clint Capela (confirmed) | Limited post touches; finishes on catches, no self-creation | nba_api | Near-baseline. Finishing in the post ≠ post offense. |
| 3.0–4.5 | Rudy Gobert (confirmed) | Near-zero post-up possessions | nba_api | Post offense at baseline. Scores on lobs and putbacks — not post offense. |

---

## Domain 2: Shooting

---

### #4 — Catch-and-Shoot 3PT

**Block A — Co-Primary Statistical Input**

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | CAS 3PT% | LeagueDashPtStats (CatchShoot) via nba_api | 🟢 Automated | Efficiency (co-primary) |
| NBA | CAS 3PA + CAS 3PA as % of total 3PA | LeagueDashPtStats (CatchShoot) via nba_api | 🟢 Automated | Volume (co-primary) |
| College | CAS 3PT% | Not available — no play-type tracking at college level | 🔴 Unavailable | Overall 3PT% used as proxy |
| College | Catch-and-shoot proxy: % assisted 3PM | Hoop-Math / EvanMiya | 🟢/🟡 | High % assisted 3PM implies CAS-heavy profile |

**Why co-primary:** CAS 3PT% alone doesn't discriminate without volume. Hield at 39.1% on 384 CAS 3PA (70% of his threes) is a fundamentally different profile than Smart at 34.3% on 105 CAS 3PA (37%). Volume + efficiency together define the catch-and-shoot skill level.

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Corner 3 FG% + FGA vs Above-the-Break 3 FG% + FGA | LeagueDashPlayerShotLocations via nba_api | 🟢 Automated | Zone split. Corner 3s are shorter and more open — high corner efficiency with low ATB signals limited range. |
| 2 | FG3% by defender distance (wide open, open, tight) | LeagueDashPlayerPtShot via nba_api | 🟢 Automated | Shows whether efficiency holds against closeouts. Note: all shots, not CAS-specific — endpoint cannot cross-filter. |
| 3 | Overall 3PT% + 3PA (season) | PlayerCareerStats via nba_api | 🟢 Automated | Context. CAS efficiency read alongside overall volume. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Elite shooter," "gravity off the ball," "forces closeouts" — convergence across 3+ sources is a real signal. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule per R1. |

**Block D — Physical / Biometric Data**

Not directly applicable. Shooting mechanics are qualitative; release speed is not tracked.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | CAS 3PT% + CAS 3PA (nba_api) + zone split (corner/ATB) + 2-season window | ±0.5 |
| Medium | Overall 3PT% + 3PA + one qualitative convergence OR single-season CAS data | ±1.0 |
| Low | Single season overall 3PT% only OR single qualitative source | ±1.5 |
| Very Low | Inferred from FT% as mechanical proxy — no shooting data | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 9.0+ | Buddy Hield (provisional) | 39.1% CAS 3PT on 384 CAS 3PA (70% of 3PA) | nba_api | Volume + efficiency combination. Shooting specialist archetype. |
| 7.0–8.5 | — | — | — | *Populate as mid-tier CAS profiles are built* |
| 5.0–6.5 | De'Aaron Fox (provisional) | 31.6% CAS 3PT on 190 CAS 3PA (25% of 3PA) | nba_api | Low CAS volume and efficiency — primary creation is off-dribble. |

---

### #5 — Off-Dribble Shooting

**Block A — Co-Primary Statistical Input**

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | Pull-up 3PT% | LeagueDashPtStats (PullUpShot) via nba_api | 🟢 Automated | Efficiency (co-primary) |
| NBA | Pull-up 3PA + Pull-up 3PA as % of total 3PA | LeagueDashPtStats (PullUpShot) via nba_api | 🟢 Automated | Volume (co-primary) |
| NBA | Pull-up zone split: 3PT vs mid-range | ShotChartDetail ACTION_TYPE classification | 🟢 Automated | Critical: separates pull-up 3s (#5) from pull-up mid-range (#6) |
| College | Not available — no CAS/pull-up split at college level | 🔴 Unavailable | Qualitative only |

**Why co-primary and why zone split matters:** The LeagueDashPtStats PullUp endpoint returns all pull-up shots combined. But pull-up 3PT feeds #5 and pull-up mid-range feeds #6. ShotChartDetail ACTION_TYPE classification (Pullup Jump shot, Step Back Jump shot, etc.) cross-referenced with SHOT_ZONE_BASIC provides the zone split. Confirmed as viable architecture S83-F06.

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Isolation PPP + possessions + FG% + TOV% | SynergyPlayTypes (Isolation) via nba_api | 🟢 Automated | Purest off-dribble creation signal. Irving 1.063 PPP (86th percentile) on 255 possessions. |
| 2 | Pull-up overall FG% + eFG% | LeagueDashPtStats (PullUpShot) | 🟢 Automated | All pull-up shots combined — context for total off-dribble scoring. |
| 3 | Late shot clock shooting (0-7 sec) | Deferred — endpoint needs investigation | 🟡 | Shot creation under pressure. Deferred to future session. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Can create his own shot," "off-the-dribble threat," "pull-up range to 30 feet." |
| Single-source scouting report | 7 | 🟢 Web search | Directional. |

**Block D — Physical / Biometric Data**

Not directly applicable.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Pull-up 3PT% + pull-up 3PA (nba_api) + zone split (ShotChart) + ISO data + 2-season window | ±0.5 |
| Medium | Pull-up stats + one of: ISO data OR qualitative convergence | ±1.0 |
| Low | Overall 3PT% only (no CAS/pull-up split) OR single qualitative source | ±1.5 |
| Very Low | Inferred from archetype only | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 9.0+ | Kyrie Irving (provisional) | 35.3% pull-up 3PT on 190 3PA (53% of 3PA); 1.063 ISO PPP (86th pctile) | nba_api | Elite self-creation. Pull-up dominant shot profile. |
| 5.0–6.5 | — | — | — | *Populate as mid-tier off-dribble profiles are built* |
| 3.0–4.5 | Buddy Hield (provisional) | 31.9% pull-up 3PT on 163 3PA (30%); 0.524 ISO PPP (6th pctile) | nba_api | Cannot create off the dribble. CAS-dependent. |

---

### #6 — Mid-Range

**Block A — Co-Primary Statistical Input**

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | Mid-range FG% (all mid-range zones) | LeagueDashPlayerShotLocations via nba_api | 🟢 Automated | Efficiency (co-primary) |
| NBA | Mid-range FGA + mid-range FGA as % of total FGA | LeagueDashPlayerShotLocations via nba_api | 🟢 Automated | Volume (co-primary) |
| College | Mid-range FG% | Hoop-Math (shot distance buckets) | 🟢 Scraper build required | College proxy |

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Pull-up mid-range FG% + FGA | ShotChartDetail zone split (from #5 architecture) | 🟢 Automated | Isolates off-dribble mid-range creation from catch-and-shoot mid-range. Priority 1 secondary. |
| 2 | Mid-range zone splits: elbow, baseline, wing | ShotChartDetail SHOT_ZONE_AREA | 🟢 Automated | Where does the player score from? Baseline vs elbow vs wing reveals shot creation patterns. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Mid-range game," "pull-up from the elbow," "fadeaway." |
| Single-source scouting report | 7 | 🟢 Web search | Directional. |

**Block D — Physical / Biometric Data**

Not directly applicable.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Mid-range FG% + FGA (shot locations) + pull-up mid split (ShotChart) + 2-season window | ±0.5 |
| Medium | Mid-range FG% + FGA + one qualitative source | ±1.0 |
| Low | Overall 2PT% only (no mid-range split) | ±1.5 |
| Very Low | Inferred from archetype | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 9.0+ | — | — | — | *Populate with elite mid-range scorers (e.g., KD, Kawhi)* |
| 7.0–8.5 | Kyrie Irving (provisional) | 40.8% mid-range on 174 FGA (18.4% of total FGA) | nba_api | High volume and efficiency. Uses the mid-range as a primary weapon. |
| 5.0–6.5 | De'Aaron Fox (provisional) | 41.2% mid-range on 194 FGA (8.3% of total FGA) | nba_api | Similar efficiency but half the usage rate — mid-range is secondary weapon. |
| 3.0–4.5 | Buddy Hield (provisional) | 34.0% mid-range on 53 FGA (6.7%) | nba_api | Near-baseline. Avoids the mid-range. |

---

### #7 — Free Throw

**Block A — Primary Statistical Input**

| Level | Stat | Source | Access |
|---|---|---|---|
| NBA | FT% (season) + FTA (season totals) | PlayerCareerStats via nba_api | 🟢 Automated |
| NBA | FT% (career — all seasons combined) | PlayerCareerStats CareerTotals via nba_api | 🟢 Automated |
| College | FT% + FTA | Basketball-Reference / EvanMiya | 🟢/🟡 |

**Why career + current:** FT% is the most stable shooting stat. Career FT% is a better predictor of future FT% than single-season FT%. Both are reported; career is the anchor, current season is the signal for improvement or regression.

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | FT% trend (last 3-5 seasons) | PlayerCareerStats via nba_api | 🟢 Automated | Trajectory. Declining FT% flags mechanical regression. Improving FT% supports projection upward. |
| 2 | Clutch FT% (last 5 min, within 5 points) | PlayerDashboardByClutch via nba_api | 🟢 Automated | Pressure performance. Small samples — directional only. |
| 3 | FT% as proxy for other shooting sub-domains | Cross-reference | Internal | FT% > 85% signals mechanical soundness that feeds #4 and #5 projections. FT% < 65% is a structural ceiling per SUB-DOMAINS. |

**Block C — Qualitative Signal Sources**

Not typically relevant — FT% is statistically definitive. Qualitative only applies when FT data is sparse (international prospects).

**Block D — Physical / Biometric Data**

Not applicable.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | FT% current season (100+ FTA) + career FT% + 2-season window | ±0.5 |
| Medium | FT% current season (50-99 FTA) OR career FT% without current season context | ±1.0 |
| Low | FT% on < 50 FTA OR single-season only for prospect | ±1.5 |
| Very Low | No FT data — inferred from shooting mechanics or touch sub-domain | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 9.0+ | Kyrie Irving (provisional) | 91.6% current, 88.8% career | nba_api | Elite. Career consistency confirms it's real. |
| 7.0–8.5 | Buddy Hield (provisional) | 82.8% current, 85.6% career | nba_api | Reliable. Career baseline is strong. |
| 5.0–6.5 | Marcus Smart (provisional) | 76.1% current, 77.9% career | nba_api | Functional but not a strength. Below league average for guards. |

## Domain 3: Ball Skills

---

### #8 — Handling / Creation

**Block A — Primary Statistical Input (play-type creation efficiency)**

The primary measure of handling is what the handling produces. Expert consensus (BBall Index, Synergy, scouting community) points to play-type creation data as the best available signal. Process metrics (time of possession, dribbles per touch) describe role, not skill quality (S84-F05).

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | ISO PPP + possessions + FG% + TOV% | SynergyPlayTypes (Isolation) via nba_api | 🟢 Automated | Self-creation efficiency — purest unstructured handling test. Cross-referenced from #5 (off-dribble shooting). |
| NBA | PnR ball handler PPP + possessions + FG% + TOV% | SynergyPlayTypes (PRBallHandler) via nba_api | 🟢 Automated | Structured creation — the NBA's most common ball-handling action. Strongest single discriminator for guard handling quality. |
| NBA | Drives/game + drive FG% + drive PTS | LeagueDashPtStats (Drives) via nba_api | 🟢 Automated | Creation output — cross-referenced from Domain 1. Drives are the physical product of handling. |
| College | Usage rate + role metric (creator vs. receiver scale) | EvanMiya | 🟡 Manual lookup | Best college proxy for creation responsibility. High usage + creator role (1–2 on EvanMiya's 1–5 scale) signals primary ball handler. |
| College | Synergy play-type data cited in scouting reports | Published prospect write-ups | 🟢 Web search capture | Same capture method as #3 (post offense). Synergy percentiles in PnR or ISO regularly appear in draft coverage. |
| International | Drives per game, creation rate from FIBA PBP where available | FIBA box scores + web search | 🟡 Manual per player | Limited. |

**Why play-type creation is primary:** Handling skill shows up in outcomes — can the player create an advantage off the dribble and convert or facilitate? ISO and PnR ball handler data measure this directly. Drives/game is already captured in Domain 1 but contextualizes here.

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | TOV per 100 touches | Derivable: TOV / touches (LeagueDashPtStats Possessions) × 100 | 🟢 Automated | Expert-preferred handling cost metric (S84-F03). Normalizes for how often the player handles. League average ~3.8. Lower = better ball security while handling. |
| 2 | Time of possession (avg sec per touch) | LeagueDashPtStats (Possessions) via nba_api | 🟢 Automated | Role descriptor, not quality measure (S84-F05). High TOP = primary creator role. |
| 3 | Dribbles per touch | LeagueDashPtStats (Possessions) via nba_api | 🟢 Automated | Role descriptor (S84-F05). High dribbles/touch = live-dribble creator. |
| 4 | Handoff PPP + possessions | SynergyPlayTypes (Handoff) via nba_api | 🟢 Automated | Third play type in BBall Index's "One on One" grade. Measures efficiency receiving and creating off dribble handoffs. |
| 5 | Standard TOV% | LeagueDashPlayerStats via nba_api / Basketball-Reference | 🟢 Automated | Universal fallback. Biased but functional within same position group. |

**Block C — Qualitative Signal Sources**

The difference between a 7.0 and a 9.0 at handling is almost entirely qualitative. Play-type data tells you the player can create — scouting language tells you how they create and whether the handle will translate. Qualitative validation is mandatory for every player (S84-F02).

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | The primary scoring lever for the upper range. Convergence on handle quality across 3+ sources is a real signal. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule per R1. |
| Recruiting-context coach quotes | 8 | 🟢 Web search | Directional only. |

**Key language triggers from SUB-DOMAINS:**

Positive (midpoint rule): "tight handle," "creative with the ball," "gets into the lane at will," "shifty," "change of pace," "creates off live dribble," "can break down his man"

Negative (anchoring): "gets his dribble picked," "loose handle," "turnover prone in traffic," "weak-hand avoidance," "one move," "slows down to execute moves," "can't create off the bounce"

**Critical scoring note:** For college prospects, qualitative signals carry more weight at this sub-domain than at any in Domains 1–2. Play-type data doesn't exist at the college level. EvanMiya usage and role data establishes creation responsibility; scouting language determines where within the range the score lands.

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Height relative to position | NBA Combine / Pro Day | 🟢 Web search | Shorter guards have structural advantage in handle tightness — lower center of gravity. Context for handle style, not quality. |
| Lateral quickness / agility testing | NBA Combine (lane agility, shuttle) | 🟢 Web search | Quick feet enable change of direction off the dribble. Elite agility corroborates handle quality. |

N/A for NBA-level evaluation.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | ISO + PnR BH play-type data (nba_api) + drives (Domain 1) + TOV/touch + 2-season window + converging qualitative (3+ sources) | ±0.5 |
| Medium | Play-type data (at least one of ISO/PnR) + TOV/touch OR EvanMiya usage/role + two independent qualitative sources converging | ±1.0 |
| Low | Standard TOV% and USG% only + single qualitative source OR EvanMiya role metric only | ±1.5 |
| Very Low | Inferred from physical profile and archetype — no creation data or scouting language available | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 9.0+ | Kyrie Irving (locked) | 1.070 ISO PPP (84th pctile, 258 poss); 1.033 PnR BH PPP (88th pctile, 283 poss); 11.7 drives/game | nba_api | Elite in every creation context. Multi-source: "best ball handler in NBA history," ambidextrous, counters to every move. |
| 7.0–8.5 | De'Aaron Fox (locked) | 1.030 PnR BH PPP (87th pctile, 430 poss); 0.915 ISO PPP (52nd pctile); 15.2 drives/game | nba_api | Speed-based creation. Elite PnR producer. ISO weakness and left-hand reliance cap craft ceiling. |
| 5.0–6.5 | Marcus Smart (locked) | 0.834 PnR BH PPP (46th pctile, 61 poss); 16 ISO poss (noise); 6.1 drives/game | nba_api | Secondary handler. "Mediocre ballhandler" (NBADraft.net). Handles functionally, doesn't create. |
| 3.0–4.5 | Buddy Hield (locked) | 21 ISO poss; 47 PnR BH poss; 1.38 sec TOP; 1.28 drib/touch | nba_api | Non-creator. "Below-average ballhandler" (HoopsHype). Catch-and-act player. |

---

### #9 — Touch / Feel

**Block A — Primary Statistical Input (proxy-based — no direct measure exists)**

Touch is a qualitative skill. No stat directly measures fingertip control, soft hands, or pass accuracy. The best available statistical signals are byproducts of touch (S84-F06).

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | FT% (current season + career) | PlayerCareerStats via nba_api | 🟢 Automated | Cleanest mechanical proxy for touch — consensus across analytics community. Cross-referenced from #7. FT% > 85% = strong positive. FT% < 65% = structural ceiling. |
| NBA | Non-dunk rim FG% | Derivable from Domain 1 data (rim FG% adjusted for dunk rate) | 🟢 Automated (derivable) | Isolates touch finishing from athletic finishing. |
| College | FT% | Basketball-Reference / EvanMiya | 🟢/🟡 | Universally available. Same proxy at all levels. |
| International | FT% from FIBA or domestic league box scores | FIBA box scores via web search | 🟡 Manual per player | Universally available. |

**Why FT% is primary even though it's already in #7:** FT% in #7 measures free throw shooting. Here it's used as a proxy for a different skill — fingertip control and hand-ball relationship. Same stat, different diagnostic purpose.

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Floater-range FG% + FGA (4–14 ft) | ShotChartDetail filtered by SHOT_DISTANCE via nba_api | 🟢 Automated | The single most direct statistical footprint of touch. Runners, teardrops, fingerrolls live in this zone. The only net new data pull for #9. |
| 2 | Paint FG% on non-dunk attempts | Derivable from rim data + ShotChartDetail | 🟢 Automated (derivable) | Broader version of non-dunk rim FG%. |
| 3 | % unassisted at rim | Cross-reference from #1 secondary | 🟢 Already in pipeline | Self-created finishes require more touch than catch-and-finish. |

**Block C — Qualitative Signal Sources**

This is the primary scoring lever for #9. More than any other sub-domain, the score is determined by scouting language (S84-F06).

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | Convergence on touch language is the strongest signal. 3+ sources = real signal. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule applies. |
| Film-based analyst breakdowns | 6 | 🟢 Web search | Analysts breaking down finish type (fingerroll vs power layup, glass usage) provide the highest-quality #9 signal. |

**Key language triggers from SUB-DOMAINS:**

Positive (midpoint rule): "soft hands," "great touch," "feathery finish," "silky," "uses the glass," "fingerroll," "creative around the rim," "good feel"

Negative (anchoring): "brick hands," "can't catch," "hard finisher," "no touch around the rim," "pass delivery that consistently requires receivers to adjust"

**Block D — Physical / Biometric Data**

Not directly applicable. Touch is skill, not physical profile.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | FT% (cross-ref #7) + floater-range FG% on 50+ FGA + non-dunk rim FG% + converging qualitative from 3+ sources | ±0.5 |
| Medium | FT% + one of: floater-range data OR non-dunk rim FG% + one qualitative source | ±1.0 |
| Low | FT% only (no paint/floater split) OR single qualitative source | ±1.5 |
| Very Low | Inferred from physical profile — no touch data or scouting language available | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 9.0+ | Kyrie Irving (locked) | 91.2% FT; 65.1% non-dunk rim FG%; 49.2% floater-range on 333 FGA (32.6% of total) | nba_api + qualitative | The archetype. Multi-source: "creative finisher," ambidextrous, fingerrolls, backboard usage. |
| 7.0–8.5 | De'Aaron Fox (locked) | 78.5% FT; 63.6% non-dunk rim FG%; 50.4% floater-range on 461 FGA (34.8%) | nba_api | Functional floater game. "Good touch on floaters" but athletic finisher, not craft finisher. |
| 5.0–6.5 | Buddy Hield (locked) | 84.8% FT; 45.4% floater-range on 80 FGA (9.9% of total) | nba_api | FT% confirms mechanical touch exists. Latent — never manifests in paint because role doesn't require it. |
| 5.0–6.5 | Marcus Smart (locked) | 76.3% FT; 42.8% floater-range on 73 FGA | nba_api | No positive touch language in any scouting source. Finishes with strength, not touch. |

---

### #10 — Ball Security

**Block A — Primary Statistical Input**

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | TOV per 100 touches | Derivable: TOV / touches (LeagueDashPtStats Possessions) × 100 | 🟢 Automated | Expert-preferred metric (S84-F03). Normalizes for how often the player handles. League average ~3.8. |
| NBA | Standard TOV% | LeagueDashPlayerStats via nba_api | 🟢 Automated | Universal fallback. Biased across positions but functional within same position group. |
| College | TOV% | Basketball-Reference | 🟢 Scrapeable | Universally available. |
| College (enhanced) | Opponent-adjusted TOV% | EvanMiya | 🟡 Manual lookup | Better version — adjusts for pace and opponent pressure. |
| International | TOV per game relative to usage and minutes | FIBA box scores via web search | 🟡 Manual per player | Basic but universally available. |

**Why TOV/touch AND TOV%:** TOV/touch requires tracking data (NBA only). Standard TOV% is the universal fallback at every level.

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | A:TO ratio | Derivable from basic stats | 🟢 Automated | Ball security in playmaking context. Positionally biased — use within position group only. |
| 2 | Touches per game | LeagueDashPtStats (Possessions) via nba_api | 🟢 Automated | Denominator context for TOV/touch. |
| 3 | TOV% trend across seasons | PlayerCareerStats via nba_api | 🟢 Automated | Rising TOV% under higher usage = overextension. Declining under stable usage = genuine improvement. |
| 4 | TOV% in clutch (last 5 min, within 5 pts) | PlayerDashboardByClutch via nba_api | 🟢 Automated | Pressure ball security. Small samples — directional only. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Takes care of the ball," "turnover prone" — convergence across 3+ sources is a real signal. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule applies. |

**Key language triggers from SUB-DOMAINS:**

Positive (midpoint rule): "takes care of the ball," "rarely turns it over," "secure handler," "protects the ball in traffic"

Negative (anchoring): "careless," "turnover machine," "can't be trusted with the ball in traffic," "turnover prone," "gets stripped," "loose with the ball"

**Block D — Physical / Biometric Data**

Not applicable.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | TOV/touch (tracking) + standard TOV% + A:TO + 2-season window + touches context | ±0.5 |
| Medium | Standard TOV% + A:TO + one qualitative source OR EvanMiya adj. TOV% + qualitative | ±1.0 |
| Low | Standard TOV% only (no touch normalization, no qualitative) | ±1.5 |
| Very Low | Inferred from role only — no TOV data available | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 7.0–8.5 | Kyrie Irving (locked) | 2.96 TOV/100 touches; 7.4% TOV%; 2.38 A:TO on 69.9 touches/game | nba_api | Elite security at elite volume. Well below league average TOV/touch. |
| 7.0–8.5 | De'Aaron Fox (locked) | 3.38 TOV/100 touches; 8.9% TOV%; 2.21 A:TO on 80.5 touches/game | nba_api | Solid security at highest volume. Near league average TOV/touch on massive handling load. |
| 5.0–6.5 | Buddy Hield (locked) | 2.62 TOV/100 touches; 8.7% TOV%; 1.80 A:TO on 44.3 touches/game | nba_api | Best raw TOV/touch but role-driven (S84-F07). Catch-and-shoot = low turnovers by design, not skill. |
| 5.0–6.5 | Marcus Smart (locked) | 5.06 TOV/100 touches; 13.2% TOV%; 1.77 A:TO on 42.0 touches/game | nba_api | Confirmed turnover-prone by multi-source scouting (S84-F04). Defensive IQ ≠ offensive ball security. |

## Domain 4: Playmaking

---

### #11 — Court Vision

**Block A — Primary Statistical Input (potential assists — teammate-independent passing volume)**

Potential assists are the expert-preferred primary because they remove the teammate shooting quality dependency that contaminates raw assists. A pass that creates a shot within one dribble is credited regardless of make/miss. Tracked since 2013-14 via Second Spectrum. BBall Index's Playmaking Talent grade uses potential assists + FT assists as its volume component.

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | Potential assists per game | LeagueDashPtStats (Passing) via nba_api | 🟢 Automated | Passing creation volume — teammate-independent. Primary. |
| NBA | Secondary assists per game | LeagueDashPtStats (Passing) via nba_api | 🟢 Automated | Purest vision signal — sees the play two passes ahead. |
| NBA | Adjusted assists (AST + secondary AST + FT AST) | LeagueDashPtStats (Passing) via nba_api | 🟢 Automated | Total creation output across all assist types. |
| College | Assist rate (AST%) | Basketball-Reference / EvanMiya | 🟢/🟡 | Universal proxy. No potential assist tracking at college level. |
| College (enhanced) | Opponent-adjusted AST% + role metric | EvanMiya | 🟡 Manual lookup | Better version — adjusts for pace, opponent, and usage context. Creator vs. receiver role (1–5 scale) calibrates whether assists reflect vision or system. |
| International | APG relative to usage and minutes | FIBA box scores via web search | 🟡 Manual per player | Basic but universally available. |

**Why potential assists over raw assists:** Raw assists punish players whose teammates miss open shots. The NBA Underground analysis confirmed: SGA averages 11.8 potential assists but only 4.4 actual assists — 37.2% conversion. Potential assists measure creation quality independent of shooter conversion. Academic research (2022, Journal of Performance Analysis in Sport) found secondary assists correlate strongly with better team shot quality and spacing.

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Adjusted assist % (adjusted AST / total passes) | Derivable from Passing endpoint | 🟢 Automated | What fraction of total passes create value. High % on high volume = elite vision. Low % on high volume = ball-dominant but not creative. |
| 2 | Passes made per game | LeagueDashPtStats (Passing) via nba_api | 🟢 Automated | Denominator context for adjusted assist %. |
| 3 | Assist rate (AST%) | LeagueDashPlayerStats via nba_api | 🟢 Automated | % of teammate FGs assisted while on floor. Standard advanced stat. Biased by teammates and role but functional within position group. |
| 4 | Assist points created per game | LeagueDashPtStats (Passing) via nba_api | 🟢 Automated | Total points generated by assists. Separates a player creating layups (2 pts) from a player creating 3s (3 pts). |
| 5 | PnR BH assist rate | Cross-reference from #8 data (SynergyPlayTypes) | 🟢 Already in pipeline | How often PnR possessions end in assists vs. scores or turnovers. High PnR assist rate = vision within the NBA's most common action. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Sees the floor," "finds the open man" — convergence across 3+ sources is a real signal. Vision language is the most reliable positive playmaking indicator. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule per R1. |
| Film-based analyst breakdowns | 6 | 🟢 Web search | Analysts describing reads — "saw the weak-side cutter before the defense rotated" — highest-quality #11 signal. |

**Key language triggers from SUB-DOMAINS:**

Positive (midpoint rule): "sees the floor," "finds the open man," "one pass ahead," "anticipates rotations," "elite court vision," "quarterback"

Negative (anchoring): "tunnel vision," "doesn't see the open man," "predictable with the ball," "first-option dependency," "forces passes into coverage"

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Height | NBA Combine / Pro Day | 🟢 Web search | Taller players have structural vision advantage — higher vantage point. Ben Taylor's Passer Rating includes height as a component. Context for vision quality, not a skill signal itself. |

N/A for NBA-level evaluation — height is already known.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Potential assists + secondary assists + adjusted assist % + passes made (Passing endpoint) + 2-season window + converging qualitative (3+ sources) | ±0.5 |
| Medium | Standard AST% + one of: potential assists OR EvanMiya adj. AST% + role metric + two independent qualitative sources | ±1.0 |
| Low | Standard AST% or APG only (no tracking context) + single qualitative source | ±1.5 |
| Very Low | Inferred from archetype and role only — no passing data available | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 7.0–8.5 | Kyrie Irving (locked) | 8.88 pot AST; 0.78 sec AST; 13.6% adj AST% on 45.0 passes/game | nba_api | Multi-source: "great vision," "court vision is superb." Scorer-first identity caps vision score — sees the floor well but prioritizes scoring. |
| 7.0–8.5 | De'Aaron Fox (locked) | 11.46 pot AST; 0.76 sec AST; 13.6% adj AST% on 53.5 passes/game | nba_api | Highest raw creation volume among test guards. Per-pass creation rate identical to Irving despite higher handling volume — volume is role-driven, not vision-driven. |
| 5.0–6.5 | Marcus Smart (locked) | 6.92 pot AST; 0.24 sec AST; 15.2% adj AST% on 28.1 passes/game | nba_api | Reduced role explains lower volume. Secondary AST (0.24) is the tell — doesn't see the extra pass. High adj AST% is efficiency in a limited role, not vision. |
| 3.0–4.5 | Buddy Hield (locked) | 3.72 pot AST; 0.32 sec AST; 8.0% adj AST% on 32.3 passes/game | nba_api | Non-creator. Vast majority of passes don't create anything. Absence, not active problem. |

---

### #12 — Decision-Making

**Block A — Primary Statistical Input (turnover type breakdown — decision quality signal)**

Decision-making is the most statistically elusive sub-domain in Domain 4. No single stat measures it directly. The strongest available signal is the *type* of turnovers a player commits — bad pass turnovers reflect decision errors; lost ball turnovers reflect ball security (#10). Cross-reference: #12 → #11.

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | Bad pass TOV + lost ball TOV (per game) | LeagueDashPlayerStats via nba_api | 🟢 Automated | Decision vs. execution error split. Bad pass TOV = wrong read. Lost ball TOV = ball security (#10). Primary discriminator. |
| NBA | Bad pass TOV rate relative to potential assists | Derivable: bad pass TOV / potential assists | 🟢 Automated (derivable) | Expert-preferred decision efficiency metric. How many bad reads per quality pass? Better than standard A:TO. |
| NBA | Standard A:TO ratio | LeagueDashPlayerStats via nba_api / Basketball-Reference | 🟢 Automated | Universal fallback. Biased by role and usage but functional within position group. |
| College | A:TO ratio | Basketball-Reference / EvanMiya | 🟢/🟡 | Universally available. No turnover type breakdown at college level. |
| College (enhanced) | Opponent-adjusted TOV% + AST% | EvanMiya | 🟡 Manual lookup | Better version — adjusts for pace and opponent pressure. |
| International | A:TO from FIBA box scores | FIBA box scores via web search | 🟡 Manual per player | Basic but universally available. |

**Why turnover type breakdown is primary:** SUB-DOMAINS explicitly separates "decision turnovers (wrong play chosen) versus execution turnovers (good decision, poor delivery)." nba_api returns bad pass TOV and lost ball TOV as separate columns. Bad pass TOV / potential assists is the closest available public metric for pure decision quality.

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | PnR BH TOV% + PPP | SynergyPlayTypes (PRBallHandler) via nba_api | 🟢 Automated (already in pipeline from #8) | Decision quality in the NBA's most common half-court action. Low TOV% + high PPP = correct reads under pressure. Cross-reference from #8 — same data, different diagnostic lens. |
| 2 | Transition play type PPP + possessions + TOV% | SynergyPlayTypes (Transition) via nba_api | 🟢 Automated | Transition decision-making — pushing on numbers advantages vs. over-dribbling. SUB-DOMAINS calls this out explicitly. |
| 3 | Drive-and-kick assist rate | Derivable: assists on drives / total drives | 🟢 Automated (partial — drives already in pipeline) | Drive-kick timing is a key decision dimension per SUB-DOMAINS. High drive-to-assist ratio = correctly reading when to finish vs. kick. |
| 4 | Clutch A:TO (last 5 min, within 5 pts) | PlayerDashboardByClutch via nba_api | 🟢 Automated (already in pipeline from #10) | Pressure decision quality. Small samples — directional only. |
| 5 | Playoff decision-making (per R13) | Scouting language + nba_api playoff splits | 🟢 Web search + nba_api | Playoff decisions against elevated defensive schemes — tailored coverages, scouted pick-and-roll reads. Channel 2 secondary input per R13. Applies when playoff sample minimum (≥2 series) is met. |

**Block C — Qualitative Signal Sources**

#12 is a universal sub-domain — scored against the full NBA population per Entry 002 of the Research Log. Scores above 7.0 for non-NBA players require in-session justification citing evidence of decision-making against advanced defensive schemes.

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Makes the right play," "high basketball IQ," "never forces it" — convergence across 3+ sources. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule per R1. |
| Film-based analyst breakdowns | 6 | 🟢 Web search | Read analysis — "correctly identified the drop coverage and pulled up" — highest-quality #12 signal. |

**Key language triggers from SUB-DOMAINS:**

Positive (midpoint rule): "makes the right play," "never forces it," "high basketball IQ," "reads the defense," "controls tempo," "plays at his pace"

Negative (anchoring): "forces it," "plays too fast," "can't slow the game down," "transition over-dribbling," "poor drive-kick timing," "bad decisions late"

**Block D — Physical / Biometric Data**

Not applicable. Decision-making is cognitive, not physical.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Bad pass TOV / potential assists + PnR BH TOV% + transition TOV% + A:TO + 2-season window + converging qualitative (3+ sources) | ±0.5 |
| Medium | Standard A:TO + one of: PnR BH data OR transition data + one qualitative convergence OR EvanMiya adj. TOV% + AST% + qualitative | ±1.0 |
| Low | Standard A:TO only (no turnover type breakdown, no play-type context) + single qualitative source | ±1.5 |
| Very Low | Inferred from archetype and role — no decision data available | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 7.0–8.5 | Kyrie Irving (locked) | 0.232 TOV/PotAST; 2.41 A:TO; transition 25.5th pctile (1.014 PPP, 222 poss); PnR BH 88th pctile | nba_api | Best TOV/PotAST among test guards. Multi-source: "good decision maker," "makes the right play." Elite half-court reads, mediocre transition decisions. |
| 7.0–8.5 | De'Aaron Fox (locked) | 0.240 TOV/PotAST; 2.21 A:TO; transition 33.5th pctile (1.044 PPP, 325 poss); PnR BH 87th pctile | nba_api | Solid TOV/PotAST on highest volume. Good structured reads. Transition decision-making concerning — pushes fast but sometimes into traffic. |
| 5.0–6.5 | Buddy Hield (locked) | 0.308 TOV/PotAST; 1.81 A:TO; transition 55th pctile (1.154 PPP, 227 poss, 9.3% TOV) | nba_api | Simple decisions executed correctly. Transition decisions surprisingly good. Knows his role and plays within it. |
| 5.0–6.5 | Marcus Smart (locked) | 0.310 TOV/PotAST; 1.76 A:TO; transition limited (51 poss, 15.5% TOV) | nba_api | Worst TOV/PotAST. Defensive IQ does not equal offensive decision-making. Active decision errors vs. Hield's absent ones. |

---

### #13 — Passing Execution

**Block A — Primary Statistical Input (proxy-based — no direct measure exists)**

Like #9 (Touch/Feel), passing execution has no direct statistical measure. No public stat captures pass accuracy, velocity calibration, or lob timing. The best available signals are byproducts of execution quality. Cross-reference: #13 → #9.

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | FT assists (passes leading to drawn fouls before 2 dribbles) | LeagueDashPtStats (Passing) via nba_api | 🟢 Automated | Passes that put the receiver in attacking position. Requires accuracy + timing. Primary proxy. |
| NBA | High-value assist proxy: assists at rim + assists on 3PT | Derivable from play-type cross-reference | 🟢 Automated (derivable) | A layup assist requires threading through traffic. A 3PT assist requires hitting the shooter in rhythm. Both test execution differently. |
| NBA | Potential assist conversion rate (AST / potential assists) | Derivable from Passing endpoint | 🟢 Automated (derivable) | Partially captures execution. Must be read with teammate context. |
| College | Assist rate | Basketball-Reference / EvanMiya | 🟢/🟡 | Universal fallback. Cannot separate vision from execution at college level. |
| International | APG from FIBA box scores | FIBA box scores via web search | 🟡 Manual per player | Basic. |

**Why FT assists are primary proxy:** An FT assist requires the pass to arrive accurately enough that the receiver can immediately attack and draw a foul within two dribbles. Tests timing, accuracy, and touch simultaneously.

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Assist points created per game | LeagueDashPtStats (Passing) via nba_api | 🟢 Automated | Higher assist points on fewer assists = each pass creates higher-value opportunities. |
| 2 | Touch / Feel score (#9) | Cross-reference — internal | Internal | SUB-DOMAINS cross-reference: #13 → #9. Pass touch and finishing touch share a mechanical root. Coherence check. |
| 3 | Bad pass TOV rate | LeagueDashPlayerStats via nba_api | 🟢 Automated | Some bad pass turnovers are execution failures (good read, bad pass). Read alongside #12 scoring. |

**Block C — Qualitative Signal Sources**

This is the primary scoring lever for #13. The score is overwhelmingly determined by scouting language (~80% qualitative).

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | Convergence on pass quality language is the strongest signal. 3+ sources = real signal. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule applies. |
| Film-based analyst breakdowns | 6 | 🟢 Web search | Analysts describing pass mechanics — "threads the needle," "lob accuracy," "off-hand delivery" — highest-quality #13 signal. |

**Key language triggers from SUB-DOMAINS:**

Positive (midpoint rule): "accurate passer," "threads the needle," "lobs arrive perfectly," "great touch on passes," "delivers the ball in rhythm," "creative passer"

Negative (anchoring): "off on his passes," "receivers have to adjust," "delivery is inconsistent," "stiff delivery," "lob inaccuracy," "one-hand pass avoidance"

**Coherence rule:** #13 should track within ±1.0 of #9 (Touch/Feel) for most players. Divergence beyond ±1.5 should trigger review — passing touch and finishing touch share a mechanical root.

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Hand size | NBA Combine / Pro Day | 🟢 Web search | Larger hands enable one-handed and off-hand passing variety. Context only. |

N/A for NBA-level evaluation.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | FT assists + assist type distribution (rim/3PT) + potential assist conversion + bad pass TOV context + #9 cross-reference + converging qualitative from 3+ sources | ±0.5 |
| Medium | Standard assist data + one of: FT assists OR assist points created + one qualitative source + #9 cross-reference | ±1.0 |
| Low | Standard APG or AST% only + single qualitative source | ±1.5 |
| Very Low | Inferred from physical profile and #9 cross-reference only — no passing data available | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 7.0–8.5 | Kyrie Irving (locked) | 0.5 FT AST; 13.6% adj AST%; #9 cross-ref = 9.5 | nba_api | Multi-source: "great passer," "top-notch passer." Touch confirms mechanical capability. Scoring identity limits passing volume. #9 → #13 gap = 1.7, justified by role. |
| 5.0–6.5 | De'Aaron Fox (locked) | 0.46 FT AST; 13.6% adj AST%; #9 cross-ref = 7.0 | nba_api | Functional passer with functional touch. Speed-based, not craft-based. #9 coherence: 0.5 gap. |
| 5.0–6.5 | Marcus Smart (locked) | 0.4 FT AST; 15.2% adj AST%; #9 cross-ref = 5.5 | nba_api | Below average touch = below average delivery. High adj AST% reflects decision efficiency in limited role, not execution quality. #9 coherence: 0.0 gap. |
| 3.0–4.5 | Buddy Hield (locked) | 0.2 FT AST; 8.0% adj AST%; #9 cross-ref = 6.0 | nba_api | Barely passes with creation intent. Mechanical touch exists but never manifests in passing — role divergence. #9 → #13 gap = 1.5, justified by role. |

---

### #14 — Off-Ball Movement

**Block A — Primary Statistical Input (Synergy play-type output — cutting and off-screen)**

Off-ball movement produces two measurable outputs: scoring off cuts and scoring off screens. BBall Index grades off-ball movement using exactly these Synergy play types (adjusted for efficiency and volume) plus a small weight for player tracking average velocity.

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | Cut play type PPP + possessions + FG% | SynergyPlayTypes (Cut) via nba_api | 🟢 Automated | Cutting output — the product of reading the defense and timing the cut. Co-primary. |
| NBA | Off-Screen play type PPP + possessions + FG% | SynergyPlayTypes (OffScreen) via nba_api | 🟢 Automated | Screen navigation output — curling, fading, popping off screens. Co-primary. |
| NBA | Average offensive speed (mph) | LeagueDashPtStats (SpeedDistance) via nba_api | 🟢 Automated | How much the player moves on offense. Directional — standing still = no off-ball movement. BBall Index uses this as a small weight. |
| College | CAS 3PT% as proxy for off-ball production | Cross-reference from #4 data | 🟢/🟡 Already in pipeline | High CAS volume in a motion offense = off-ball movement producing shots. College-level proxy. |
| College (enhanced) | Points off screens / off-screen efficiency | EvanMiya or Synergy data cited in scouting reports | 🟡 Manual lookup or web search capture | Best available college off-ball signal. |
| International | Points off movement from FIBA PBP where available | FIBA box scores via web search | 🟡 Manual per player | Limited. |

**Why Synergy cut + off-screen are co-primary:** BBall Index's Off-Ball Movement grade uses exactly these two play types as primary inputs. They directly measure what SUB-DOMAINS defines: "reading and using screens, cutting, creating space without the ball."

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | CAS 3PT% + volume | Cross-reference from #4 | 🟢 Already in pipeline | Off-ball shooting production. High CAS volume + high off-ball movement = full profile. |
| 2 | Offensive distance covered per game | LeagueDashPtStats (SpeedDistance) via nba_api | 🟢 Automated | Total offensive movement. Context for average speed. |
| 3 | % of FGA that are catch-and-shoot | Cross-reference from #4 data | 🟢 Already in pipeline | Role context. 70%+ CAS share demonstrates off-ball movement by definition. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Moves without the ball," "great cutter," "uses screens effectively" — convergence across 3+ sources is a real signal. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule applies. |
| System context | — | 🟢 Web search | A player in a structured motion offense has more off-ball signal. Context, not a score mover. |

**Key language triggers from SUB-DOMAINS:**

Positive (midpoint rule): "moves well without the ball," "great off-ball cutter," "uses screens effectively," "always in the right spot," "creates his own shots off movement"

Negative (anchoring): "stands around without the ball," "disappears off the ball," "doesn't move in the half-court," "ball-watching," "poor screen navigation," "spacing violations"

**Archetype context note:** Off-ball movement is the sub-domain where archetype context matters most. Hield's entire value is off-ball — scoring him low on #14 would be wrong. Irving's value is on-ball — low #14 is expected, not a weakness for his archetype.

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Lateral quickness / agility | NBA Combine (lane agility, shuttle) | 🟢 Web search | Quick feet enable sharp cuts and screen navigation. Cross-reference #22. Context for movement quality. |

N/A for NBA-level evaluation.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Cut + Off-Screen Synergy data (nba_api) + average offensive speed + CAS cross-reference (#4) + 2-season window + converging qualitative (3+ sources) | ±0.5 |
| Medium | Cut OR Off-Screen Synergy data + CAS cross-reference + one qualitative source OR EvanMiya off-screen data + qualitative convergence | ±1.0 |
| Low | CAS 3PT% only (no play-type breakdown) + single qualitative source | ±1.5 |
| Very Low | Inferred from archetype and system context — no movement data available | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 7.0–8.5 | Buddy Hield (locked) | 122 off-screen poss (0.95 PPP); 24 cut poss (1.29 PPP); 5.11 mph off speed; CAS 8.5 cross-ref | nba_api | The archetype. Entire offensive identity is off-ball. 122 off-screen possessions dwarfs all other test guards. Highest offensive speed. |
| 5.0–6.5 | Kyrie Irving (locked) | 45 cut poss (1.456 PPP, 78.5th pctile); 49 off-screen poss (1.006 PPP); 4.24 mph off speed | nba_api | More off-ball game than expected for on-ball creator. Elite cut efficiency. Functional awareness he doesn't fully exploit. |
| 5.0–6.5 | De'Aaron Fox (locked) | 38 cut poss (1.274 PPP); 16 off-screen poss; 4.73 mph off speed | nba_api | On-ball dominant. 16 off-screen possessions across two seasons is negligible. Cuts occasionally, doesn't work off screens. |
| 3.0–4.5 | Marcus Smart (locked) | 0 cut poss; 0 off-screen poss; 0.92 mi off distance (lowest); 4.35 mph off speed | nba_api | Zero off-ball scoring production. Literally no cut or off-screen data. Definitive absence. |

## Domain 5: Defense

---

### #15 — On-Ball Pressure

**Block A — Co-Primary Statistical Input (opponent shooting suppression + active disruption)**

On-ball defense produces two measurable outputs: how well you contain (opponent shooting efficiency) and how much you disrupt (deflections and steals). Expert consensus converges on opponent FG% as closest defender (DFGPOE) as the primary containment signal, and deflections as the primary disruption signal. BBall Index separates these as distinct metrics — Perimeter Isolation Defense for containment, Picket Pocket Rating for disruption. Both are required to capture the full picture of on-ball pressure.

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | Opponent FG% as closest defender (Overall) + D_FGA | LeagueDashPtDefend (DefenseCategory=Overall) via nba_api | 🟢 Automated | Containment efficiency + volume. How many shots defended and how well. Co-primary. |
| NBA | PCT_PLUSMINUS (DFGPOE) — opponent FG% vs their normal FG% | LeagueDashPtDefend via nba_api | 🟢 Automated | Shot suppression relative to opponent baseline. The best available isolation of individual defensive impact on shooting. Co-primary. |
| NBA | Opponent FG% on 3PT (Greater Than 15Ft) + D_FGA | LeagueDashPtDefend (DefenseCategory=3 Pointers) via nba_api | 🟢 Automated | Perimeter containment specifically. For guards, this is the most relevant zone split. Co-primary zone context. |
| NBA | Deflections per game | LeagueHustleStatsPlayer via nba_api | 🟢 Automated | Active disruption. Expert consensus: deflections are better than steals for measuring ball-disruption skill because steals include loose ball recovery randomness. Co-primary. |
| NBA | STL per game + STL rate | LeagueDashPlayerStats via nba_api | 🟢 Automated | Conversion output of disruption. Read alongside deflections — high steals on low deflections = gambling; high deflections with proportional steals = genuine skill. Co-primary. |
| College | Steal rate per possession | Basketball-Reference / EvanMiya | 🟢/🟡 | Universal proxy. No deflection tracking at college level. |
| College (enhanced) | Opponent-adjusted steal rate | EvanMiya | 🟡 Manual lookup | Better version — adjusts for opponent and pace. |
| International | STL per game from FIBA box scores | FIBA box scores via web search | 🟡 Manual per player | Basic but universally available. |

**Why co-primary (containment + disruption):** A player who holds opponents to low FG% but never gets deflections or steals is a positional defender — solid but passive. A player with high deflections but poor opponent FG% is a gambler — disrupts but gets burned. Elite on-ball pressure requires both.

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Contested shots per game (3PT split) | LeagueHustleStatsPlayer via nba_api | 🟢 Automated | Shot contest volume. High contested shots = engaged on-ball defender. 3PT contest split isolates perimeter activity. |
| 2 | Personal fouls per game | LeagueDashPlayerStats via nba_api | 🟢 Automated | Negative proxy. High fouls = reaching, lateral limitations, or over-aggression. Low fouls with high deflections = clean defender. |
| 3 | Opponent FG% on 2PT (Less Than 10Ft) | LeagueDashPtDefend (DefenseCategory=Less Than 10Ft) via nba_api | 🟢 Automated | Interior containment. For guards, measures how well they contest after being beaten — recovery finishing defense. |
| 4 | Isolation defense PPP + possessions | SynergyPlayTypes (Isolation, defensive) via nba_api | 🟢 Automated | Purest on-ball test — 1-on-1 with no screen action. Low PPP allowed = elite isolation stopper. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Elite perimeter defender," "lockdown," "clamps" — convergence across 3+ sources is a real signal. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule per R1. |
| BBall Index All-Defensive write-ups | 6 | 🟢 Web search | Matchup Difficulty percentile, On-Ball Defense percentile, Perimeter Isolation Defense percentile regularly cited. Capture during research. High-quality secondary signal. |
| All-Defensive team selections | 6 | 🟢 Web search | NBA All-Defensive team voting is a strong consensus signal for the top tier. Presence = real signal. Absence is not a negative signal. |

**Key language triggers from SUB-DOMAINS:**

Positive (midpoint rule): "hounds ball handlers," "active hands," "makes it difficult," "quick feet," "stays in front," "physical defender," "lockdown," "clamps"

Negative (anchoring): "gets beat off the dribble," "struggles to stay in front," "poor on-ball defender," reaching fouls, over-helping tendency

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Wingspan relative to height | NBA Combine / Pro Day | 🟢 Web search | +4" wingspan differential = structural on-ball advantage. Extends reach for contests and deflections. |
| Lateral quickness (lane agility, shuttle) | NBA Combine / Pro Day | 🟢 Web search | Cross-reference #22. Sets physical ceiling on on-ball coverage. |

N/A for NBA-level evaluation.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Opponent FG% + DFGPOE (LeagueDashPtDefend) + deflections + steals (hustle stats) + contested shots + 2-season window + converging qualitative from 3+ sources | ±0.5 |
| Medium | Opponent FG% OR deflections/steals + one qualitative source + personal fouls context OR standard box score + multiple qualitative convergence | ±1.0 |
| Low | STL rate only (no tracking context) + single qualitative source | ±1.5 |
| Very Low | Inferred from physical profile and archetype only — no defensive data available | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 7.0–8.5 | Marcus Smart (locked) | DFGPOE -4.6%; .419 opp FG%; ISO def 0.62 PPP; 2.57 defl/g; 1.5 stl/g; DPOY 2022 | nba_api + qualitative | The archetype. Only test guard who suppresses shooting below opponent baseline. 2x All-Defensive First Team. Multi-source: "elite defender," "lockdown," "shutdown." |
| 5.0–6.5 | De'Aaron Fox (locked) | DFGPOE +2.1%; 3.33 defl/g; 1.7 stl/g; 4.37 contested/g; ISO def 0.651 PPP (current 97th pctile) | nba_api + qualitative | Highest raw activity but opponents still shoot above baseline. Athletic tools + engagement without containment results. Improving. |
| 5.0–6.5 | Kyrie Irving (locked) | DFGPOE +1.1%; .474 opp FG%; 2.99 defl/g; 1.3 stl/g; ISO def 0.782 PPP | nba_api + qualitative | Neutral containment, moderate activity. No positive defensive reputation. Average-to-below guard defender. |
| 3.0–4.5 | Buddy Hield (locked) | DFGPOE +2.9%; .494 opp FG%; 1.72 defl/g; 0.8 stl/g; ISO def 1.053 PPP (~24th pctile) | nba_api + qualitative | Worst by every measure. Documented liability. Targeted in ISO. Zero charges drawn. |

---

### #16 — Help Defense

**Block A — Primary Statistical Input (composite of activity metrics + team defensive impact — no single stat captures help defense)**

Help defense is the hardest sub-domain to measure statistically. Rotations, weak-side positioning, and help-and-recover execution are invisible in every public database. The best available approach: combine team defensive impact (on/off splits) with hustle activity metrics as directional signals, then lean heavily on qualitative.

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | Team DRtg on-court vs off-court (differential) | LeagueDashPlayerStats (MeasureType=Advanced) via nba_api | 🟢 Automated | Directional — how much the team's defense improves when this player is on the floor. Heavily team-dependent but functional within the same team context. Primary directional signal. |
| NBA | DBPM (Defensive Box Plus/Minus) | Basketball-Reference | 🟢 Scrapeable | Estimates defensive contribution from box score. Biased but universally available and positionally adjusted. |
| NBA | Deflections per game | LeagueHustleStatsPlayer via nba_api | 🟢 Automated | Off-ball deflections signal active hands in passing lanes. Cross-referenced from #15 — same data, different diagnostic lens (off-ball vs on-ball context determined qualitatively). Priority 1 secondary for #16. |
| NBA | Charges drawn per game | LeagueHustleStatsPlayer via nba_api | 🟢 Automated | Help-side positioning signal. Drawing charges requires reading the play and establishing position in the lane before the driver arrives. |
| College | DBPR (defensive BPR) | EvanMiya | 🟡 Manual lookup | Supplementary signal for defensive sub-domains per established signal hierarchy. |
| College (fallback) | STL + BLK + DREB composite | Basketball-Reference | 🟢 Scrapeable | Crude proxy. Composite reading required. |
| International | Team DRtg equivalent from FIBA box scores where available | FIBA box scores via web search | 🟡 Manual per player | Limited. |

**Why no single stat is primary:** SUB-DOMAINS defines help defense as "rotations, weak-side positioning, switching, team defensive IQ." None of these have direct statistical measures. Team DRtg on/off is the broadest signal — it captures everything the player does defensively in one number, including help defense. But it's noisy (teammates, scheme, opponents). Best used as directional confirmation alongside qualitative evidence.

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | BLK rate for non-bigs | LeagueDashPlayerStats via nba_api | 🟢 Automated | Blocks from guards/wings signal help-side awareness — they're arriving from off-ball positions to contest at the rim. Different skill than rim protection (#17). |
| 2 | Loose balls recovered (defensive) | LeagueHustleStatsPlayer via nba_api | 🟢 Automated | Positioning and anticipation. Players in the right help position recover more loose balls. |
| 3 | Box-outs (defensive) | LeagueHustleStatsPlayer via nba_api | 🟢 Automated | Effort signal that crosses into help-side positioning. Active box-out after helping on a drive = full sequence execution. |
| 4 | Personal fouls per game | LeagueDashPlayerStats via nba_api | 🟢 Automated | Context. High fouls can indicate aggressive help (positive) or undisciplined help (negative). Read alongside qualitative. |

**Block C — Qualitative Signal Sources**

This is the primary scoring lever for #16. More than any other Domain 5 sub-domain, help defense is determined by scouting language and film-based analysis.

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Great rotations," "always in the right spot," "high defensive IQ" — convergence across 3+ sources is a real signal. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule per R1. |
| BBall Index All-Defensive write-ups | 6 | 🟢 Web search | Help Defense Talent percentile, Defensive Positional Versatility, D-LEBRON regularly cited. Capture during research. |
| Coaching system context | — | 🟢 Web search | Defensive praise within a scheme-heavy system carries more weight. System matters more for help defense than any other sub-domain. |

**Key language triggers from SUB-DOMAINS:**

Positive (midpoint rule): "reads the game defensively," "great rotations," "always in the right spot," "high defensive IQ," "switches well," "versatile defender"

Negative (anchoring): "ball-watching," "late rotations," "gambles for steals," "out of position," "loses assignments," switching refusal or inability

**Archetype context note:** Help defense is the sub-domain where effort (#25) and IQ (#24) crossover is highest. High on-ball effort with documented weak-side lapses scores at midpoint per SUB-DOMAINS — effort does not equal IQ.

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Wingspan | NBA Combine / Pro Day | 🟢 Web search | Longer wingspan enables help-side contest without leaving assignment as far. Context for recovery capability. |
| Lateral quickness | Cross-reference #22 | Internal | Lateral quickness determines how quickly a player can help and recover. Low #22 = structural ceiling on help-and-recover. |

N/A for NBA-level evaluation.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Team DRtg on/off + DBPM + deflections + charges drawn + hustle stats + 2-season window + converging qualitative from 3+ sources | ±0.5 |
| Medium | Team DRtg on/off OR DBPM + one of: hustle stats OR qualitative convergence (2+ sources) | ±1.0 |
| Low | Standard box score defensive stats only (STL, BLK) + single qualitative source | ±1.5 |
| Very Low | Inferred from archetype and role only — no defensive data or scouting language available | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 7.0–8.5 | Marcus Smart (locked) | DEF_RATING 108.1; 0.21 charges/g; 0.604 def box-outs/g; DPOY; multi-source "high defensive IQ," "can defend any position" | nba_api + qualitative | Help defense and switching IS his identity. DEF_RATING 5+ points better than all other test guards. |
| 5.0–6.5 | Kyrie Irving (locked) | DEF_RATING 113.4; 0.5 blk/g (highest); 0.516 loose balls/g; 0.06 charges/g | nba_api + qualitative | Highest BLK rate among test guards — help-side blocks signal some awareness. No positive defensive reputation overall. Slightly more activity than expected. |
| 3.0–4.5 | De'Aaron Fox (locked) | DEF_RATING 113.9; 0.028 charges/g; 0.4 blk/g; documented effort gaps | nba_api + qualitative | "Coasted on offensive brilliance." Team measurably worse with him on floor. Athletic tools without consistent rotational commitment. |
| 3.0–4.5 | Buddy Hield (locked) | DEF_RATING 112.3 (team context); 0.0 charges/g; lowest activity across all help metrics | nba_api + qualitative | Zero charges drawn across two seasons. Doesn't rotate, doesn't help. DEF_RATING inflated by Golden State defensive infrastructure. |

---

### #17 — Rim Protection

**Block A — Primary Statistical Input (opponent FG% at rim as closest defender)**

Rim protection has the cleanest single-stat signal of any defensive sub-domain. Opponent FG% at the rim when the player is the closest defender directly measures the skill SUB-DOMAINS defines.

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | Opponent FG% at rim (Less Than 6Ft) + D_FGA | LeagueDashPtDefend (DefenseCategory=Less Than 6Ft) via nba_api | 🟢 Automated | Efficiency + volume. The definitive rim protection metric. Primary. |
| NBA | PCT_PLUSMINUS at rim (DFGPOE) | LeagueDashPtDefend via nba_api | 🟢 Automated | How much the player suppresses rim shooting vs opponent baseline. Primary context. |
| NBA | BLK per game + BLK rate | LeagueDashPlayerStats via nba_api | 🟢 Automated | Shot-blocking output. Fallback proxy where tracking data is unavailable. Co-primary for college/international. |
| College | BLK rate per possession | Basketball-Reference / EvanMiya | 🟢/🟡 | No opponent FG% at rim at college level. BLK rate is the primary proxy. |
| College (enhanced) | Opponent-adjusted BLK rate | EvanMiya | 🟡 Manual lookup | Better version — adjusts for opponent and pace. |
| International | BLK per game from FIBA box scores | FIBA box scores via web search | 🟡 Manual per player | Basic but universally available. |

**Why opponent FG% at rim is definitive:** FiveThirtyEight's DRAYMOND metric and BBall Index's Rim Protection metric both use opponent FG% at the rim as the primary component. Analytics community converges here.

**Guard-specific note:** Guards rarely defend shots at the rim as the closest defender. D_FGA at rim for guards is typically very low — often single digits per season. Low volume IS the data — guards are not rim protectors. All four test guards scored at baseline (2.5).

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Contested shots (2PT) | LeagueHustleStatsPlayer via nba_api | 🟢 Automated | Interior contest volume. High 2PT contests without high blocks = shot alteration, not blocking. |
| 2 | Personal fouls per game | LeagueDashPlayerStats via nba_api | 🟢 Automated (total PF only) | Negative proxy. High fouls + high blocks = aggressive but undisciplined. Low fouls + high blocks = verticality and timing. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Protects the rim," "shot blocker," "deters drives," "great timing" — convergence across 3+ sources is a real signal. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule per R1. |

**Key language triggers from SUB-DOMAINS:**

Positive (midpoint rule): "protects the rim," "deters drives," "great timing," "shot blocker," "verticality"

Negative (anchoring): low block rate at competition level, high foul rate on block attempts, "gets out of position chasing blocks," deterrence failure

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Standing reach | NBA Combine / Pro Day | 🟢 Web search | Single most predictive physical measurement for rim protection ceiling per SUB-DOMAINS. |
| Wingspan relative to height | NBA Combine / Pro Day / FIBA testing | 🟢 Web search | Elite wingspan differential enables shot altering even without elite vertical. |
| Max vertical | NBA Combine / Pro Day | 🟢 Web search | Combined with standing reach, defines the player's blocking plane. Cross-reference #21. |

N/A for NBA-level evaluation.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Opponent FG% at rim + D_FGA volume (LeagueDashPtDefend, Less Than 6Ft) + BLK rate + contested 2PT + 2-season window + qualitative convergence | ±0.5 |
| Medium | BLK rate + contested shots + one qualitative source OR opponent FG% at rim on limited volume | ±1.0 |
| Low | BLK rate only (no tracking context) + single qualitative source | ±1.5 |
| Very Low | Inferred from physical profile (standing reach, wingspan) only — no rim defense data | ±2.0 |

**Practical note for guards:** Guard evaluation at #17 will almost always be High confidence at near baseline. The absence of rim defense IS the data, confirmed by near-zero D_FGA at rim.

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 9.0+ | Rudy Gobert (confirmed anchor library) | Elite opponent FG% at rim, elite BLK rate, DPOY selections | nba_api | The archetype for rim protection. |
| 2.0–3.0 | All four test guards (locked) | N/A — no D_FGA at rim data | nba_api | Guards do not protect the rim. Baseline at high confidence. |

---

### #18 — Post Defense

**Block A — Primary Statistical Input (opponent post-up efficiency)**

Post defense mirrors #3 (Post offense) in data architecture: play-type tracking is the primary signal, and college-level access is the hardest problem.

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | Opponent post-up PPP + possessions + FG% (defensive) | SynergyPlayTypes (PostUp, defensive) via nba_api | 🟢 Automated | How efficiently opponents score in the post against this player. Primary where volume exists. |
| NBA | Opponent FG% at Less Than 6Ft (as closest defender) | LeagueDashPtDefend (DefenseCategory=Less Than 6Ft) via nba_api | 🟢 Automated | Broader interior defense signal. Cross-referenced from #17 with different diagnostic intent. |
| College | Opponent post-up data cited in scouting reports | Synergy data in published prospect write-ups | 🟢 Web search capture | Same capture method as #3. |
| College (fallback) | DBPR + weight profile + qualitative | EvanMiya + web search | 🟡/🟢 | No post defense tracking at college level. |
| International | Post defense context from FIBA PBP where available | FIBA box scores via web search | 🟡 Manual per player | Limited. |

**Why Synergy post-up defense is primary:** It directly measures what SUB-DOMAINS defines — holding position, contesting post moves, denying deep catches.

**Guard-specific note:** Guards are rarely the primary defender on post-ups. For guard evaluation, the question is: "when switched onto a bigger player in the post, does the player hold or collapse?" This is more qualitative than statistical for guards.

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Defensive box-outs per game | LeagueHustleStatsPlayer via nba_api | 🟢 Automated | Post defense includes securing position after a post contest. |
| 2 | Personal fouls per game | LeagueDashPlayerStats via nba_api | 🟢 Automated | High fouls in interior situations = inability to hold position legally. |
| 3 | Opponent post-up frequency (possessions defended) | SynergyPlayTypes via nba_api | 🟢 Automated | Volume denominator. Context-dependent. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Holds position in the post," "tough to back down," "denies the catch" — convergence across 3+ sources is a real signal. Post defense language is rare for guards — its presence is notable. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule per R1. |

**Key language triggers from SUB-DOMAINS:**

Positive (midpoint rule): "holds position in the post," "tough to back down," "denies the catch," "strong base"

Negative (anchoring): "gets backed down," "too weak to hold position," "gives up deep catches easily," high foul rate in post defense

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Weight relative to position | NBA Combine / Pro Day | 🟢 Web search | Undersized post defender has structural ceiling. Cross-reference #23 (Strength). |
| Strength profile | Cross-reference #23 | Internal | #23 is the physical gate for post defense, same as #3 (post offense). |

N/A for NBA-level evaluation.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Opponent post-up PPP + possessions (Synergy defensive) + opponent FG% at rim + box-out rate + 2-season window + qualitative convergence | ±0.5 |
| Medium | Opponent FG% at rim (no post-specific split) + box-out data + one qualitative source OR Synergy post-up data on limited volume | ±1.0 |
| Low | Standard box score defensive stats only (no post-specific tracking) + single qualitative source | ±1.5 |
| Very Low | Inferred from physical profile and strength score only — no post defense data available | ±2.0 |

**Practical note for guards:** Guard evaluation at #18 will almost always be baseline at high confidence. Guards don't defend posts. Smart may edge slightly higher due to documented switching reputation.

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 5.0–6.5 | Marcus Smart (locked) | 0.6 post-up poss (prior only); multi-source: "can defend any position including center" | nba_api + qualitative | One of the few guards with documented post-switch capability. Statistical sample near-zero; qualitative reputation does the work. |
| 2.0–3.0 | Irving, Fox, Hield (locked) | Near-zero post-up possessions defended | nba_api | Guards do not defend posts. Baseline. |

## Domain 6: Rebounding

---

### #19 — Offensive Rebounding

**Block A — Primary Statistical Input (rate-based)**

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | OREB% (offensive rebound percentage) | LeagueDashPlayerStats (Advanced) via nba_api | 🟢 Automated | Rate-based primary. % of available offensive rebounds grabbed while on floor. Position-adjusted. |
| NBA | OREB per game | LeagueDashPlayerStats (Base) via nba_api | 🟢 Automated | Volume co-primary. Raw count provides context for rate. |
| College | OREB rate | Basketball-Reference / EvanMiya | 🟢/🟡 | Universally available. |
| International | OREB per game from FIBA box scores | FIBA box scores via web search | 🟡 Manual per player | Basic but universally available. |

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Contested OREBs per game | LeagueDashPtStats (Rebounding) via nba_api | 🟢 Automated | Effort signal. Contested boards require physicality and positioning. |
| 2 | OREB chances per game | LeagueDashPtStats (Rebounding) via nba_api | 🟢 Automated | How often the player is in position to grab an offensive board. Denominator for conversion rate. |
| 3 | OREB chance conversion % | LeagueDashPtStats (Rebounding) via nba_api | 🟢 Automated | When near an OREB, how often do they get it? Skill vs. opportunity. |
| 4 | Offensive box-outs per game | LeagueHustleStatsPlayer via nba_api | 🟢 Automated | Effort/positioning signal for creating second chances. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Crashes the glass," "relentless on the offensive boards" — rare for guards, presence is notable. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule per R1. |

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Weight relative to position | NBA Combine / Pro Day | 🟢 Web search | Heavier players have advantage battling for position. Cross-reference #23. |
| Wingspan | NBA Combine / Pro Day | 🟢 Web search | Longer reach extends rebounding radius. |

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | OREB% + OREB/g + contested/uncontested split + OREB chances + 2-season window + qualitative | ±0.5 |
| Medium | OREB rate + volume + box-outs + one qualitative source | ±1.0 |
| Low | Raw OREB/g only + single qualitative source | ±1.5 |
| Very Low | Inferred from physical profile only | ±2.0 |

**Guard-specific note:** Near baseline at high confidence for most guards. Guards don't crash the offensive glass.

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 9.0+ | Russell Westbrook (peak) | Elite OREB% for a guard, triple-double seasons | Basketball-Reference | The archetype for guard offensive rebounding. |
| 2.0–3.5 | All four test guards (locked) | OREB% 1.8–2.8%; OREB/g 0.42–1.04 | nba_api | Near baseline. Guards do not crash the offensive glass. |

---

### #20 — Defensive Rebounding

**Block A — Primary Statistical Input (rate-based)**

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | DREB% (defensive rebound percentage) | LeagueDashPlayerStats (Advanced) via nba_api | 🟢 Automated | Rate-based primary. % of available defensive rebounds grabbed while on floor. Position-adjusted. |
| NBA | DREB per game | LeagueDashPlayerStats (Base) via nba_api | 🟢 Automated | Volume co-primary. |
| College | DREB rate | Basketball-Reference / EvanMiya | 🟢/🟡 | Universally available. |
| International | DREB per game from FIBA box scores | FIBA box scores via web search | 🟡 Manual per player | Basic but universally available. |

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Contested DREBs per game | LeagueDashPtStats (Rebounding) via nba_api | 🟢 Automated | Boards won against competition. |
| 2 | DREB chances per game | LeagueDashPtStats (Rebounding) via nba_api | 🟢 Automated | Denominator for conversion rate. |
| 3 | DREB chance conversion % | LeagueDashPtStats (Rebounding) via nba_api | 🟢 Automated | Conversion efficiency — how often they finish the rebound when near it. |
| 4 | Defensive box-outs per game | LeagueHustleStatsPlayer via nba_api | 🟢 Automated | Process signal. High box-outs with low DREB% = boxes out for teammates (Smart pattern, S87-F01). |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Secures the defensive glass," "strong rebounder," "boxes out well." |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule per R1. |

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Height, weight, wingspan relative to position | NBA Combine / Pro Day | 🟢 Web search | Bigger guards rebound more. Cross-reference #23. |

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | DREB% + DREB/g + contested/uncontested split + DREB chances + box-outs + 2-season window + qualitative | ±0.5 |
| Medium | DREB rate + volume + box-outs + one qualitative source | ±1.0 |
| Low | Raw DREB/g only + single qualitative source | ±1.5 |
| Very Low | Inferred from physical profile only | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 9.0+ | Russell Westbrook (peak) | Elite DREB% for a guard | Basketball-Reference | The archetype for guard rebounding. |
| 5.0–6.5 | Fox (locked) | DREB% 10.5%; 3.82 DREB/g; 66.7% conversion (highest) | nba_api | Athletic tools enable board-work. Average-to-slightly-above for a guard. |
| 5.0–6.5 | Hield (locked) | DREB% 10.6% (highest rate); 2.56 DREB/g | nba_api | Highest rate despite fewest minutes. Functional per-minute rebounder. |
| 3.0–4.5 | Smart (locked) | DREB% 7.1%; 0.44 box-outs/g (highest); contested 25.9% (highest) | nba_api | Process-vs-output split (S87-F01). Boxes out for teammates. |

---

## Domain 7: Athleticism

---

### #21 — Burst / Explosion

**Block A — Primary Statistical Input (combine measurements + career performance)**

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA / Prospect | Max vertical leap (standing + max) | NBA Combine / Pro Day results | 🟢 Web search — publicly published | The definitive physical measurement for explosion. Primary for prospects. |
| NBA | Above-rim finishing frequency (dunk rate) | Derivable from Domain 1 data (ShotChartDetail) | 🟢 Automated (already in pipeline) | Career performance proxy. High dunk rate = above-rim player. |
| NBA | Drive rate (drives per game) | LeagueDashPtStats (Drives) via nba_api | 🟢 Automated (already in pipeline) | Drive volume reflects first-step burst — players with elite burst drive more. |
| NBA | Transition finishing frequency | SynergyPlayTypes (Transition) via nba_api | 🟢 Automated (already in pipeline) | Open-court speed and finishing. Cross-reference from Domain 4 data. |
| College | Vertical leap from combine/pro day | Web search | 🟢 Web search | Same measurement, same application. |
| International | Combine/camp vertical data where available | Web search | 🟡 Manual per player | Limited. |

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Sprint / 3/4 court sprint time | NBA Combine / Pro Day | 🟢 Web search | Straight-line speed. Context for burst type (horizontal vs vertical). |
| 2 | Fastbreak points relative to team | Derivable from transition data | 🟢 Automated | Open-court scoring output. |
| 3 | Transition play-type PPP + possessions | SynergyPlayTypes (Transition) via nba_api | 🟢 Already in pipeline | Transition production as explosion proxy. |
| 4 | Average speed / distance covered | LeagueDashPtStats (SpeedDistance) via nba_api | 🟢 Automated | Supplementary signal for burst/explosion. Confirms athletic profile. Not a primary — measures conditioning/role more than pure burst. Flagged Session 87, documented Session 88. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Explosive," "elite first step," "blur in the open floor," "above the rim." |
| Single-source scouting report | 7 | 🟢 Web search | Directional. |

**Key language triggers:** Positive: "explosive," "elite first step," "above the rim," "freak athlete." Negative: "lacks burst," "straight-line only," "no first step," "below the rim."

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Vertical leap (standing + max) | NBA Combine / Pro Day | 🟢 Web search | Primary measurement for explosion. |
| Standing reach | NBA Combine / Pro Day | 🟢 Web search | Combined with vertical, defines finishing plane. |
| Wingspan | NBA Combine / Pro Day | 🟢 Web search | Context for finishing reach. |

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Combine vertical + dunk rate + drive data + transition data + qualitative convergence | ±0.5 |
| Medium | Combine data OR dunk rate/drive data + qualitative | ±1.0 |
| Low | Recruiting athleticism grades + single qualitative | ±1.5 |
| Very Low | Inferred from physical profile only | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 8.0–9.0 | De'Aaron Fox (locked) | 38.5" vertical (reported); 8.6% dunk rate; 15.2 drives/game | nba_api + combine | Elite speed. Entire identity built on burst. |
| 6.5–7.5 | Kyrie Irving (locked) | 34.5" vertical; 0.5% dunk rate; craft-dominant | combine + nba_api | Good first step. Change-of-pace, not raw explosion. |
| 4.5–5.5 | Smart/Hield (locked) | Below average burst; limited above-rim play | combine + qualitative | Functional legs, limited explosion. |

---

### #22 — Lateral Quickness

**Block A — Primary Statistical Input (combine measurements + defensive performance)**

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA / Prospect | Lane agility time | NBA Combine / Pro Day results | 🟢 Web search — publicly published | The definitive measurement for lateral quickness. Primary for prospects. |
| NBA / Prospect | Shuttle run time | NBA Combine / Pro Day results | 🟢 Web search | Secondary agility measurement. |
| NBA | On-ball defense performance (#15 cross-reference) | LeagueDashPtDefend via nba_api | 🟢 Automated (already in pipeline) | Career performance proxy. Strong on-ball defense requires lateral quickness. |
| NBA | Opponent FG% as closest defender | LeagueDashPtDefend via nba_api | 🟢 Automated (already in pipeline) | Containment results reflect lateral ability. |
| College | Lane agility from combine/pro day | Web search | 🟢 Web search | Same measurement. |
| International | Combine/camp agility data where available | Web search | 🟡 Manual per player | Limited. |

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Reaching fouls as negative proxy | LeagueDashPlayerStats via nba_api | 🟢 Automated (total PF only) | High fouls can indicate lateral limitations — reaching because feet can't keep up. |
| 2 | Steals/deflections per possession | From Domain 5 data | 🟢 Already in pipeline | Active hands + quick feet together signal elite lateral quickness. |
| 3 | Contested shots per game | LeagueHustleStatsPlayer via nba_api | 🟢 Already in pipeline | Volume of contests reflects ability to stay in defensive position. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Quick feet," "stays in front," "mirrors the ball handler," "fluid hips." |
| Single-source scouting report | 7 | 🟢 Web search | Directional. |

**Key language triggers:** Positive: "quick feet," "stays in front," "mirrors," "fluid hips," "slides well." Negative: "heavy feet," "flat-footed," "slow laterally," "can't stay in front."

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Lane agility time | NBA Combine / Pro Day | 🟢 Web search | Primary measurement. |
| Shuttle run time | NBA Combine / Pro Day | 🟢 Web search | Secondary measurement. |

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Combine lane agility + #15 cross-reference + opponent FG% + qualitative convergence | ±0.5 |
| Medium | #15 cross-reference + qualitative | ±1.0 |
| Low | Single qualitative + physical inference | ±1.5 |
| Very Low | Body type inference only | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 7.5–8.5 | Marcus Smart (locked) | Lane agility 10.82s (elite); DPOY; #15 = 8.5; 6'9.25" wingspan | combine + nba_api | Elite. DPOY-level lateral quickness. |
| 6.5–7.5 | De'Aaron Fox (locked) | #15 = 6.2; athletic lateral movement; effort inconsistency | nba_api + qualitative | Solid tools, not elite application. |
| 5.5–6.5 | Kyrie Irving (locked) | #15 = 5.5; average wingspan | nba_api + qualitative | Average guard lateral quickness. |
| 4.0–5.0 | Buddy Hield (locked) | #15 = 4.0; ISO def 24th pctile; targeted | nba_api + qualitative | Significant liability. Root cause of defensive limitations. |

---

### #23 — Strength

**Block A — Primary Statistical Input (combine measurements + contact performance)**

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA / Prospect | Weight and body composition | NBA Combine / Pro Day results | 🟢 Web search — publicly published | The baseline physical measurement. Primary for prospects. |
| NBA / Prospect | Bench press (185 lbs reps) | NBA Combine / Pro Day results | 🟢 Web search | Direct strength measurement where available. |
| NBA | Contact finishing (#2 cross-reference) — FTR | From Domain 1 data | 🟢 Automated (already in pipeline) | FTR reflects ability to absorb and initiate contact. High FTR = functional strength. |
| NBA | Post defense (#18 cross-reference) | From Domain 5 data | 🟢 Already in pipeline | Holding position against post-ups requires strength. |
| College | Weight from combine/pro day | Web search | 🟢 Web search | Same measurement. |
| International | Weight from FIBA/combine data | Web search | 🟡 Manual per player | Limited. |

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Box-out effectiveness | LeagueHustleStatsPlayer via nba_api | 🟢 Already in pipeline | Box-outs require lower-body strength. Effective box-outs = functional strength. |
| 2 | Personal fouls in interior situations | LeagueDashPlayerStats via nba_api | 🟢 Automated | High interior fouls can indicate inability to hold position without fouling. |
| 3 | Screen quality | Qualitative only | 🟢 Web search | Setting effective screens requires strength. Rarely tracked statistically. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Strong," "physical," "uses body well," "strong base." |
| Single-source scouting report | 7 | 🟢 Web search | Directional. |

**Key language triggers:** Positive: "strong," "physical," "uses body well," "strong base," "powerful." Negative: "gets pushed off spot," "too slight," "needs to add strength," "gets overpowered."

**Block D — Physical / Biometric Data**

| Measurement | Source | Access | Application |
|---|---|---|---|
| Weight | NBA Combine / Pro Day | 🟢 Web search | Baseline. |
| Bench press (185 lbs reps) | NBA Combine / Pro Day | 🟢 Web search | Direct strength test where available. |
| Body composition (visual/qualitative) | Combine medical / scouting reports | 🟢 Web search | Functional weight matters more than scale weight. |

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Combine weight/bench + #2 cross-reference + FTR + #18 cross-reference + qualitative convergence | ±0.5 |
| Medium | Weight data + one cross-reference + qualitative | ±1.0 |
| Low | Estimated weight + single qualitative | ±1.5 |
| Very Low | Visual inference only | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 8.0–9.0 | Marcus Smart (locked) | ~220 lbs at 6'3"; bench 185 x 19 reps; "can defend any position including center"; #18 = 5.5 | combine + qualitative | Elite guard strength. Weapon. |
| 6.0–7.0 | Buddy Hield (locked) | 212 lbs at 6'3.75"; 6'9.25" wingspan; "strong physique" | combine + qualitative | Functional frame. Doesn't manifest offensively. |
| 5.5–6.5 | De'Aaron Fox (locked) | 169.6 lbs combine → ~200 lbs current; FTR .293; "exploited by bigger guards" | combine + nba_api | Average. Developed functional strength. |
| 5.0–6.0 | Kyrie Irving (locked) | 191 lbs; 6'4" wingspan; FTR .228; craft compensates | combine + nba_api | Below average. Avoids contact by design. |

## Domain 8: IQ / Motor

---

### #24 — Shot Selection

**Block A — Primary Statistical Input (shot quality distribution)**

*Expert consensus: shot selection is about the decisions, not the outcomes. Closest-defender openness distribution + zone distribution are the best accessible proxies. BBall Index Shot Making has 0.66 year-to-year stability vs. 0.28 for raw eFG% — shot quality context separates signal from noise. Second Spectrum qSQ is the gold standard but enterprise-only.*

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | Closest defender distance distribution (% of FGA at Very Tight 0-2ft, Tight 2-4ft, Open 4-6ft, Wide Open 6+ft) | LeagueDashPtShots via nba_api | 🟢 Automated | Shot quality distribution primary. Cross-reference with efficiency at each band to separate good selection from poor selection. |
| NBA | Shot distribution by zone (% at rim, % mid-range, % 3PT) | ShotChartDetail via nba_api | 🟢 Automated (already in pipeline from Domain 2) | Shot diet primary. |
| NBA | TS% relative to usage rate | LeagueDashPlayerStats (Advanced) via nba_api | 🟢 Automated | Composite efficiency cross-check. |
| College | Shot distribution by zone | Hoop-Math | 🟢 Scraper build required | Same logic. |
| College | TS% relative to usage | Basketball-Reference / EvanMiya | 🟢/🟡 | Same composite cross-check. |
| International | Shot distribution from FIBA box scores | FIBA box scores via web search | 🟡 Manual per player | Limited. |

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | FG% at each defender-distance band | LeagueDashPtShots via nba_api | 🟢 Automated | Separates shot selection from shot making. |
| 2 | Shot clock distribution | LeagueDashPtShots (GeneralRange) via nba_api | 🟢 Automated — pipeline issue: only 24-22 range returned data in v1; parameter investigation needed | Shot clock discipline. |
| 3 | Pull-up vs. catch-and-shoot ratio | LeagueDashPtShots via nba_api | 🟢 Automated (already in pipeline from Domain 2) | Context for shot diet. |
| 4 | Assist-to-FGA ratio | Derivable from existing data | 🟢 Automated | Restraint signal. Cross-references #11. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports | 6 | 🟢 Web search | "Takes the right shots," "knows his spots," "never forces it." |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule per R1. |
| Coach quotes about shot selection | 8 (elevated) | 🟢 Web search | Coaches see selection in practice context. |

**Key language triggers:** Positive: "takes the right shots," "knows his spots," "never forces it," "plays within himself." Negative: "forces shots," "shoots too many bad shots," "tunnel vision," "settles for tough looks."

**Block D — Physical / Biometric Data**

N/A. Shot selection is a cognitive/decision sub-domain.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Defender-distance distribution + zone distribution + TS%/usage + shot clock splits + qualitative convergence | ±0.5 |
| Medium | Zone distribution + TS%/usage + one qualitative source | ±1.0 |
| Low | TS% only (no shot quality context) + single qualitative source | ±1.5 |
| Very Low | Qualitative inference only | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 7.0–8.0 | Irving, Hield (locked) | Irving: 51.5% contested, justified by elite conversion. Hield: 37.4% wide-open, never forces. | nba_api + qualitative | Different paths to same band — creation aggression vs. role discipline. |
| 6.0–7.0 | Fox (locked) | 43% contested; good rim selection; documented 3PT forcing | nba_api + qualitative | Selection improving but perimeter diet runs ahead of ability. |
| 5.0–6.0 | Smart (locked) | Career-long multi-source shot selection criticism; improved but not resolved | nba_api + qualitative | Forces shots beyond his skill level. Below average. |

---

### #25 — Effort / Motor

**Block A — Primary Statistical Input (hustle stats — deflections + loose balls co-primary)**

*NBA hustle stat system (9 categories, human-charted since 2016) is the best available framework. Deflections and loose balls are most effort-driven and least position-biased. 82games.com finding: non-steal deflections negatively correlate with team winning — activity without quality is not effort. Marcus Smart is the only 3x Hustle Award winner.*

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | Deflections per game | LeagueHustleStatsPlayer via nba_api | 🟢 Automated (already in pipeline) | Activity primary. Must be contextualized — non-steal deflections alone correlate negatively with winning. |
| NBA | Loose balls recovered per game | LeagueHustleStatsPlayer via nba_api | 🟢 Automated (already in pipeline) | Willingness primary. Purest effort signal. Least position-biased. |
| NBA | Charges drawn per game | LeagueHustleStatsPlayer via nba_api | 🟢 Automated (already in pipeline) | Sacrifice signal. Strongest single-signal for competitive willingness. |
| College | Hustle stats where tracked | Limited | 🟡 Manual lookup | Not universally available. |
| International | Not tracked | N/A | 🔴 | Pure qualitative for international players. |

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | Contested shots per game (2PT + 3PT) | LeagueHustleStatsPlayer via nba_api | 🟢 Already in pipeline | Defensive effort. Position-biased — bigs contest more by default. |
| 2 | Box-outs per game (off + def) | LeagueHustleStatsPlayer via nba_api | 🟢 Already in pipeline | Effort on boards. Most impactful for team winning per modeling. Position-biased. |
| 3 | Screen assists | LeagueHustleStatsPlayer via nba_api | 🟢 Already in pipeline | Offensive effort. Most position-biased stat. |
| 4 | Average speed / distance covered | LeagueDashPtStats (SpeedDistance) via nba_api | 🟢 Automated | Conditioning/role signal more than effort. Supplementary only. |
| 5 | Playoff effort signal (per R13) | Scouting language + hustle stats | 🟢 Web search + nba_api | Playoff rise/fall specifically attributable to effort — e.g. "motor visibly elevated Games 5–7," visibly heightened screen navigation in elimination games. Channel 2 secondary input per R13. Applies when playoff sample minimum met. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Coach quotes about effort (non-recruiting) | 6 (elevated) | 🟢 Web search | Coaches see effort in practice. Carries more than directional weight per SUB-DOMAINS. |
| Multi-source scouting reports | 6 | 🟢 Web search | "Never stops," "relentless," "high motor," "first to the floor." |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule per R1. |

**Key language triggers:** Positive: "never stops," "first to the floor," "relentless," "high motor," "elite effort." Negative: "coasts," "selective effort," "disappears in stretches," "not always engaged," "takes plays off."

**Block D — Physical / Biometric Data**

N/A. Effort/Motor is a behavioral sub-domain.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Full hustle suite (deflections + loose balls + charges + contested + box-outs) + 2-season window + qualitative convergence | ±0.5 |
| Medium | Deflections + loose balls + one qualitative source | ±1.0 |
| Low | Single hustle stat + single qualitative source | ±1.5 |
| Very Low | Qualitative inference only | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 8.0–9.0 | Smart (locked) | 3x Hustle Award; DPOY; highest charges/box-outs among test guards | nba_api + qualitative | Effort IS the identity. Age-adjusted from 9.0. |
| 5.5–6.5 | Irving, Fox (locked) | Irving: average overall, "solid defender if focused." Fox: highest raw activity, documented defensive gaps. | nba_api + qualitative | Different paths to same band — adequate vs. paradoxical. |
| 5.0–6.0 | Hield (locked) | Zero charges; lowest hustle stats; highest off-ball speed | nba_api + qualitative | Selective effort. Offensive movement, absent defensive effort. |

---

### #26 — Competitive Character

**Block A — Primary Statistical Input (clutch stats — supplementary only)**

*Expert consensus divided on whether clutch is a persistent trait or noise. NBA defines clutch as last 5 min within 5 pts. This sub-domain is ~90% qualitative. Negative signals are more reliably predictive than positive per expert research and SUB-DOMAINS definition.*

| Level | Stat | Source | Access | Role |
|---|---|---|---|---|
| NBA | Clutch stats (FG%, TS%, plus/minus, usage) | LeagueDashPlayerClutch via nba_api | 🟢 Automated | Supplementary. Confirms or contradicts qualitative picture. Small samples — noisy. |
| NBA | Playoff rise/shrink vs. regular season (per R13) | Basketball-Reference / nba_api | 🟢 Automated/Scrapeable | **Co-primary** with clutch stats. Multi-run performance trajectory under elevated stakes. R13 Channel 2 direct input. |
| College | Tournament performance | Basketball-Reference / web search | 🟢 Web search | March Madness is highest-leverage sample for college players. |
| International | FIBA knockout round performance | FIBA box scores via web search | 🟡 Manual per player | Limited but meaningful when available. |

**R13 playoff treatment (Channel 2 primary):** Playoff track record is a primary input for #26, not supplementary. Classification follows R13 Stage 1 (strong/moderate rise or shrink based on statistical + qualitative convergence across ≥2 runs). Multi-run risers anchor the upper band (7.5+); multi-run shrinkers anchor the lower band (≤5.5). Single-run samples are directional only. See SCORING-RULES.md R13 for the full classification protocol.

**Block B — Secondary Statistical Inputs**

| Priority | Stat | Source | Access | What it adds |
|---|---|---|---|---|
| 1 | 4th quarter performance splits | LeagueDashPlayerStats (Period=4) via nba_api | 🟢 Automated | Does output hold in Q4? |
| 2 | Road vs. home splits | LeagueDashPlayerStats (Location) via nba_api | 🟢 Automated | Weak signal — many confounds. |
| 3 | Games played / availability | Basketball-Reference | 🟢 Scrapeable | Longevity and availability per SUB-DOMAINS. |

**Block C — Qualitative Signal Sources**

| Source type | R2 priority | Access | Credibility note |
|---|---|---|---|
| Multi-source scouting reports (character convergence) | 5 (elevated — highest for this sub-domain) | 🟢 Web search | Convergence across 3+ independent sources is the strongest signal. |
| Peer and opponent testimony | 5 (elevated) | 🟢 Web search | "It sucks to play against this player." Highest-credibility character source. |
| Coach quotes (non-recruiting) | 6 | 🟢 Web search | Post-game/post-season language. Higher credibility than recruiting context. |
| Single-source scouting report | 7 | 🟢 Web search | Directional. Midpoint rule per R1. |
| Off-court character data | Variable | 🟢 Web search | Transfer history, attitude issues, coaching relationships. Multiple flags across programs = ceiling. |

**Key language triggers:** Positive: "competes every possession," "hates to lose," "tough," "warrior," "thrives in big moments." Negative (MORE predictive): "soft," "folds under pressure," "disappears in big games," "quits," "disengages after bad moments."

**Critical weighing note:** Negative signals carry MORE weight than positive per expert research and SUB-DOMAINS. Scouts more reliably identify who won't compete than who will. No negative signals + moderate positive = 6.5–7.0 default.

**Block D — Physical / Biometric Data**

N/A. Competitive character is a behavioral/psychological sub-domain.

**Block E — Confidence Threshold Table**

| Confidence | Required inputs | R4 interval |
|---|---|---|
| High | Clutch stats (2-season) + playoff data + multi-source qualitative convergence (3+) + peer/opponent testimony | ±0.5 |
| Medium | Clutch stats + one qualitative source OR multi-source qualitative without statistical confirmation | ±1.0 |
| Low | Single qualitative source + limited statistical data | ±1.5 |
| Very Low | Inferred from role and team context only | ±2.0 |

**Block F — Peer Comparison Reference**

| Band | Player | Key stat | Source | Notes |
|---|---|---|---|---|
| 8.0–9.0 | Smart (locked) | Multi-source coach/teammate/opponent testimony; DPOY; 2022 Finals | nba_api + qualitative | Competitive character IS the identity. |
| 7.0–8.0 | Irving (locked) | 2016 Finals Game 7 dagger; documented big-moment performer; off-court flags cap | nba_api + qualitative | On-court fire is real. Off-court pattern caps below 8.0. |
| 6.5–7.5 | Fox (locked) | 2023 playoffs 28.5 PPG; no negative signals; limited sample | qualitative | Solid competitor. Medium confidence. |
| 5.5–6.5 | Hield (locked) | No signal either direction; role player default | qualitative | Absence = average. Medium confidence. |

---

## NBA Comp Matching (Skill 5)

This section documents data sources for the statistical similarity match in the NBA Comp Methodology. These stats are not sub-domain inputs — they feed the comp assignment process in Skill 5 (scout-output) per NBA-COMP-METHODOLOGY.md.

---

### Statistical Similarity Stats

**Script:** NBA_Comp_Stats.py
**Endpoint:** LeagueDashPlayerStats (MeasureType=Advanced) + PlayerCareerStats (for rookie season detection)
**Default mode:** Comp candidate's rookie season. Flags: `--current` for active evaluation, `--season YYYY-YY` for specific season.

| Stat | nba_api field | Group usage | Tolerance band | Notes |
|---|---|---|---|---|
| True Shooting % | TS_PCT | All groups (primary signal) | ±5% | Fallback to PPG (±4 pts) when unavailable |
| Usage rate | USG_PCT | All groups (secondary) | ±5% | |
| Assist rate | AST_PCT | Guards (secondary) | ±4% | |
| Turnover rate | TOV_PCT | Guards (secondary) | ±2% | |
| Rebound rate | REB_PCT | Wings + Bigs (secondary) | ±5% | Total rebound rate. OREB_PCT and DREB_PCT also pulled for context. |
| Steal rate | STL_PCT | Wings (secondary) | ±1.5% | May not be available in all Advanced endpoint responses — verify per season |
| Block rate | BLK_PCT | Bigs (secondary) | ±2% | May not be available in all Advanced endpoint responses — verify per season |
| PPG | PTS (Base, PerGame) | Fallback only | ±4 pts | Used when TS% is unavailable |

### Group-Specific Stat Sets

| Group | Primary | Secondary signals |
|---|---|---|
| Guards | TS% | Usage rate, Assist rate, Turnover rate |
| Wings | TS% | Usage rate, Rebound rate, Steal rate |
| Bigs | TS% | Usage rate, Rebound rate, Block rate |

### Comp Tier Determination (from NBA-COMP-METHODOLOGY.md)

| Tier | Criteria |
|---|---|
| 🟢 Full | Primary signal confirmed + at least two secondary signals within tolerance |
| 🟡 Partial | Primary confirmed + one secondary within tolerance; remainder inferred |
| 🔴 Rubric only | Primary unavailable or no statistical match achievable |

### Access and Coverage

| Level | Access | Notes |
|---|---|---|
| NBA | 🟢 Automated via nba_api | LeagueDashPlayerStats Advanced available for all NBA seasons since tracking era |
| College | 🔴 Not available | Advanced rate stats (USG%, AST%, etc.) not available for college. Comp matching is NBA-to-NBA only. Prospect stats are projected from rubric, not pulled. |
| International | 🔴 Not available | Same limitation as college |

### Data Flow

1. Skill 3 identifies the prospect's archetype and positional group
2. Skill 5 identifies 2–3 comp candidates (same group, same archetype bucket)
3. Run `NBA_Comp_Stats.py 'Comp Candidate' --rookie` for each candidate → gets their rookie-season stats
4. Compare candidate stats against the prospect's projected stats (derived from rubric profile, not from a script)
5. Apply tolerance bands → determine comp tier (🟢/🟡/🔴)
6. Comp tier gates the projection midpoint weight (25%/15%/5%)
