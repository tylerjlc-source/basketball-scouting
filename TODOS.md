# TODOs

## TD-001 — Continuous forward-validation infrastructure

**What:** Design and implement a continuous forward-validation ledger that captures evaluation date for every profile and computes rolling Spearman against subsequent player outcomes as years pass.

**Why:** The 2021-cohort back-test (Approach C) Limitations subsection explicitly names forward-validation as "the true out-of-sample answer." This TODO is the path to making the validation paper a living methodology, not a one-off — each new evaluation in `output/[Player]/[YYYY-MM-DD]_profile.md` becomes a future data point.

**Pros:**
- Compounding credibility — every new evaluation adds to the validation series
- Automatic update artifact for the methodology page
- Justifies the rubric over time without manual re-tests

**Cons:**
- Multi-year payoff; no near-term benefit
- May require schema additions to `wiki/evaluations.jsonl` for date tracking

**Context:** Depends on the BRANCH per-player history layout already being in place (per SCHEMA-SPEC.md §10-A — it is). Triggered by the back-test launch paper acknowledging this as future work.

**Depends on / blocked by:** Nothing structurally. No value to start before the 2021 back-test launch paper ships.

---

## TD-002 — Preserve G-League + International stat-source mappings from D7 audit

**What:** After the D7 pre-flight source-map audit completes for the back-test, formalize the G-League and International additions as permanent rows in `docs/SUB-DOMAIN-SOURCE-MAP_v1.md` so future non-NBA prospect evaluations can reuse them.

**Why:** The back-test audit will do this work anyway as a dependency. Preserving it as a permanent doc artifact pays off year-2 college/international expansion (design doc P6) and any one-off non-NBA prospect work that comes up sooner (Wemby-style cases, international stars considered for evaluation).

**Pros:**
- Zero marginal cost during the back-test (audit work is already happening)
- Real ongoing value afterward
- Removes friction for ad-hoc evals of international/G-League prospects between now and year-2 expansion

**Cons:**
- Requires keeping maps current (sites go down, sources move, league data formats change)

**Context:** D7 (back-test source-map audit) is the trigger. Treat the audit output as a durable artifact rather than a back-test-only deliverable. The doc update is the deliverable; this TODO is the discipline commitment to maintain it.

**Depends on / blocked by:** D7 audit completion (Week 1-2 of back-test).
