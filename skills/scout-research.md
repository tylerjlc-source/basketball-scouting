---
name: scout-research
description: "Gather all available data for a basketball player evaluation. Runs statistical scripts for NBA players, searches for scouting reports, biometrics, character signals, and qualitative evidence. Produces a structured research packet that feeds scout-scoring. Invoke when asked to scout, evaluate, research, or pull data on a basketball player — this is always the first step before any scoring begins."
---

# Skill 1 — Scout Research

**Job:** Gather every available data point for a player evaluation. Structure it into a research packet.
**Position in chain:** First. Nothing scores until research is complete.
**Hands off to:** Skill 2 (scout-scoring)

---

## LOADING INSTRUCTIONS

On every invocation, load:
1. **This file (SKILL.md)** — research protocol and output format
2. **BASKETBALL-BRAIN.md** — foundational domain knowledge. Read before researching. Shapes what to look for and how to interpret what you find.
3. **SCRIPT-REGISTRY.md** — maps Python scripts to sub-domains. Governs automated data collection for NBA players.
4. **learnings/scout-research-learnings.md** — active calibration learnings for this skill. Apply before executing research protocol.

Load conditionally:
5. **SUB-DOMAIN-SOURCE-MAP_v1.md** — deep reference for what data feeds each sub-domain. Load specific sub-domain blocks when you need to verify what sources exist for a particular skill area. Do not load the entire file upfront — it is 1,683 lines. Search by sub-domain number.

---

## RESEARCH PROTOCOL

### Step 1 — Identify the player

Resolve internally before proceeding: full name, listed position, current team/school/club, competition level (NBA / College D1 / International / HS), age (or draft-year age if prospect).

**For known active NBA players, proceed silently to Step 2 — do not echo metadata back to the user.** Only ask for confirmation when the player is genuinely ambiguous (multiple players with same name, prospect with unclear declaration status, retired-vs-active uncertainty, competition level not obvious from context). Wrong competition level means wrong data pipeline.

### Step 2 — Run the statistical pipeline

**NBA players only.** College, international, and high school players skip to Step 3.

Run all seven domain scripts per SCRIPT-REGISTRY.md (execution protocol, evaluation window, and conditional Playoff_Track_Record run all governed there).

If a script fails or returns incomplete data, log the gap in the research packet. Do not skip the sub-domains it feeds — they score at lower confidence, not zero.

### Step 3 — Qualitative research (all competition levels)

Search for and collect:

**Scouting reports** (target: 3+ independent sources)
- Published prospect write-ups (NBADraft.net, 247Sports, On3, The Ringer, ESPN, The Athletic, Bleacher Report)
- Capture specific language — "tight handle," "struggles against length," "elite motor" — not summaries
- Note source and date for each report
- Capture any Synergy data cited in reports (percentiles, PPP by play type)

**Biometrics and physical data**
- Height, weight, wingspan, standing reach (NBA Combine / Pro Day / FIBA testing)
- Vertical leap (standing + max), lane agility, shuttle run, bench press reps
- Body type observations from scouting language

**Character and behavioral signals**
- Coach quotes (distinguish recruiting context vs. post-game/post-season)
- Transfer history, program relationships
- Work ethic language from multiple sources
- Negative signals: attitude issues, effort concerns, disengagement patterns
- Peer and opponent testimony where available

**Competition context**
- Conference / league strength
- Role on team (primary option, secondary, role player)
- Year-over-year statistical trajectory (improving, flat, declining)

**Playoff / big-game track record**
- **Sample minimums:** ≥2 separate playoff series across different years (NBA), ≥4 career tournament games (NCAA prospects). Below minimum: narrative mention only, no R13 modifier consequence.
- **Collect:** multi-source rise/fall language and playoff-vs-regular-season statistical deltas (TS% career-matched delta is the primary stat; archetype-primary stats like DFGPOE substitute when better suited).
- **Classification labels for the packet** (Skill 2/4 apply the modifier from these): strong rise / moderate rise / neutral / moderate shrink / strong shrink / below sample.
- **Recency status:** active (within last 2 playoff cycles) / historical-only (last playoff ≥3 years ago) / active-injury dormant (recent activity but documented multi-source injury rules out next playoff cycle).
- Skill 2 / Skill 4 apply the magnitude logic per SCORING-RULES.md R13. Skill 1's job here is evidence collection and classification only.

**Non-NBA data sources** (college, international): see SCRIPT-REGISTRY.md "COLLEGE / HS / INTERNATIONAL PLAYERS" section for source list. Load specific sub-domain blocks from SUB-DOMAIN-SOURCE-MAP_v1.md when verifying which sources feed a given skill area.

### Step 4 — Identify data gaps

Before assembling the packet, explicitly list:
- Which sub-domains have strong statistical support
- Which sub-domains rely on qualitative evidence only
- Which sub-domains have no direct evidence (will score at Very Low confidence)
- Any conflicting signals between sources

