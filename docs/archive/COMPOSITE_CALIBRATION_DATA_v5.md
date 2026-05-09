# COMPOSITE CALIBRATION DATA — Layer 1 Scouting Rubric — v5

**ARCHIVED 2026-05-09.** Superseded by `docs/ANCHOR-LIBRARY.md` (current confirmed composite anchors) and `docs/COMPOSITE-SCALE-AND-TIERS.md` (current tier scale). Preserved as the historical calibration-set audit trail from the formula reverse-engineering phase. Do not consult for active scoring — anchors here are stale relative to the current rubric. Original "Load alongside" pointers below reference docs that have themselves been superseded; treat the file as read-only history.

**Purpose:** Accumulating dataset of player builds for composite formula analysis and validation.
**Load alongside:** COMPOSITE-SCALE-AND-TIERS.md, ARCHETYPE-WEIGHTS_v3.md, POSITION-WEIGHTS-AND-NONNEG.md

---

## DOCUMENT RULES

**Status codes:**
- `calibration` — confirmed anchor player; target composite is a fixed reference point
- `validation` — new player scored against the rubric; used to test formula consistency
- `prospect` — draft prospect build; no confirmed target yet

**Domain scores** are computed from sub-domain scores using position-weighted two-stage formula.
**Raw composite** is computed using archetype-flat formula (H=3, M=2, L=1, N=0).
**Formula status:** NOT LOCKED. Raw composite is a working value — do not treat as final output.
**Target composite** is the calibration anchor. The formula is being reverse-engineered to match it.

**Gap** = Raw composite − Target midpoint. Negative = formula underweights the player.

---

## CALIBRATION PLAYERS

---

### Steph Curry

| Field | Value |
|---|---|
| Archetype | Offensive Engine |
| Position | PG |
| Status | calibration |
| Notes | Career median |
| Target composite | 9.00–9.10 |
| Target midpoint | 9.05 |
| Raw composite | 8.28 |
| Gap | −0.77 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 6.75 |
| D2 Shooting | 9.35 |
| D3 Ball Skills | 8.69 |
| D4 Playmaking | 8.40 |
| D5 Defense | 7.25 |
| D6 Rebounding | 5.50 |
| D7 Athleticism | 7.30 |
| D8 IQ / Motor | 9.00 |

**Sub-domain scores:**

| # | Sub-domain | Score |
|---|---|---|
| 1 | At-basket finishing | 6.5 |
| 2 | Contact finishing / foul draw | 7.0 |
| 3 | Post offense | 2.5 |
| 4 | Catch-and-shoot 3PT | 10.0 |
| 5 | Off-dribble shooting | 9.5 |
| 6 | Mid-range | 8.0 |
| 7 | Free throw | 9.5 |
| 8 | Handling / creation | 9.0 |
| 9 | Touch / feel | 8.5 |
| 10 | Ball security | 8.5 |
| 11 | Court vision | 8.5 |
| 12 | Decision-making | 9.0 |
| 13 | Passing execution | 8.0 |
| 14 | Off-ball movement | 7.5 |
| 15 | On-ball pressure | 7.0 |
| 16 | Help defense | 7.5 |
| 17 | Rim protection | 2.0 |
| 18 | Post defense | 2.5 |
| 19 | Offensive rebounding | 3.0 |
| 20 | Defensive rebounding | 5.5 |
| 21 | Burst / explosion | 8.0 |
| 22 | Lateral quickness | 7.5 |
| 23 | Strength | 5.5 |
| 24 | Shot selection | 10.0 |
| 25 | Effort / motor | 7.5 |
| 26 | Competitive character | 9.0 |

---

### Shai Gilgeous-Alexander

| Field | Value |
|---|---|
| Archetype | Offensive Engine |
| Position | PG |
| Status | calibration |
| Notes | Current |
| Target composite | 9.10–9.20 |
| Target midpoint | 9.15 |
| Raw composite | 8.75 |
| Gap | −0.40 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 9.50 |
| D2 Shooting | 8.65 |
| D3 Ball Skills | 9.00 |
| D4 Playmaking | 8.45 |
| D5 Defense | 8.50 |
| D6 Rebounding | 6.00 |
| D7 Athleticism | 8.40 |
| D8 IQ / Motor | 9.07 |

**Sub-domain scores:**

| # | Sub-domain | Score |
|---|---|---|
| 1 | At-basket finishing | 9.5 |
| 2 | Contact finishing / foul draw | 9.5 |
| 3 | Post offense | 4.0 |
| 4 | Catch-and-shoot 3PT | 7.0 |
| 5 | Off-dribble shooting | 9.5 |
| 6 | Mid-range | 9.5 |
| 7 | Free throw | 9.0 |
| 8 | Handling / creation | 9.5 |
| 9 | Touch / feel | 9.0 |
| 10 | Ball security | 8.5 |
| 11 | Court vision | 8.5 |
| 12 | Decision-making | 9.0 |
| 13 | Passing execution | 8.5 |
| 14 | Off-ball movement | 6.5 |
| 15 | On-ball pressure | 8.5 |
| 16 | Help defense | 8.5 |
| 17 | Rim protection | 2.0 |
| 18 | Post defense | 3.0 |
| 19 | Offensive rebounding | 3.5 |
| 20 | Defensive rebounding | 6.0 |
| 21 | Burst / explosion | 9.0 |
| 22 | Lateral quickness | 8.5 |
| 23 | Strength | 7.0 |
| 24 | Shot selection | 9.5 |
| 25 | Effort / motor | 8.5 |
| 26 | Competitive character | 9.0 |

---

### Damian Lillard

| Field | Value |
|---|---|
| Archetype | Offensive Engine |
| Position | PG |
| Status | calibration |
| Notes | Career median |
| Target composite | 8.75–8.85 |
| Target midpoint | 8.80 |
| Raw composite | 7.62 |
| Gap | −1.18 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 7.50 |
| D2 Shooting | 8.45 |
| D3 Ball Skills | 8.38 |
| D4 Playmaking | 7.55 |
| D5 Defense | 6.25 |
| D6 Rebounding | 5.50 |
| D7 Athleticism | 6.10 |
| D8 IQ / Motor | 7.79 |

**Sub-domain scores:**

| # | Sub-domain | Score |
|---|---|---|
| 1 | At-basket finishing | 6.5 |
| 2 | Contact finishing / foul draw | 8.5 |
| 3 | Post offense | 3.5 |
| 4 | Catch-and-shoot 3PT | 8.0 |
| 5 | Off-dribble shooting | 9.5 |
| 6 | Mid-range | 7.5 |
| 7 | Free throw | 8.5 |
| 8 | Handling / creation | 9.0 |
| 9 | Touch / feel | 8.0 |
| 10 | Ball security | 8.0 |
| 11 | Court vision | 7.5 |
| 12 | Decision-making | 8.0 |
| 13 | Passing execution | 7.5 |
| 14 | Off-ball movement | 6.5 |
| 15 | On-ball pressure | 6.0 |
| 16 | Help defense | 6.5 |
| 17 | Rim protection | 2.5 |
| 18 | Post defense | 3.0 |
| 19 | Offensive rebounding | 3.5 |
| 20 | Defensive rebounding | 5.5 |
| 21 | Burst / explosion | 7.0 |
| 22 | Lateral quickness | 5.5 |
| 23 | Strength | 5.5 |
| 24 | Shot selection | 8.5 |
| 25 | Effort / motor | 6.0 |
| 26 | Competitive character | 8.5 |

---

### Luka Doncic

