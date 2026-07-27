---
description: Pre-purchase gate — seven sequential checks a company must pass before it is buyable, designed to stop early rather than to produce a score.
argument-hint: <ticker or company name>
---

# Pre-Purchase Checklist

Run the buy gate on **$ARGUMENTS**.

This is a gate, not a scorecard. The checks run in order, and **a hard failure ends the
review** — there is no compensating for a broken balance sheet with an attractive growth
rate. Most companies should fail this, and fail it early. A checklist that passes
everything you point it at is decoration.

Report the gate that stopped the review, and stop there. Analyzing the price of a business
you have already established you do not understand is wasted effort.

---

## Gate 1 — Do I understand this?

The only gate with no numbers, and the one most often skipped.

- Explain how the company earns a dollar, in plain language, without industry jargon.
- Name the three variables that determine whether it earns more or less next year.
- Say what would have to happen for this business to be worth half of today's price.

**Hard fail:** the explanation needs terms you cannot define, or the answer to any of the
three is guesswork.

There is no penalty for a small circle of competence and a severe penalty for
misjudging where its edge is. Passing this gate on the strength of a week's reading is
the most common way to fail it.

## Gate 2 — Is this a good business?

| Test | Threshold | Why it matters |
|------|:---------:|----------------|
| Return on invested capital | > 12% sustained over 5 years, excluding goodwill from acquisitions | Persistently low returns mean the business consumes capital rather than compounding it |
| Return on **incremental** invested capital | Above cost of capital and stable | This, not historical ROIC, determines what growth is worth |
| Gross margin trend | Stable or rising over 5 years | Sustained erosion is competition arriving |
| Free cash flow conversion | FCF / net income > 0.7 across a cycle | Earnings that never become cash are an accounting position, not a result |
| Capital intensity | Maintenance capex well below operating cash flow | Businesses that must spend everything to stand still have no owner earnings |

**Hard fail:** ROIC below cost of capital across a full cycle, or free cash flow
persistently and unexplainably below net income.

A cyclical business must be judged across a whole cycle. Trough ROIC in a downturn is not
a failure; average ROIC below cost of capital across the cycle is.

## Gate 3 — Is the advantage durable?

Name the mechanism, then test it. Naming is not evidence.

| Claimed advantage | Evidence that would confirm it |
|-------------------|-------------------------------|
| Brand | Sustained price premium over comparable substitutes, with volume held |
| Switching costs | Low churn, rising revenue per retained customer, long contract lives |
| Network effects | Unit economics that improve with scale, and a failed challenger |
| Cost advantage | Structurally lower unit cost from a source competitors cannot replicate |
| Scale | Fixed costs spread over a base rivals cannot reach |
| Regulatory or licence | The barrier is real, and the regulator is not about to change it |

Then invert: **how does this advantage end?** Name the specific mechanism — a technology
shift, a distribution change, a regulatory change, a better-capitalized entrant. If no
plausible mechanism can be described, the analysis is not finished.

**Hard fail:** no mechanism can be evidenced, or a credible destruction path is already
visible in the numbers.

## Gate 4 — Can management be trusted with the capital?

Judge the record, not the letter to shareholders.

- **Capital allocation history:** where did the last five years of free cash flow go —
  reinvestment, acquisitions, buybacks, dividends, debt reduction? What return did each
  earn?
- **Buyback discipline:** were shares repurchased below intrinsic value, or at the highs
  when cash was plentiful? The pattern reveals whether management understands value.
- **Acquisitions:** did returns on acquired capital exceed cost of capital, or did
  goodwill get written down later?
- **Candor:** does the annual report discuss mistakes in specific terms? Compare last
  year's stated plan to this year's outcome.
- **Incentives:** what are executives actually paid to maximize? Adjusted EPS targets
  invite adjustment; returns on capital and per-share value are harder to game.
- **Alignment:** meaningful ownership bought with their own money, versus granted equity
  that is sold as soon as it vests.

**Hard fail:** a history of value-destructive acquisitions with no acknowledgment,
related-party dealing that benefits insiders, or any evidence of dishonesty in past
disclosure. Integrity failures do not get priced in — they get discovered later.

For deeper work here, run `skills/management.md`.

## Gate 5 — Does it survive a bad outcome?

- Debt to EBITDA, and the maturity schedule — what refinances in the next 24 months, at
  what rates?
- Interest coverage at trough earnings, not current earnings.
- Off-balance-sheet obligations: leases, pensions, purchase commitments, guarantees.
- Liquidity: cash, undrawn facilities, and working capital swings under stress.
- Customer and supplier concentration — what happens if the largest one leaves?

**Hard fail:** the company requires access to capital markets to survive two bad years. A
business whose survival depends on refinancing conditions is not one you can hold through
a downturn, which is exactly when you would need to.

## Gate 6 — Is the price right?

Only now. Valuing a business before establishing it is worth owning inverts the process
and encourages you to justify a price you have already anchored on.

- Estimate intrinsic value from owner earnings and a defensible discount rate. State the
  assumptions; the assumptions are the estimate.
- Run bear, base, and bull with `tools/rigor.py scenarios`. Report the range, not a point.
- **Margin of safety** = (intrinsic value − price) / intrinsic value. State it as a number.
- What is priced in? Reverse the DCF: what growth rate and margin does today's price
  require? Is that assumption defensible?
- Compare against the company's own history and its closest peers, and say why any premium
  or discount is deserved.

**Hard fail:** no margin of safety at current prices, or intrinsic value that can only be
justified with assumptions the business has never achieved.

Failing Gate 6 alone is the good outcome — a quality business at the wrong price becomes a
watchlist entry with a target, not a rejection.

## Gate 7 — Does it fit the portfolio?

- Position size relative to conviction and to what a permanent loss here would do.
- Correlation with existing holdings — the same bet expressed three ways is one bet with
  three times the size.
- Opportunity cost: is this better than adding to the best thing already owned? That is
  the real comparison, not this against cash.
- **Sell conditions, written before buying.** Establish them now, via `skills/thesis.md`,
  while judgment is uncontaminated by ownership.

**Hard fail:** you cannot state in advance what would make you sell.

---

## Output

```
GATE RESULT: PASS / FAIL at Gate N

| Gate | Result | Evidence |
|------|:------:|----------|
| 1. Understanding    | pass/fail | |
| 2. Business quality | pass/fail | |
| 3. Durability       | pass/fail | |
| 4. Management       | pass/fail | |
| 5. Survivability    | pass/fail | |
| 6. Price            | pass/fail | |
| 7. Portfolio fit    | pass/fail | |
```

Then:
- **Failed:** name the gate, the evidence, and whether the failure is permanent (a bad
  business) or conditional (a good business at a bad price). Record the price that would
  reopen the question.
- **Passed:** state position size, the entry range, and go write the thesis with
  `skills/thesis.md` before placing any order.

Append the outcome to `memory/decisions/<COMPANY>.md`, including failures. A record of what
you rejected and why is more useful later than a record of what you bought — it is the only
way to find out whether your rejections were right.

> This skill produces research, not advice. See the disclaimer in README.md.
