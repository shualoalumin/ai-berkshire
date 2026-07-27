---
description: Narrow a universe of companies to a short list using exclusion-first quality filters, so research time goes to candidates that can survive scrutiny.
argument-hint: <sector, theme, or list of tickers>
---

# Quality Screen

Screen **$ARGUMENTS** down to a short list worth real research time.

Screening is triage, not analysis. Its only job is to spend your attention well: eliminate
quickly and cheaply, so that deep work goes to companies that can survive it. A screen that
returns forty names has failed at the one thing it was for.

**Exclusions run before rankings.** It is far easier to identify businesses that are
definitely not worth owning than to rank the ones that might be, and the exclusions are
where most of the value is. A cheap multiple on a structurally declining business is the
most expensive thing on any screen.

---

## Step 1 — Define the universe

State it explicitly, because it determines what the screen can possibly find:

- Sector, theme, index, or an explicit ticker list
- Market capitalization floor — below roughly $300M, liquidity and disclosure quality
  degrade enough to change the process
- Geography and listing venue, which determines available disclosure
- Anything deliberately excluded, and why

Record the universe size. The funnel arithmetic is part of the output.

## Step 2 — Exclusions

Each filter is a hard exclusion. Run them in order; a company excluded at any step is out,
and needs no further data gathering.

| # | Exclude | Rationale |
|---|---------|-----------|
| 1 | Cannot explain the business model in three sentences | An unexplainable business cannot be underwritten, only hoped for |
| 2 | Persistent negative free cash flow with no funded, credible path | Financing risk dominates business outcomes |
| 3 | Net debt / EBITDA above ~4x outside a stable-cashflow structure | Leverage removes the option to wait, which is your main advantage |
| 4 | ROIC below cost of capital across a full cycle | The business consumes capital; growth makes it worse |
| 5 | Five-year revenue trend structurally declining | Turnarounds seldom turn, and demand this be an explicit thesis rather than a screen result |
| 6 | Serial dilution without matching per-share value growth | Your claim shrinks faster than the pie grows |
| 7 | Accounting or governance flags | Repeated restatements, auditor changes, resignations, material weaknesses, opaque related-party dealings, adjustments that recur every year |
| 8 | Single customer, supplier, or regulator controls the outcome | Concentration you cannot analyze from outside |

Filters 7 and 8 catch what pure numeric screeners miss, and they are the reason this step
is not simply a stock screener query. Governance failures do not show up as a ratio.

## Step 3 — Quality ranking

Rank survivors only. Gather from primary filings and the `yahoo-finance` and `sec-edgar`
MCP tools, per `skills/data-standards.md`.

| Dimension | Metric | Weight |
|-----------|--------|:------:|
| Capital returns | 5-year average ROIC; trend in return on incremental invested capital | 30% |
| Cash generation | FCF / net income; FCF margin trend | 25% |
| Balance sheet | Net debt / EBITDA; interest coverage at trough; maturity profile | 20% |
| Consistency | Revenue and margin variability across the cycle | 15% |
| Per-share discipline | Change in share count; buyback prices against value | 10% |

Note valuation but **do not rank on it**. Cheapness is a reason to look closer, never a
reason to make a short list — the cheapest deciles of any screen are dominated by
businesses that deserve to be there.

## Step 4 — Report

```
FUNNEL
  Universe                  N
  After exclusions          n1   (largest single exclusion: filter #X, k names)
  Short list                n2
```

**Short list** — five to ten names maximum:

| Company | Quality | Why it survived | What must be verified | Valuation note |
|---------|:-------:|-----------------|----------------------|----------------|

The "must be verified" column is the point of the output. It hands the next stage a
specific question rather than a general instruction to go research something.

**Notable exclusions** — three to five names a reader would expect to see, with the reason
they were cut. This is where a screen earns trust, and where you find your own errors: if a
well-regarded company was excluded, either you learned something or your filter is wrong.

**Screen limitations** — state them. Screens are backward-looking and favor the legible.
They systematically miss: businesses mid-transition, companies whose economics are hidden
inside a segment, high-quality businesses that reinvest so heavily that current earnings
understate earning power, and anything whose disclosure is poor for legitimate reasons.

## Step 5 — Route

- Short list → `skills/council.md` for full review, or `skills/deep-dive.md` for a single
  name.
- Record the screen date, universe, and short list in `memory/decisions/`. Revisiting a
  screen a year later tells you whether your filters select for the right things, which no
  single screen run can.

---

## Principles

- **Exclude first.** Avoiding the worst outcomes contributes more to results than
  selecting the best ones.
- **Never rank on cheapness.** Price enters at the valuation gate, not the screening gate.
- **Judge cyclicals across the cycle.** Trough metrics exclude good businesses; peak
  metrics admit bad ones.
- **A screen produces questions, not conclusions.** Nothing on the short list is buyable
  until it has been through the gate and the council.

> This skill produces research, not advice. See the disclaimer in README.md.