| Field | Value |
|---|---|
| Archetype | Jumbo Playmaker |
| Position | PG |
| Status | calibration |
| Notes | Current |
| Target composite | 8.75–8.85 |
| Target midpoint | 8.80 |
| Raw composite | 7.94 |
| Gap | −0.86 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 8.45 |
| D2 Shooting | 8.22 |
| D3 Ball Skills | 8.72 |
| D4 Playmaking | 8.83 |
| D5 Defense | 6.35 |
| D6 Rebounding | 8.20 |
| D7 Athleticism | 5.56 |
| D8 IQ / Motor | 7.73 |

**Sub-domain scores:**

| # | Sub-domain | Score |
|---|---|---|
| 1 | At-basket finishing | 8.3 |
| 2 | Contact finishing / foul draw | 8.6 |
| 3 | Post offense | 8.1 |
| 4 | Catch-and-shoot 3PT | 7.4 |
| 5 | Off-dribble shooting | 9.4 |
| 6 | Mid-range | 8.7 |
| 7 | Free throw | 7.2 |
| 8 | Handling / creation | 9.2 |
| 9 | Touch / feel | 9.4 |
| 10 | Ball security | 7.8 |
| 11 | Court vision | 9.5 |
| 12 | Decision-making | 9.1 |
| 13 | Passing execution | 9.0 |
| 14 | Off-ball movement | 5.5 |
| 15 | On-ball pressure | 6.2 |
| 16 | Help defense | 6.5 |
| 17 | Rim protection | 2.5 |
| 18 | Post defense | 3.5 |
| 19 | Offensive rebounding | 6.5 |
| 20 | Defensive rebounding | 8.2 |
| 21 | Burst / explosion | 5.5 |
| 22 | Lateral quickness | 4.8 |
| 23 | Strength | 7.2 |
| 24 | Shot selection | 9.1 |
| 25 | Effort / motor | 5.8 |
| 26 | Competitive character | 7.6 |

---

### LeBron James

| Field | Value |
|---|---|
| Archetype | Jumbo Playmaker |
| Position | PG |
| Status | calibration |
| Notes | Peak |
| Target composite | 9.75–9.80 |
| Target midpoint | 9.775 |
| Raw composite | 8.69 |
| Gap | −1.085 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 9.25 |
| D2 Shooting | 7.70 |
| D3 Ball Skills | 8.56 |
| D4 Playmaking | 9.12 |
| D5 Defense | 8.90 |
| D6 Rebounding | 8.10 |
| D7 Athleticism | 8.92 |
| D8 IQ / Motor | 8.40 |

**Sub-domain scores:**

| # | Sub-domain | Score |
|---|---|---|
| 1 | At-basket finishing | 9.7 |
| 2 | Contact finishing / foul draw | 8.8 |
| 3 | Post offense | 8.4 |
| 4 | Catch-and-shoot 3PT | 7.6 |
| 5 | Off-dribble shooting | 7.8 |
| 6 | Mid-range | 8.6 |
| 7 | Free throw | 6.8 |
| 8 | Handling / creation | 8.7 |
| 9 | Touch / feel | 8.9 |
| 10 | Ball security | 8.2 |
| 11 | Court vision | 9.7 |
| 12 | Decision-making | 9.4 |
| 13 | Passing execution | 9.3 |
| 14 | Off-ball movement | 6.0 |
| 15 | On-ball pressure | 8.8 |
| 16 | Help defense | 9.0 |
| 17 | Rim protection | 5.5 |
| 18 | Post defense | 6.5 |
| 19 | Offensive rebounding | 7.2 |
| 20 | Defensive rebounding | 8.1 |
| 21 | Burst / explosion | 9.3 |
| 22 | Lateral quickness | 8.4 |
| 23 | Strength | 9.2 |
| 24 | Shot selection | 8.8 |
| 25 | Effort / motor | 7.0 |
| 26 | Competitive character | 9.2 |

---

### Jamal Shead

| Field | Value |
|---|---|
| Archetype | Pure Point Guard |
| Position | PG |
| Status | validation |
| Notes | 2024 NBA Draft #61 — Toronto Raptors. Current level. Archetype note: AAG in college, PPG at NBA level — confirmed Session 54. |
| Target composite | 7.20–7.40 |
| Target midpoint | 7.30 |
| Raw composite | 7.13 |
| Gap | −0.17 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 6.00 |
| D2 Shooting | 6.05 |
| D3 Ball Skills | 7.06 |
| D4 Playmaking | 7.40 |
| D5 Defense | 7.75 |
| D6 Rebounding | 5.00 |
| D7 Athleticism | 6.90 |
| D8 IQ / Motor | 8.07 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 6.0 | medium |
| 2 | Contact finishing / foul draw | 6.0 | medium |
| 3 | Post offense | 2.5 | high |
| 4 | Catch-and-shoot 3PT | 6.5 | high |
| 5 | Off-dribble shooting | 5.0 | medium |
| 6 | Mid-range | 5.5 | low |
| 7 | Free throw | 7.5 | high |
| 8 | Handling / creation | 7.0 | medium |
| 9 | Touch / feel | 6.5 | low |
| 10 | Ball security | 7.5 | high |
| 11 | Court vision | 7.5 | high |
| 12 | Decision-making | 8.0 | high |
| 13 | Passing execution | 7.0 | medium |
| 14 | Off-ball movement | 6.5 | low |
| 15 | On-ball pressure | 8.0 | high |
| 16 | Help defense | 7.5 | medium |
| 17 | Rim protection | 2.5 | high |
| 18 | Post defense | 3.0 | high |
| 19 | Offensive rebounding | 3.5 | medium |
| 20 | Defensive rebounding | 5.0 | medium |
| 21 | Burst / explosion | 7.0 | medium |
| 22 | Lateral quickness | 7.5 | medium |
| 23 | Strength | 5.5 | medium |
| 24 | Shot selection | 7.5 | high |
| 25 | Effort / motor | 8.5 | high |
| 26 | Competitive character | 8.5 | high |

**Session 54 notes:** Gap of −0.17 is the smallest in the dataset at time of build. Archetype switch (AAG → PPG) contributed to gap discussion but was not the primary driver; sub-domain score level was. Session 53 reference composite was 6.52 under PPG; this build scores him higher due to more confident defensive sub-domain scoring. Needs stat verification on #5, #6, #9, #14.

---

### Mikal Bridges

| Field | Value |
|---|---|
| Archetype | 3-and-D Wing |
| Position | SF |
| Status | validation |
| Notes | Current level |
| Target composite | 7.90–8.10 |
| Target midpoint | 8.00 |
| Raw composite | 7.50 |
| Gap | −0.50 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 5.41 |
| D2 Shooting | 7.39 |
| D3 Ball Skills | 7.00 |
| D4 Playmaking | 7.13 |
| D5 Defense | 7.61 |
| D6 Rebounding | 4.83 |
| D7 Athleticism | 7.44 |
| D8 IQ / Motor | 8.50 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 6.8 | medium |
| 2 | Contact finishing / foul draw | 5.0 | high |
| 3 | Post offense | 2.5 | high |
| 4 | Catch-and-shoot 3PT | 8.5 | high |
| 5 | Off-dribble shooting | 6.0 | medium |
| 6 | Mid-range | 6.5 | medium |
| 7 | Free throw | 8.0 | high |
| 8 | Handling / creation | 6.5 | medium |
| 9 | Touch / feel | 7.0 | medium |
| 10 | Ball security | 7.5 | high |
| 11 | Court vision | 6.5 | medium |
| 12 | Decision-making | 7.5 | high |
| 13 | Passing execution | 6.5 | medium |
| 14 | Off-ball movement | 7.5 | high |
| 15 | On-ball pressure | 9.0 | high |
| 16 | Help defense | 8.0 | medium |
| 17 | Rim protection | 4.5 | high |
| 18 | Post defense | 6.5 | medium |
| 19 | Offensive rebounding | 3.5 | high |
| 20 | Defensive rebounding | 5.5 | medium |
| 21 | Burst / explosion | 7.0 | medium |
| 22 | Lateral quickness | 8.5 | high |
| 23 | Strength | 6.5 | medium |
| 24 | Shot selection | 8.5 | high |
| 25 | Effort / motor | 8.5 | high |
| 26 | Competitive character | 8.5 | high |

