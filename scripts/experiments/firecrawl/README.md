# Firecrawl experiments

Test artifacts from exploring [Firecrawl](https://firecrawl.dev) (a web-scraping API) as an alternative source for Skill 1 research packets. **Not production data.** Production research packets live in `raw/[Player]/[YYYY-MM-DD]_research-packet.md`.

## Why this folder exists

`raw/` is the immutable production-evidence layer. Mixing experimental packets in there made it ambiguous which packet was "the real one" for a given player. This folder isolates research-tooling experiments from the production layer per the architectural rule: experiments live under `scripts/experiments/`, never `raw/`.

## Contents

- **`Myles_Turner/2026-04-26_research-packet-test.md`** — first-iteration Firecrawl-driven research packet, generated alongside the canonical 2026-04-25 production packet for comparison.
- **`Myles_Turner/2026-04-26_research-packet-test-iter2.md`** — second iteration with prompt/source-list refinements.
- **`Myles_Turner/scraped/2026-04-26/`** — 14 individual source-by-source markdown scrapes that fed into the test packets, numbered by retrieval order.

## Status

Inactive experiment, kept for reference. If Firecrawl integration becomes a serious option, start a new dated experiment alongside these and document the diff in this README.