This gap inventory feeds confidence scoring in Skill 2.

### Step 5 — Persist the packet

After the packet is assembled, save it to:

`raw/[Player_Name]/[YYYY-MM-DD]_research-packet.md`

- `[Player_Name]` uses underscores (matches output/ convention).
- `[YYYY-MM-DD]` matches the EVALUATION DATE field in the packet header.
- Create the player folder if it does not exist.
- File content: a top-level H1 (`# Research Packet — [Player Name] — [YYYY-MM-DD]`) followed by the packet body exactly as assembled in the OUTPUT section below.

The saved packet is immutable. Later evaluations of the same player write new dated files to the same folder; never overwrite prior packets. This preserves longitudinal history for cross-season comparison, calibration drift detection, and future wiki indexing.

Save before handing off to Skill 2. If saving fails, stop and surface — do not proceed to scoring with an unpersisted packet.

---

## OUTPUT — RESEARCH PACKET FORMAT

The research packet is the handoff to Skill 2 (scout-scoring). It must be structured, not raw. Organize by domain, not by source.

```
=== RESEARCH PACKET ===
PLAYER: [Full name]
POSITION: [Listed position]
AGE: [Current age or draft-day age]
TEAM: [Current team / school / club]
COMPETITION LEVEL: [NBA / College D1 / Mid-major / International / HS]
EVALUATION DATE: [Date of research]

--- PHYSICAL PROFILE ---
Height:         [ft/in]
Wingspan:       [ft/in or unknown]
Weight:         [lbs or estimated]
Standing reach: [in or unknown]
Vertical:       [in or unknown] (standing / max)
Lane agility:   [sec or unknown]
Body type:      [lean/projectable | filled-out | undersized | etc.]

--- DOMAINS 1–8 (one section per domain) ---
Each domain section contains three blocks:
[Statistical data — key stats from scripts or manual lookup]
[Qualitative signals — specific scouting language with source attribution]
[Data gaps — what's missing or unavailable]
Domains: 1-Finishing, 2-Shooting, 3-Ball Skills, 4-Playmaking, 5-Defense, 6-Rebounding, 7-Athleticism, 8-IQ/Motor

--- CHARACTER / PROJECTION SIGNALS ---
[Work ethic evidence — sources and language]
[Competitive character evidence — sources and language]
[Negative signals — if any, with sources]
[Trajectory: improving / flat / declining — with evidence]

--- PLAYOFF / BIG-GAME TRACK RECORD (if R13 sample minimum met) ---
[Statistical rise/fall vs. regular-season baseline — from Playoff_Track_Record.py or manual playoff box-score comparison]
[Qualitative language — multi-source, with source attribution]
[Classification: strong rise / moderate rise / neutral / moderate shrink / strong shrink / below sample]
[Recency status: active (within last 2 playoff cycles) / historical-only / active-injury dormant]

--- INJURY HISTORY ---
[Documented injuries with dates and recovery status]
[If R9 (injury temper) may apply, flag with named injury, multi-source confirmation, pre-injury baseline, mechanism-mapped decline]
[If R12 may apply (both eval-window seasons compromised by named multi-source injury), flag with the healthy anchor season identified for Skill 2 to apply. S120 step-back case: if current is 0-GP miss but prior is healthy, note that the eval window can shift one position back rather than R12 anchor mode.]

--- DATA GAP INVENTORY ---
[Sub-domains with strong support (3+ sources)]
[Sub-domains with moderate support (2 sources)]
[Sub-domains with weak support (1 source)]
[Sub-domains with no direct evidence]
[Conflicting signals between sources]
```

---

## RULES FOR RESEARCH

**R1 — Capture language, not summaries.** Record the actual words scouts use. "Struggles against length at the rim" is data. "Needs to improve finishing" is noise. Specific language feeds sub-domain scoring. Vague language does not.

**R2 — Source quality matters.** Tag every piece of evidence with its source. Signal hierarchy (8 levels, descending): combine biometric > multi-season Power Conf stats > single-season > multi-circuit EYBL/AAU (with competition temper) > international (with competition-level temper) > multi-source qualitative scouting > single-source qualitative > recruiting coach quotes (directional only — never primary justification). Three independent reports converging on the same observation is a real signal.

**R3 — Negative signals get equal search effort.** For every positive attribute found, actively search for negative evidence on the same skill. Do not stop searching when you find something good.

**R4 — Absence is data.** If web search returns zero post-up language for a player, that IS the finding. Log it. "No documented post role at any level" is a research result that feeds a baseline score. Do not leave the domain section blank — state what was not found.

**R5 — Do not score during research.** The research packet contains evidence, not verdicts. No sub-domain scores appear in this output — scoring happens in Skill 2.

---

*Skill 1 of 6 in the scouting chain.*