**Session 55 notes:** Gap −0.50. First wing in dataset. 3-and-D Wing archetype. Key negative balance: #2 contact finishing / foul draw at 5.0 (chronically low FTR well-documented). Rebounding domain suppressed (4.83) — expected for archetype. IQ/Motor domain highest in build (8.50).

---

### Kawhi Leonard

| Field | Value |
|---|---|
| Archetype | All-Around Wing |
| Position | SF |
| Status | validation |
| Notes | Current level (2023–24 Clippers — availability-adjusted) |
| Target composite | 8.80–8.90 |
| Target midpoint | 8.85 |
| Raw composite | 8.18 |
| Gap | −0.67 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 7.93 |
| D2 Shooting | 8.83 |
| D3 Ball Skills | 8.33 |
| D4 Playmaking | 7.06 |
| D5 Defense | 8.28 |
| D6 Rebounding | 5.83 |
| D7 Athleticism | 8.25 |
| D8 IQ / Motor | 9.00 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 8.5 | high |
| 2 | Contact finishing / foul draw | 8.0 | high |
| 3 | Post offense | 6.0 | medium |
| 4 | Catch-and-shoot 3PT | 8.5 | high |
| 5 | Off-dribble shooting | 9.0 | high |
| 6 | Mid-range | 9.0 | high |
| 7 | Free throw | 9.0 | high |
| 8 | Handling / creation | 8.0 | medium |
| 9 | Touch / feel | 8.5 | high |
| 10 | Ball security | 8.5 | high |
| 11 | Court vision | 7.0 | medium |
| 12 | Decision-making | 9.0 | high |
| 13 | Passing execution | 6.5 | medium |
| 14 | Off-ball movement | 6.0 | low |
| 15 | On-ball pressure | 9.5 | high |
| 16 | Help defense | 8.5 | high |
| 17 | Rim protection | 5.5 | medium |
| 18 | Post defense | 7.5 | medium |
| 19 | Offensive rebounding | 3.5 | high |
| 20 | Defensive rebounding | 7.0 | medium |
| 21 | Burst / explosion | 7.5 | medium |
| 22 | Lateral quickness | 8.5 | high |
| 23 | Strength | 9.0 | high |
| 24 | Shot selection | 9.5 | high |
| 25 | Effort / motor | 8.0 | medium |
| 26 | Competitive character | 9.5 | high |

**Session 55 notes:** Gap −0.67. Second wing in dataset. All-Around Wing archetype. Target set at availability-adjusted current level (8.85), not peak tier (9.00–9.29). #25 effort/motor deliberately scored below #26 — load management is a documented signal. #14 off-ball movement scored at midpoint (6.0) due to low confidence — primarily an on-ball player.

---

### Jaren Jackson Jr.

| Field | Value |
|---|---|
| Archetype | Switchable Big |
| Position | PF |
| Status | calibration |
| Notes | Current level — DPOY 2023–24 |
| Target composite | 8.11 |
| Target midpoint | 8.11 |
| Raw composite | 7.48 |
| Gap | −0.63 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 6.36 |
| D2 Shooting | 6.92 |
| D3 Ball Skills | 6.50 |
| D4 Playmaking | 6.63 |
| D5 Defense | 8.45 |
| D6 Rebounding | 6.00 |
| D7 Athleticism | 8.07 |
| D8 IQ / Motor | 8.50 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 7.5 | medium |
| 2 | Contact finishing / foul draw | 6.0 | medium |
| 3 | Post offense | 5.0 | medium |
| 4 | Catch-and-shoot 3PT | 7.5 | high |
| 5 | Off-dribble shooting | 5.0 | low |
| 6 | Mid-range | 6.5 | medium |
| 7 | Free throw | 7.5 | high |
| 8 | Handling / creation | 5.5 | medium |
| 9 | Touch / feel | 7.5 | medium |
| 10 | Ball security | 6.5 | medium |
| 11 | Court vision | 5.5 | medium |
| 12 | Decision-making | 7.0 | medium |
| 13 | Passing execution | 5.5 | low |
| 14 | Off-ball movement | 7.0 | medium |
| 15 | On-ball pressure | 8.0 | high |
| 16 | Help defense | 9.0 | high |
| 17 | Rim protection | 9.5 | high |
| 18 | Post defense | 7.5 | medium |
| 19 | Offensive rebounding | 5.5 | medium |
| 20 | Defensive rebounding | 6.5 | medium |
| 21 | Burst / explosion | 8.5 | medium |
| 22 | Lateral quickness | 8.5 | high |
| 23 | Strength | 7.5 | medium |
| 24 | Shot selection | 8.5 | high |
| 25 | Effort / motor | 8.5 | high |
| 26 | Competitive character | 8.5 | high |

**Session 55 notes:** Gap −0.63. First big in dataset. Switchable Big archetype. #20 defensive rebounding at 6.5 confirmed — documented relative weakness for his size; archetype down-weights this appropriately. #17 rim protection at 9.5 is highest single sub-domain score in a big so far. Sub-domain fine-tuning deferred to later session.

---

### Bam Adebayo

| Field | Value |
|---|---|
| Archetype | All-Around Big |
| Position | C |
| Status | calibration |
| Notes | Current level |
| Target composite | 8.40 |
| Target midpoint | 8.40 |
| Raw composite | 7.75 |
| Gap | −0.65 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 7.56 |
| D2 Shooting | 6.33 |
| D3 Ball Skills | 8.17 |
| D4 Playmaking | 8.00 |
| D5 Defense | 8.00 |
| D6 Rebounding | 6.75 |
| D7 Athleticism | 8.58 |
| D8 IQ / Motor | 8.50 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 8.5 | high |
| 2 | Contact finishing / foul draw | 7.0 | high |
| 3 | Post offense | 7.0 | medium |
| 4 | Catch-and-shoot 3PT | 4.5 | high |
| 5 | Off-dribble shooting | 5.0 | medium |
| 6 | Mid-range | 7.0 | medium |
| 7 | Free throw | 7.5 | high |
| 8 | Handling / creation | 7.5 | high |
| 9 | Touch / feel | 8.5 | high |
| 10 | Ball security | 7.5 | high |
| 11 | Court vision | 8.5 | high |
| 12 | Decision-making | 8.0 | high |
| 13 | Passing execution | 8.0 | high |
| 14 | Off-ball movement | 7.5 | medium |
| 15 | On-ball pressure | 8.0 | high |
| 16 | Help defense | 9.0 | high |
| 17 | Rim protection | 7.0 | high |
| 18 | Post defense | 8.0 | medium |
| 19 | Offensive rebounding | 6.0 | high |
| 20 | Defensive rebounding | 7.5 | high |
| 21 | Burst / explosion | 8.5 | high |
| 22 | Lateral quickness | 9.0 | high |
| 23 | Strength | 8.5 | high |
| 24 | Shot selection | 8.0 | high |
| 25 | Effort / motor | 8.5 | high |
| 26 | Competitive character | 9.0 | high |

**Session 56 notes:** Gap −0.65. First All-Around Big in dataset. First C. #4 CAS 3PT corrected to 4.5 post-research — 2025-26 shows 31.5% on real volume; developing but at negative balance threshold; originally scored as structural zero. #26 Competitive character raised to 9.0 — 83-point game in 2025-26 (second-highest individual scoring performance in NBA history). Weight confirmed 255 lbs. FT% confirmed 75.9% career / 77.6% 2025-26. D7 Athleticism (8.58) and D3 Ball Skills (8.17) highest domains — anomalous for C archetype, reflects elite physical profile. D2 Shooting (6.33) drag domain despite #6/#7 being functional — #4 still suppresses.

