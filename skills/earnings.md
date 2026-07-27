---
description: Read an earnings report from the primary filing rather than the press release — segment detail, cash quality, guidance changes, and what management avoided saying.
argument-hint: <ticker> [quarter, e.g. Q3 FY2026]
---

# Earnings Review

Analyze the latest earnings for **$ARGUMENTS**.

The press release is written to shape the reaction. The filing is written to satisfy
lawyers. Read the filing.

Most of what matters in an earnings report is not in the headline numbers, which are
anticipated and largely priced within minutes. It is in the segment tables, the cash flow
statement, the changes in language from the prior quarter, and the questions management
declined to answer directly.

---

## Step 0 — Establish expectations first

Before opening the filing, write down what you expected. Otherwise every result will look
like it was foreseeable.

- What did the prior quarter's guidance say?
- Which assumptions from `research/<COMPANY>/thesis.md` does this quarter test?
- What was consensus expecting on the two or three figures that matter for this business?
- What did the last review flag as the thing to watch?

This step takes two minutes and prevents the most common failure in earnings analysis,
which is narrating the result as though you had predicted it.

## Step 1 — Get the primary document

Use the `sec-edgar` MCP tools for US filers: the 10-Q or 10-K, not the 8-K press release.
For other markets, use the exchange filing or annual report from investor relations.

Read, in this order:

1. **The financial statements themselves** — before any management commentary
2. **Segment note** — where the actual story usually is
3. **Cash flow statement** — the hardest statement to manage
4. **Management's discussion** — for explanation and for what it avoids
5. **Risk factor changes** — new or materially rewritten risks are a deliberate signal
6. **Subsequent events and commitments**

Reading the narrative before the numbers lets someone else's framing anchor you.

## Step 2 — The numbers

| Line | This period | Prior year | Δ | Versus guidance |
|------|------------|-----------|---|-----------------|

Then go beneath the headline, which is where the information is:

- **Segments.** Which one drove the result? Consolidated growth frequently conceals one
  segment decelerating while another accelerates — that mix shift is often more important
  than the total.
- **Growth decomposition.** Volume, price, mix, currency, acquisitions. Growth from
  acquisition is not growth from the business; growth from price in an inflationary period
  is not the same as growth from units.
- **Margins.** Every material move needs a cause, and "cost discipline" is not a cause.
- **Cash.** Operating cash flow against net income. Working capital movements —
  receivables growing faster than revenue means revenue is being recognized before it is
  being collected, which eventually matters.
- **Share count.** Buybacks against dilution. Companies that repurchase exactly enough to
  offset issuance are transferring value to employees, not returning it to owners.
- **Capitalization choices.** Costs moved from the income statement to the balance sheet
  improve current earnings and reduce their quality. Compare capitalization rates to prior
  periods.

Verify arithmetic with `tools/rigor.py`. Follow `skills/data-standards.md` on sourcing.

## Step 3 — Adjustments

Build the bridge from GAAP to whatever management is highlighting, item by item.

| Adjustment | Amount | Recurs every year? | Legitimate? |
|-----------|-------:|:-----------------:|-------------|

The governing question: **is this a real cost to shareholders?** Stock compensation is a
real cost — the shares are real and the dilution is real. Restructuring charges that
appear in five consecutive years are an operating cost with a favorable name. A genuine
one-time item — a settled lawsuit, a disposed segment — is legitimately excluded.

If adjusted earnings exceed GAAP earnings every year for five years, the adjustments are
the business model, not the exceptions.

## Step 4 — Language

Compare this quarter's wording with last quarter's on the same topics.

- Guidance: raised, held, lowered, widened, or quietly withdrawn?
- Metrics that were emphasized before and have now disappeared. A metric stops being
  disclosed shortly after it stops being flattering — its absence is the disclosure.
- Hedging that was not there before: "headwinds," "transitory," "investment year,"
  "normalization."
- New or rewritten risk factors.

On the call: which analyst questions received direct answers with numbers, and which
received a restatement of strategy? A question deflected twice is the question that
matters.

## Step 5 — Thesis impact

This is the step that converts an earnings report into a decision, and the reason to do
any of this.

| Assumption | Status before | Evidence this quarter | Status now |
|-----------|:-------------:|----------------------|:----------:|

Use the four states from `skills/thesis.md`: intact, weakening, impaired, broken. Then
check red lines. If any triggered, that goes at the top of the report with the action
that was decided in advance.

## Step 6 — Report

```
1. One-line summary — what this quarter actually showed
2. Expected versus delivered (from Step 0)
3. Numbers, with segment detail
4. Quality of earnings — adjustments, cash conversion, capitalization
5. Language and disclosure changes
6. Thesis impact — assumption table and red line check
7. Conclusion — does anything change? what is next quarter's test?
```

Save to `research/<COMPANY>/earnings-<PERIOD>.md`. Append to
`memory/decisions/<COMPANY>.md`, and if a thesis exists, run its Mode B review.

---

## Principles

- **Write expectations before reading results.** Hindsight arrives instantly and is
  worthless.
- **Cash flow is the least manageable statement.** When statements disagree, weight it.
- **One quarter is weak evidence about a business** and strong evidence about management's
  candor. Judge the business over years and the disclosure over quarters.
- **What disappeared from disclosure is a finding**, and usually a more reliable one than
  anything that was added.
- **Price reaction is not information.** The market's same-day judgment is a data point
  about positioning, not about the business.

> This skill produces research, not advice. See the disclaimer in README.md.
