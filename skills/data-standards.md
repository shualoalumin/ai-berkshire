---
description: Sourcing and cross-validation rules for every figure used in research — source hierarchy, two-source rule, tolerance bands, and how to report discrepancies.
argument-hint: (reference skill — usually invoked by other skills)
---

# Data Standards

The rules every other skill in this plugin follows when handling numbers. Invoke it
directly to check a specific figure, or read it as the reference it is.

A research process is only as good as its worst-sourced number, and a single wrong figure
that survives into a conclusion discredits everything around it. These rules exist to make
bad numbers visible before they reach a conclusion.

---

## Source hierarchy

Prefer sources in this order. Move down only when the level above genuinely lacks the
figure.

| Tier | Source | Notes |
|------|--------|-------|
| 1 | **Primary filings** — 10-K, 10-Q, 20-F, 6-K, proxy statement, annual report | The company's own audited statements. Everything else is derived from these. Access via the `sec-edgar` MCP tools for US filers. |
| 2 | **Structured market data** — `yahoo-finance` MCP tools | Prices, shares outstanding, statement summaries, ratios. Fast and machine-readable; occasionally stale near earnings dates. |
| 3 | **Aggregators** — established financial data sites | Convenient for long historical series. Normalization choices differ between them, which is exactly why the two-source rule exists. |
| 4 | **Macro series** — `fred` MCP tools | Rates, inflation, employment, sector indices. Needs a free `FRED_API_KEY`. |
| 5 | **Commentary** — press, analyst notes, transcripts | Useful for *what management said* and for identifying questions. Never the source of a figure. |

Non-US listings often have no tier-1 electronic source available through these tools. Use
the exchange's own disclosure portal and the company's investor relations page, and say in
the report which tier the figures came from.

## The two-source rule

**Every material figure needs two independent sources.** Material means: it appears in a
conclusion, a valuation, or a table in the final report.

Two sources are independent only if neither derives from the other. A data aggregator and
a site that republishes that aggregator are one source wearing two hats. When in doubt,
one of the two should be the primary filing.

### Tolerance

```
discrepancy = |a - b| / |a|
```

| Discrepancy | Handling |
|-------------|----------|
| ≤ 1% | Agreement. Use the higher-tier source, cite both. |
| 1% – 5% | Report both figures with the gap and the likely cause. Usable with the caveat attached. |
| > 5% | Do not use. Resolve against the primary filing first, then report the resolved figure and note which source was wrong. |

### Reporting format

```
Revenue: $12.4B  [agreement, 0.3%]
  10-K FY2025: $12.41B
  yahoo-finance: $12.37B
```

```
Net income: $2.45B  [discrepancy, 13.5% — non-comparable basis]
  10-K FY2025 (GAAP): $2.45B
  aggregator (adjusted): $2.78B
  Using GAAP. The adjusted figure excludes stock compensation,
  which recurs annually and is a real cost to shareholders.
```

## Common causes of legitimate discrepancy

Not every gap is an error. Diagnose before discarding.

| Cause | What it looks like |
|-------|-------------------|
| GAAP vs adjusted | Profit lines diverge, revenue agrees. The most frequent cause by far. |
| Fiscal calendar | "FY2025" means different periods at different companies. |
| Currency and translation | Reporting currency, presentation currency, and the rate date all differ. |
| Consolidation | Minority interests included in one source, excluded in the other. |
| Restatement | An older figure was revised; one source updated and the other did not. |
| Share count basis | Basic, diluted, period-end, or weighted average — four different numbers. |
| Staleness | An aggregator has not yet ingested the newest filing. |

State the cause in the report. "Sources disagree" is an observation; "sources disagree
because one adjusts for stock compensation" is an analysis.

## Arithmetic

Never do valuation arithmetic mentally or in prose. Use `tools/rigor.py`:

```bash
# Does the reported market cap actually equal price x shares?
python3 tools/rigor.py market-cap --price 178.50 --shares 1520000000 --reported 271.3e9

# Multiples from first principles
python3 tools/rigor.py multiples --price 178.50 --eps 8.42 --bvps 31.10

# Bear / base / bull, stated as assumptions rather than a single false-precision number
python3 tools/rigor.py scenarios --price 178.50 --eps 8.42 \
    --growth 0.03 0.08 0.14 --exit-pe 12 18 25

# Cross-validate two or more sources against the tolerance bands above
python3 tools/rigor.py cross-check --label "FY25 revenue" --values 12.41e9 12.37e9
```

Paste the tool output into the report as the verification record. Decimal arithmetic in a
tool is auditable; arithmetic in a sentence is not.

## Units and currency

- Always state the currency. A price in HKD compared against a valuation in USD is a
  wrong answer that looks right.
- Always state the scale — millions, billions, or lakh/crore for Indian filers.
- ADR ratios matter: an ADR may represent a fraction or a multiple of an ordinary share,
  so per-share figures do not transfer between them without conversion.

## Estimates and gaps

- A figure you derived rather than read is an **estimate**. Label it, show the derivation,
  and give it a confidence.
- A figure you cannot source is **not available**. Write that. Do not substitute a peer
  company's number, a prior year, or a plausible round figure.
- Private and pre-IPO companies usually cannot satisfy the two-source rule. Mark the whole
  section as single-sourced rather than pretending otherwise.

## Before publishing

Run through this list on any report that reaches a conclusion:

- [ ] Every figure in a conclusion has two sources or an explicit single-source label
- [ ] Every discrepancy above 1% is reported with its cause
- [ ] Market capitalization was verified against price × shares
- [ ] Currency and scale are stated on every table
- [ ] Estimates are labeled and their derivation is shown
- [ ] Gaps are written as gaps, not filled with inference
- [ ] Fact and interpretation are visually separable by a reader in a hurry