---

### Rudy Gobert

| Field | Value |
|---|---|
| Archetype | Rim Protector |
| Position | C |
| Status | calibration |
| Notes | Current level |
| Target composite | 8.03 |
| Target midpoint | 8.03 |
| Raw composite | 7.67 |
| Gap | −0.36 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 6.19 |
| D2 Shooting | 2.67 |
| D3 Ball Skills | 6.17 |
| D4 Playmaking | 5.83 |
| D5 Defense | 8.75 |
| D6 Rebounding | 8.00 |
| D7 Athleticism | 6.92 |
| D8 IQ / Motor | 8.14 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 7.5 | high |
| 2 | Contact finishing / foul draw | 6.0 | high |
| 3 | Post offense | 4.5 | high |
| 4 | Catch-and-shoot 3PT | 1.0 | high |
| 5 | Off-dribble shooting | 1.0 | high |
| 6 | Mid-range | 2.0 | high |
| 7 | Free throw | 5.0 | high |
| 8 | Handling / creation | 2.0 | high |
| 9 | Touch / feel | 6.0 | medium |
| 10 | Ball security | 6.5 | high |
| 11 | Court vision | 4.0 | high |
| 12 | Decision-making | 6.0 | medium |
| 13 | Passing execution | 3.5 | high |
| 14 | Off-ball movement | 7.5 | high |
| 15 | On-ball pressure | 5.0 | high |
| 16 | Help defense | 9.5 | high |
| 17 | Rim protection | 9.5 | high |
| 18 | Post defense | 8.5 | high |
| 19 | Offensive rebounding | 6.5 | high |
| 20 | Defensive rebounding | 9.5 | high |
| 21 | Burst / explosion | 7.5 | high |
| 22 | Lateral quickness | 4.5 | high |
| 23 | Strength | 8.0 | high |
| 24 | Shot selection | 7.0 | high |
| 25 | Effort / motor | 9.0 | high |
| 26 | Competitive character | 8.0 | high |

**Session 56 notes:** Gap −0.36. First Rim Protector in dataset. Second C. Second-smallest gap after Shead — N=0 zone hypothesis supported: 5 structural zeros in offensive sub-domains eliminate surface area for formula compression. #7 FT corrected to 5.0 post-research — career 63–64%, 2025-26 regressing to ~52.5%. Weight corrected to 258 lbs (was stated as 245 lbs during build). Career BPG 2.0 confirmed. D5 Defense (8.75) and D6 Rebounding (8.00) dominate — archetype functioning as designed. #22 Lateral quickness (4.5) the profile's defining weakness.

---

### OG Anunoby

| Field | Value |
|---|---|
| Archetype | 3-and-D Wing |
| Position | SF |
| Status | calibration |
| Notes | Current level |
| Target composite | 8.05 |
| Target midpoint | 8.05 |
| Raw composite | 7.57 |
| Gap | −0.48 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 5.57 |
| D2 Shooting | 6.89 |
| D3 Ball Skills | 6.33 |
| D4 Playmaking | 7.13 |
| D5 Defense | 8.00 |
| D6 Rebounding | 5.33 |
| D7 Athleticism | 8.06 |
| D8 IQ / Motor | 8.33 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 6.5 | medium |
| 2 | Contact finishing / foul draw | 5.5 | high |
| 3 | Post offense | 3.0 | medium |
| 4 | Catch-and-shoot 3PT | 8.0 | high |
| 5 | Off-dribble shooting | 5.5 | medium |
| 6 | Mid-range | 6.0 | medium |
| 7 | Free throw | 7.5 | high |
| 8 | Handling / creation | 5.5 | medium |
| 9 | Touch / feel | 6.5 | medium |
| 10 | Ball security | 7.0 | high |
| 11 | Court vision | 5.5 | medium |
| 12 | Decision-making | 7.5 | high |
| 13 | Passing execution | 5.5 | medium |
| 14 | Off-ball movement | 8.5 | high |
| 15 | On-ball pressure | 9.0 | high |
| 16 | Help defense | 8.5 | high |
| 17 | Rim protection | 5.5 | high |
| 18 | Post defense | 7.0 | medium |
| 19 | Offensive rebounding | 3.0 | high |
| 20 | Defensive rebounding | 6.5 | high |
| 21 | Burst / explosion | 7.5 | medium |
| 22 | Lateral quickness | 9.0 | high |
| 23 | Strength | 7.5 | high |
| 24 | Shot selection | 8.0 | high |
| 25 | Effort / motor | 8.5 | high |
| 26 | Competitive character | 8.5 | high |

