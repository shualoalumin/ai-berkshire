---
description: Review a portfolio as a single system — concentration, hidden correlation, thesis health across positions, and whether each holding still earns its place.
argument-hint: <holdings list, or path to a holdings file>
---

# Portfolio Review

Review the portfolio: **$ARGUMENTS**.

A portfolio is not the sum of its positions. Holdings that look independent frequently
express the same underlying bet, and the most common way a concentrated portfolio fails
is not one bad stock but five positions that turn out to have been one position.

Review the system, then the components.

---

## Step 1 — Establish the current state

If holdings were not supplied in detail, ask for: ticker, shares, average cost, current
price, and purchase date for each.

| Holding | Weight | Cost basis | Current | Return | Held since |
|---------|:------:|-----------:|--------:|:------:|:----------:|

Include cash as a position. Cash is an active allocation decision — it holds optionality
and it costs you real return during rising markets. Treating it as residual hides the
decision.

## Step 2 — Concentration

- **Position sizes.** Top holding, top three, top five as percentages of the total.
- **Sector and geography.** Where is exposure concentrated, and was that deliberate?
- **Factor exposure.** Are these all long-duration growth, all deep value, all rate-
  sensitive? Style concentration is real concentration and is usually accidental.
- **Currency.** Revenue currency matters more than listing currency for an operating
  business.

There is no correct concentration level. Concentration is how outperformance is achieved
and also how capital is permanently lost; the point is that it should be a choice. State
what the current level implies and whether it matches intent.

## Step 3 — Hidden correlation

The step that most reviews skip, and the one most likely to change a decision.

For each pair of significant holdings, ask what single event would damage both. Not
statistical correlation — **shared dependency**, which is what actually matters in a
drawdown:

| Shared dependency | Which holdings | Combined weight |
|-------------------|----------------|:---------------:|
| Same end customer or industry demand | | |
| Same key supplier or input cost | | |
| Same regulatory regime | | |
| Same macro driver (rates, oil, housing, freight) | | |
| Same underlying thesis | | |

Four semiconductor companies at 8% each is a 32% bet on one capex cycle, not four
diversified positions. Historical correlations are least reliable in exactly the
conditions where you need them, because in a genuine dislocation everything you own
correlates to one.

## Step 4 — Position-level health

For each holding with a thesis on file, run the Mode B review from `skills/thesis.md` or
load the most recent one.

| Holding | Thesis health | Assumptions impaired | Red lines | Action |
|---------|:-------------:|:--------------------:|:---------:|--------|

For holdings **without** a written thesis: that is the finding. You cannot evaluate a
position whose original reasoning was never recorded, and you will reconstruct a
flattering version of it. Write the thesis now, based on today's evidence, and note that
it is a reconstruction rather than the original.

## Step 5 — The questions that matter

Ask these of every position, honestly:

1. **Would you buy it today at today's price, at this weight?** If not, you are holding
   only because you already hold it. The tax and transaction costs are real inputs, but
   they are not a thesis.
2. **Is it earning its place?** The comparison is not against cash or against an index —
   it is against adding to the best thing you already own. Most portfolios hold several
   positions that are worse than more of the best one.
3. **Has the position drifted from intent?** A winner that has become 30% of the portfolio
   is a different risk than the 10% position you originally sized. Trimming is not a
   verdict on the business; it is a decision about the portfolio.
4. **Is a loser being held for the wrong reason?** Down 40% with the thesis intact is a
   possible opportunity. Down 40% with the thesis broken is a decision being avoided. The
   entry price is not information about the future.

## Step 6 — Report

```
1. Portfolio snapshot — holdings, weights, returns, cash
2. Concentration — position, sector, factor, currency
3. Hidden correlation — shared dependency table
4. Thesis health across positions
5. Actions — by position, with reasoning
6. What is watched next, and when
```

**Actions table:**

| Holding | Action | Reason | Trigger or price |
|---------|--------|--------|------------------|

The default action is to do nothing, and it should be the most common entry. A review that
generates trades in most positions is a review that has confused activity with judgment.
Turnover is a cost paid with certainty for a benefit that is not.

Save to `research/portfolio-<YYYY-MM-DD>.md`. Record material changes in
`memory/decisions/`.

---

## Principles

- **Correlation is measured in shared dependencies**, not in historical price series.
- **Cash is a position.** Give it a weight and a reason.
- **Sizing follows conviction and downside**, not enthusiasm or recent performance.
- **The alternative to any holding is more of your best holding**, not the index.
- **Doing nothing is usually correct** and is the hardest recommendation to write.
- **Your entry price is not a fact about the business.** The market has no record of it.

> This skill produces research, not advice. See the disclaimer in README.md.