**Session 56 notes:** Gap −0.48. Second 3-and-D Wing in dataset. Gap nearly identical to Bridges (−0.50) — same archetype, same two N=0 zones (#3/#19), formula behaving consistently across both. Wingspan 7'2" confirmed. Career FG3% 37.6%, 2025-26 39.6%. D7 Athleticism (8.06) and D8 IQ/Motor (8.33) highest domains — physical tools plus defensive intelligence is the value profile. D6 Rebounding (5.33) drag domain — N=0 on #19 by archetype design.

---

### Draymond Green

| Field | Value |
|---|---|
| Archetype | Defensive-Engine Playmaker |
| Position | PF |
| Status | calibration |
| Notes | Current level (2025-26) |
| Target composite | 8.00 |
| Target midpoint | 8.00 |
| Raw composite | 7.64 |
| Gap | −0.36 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 5.64 |
| D2 Shooting | 3.42 |
| D3 Ball Skills | 7.33 |
| D4 Playmaking | 6.88 |
| D5 Defense | 8.10 |
| D6 Rebounding | 5.75 |
| D7 Athleticism | 7.00 |
| D8 IQ / Motor | 8.43 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 5.5 | high |
| 2 | Contact finishing / foul draw | 4.0 | high |
| 3 | Post offense | 7.5 | high |
| 4 | Catch-and-shoot 3PT | 3.0 | high |
| 5 | Off-dribble shooting | 2.0 | high |
| 6 | Mid-range | 4.0 | medium |
| 7 | Free throw | 5.5 | high |
| 8 | Handling / creation | 7.0 | high |
| 9 | Touch / feel | 7.5 | high |
| 10 | Ball security | 7.5 | high |
| 11 | Court vision | 9.0 | high |
| 12 | Decision-making | 8.5 | high |
| 13 | Passing execution | 9.0 | high |
| 14 | Off-ball movement | 5.0 | medium |
| 15 | On-ball pressure | 8.5 | high |
| 16 | Help defense | 9.5 | high |
| 17 | Rim protection | 6.5 | high |
| 18 | Post defense | 7.5 | high |
| 19 | Offensive rebounding | 4.5 | high |
| 20 | Defensive rebounding | 7.0 | high |
| 21 | Burst / explosion | 5.5 | high |
| 22 | Lateral quickness | 7.0 | medium |
| 23 | Strength | 8.0 | high |
| 24 | Shot selection | 8.0 | high |
| 25 | Effort / motor | 9.0 | high |
| 26 | Competitive character | 8.0 | high |

**Session 57 notes:** Gap −0.36. Ties Gobert for second-smallest gap in dataset at time of build. Defensive-Engine Playmaker archetype. 3 archetype N=0 zones (#4, #5, #6). D2 Shooting (3.42) second-lowest domain score in dataset after Gobert (2.67) — near-zero shooting across all three sub-domains. D8 IQ/Motor (8.43) and D5 Defense (8.10) dominant domains. #26 Competitive character anchored to 8.0 — documented pattern of violent conduct (chokehold on Gobert 2023, struck Nurkić 2023), 21 career ejections (2nd all-time); this is a genuine negative balance signal, not edge-of-competitiveness. #17 Rim protection scored at 6.5 despite not being a primary rim protector — 1.0 BPG is a real signal. Gap ties Gobert from a completely different archetype and position — two data points at −0.36 with concentrated profiles and structural zeros strengthens N=0 hypothesis. Physical: 6'6" / 230 lbs / wingspan 7'1". Wingspan confirmed.

---

### Keon Ellis

| Field | Value |
|---|---|
| Archetype | 3-and-D Guard |
| Position | SG |
| Status | calibration |
| Notes | Current level (2024-25, Sacramento Kings) |
| Target composite | 7.25 |
| Target midpoint | 7.25 |
| Raw composite | 6.91 |
| Gap | −0.34 |

**Correction note:** In-session composite reported as 6.95/−0.30 using preliminary sub-domain estimates. Final scored values (#2=4.5, #5=4.5, #6=4.5, #23=4.5) produce 6.91/−0.34. Corrected values recorded here.

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 5.00 |
| D2 Shooting | 5.70 |
| D3 Ball Skills | 5.93 |
| D4 Playmaking | 6.43 |
| D5 Defense | 8.25 |
| D6 Rebounding | 4.00 |
| D7 Athleticism | 7.29 |
| D8 IQ / Motor | 7.64 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 6.5 | medium |
| 2 | Contact finishing / foul draw | 4.5 | medium |
| 3 | Post offense | 2.0 | high |
| 4 | Catch-and-shoot 3PT | 7.5 | high |
| 5 | Off-dribble shooting | 4.5 | medium |
| 6 | Mid-range | 4.5 | low |
| 7 | Free throw | 6.0 | medium |
| 8 | Handling / creation | 5.5 | medium |
| 9 | Touch / feel | 6.0 | medium |
| 10 | Ball security | 6.5 | medium |
| 11 | Court vision | 5.5 | medium |
| 12 | Decision-making | 6.5 | medium |
| 13 | Passing execution | 5.5 | medium |
| 14 | Off-ball movement | 7.0 | medium |
| 15 | On-ball pressure | 8.5 | high |
| 16 | Help defense | 8.0 | high |
| 17 | Rim protection | 5.5 | medium |
| 18 | Post defense | 4.5 | low |
| 19 | Offensive rebounding | 2.5 | high |
| 20 | Defensive rebounding | 5.5 | medium |
| 21 | Burst / explosion | 7.0 | medium |
| 22 | Lateral quickness | 8.5 | high |
| 23 | Strength | 4.5 | high |
| 24 | Shot selection | 7.5 | high |
| 25 | Effort / motor | 8.0 | high |
| 26 | Competitive character | 7.5 | medium |

**Session 57 notes:** Gap −0.34. 4 archetype N=0 zones (#3, #17, #18, #19). First SG in dataset. 3-and-D Guard archetype — Derrick White profile match confirmed. D5 Defense (8.25) dominant domain; D6 Rebounding (4.00) lowest. #17 scored at 5.5 despite archetype N=0 — 0.8 BPG as a guard is a real signal, acknowledged but weight-suppressed by archetype design. #23 Strength (4.5) physical limitation — 175 lbs; hard floor for interior contests. Wingspan unconfirmed — flag for any Layer 2 build. Traded to Cleveland Cavaliers February 2026. Physical: 6'4" / 175 lbs. Key stats: 8.2 PPG, 1.5 SPG, 0.8 BPG, 41.7% 3PT (2023-24), 48.9% FG (2024-25), 24.4 min, 80 games.

---

### Donovan Mitchell

| Field | Value |
|---|---|
| Archetype | Offensive Engine |
| Position | SG |
| Status | calibration |
| Notes | Current level (2025-26) |
| Target composite | 8.65 |
| Target midpoint | 8.65 |
| Raw composite | 8.01 |
| Gap | −0.64 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 7.86 |
| D2 Shooting | 8.20 |
| D3 Ball Skills | 8.14 |
| D4 Playmaking | 7.21 |
| D5 Defense | 7.00 |
| D6 Rebounding | 4.50 |
| D7 Athleticism | 7.86 |
| D8 IQ / Motor | 8.50 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 8.5 | high |
| 2 | Contact finishing / foul draw | 9.0 | high |
| 3 | Post offense | 2.5 | high |
| 4 | Catch-and-shoot 3PT | 7.0 | high |
| 5 | Off-dribble shooting | 9.0 | high |
| 6 | Mid-range | 8.5 | high |
| 7 | Free throw | 8.5 | high |
| 8 | Handling / creation | 9.0 | high |
| 9 | Touch / feel | 7.5 | medium |
| 10 | Ball security | 7.5 | high |
| 11 | Court vision | 7.5 | high |
| 12 | Decision-making | 8.0 | high |
| 13 | Passing execution | 7.5 | medium |
| 14 | Off-ball movement | 6.5 | medium |
| 15 | On-ball pressure | 7.5 | high |
| 16 | Help defense | 6.5 | medium |
| 17 | Rim protection | 2.0 | high |
| 18 | Post defense | 3.0 | high |
| 19 | Offensive rebounding | 2.5 | high |
| 20 | Defensive rebounding | 6.5 | high |
| 21 | Burst / explosion | 8.5 | high |
| 22 | Lateral quickness | 7.5 | high |
| 23 | Strength | 7.0 | high |
| 24 | Shot selection | 8.5 | high |
| 25 | Effort / motor | 8.0 | high |
| 26 | Competitive character | 9.0 | high |

**Session 57 notes:** Gap −0.64. First Offensive Engine SG in dataset. 4 archetype N=0 zones (#3, #17, #18, #19). D8 IQ/Motor (8.50) highest domain; D6 Rebounding (4.50) lowest. #26 Competitive character 9.0 — 71-point game Jan 2023, 50 points in potential elimination playoff game, 89 combined points G6/G7 same series; multi-source high-stakes evidence. #20 Defensive rebounding 6.5 — career-high 5.1 RPG in 2024-25, exceptional for 6'2" guard. Gap comparison to SGA (−0.40): difference driven primarily by lower court vision (#11: 7.5 vs 8.5) and decision-making (#12: 8.0 vs 9.0) — both High weight in Offensive Engine archetype. Key stats: 27.8 PPG, 5.7 APG, 4.5 RPG, 48.1% FG, 61.4% TS (2025-26). 7x All-Star. Physical: 6'2" / 215 lbs. Wingspan unconfirmed.

---

### Lindy Waters III

| Field | Value |
|---|---|
| Archetype | 3-and-D Guard |
| Position | SG |
| Status | calibration |
| Notes | Current level (2025-26, San Antonio Spurs) |
| Target composite | 6.75 |
| Target midpoint | 6.75 |
| Raw composite | 6.20 |
| Gap | −0.55 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 3.93 |
| D2 Shooting | 5.05 |
| D3 Ball Skills | 5.14 |
| D4 Playmaking | 6.29 |
| D5 Defense | 6.25 |
| D6 Rebounding | 3.75 |
| D7 Athleticism | 6.21 |
| D8 IQ / Motor | 7.50 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 5.0 | medium |
| 2 | Contact finishing / foul draw | 3.5 | high |
| 3 | Post offense | 2.0 | high |
| 4 | Catch-and-shoot 3PT | 6.5 | medium |
| 5 | Off-dribble shooting | 3.0 | high |
| 6 | Mid-range | 4.0 | low |
| 7 | Free throw | 7.0 | medium |
| 8 | Handling / creation | 4.0 | high |
| 9 | Touch / feel | 5.5 | medium |
| 10 | Ball security | 6.5 | high |
| 11 | Court vision | 5.0 | high |
| 12 | Decision-making | 6.5 | medium |
| 13 | Passing execution | 5.0 | medium |
| 14 | Off-ball movement | 7.0 | medium |
| 15 | On-ball pressure | 6.5 | medium |
| 16 | Help defense | 6.0 | medium |
| 17 | Rim protection | 2.0 | high |
| 18 | Post defense | 2.5 | high |
| 19 | Offensive rebounding | 2.5 | high |
| 20 | Defensive rebounding | 5.0 | medium |
| 21 | Burst / explosion | 6.0 | medium |
| 22 | Lateral quickness | 6.5 | medium |
| 23 | Strength | 6.0 | medium |
| 24 | Shot selection | 7.5 | high |
| 25 | Effort / motor | 7.5 | high |
| 26 | Competitive character | 7.5 | high |

**Session 58 notes:** Gap −0.55. First entry in 6.50–7.19 fringe rotation tier. 3-and-D Guard archetype. 4 archetype N=0 zones (#3, #17, #18, #19). D1 Finishing (3.93) and D6 Rebounding (3.75) drag domains — structural for archetype. D8 IQ/Motor (7.50) dominant domain. #4 CAS 3PT at 6.5 medium confidence — career 36–38% anchor holds but 2025-26 regression to 34.2% on minimal attempts noted. #7 FT at 7.0 uses career 81.5% through 2024 as anchor over small-sample 66.7%. Undrafted-to-multi-year contract trajectory confirms #25/#26. Same archetype as Ellis; lower profile elevation drives larger gap (−0.55 vs −0.34) — consistent with profile elevation pattern. Physical: 6'5" / 210 lbs. Wingspan unconfirmed.

---

### Brandon Ingram

| Field | Value |
|---|---|
| Archetype | Dribble Pass Shoot Wing |
| Position | SF |
| Status | calibration |
| Notes | Current level (2025-26, Toronto Raptors) |
| Target composite | 8.32 |
| Target midpoint | 8.32 |
| Raw composite | 7.19 |
| Gap | −1.13 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 7.64 |
| D2 Shooting | 8.00 |
| D3 Ball Skills | 7.67 |
| D4 Playmaking | 6.56 |
| D5 Defense | 4.94 |
| D6 Rebounding | 5.67 |
| D7 Athleticism | 6.50 |
| D8 IQ / Motor | 7.17 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 8.5 | high |
| 2 | Contact finishing / foul draw | 7.5 | high |
| 3 | Post offense | 5.5 | medium |
| 4 | Catch-and-shoot 3PT | 7.0 | medium |
| 5 | Off-dribble shooting | 8.5 | high |
| 6 | Mid-range | 9.0 | high |
| 7 | Free throw | 8.0 | high |
| 8 | Handling / creation | 7.5 | high |
| 9 | Touch / feel | 8.5 | high |
| 10 | Ball security | 7.0 | medium |
| 11 | Court vision | 6.5 | medium |
| 12 | Decision-making | 7.5 | high |
| 13 | Passing execution | 6.5 | medium |
| 14 | Off-ball movement | 6.0 | medium |
| 15 | On-ball pressure | 6.0 | medium |
| 16 | Help defense | 6.0 | medium |
| 17 | Rim protection | 2.5 | high |
| 18 | Post defense | 3.0 | high |
| 19 | Offensive rebounding | 4.0 | high |
| 20 | Defensive rebounding | 6.5 | high |
| 21 | Burst / explosion | 7.5 | high |
| 22 | Lateral quickness | 6.5 | medium |
| 23 | Strength | 5.0 | high |
| 24 | Shot selection | 8.0 | high |
| 25 | Effort / motor | 6.5 | medium |
| 26 | Competitive character | 7.0 | medium |

**Session 58 notes:** Gap −1.13. Second-largest gap in dataset behind Lillard (−1.18) at time of build. DPS Wing archetype — confirmed fit in ARCHETYPE-WEIGHTS_v3.md. Only 2 structural N=0 zones (#17, #18) — fewest of any non-KAT player. D2 Shooting (8.00) and D3 Ball Skills (7.67) dominant; D5 Defense (4.94) primary drag. Large gap driven by pure breadth compression — no sub-domain below 4.0 except structural zeros, but defensive drag pulls hard against offensive ceiling. Distinct from Lillard bimodal: no near-zero non-N=0 scores. Injury history: 70+ games once in 9 seasons. $25K fine Nov 2025 (water bottle incident). Physical: 6'8" / ~215 lbs. Wingspan unconfirmed.

---

### Karl-Anthony Towns

| Field | Value |
|---|---|
| Archetype | Stretch Big |
| Position | C |
| Status | calibration |
| Notes | Current level (2025-26, New York Knicks) |
| Target composite | 8.52 |
| Target midpoint | 8.52 |
| Raw composite | 7.11 |
| Gap | −1.41 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 6.75 |
| D2 Shooting | 8.00 |
| D3 Ball Skills | 7.83 |
| D4 Playmaking | 7.17 |
| D5 Defense | 5.40 |
| D6 Rebounding | 7.00 |
| D7 Athleticism | 6.58 |
| D8 IQ / Motor | 7.14 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 8.0 | high |
| 2 | Contact finishing / foul draw | 7.5 | high |
| 3 | Post offense | 5.0 | medium |
| 4 | Catch-and-shoot 3PT | 8.5 | high |
| 5 | Off-dribble shooting | 5.5 | medium |
| 6 | Mid-range | 7.0 | medium |
| 7 | Free throw | 8.5 | high |
| 8 | Handling / creation | 5.5 | medium |
| 9 | Touch / feel | 8.5 | high |
| 10 | Ball security | 6.5 | medium |
| 11 | Court vision | 6.5 | medium |
| 12 | Decision-making | 7.5 | high |
| 13 | Passing execution | 6.5 | medium |
| 14 | Off-ball movement | 7.5 | high |
| 15 | On-ball pressure | 4.5 | high |
| 16 | Help defense | 6.0 | medium |
| 17 | Rim protection | 5.0 | high |
| 18 | Post defense | 5.5 | medium |
| 19 | Offensive rebounding | 5.5 | medium |
| 20 | Defensive rebounding | 8.5 | high |
| 21 | Burst / explosion | 7.0 | high |
| 22 | Lateral quickness | 6.0 | medium |
| 23 | Strength | 6.5 | medium |
| 24 | Shot selection | 8.5 | high |
| 25 | Effort / motor | 6.0 | medium |
| 26 | Competitive character | 7.5 | high |

**Session 58 notes:** Gap −1.41. Largest gap in dataset — 0.23 points wider than previous maximum (Lillard −1.18). Stretch Big archetype — confirmed fit in ARCHETYPE-WEIGHTS_v3.md. Only 1 structural N=0 zone (#3 post offense) — fewest of any player in dataset. Maximum breadth compression confirmed. D2 Shooting (8.00) and D3 Ball Skills (7.83) dominant; D5 Defense (5.40) primary drag. League-leading 45+ double-doubles; #20 defensive rebounding 8.5. #17 Rim protection non-negotiable flag: 0.5 BPG this season sits at C threshold of 5.0; cap live at age 29, no development pathway — does not affect composite at this tier. Physical: 6'11" / ~245 lbs. Wingspan unconfirmed.

---

### Buddy Hield

| Field | Value |
|---|---|
| Archetype | Guard Shooting Specialist |
| Position | SG |
| Status | calibration |
| Notes | Current level (2025-26, Warriors then Atlanta Hawks) |
| Target composite | 7.34 |
| Target midpoint | 7.34 |
| Raw composite | 7.18 |
| Gap | −0.16 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 3.93 |
| D2 Shooting | 5.90 |
| D3 Ball Skills | 5.50 |
| D4 Playmaking | 7.00 |
| D5 Defense | 5.25 |
| D6 Rebounding | 3.50 |
| D7 Athleticism | 5.93 |
| D8 IQ / Motor | 7.64 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 5.0 | medium |
| 2 | Contact finishing / foul draw | 3.5 | high |
| 3 | Post offense | 2.0 | high |
| 4 | Catch-and-shoot 3PT | 9.0 | high |
| 5 | Off-dribble shooting | 3.0 | high |
| 6 | Mid-range | 3.5 | high |
| 7 | Free throw | 8.0 | high |
| 8 | Handling / creation | 3.5 | high |
| 9 | Touch / feel | 7.5 | medium |
| 10 | Ball security | 6.5 | high |
| 11 | Court vision | 5.0 | high |
| 12 | Decision-making | 7.0 | high |
| 13 | Passing execution | 4.5 | high |
| 14 | Off-ball movement | 8.5 | high |
| 15 | On-ball pressure | 5.0 | medium |
| 16 | Help defense | 5.5 | medium |
| 17 | Rim protection | 2.0 | high |
| 18 | Post defense | 2.5 | high |
| 19 | Offensive rebounding | 2.5 | high |
| 20 | Defensive rebounding | 4.5 | high |
| 21 | Burst / explosion | 6.5 | medium |
| 22 | Lateral quickness | 5.5 | medium |
| 23 | Strength | 5.5 | high |
| 24 | Shot selection | 8.5 | high |
| 25 | Effort / motor | 7.0 | high |
| 26 | Competitive character | 7.0 | high |

**Session 58 notes:** Gap −0.16. Smallest gap in dataset — surpasses Shead (−0.17). Guard Shooting Specialist archetype — confirmed fit in ARCHETYPE-WEIGHTS_v3.md. 11 structural N=0 zones (#3, #5, #6, #8, #11, #13, #17, #18, #19, #20, #23) — most of any player in dataset. Only 15 sub-domains contribute; total weight pool = 25 (smallest in dataset). Formula pulls almost entirely toward elite skills: #4 CAS 3PT (9.0), #14 off-ball movement (8.5), #24 shot selection (8.5). Career 39.5% 3PT; second-fastest to 1,500 career 3s behind Curry. Current-season decline to 34.2% noted — career level is the skill anchor. Wingspan confirmed 6'9". Physical: 6'4" / ~214 lbs.

---

### Devin Booker

| Field | Value |
|---|---|
| Archetype | All-Around Guard |
| Position | SG |
| Status | calibration |
| Notes | Current level (2025-26, Phoenix Suns) |
| Target composite | 8.81 |
| Target midpoint | 8.81 |
| Raw composite | 7.48 |
| Gap | −1.33 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 7.00 |
| D2 Shooting | 8.35 |
| D3 Ball Skills | 8.21 |
| D4 Playmaking | 7.00 |
| D5 Defense | 6.00 |
| D6 Rebounding | 3.25 |
| D7 Athleticism | 6.71 |
| D8 IQ / Motor | 8.36 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 7.5 | high |
| 2 | Contact finishing / foul draw | 8.0 | high |
| 3 | Post offense | 2.5 | high |
| 4 | Catch-and-shoot 3PT | 7.0 | medium |
| 5 | Off-dribble shooting | 8.5 | high |
| 6 | Mid-range | 9.0 | high |
| 7 | Free throw | 9.5 | high |
| 8 | Handling / creation | 8.5 | high |
| 9 | Touch / feel | 9.0 | high |
| 10 | Ball security | 7.0 | high |
| 11 | Court vision | 7.5 | high |
| 12 | Decision-making | 7.5 | high |
| 13 | Passing execution | 7.0 | medium |
| 14 | Off-ball movement | 6.5 | medium |
| 15 | On-ball pressure | 6.0 | medium |
| 16 | Help defense | 6.0 | medium |
| 17 | Rim protection | 1.5 | high |
| 18 | Post defense | 2.0 | high |
| 19 | Offensive rebounding | 2.0 | high |
| 20 | Defensive rebounding | 4.5 | medium |
| 21 | Burst / explosion | 7.5 | high |
| 22 | Lateral quickness | 6.5 | high |
| 23 | Strength | 5.0 | high |
| 24 | Shot selection | 8.5 | high |
| 25 | Effort / motor | 7.5 | high |
| 26 | Competitive character | 9.0 | high |

**Session 59 notes:** Gap −1.33. Third-largest gap in dataset behind KAT (−1.41) and Ingram (−1.13). All-Around Guard archetype — first AAG build, completes guard archetype coverage. 4 structural N=0 zones (#3, #17, #18, #19). Large gap despite 4 zeros explained by H-weight defense drag: #15 On-ball pressure and #16 Help defense are both H-weight (3) in AAG but score 6.0/6.0 — D-RTG 117.3 in 2023-24 confirms below-average defensive impact, wingspan 6'8" is the physical ceiling. Not bimodal — no near-zero non-N=0 sub-domains; gap driven by high target tier + defense drag, structurally similar to Ingram. #4 CAS 3PT at 7.0 medium confidence — career 35.4% used as anchor over consecutive dips to 33.2% (2024-25) and 30.7% (2025-26); if permanent decline confirmed, #4 drops to 6.0–6.5. Offensive profile elite: #6 mid-range 9.0, #7 FT 9.5, #9 touch 9.0. Physical: 6'5" / 206 lbs. Wingspan 6'8" confirmed.

---

### Kevin Durant

| Field | Value |
|---|---|
| Archetype | All-Around Wing |
| Position | SF |
| Status | calibration |
| Notes | Career median |
| Target composite | 9.38 |
| Target midpoint | 9.38 |
| Raw composite | 8.13 |
| Gap | −1.25 |

**Domain scores (position-weighted):**

| Domain | Score |
|---|---|
| D1 Finishing | 8.50 |
| D2 Shooting | 9.22 |
| D3 Ball Skills | 8.33 |
| D4 Playmaking | 7.94 |
| D5 Defense | 7.11 |
| D6 Rebounding | 7.00 |
| D7 Athleticism | 7.81 |
| D8 IQ / Motor | 8.50 |

**Sub-domain scores:**

| # | Sub-domain | Score | Confidence |
|---|---|---|---|
| 1 | At-basket finishing | 9.0 | high |
| 2 | Contact finishing / foul draw | 8.5 | high |
| 3 | Post offense | 7.0 | high |
| 4 | Catch-and-shoot 3PT | 9.0 | high |
| 5 | Off-dribble shooting | 9.5 | high |
| 6 | Mid-range | 9.5 | high |
| 7 | Free throw | 9.0 | high |
| 8 | Handling / creation | 8.0 | high |
| 9 | Touch / feel | 9.5 | high |
| 10 | Ball security | 7.5 | high |
| 11 | Court vision | 7.5 | high |
| 12 | Decision-making | 8.5 | high |
| 13 | Passing execution | 7.5 | high |
| 14 | Off-ball movement | 8.0 | high |
| 15 | On-ball pressure | 7.5 | high |
| 16 | Help defense | 7.5 | high |
| 17 | Rim protection | 6.0 | high |
| 18 | Post defense | 6.5 | high |
| 19 | Offensive rebounding | 5.0 | high |
| 20 | Defensive rebounding | 8.0 | high |
| 21 | Burst / explosion | 8.5 | high |
| 22 | Lateral quickness | 8.0 | high |
| 23 | Strength | 6.5 | medium |
| 24 | Shot selection | 9.5 | high |
| 25 | Effort / motor | 7.5 | medium |
| 26 | Competitive character | 8.5 | medium |

**Session 59 notes:** Gap −1.25. 0-zero player — All-Around Wing has no structural N=0 zones; all 26 sub-domains contribute; total weight pool = 59 (largest in dataset). Career median build. Critical finding: gap of −1.25 does NOT match the 0-zero cluster (Kawhi −0.67, JJJ −0.63, Bam −0.65) — nearly double despite same zero count. Prior 0-zero builds all had targets 8.11–8.85; Durant sits at 9.38. Flat correction assumption broken — correction factor scales with target tier, not zero count alone. D2 Shooting (9.22) highest single domain score in dataset. #5 off-dribble (9.5) and #6 mid-range (9.5) reflect historically elite scoring profile. #26 competitive character 8.5 medium — negative balance: Warriors decision and Brooklyn drama are documented choices of comfort over competition. #25 effort/motor 7.5 medium — documented passivity on defense in comfortable games. #23 strength 6.5 medium — lean frame historically documented limitation. Physical: 6'10" / ~240 lbs. Wingspan 7'4" confirmed. 15x All-Star, 9x All-NBA, 1 MVP, 2 Finals MVPs.

---

## SUMMARY TABLE — UPDATED (Session 59)

| Player | Archetype | Target | Raw | Gap | Status |
|---|---|---|---|---|---|
| Steph Curry | Offensive Engine | 9.00–9.10 | 8.28 | −0.77 | calibration |
| SGA | Offensive Engine | 9.10–9.20 | 8.75 | −0.40 | calibration |
| Damian Lillard | Offensive Engine | 8.75–8.85 | 7.62 | −1.18 | calibration |
| Luka Doncic | Jumbo Playmaker | 8.75–8.85 | 7.94 | −0.86 | calibration |
| LeBron James | Jumbo Playmaker | 9.75–9.80 | 8.69 | −1.09 | calibration |
| Jamal Shead | Pure Point Guard | 7.20–7.40 | 7.13 | −0.17 | validation |
| Mikal Bridges | 3-and-D Wing | 7.90–8.10 | 7.50 | −0.50 | validation |
| Kawhi Leonard | All-Around Wing | 8.80–8.90 | 8.18 | −0.67 | validation |
| Jaren Jackson Jr. | Switchable Big | 8.11 | 7.48 | −0.63 | calibration |
| Bam Adebayo | All-Around Big | 8.40 | 7.75 | −0.65 | calibration |
| Rudy Gobert | Rim Protector | 8.03 | 7.67 | −0.36 | calibration |
| OG Anunoby | 3-and-D Wing | 8.05 | 7.57 | −0.48 | calibration |
| Draymond Green | Defensive-Engine Playmaker | 8.00 | 7.64 | −0.36 | calibration |
| Keon Ellis | 3-and-D Guard | 7.25 | 6.91 | −0.34 | calibration |
| Donovan Mitchell | Offensive Engine | 8.65 | 8.01 | −0.64 | calibration |
| Lindy Waters III | 3-and-D Guard | 6.75 | 6.20 | −0.55 | calibration |
| Brandon Ingram | DPS Wing | 8.32 | 7.19 | −1.13 | calibration |
| Karl-Anthony Towns | Stretch Big | 8.52 | 7.11 | −1.41 | calibration |
| Buddy Hield | Guard Shooting Specialist | 7.34 | 7.18 | −0.16 | calibration |
| Devin Booker | All-Around Guard | 8.81 | 7.48 | −1.33 | calibration |
| Kevin Durant | All-Around Wing | 9.38 | 8.13 | −1.25 | calibration |

Gap range: −0.16 to −1.41. All gaps negative. 21 players across 5 positions and 15 archetypes.
Session 59 additions: Devin Booker (All-Around Guard, SG), Kevin Durant (All-Around Wing, SF).

---

*Session 59 pattern check: Flat correction assumption broken — Durant (0 zeros, −1.25) vs 0-zero cluster Kawhi/JJJ/Bam (−0.63 to −0.67): same zero count, gap nearly double. Prior 0-zero builds all had targets 8.11–8.85; Durant at 9.38 demonstrates correction factor scales with target tier, not zero count alone. Booker (4 zeros, −1.33) third-largest gap in dataset: H-weight defense sub-domains (#15/#16 both scoring 6.0) in AAG archetype are primary driver — confirms that archetype weight placement on drag domains amplifies compression beyond what zero count predicts. Guard archetype coverage now complete with Booker (AAG). Formula architecture decision reached: weighted average is structurally incapable of tight fit across full dataset; ceiling-weighted formula required. Formula design begins Session 60.*

*Session 58 pattern check: N=0 count confirmed as primary compression driver across full spectrum — Hield (11 zeros, −0.16) and KAT (1 zero, −1.41) represent the poles; directional relationship holds. Within-band noise confirmed: 2-zero band spans −0.48 to −1.13, indicating profile elevation and drag domain depth as co-drivers within bands. KAT is largest gap in dataset (−1.41) — Stretch Big has only 1 structural zero, maximum breadth compression. Hield is smallest gap in dataset (−0.16) — Guard Shooting Specialist has 11 structural zeros, minimum compression. Ingram (−1.13) confirms: breadth compression without bimodal structure still produces large gaps when defense is a genuine drag domain. Waters vs. Ellis (same archetype, same N=0 count, −0.55 vs −0.34): lower profile elevation = larger gap within archetype, consistent with profile elevation as secondary driver. Formula analysis deferred to Session 59 — dataset now at 19 players across 14 archetypes; ready for hypothesis testing.*

*Session 57 pattern check: N=0 count does not independently suppress compression at higher tiers — Mitchell (4 zeros, −0.64) vs. Ellis (4 zeros, −0.34): Mitchell's non-zero sub-domains cluster 7.5–9.0; Ellis's cluster 4.5–8.5. Profile elevation drives compression more than N=0 count at the margin. Draymond ties Gobert at −0.36 from a completely different archetype — two data points at −0.36 with concentrated profiles and structural zeros strengthens N=0 hypothesis. Ellis correction logged: in-session composite 6.95/−0.30 using preliminary estimates; corrected to 6.91/−0.34 using final scored values. No formula changes. No architectural decisions.*

*Session 56 pattern check: N=0 zone hypothesis strengthened — 4 of 5 smallest gaps belong to players with the most structural zeros (Shead 5 zeros −0.17, Gobert 5 zeros −0.36, OG 2 zeros −0.48, Bridges 2 zeros −0.50). 3-and-D Wing archetype producing highly consistent gaps (−0.48, −0.50) across two players at different tier levels — formula stable within archetype. Jumbo Playmaker remains highest-compression archetype (−0.86, −1.09). Lillard anomaly identified: bimodal profile (elite shooting/ball skills + weak defense/athleticism) produces more compression than uniformly elevated profiles — distinct from distributed-breadth compression. Within-C split: Gobert (−0.36) vs Bam (−0.65) confirms archetype concentration drives compression more than position. 12-player threshold met — dataset ready for formula analysis when directed. No formula changes. No architectural decisions.*

*Session 55 pattern check: Tier correlation present but noisy — higher target generally produces larger gap but not cleanly. Jumbo Playmaker archetype produces consistently large gaps (−0.86, −1.09) — broadly distributed profiles compress more than concentrated profiles. Smallest gaps cluster around players with real N=0 zones in their archetype weight table. Working hypothesis: formula compresses more when a player is elite across many dimensions simultaneously. Needs more bigs and wing archetypes to confirm. No formula changes. No architectural decisions. All held until 12+ players.*

*Session 54 additions: Shead (validation). Archetype weighting removal flagged as open architectural question — defer until wings and bigs added to dataset. Key product design note logged: composite answers "how good at basketball period" not "how good at your role" — has implications for weighting system.*
