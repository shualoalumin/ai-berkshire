---
description: Triage a sharp price move fast — find the actual cause, classify it as noise or signal, and decide whether the thesis is affected before reacting.
argument-hint: <ticker> [what happened, if known]
---

# Pulse

Triage the price move in **$ARGUMENTS**.

A stock moved sharply and you want to know whether it matters. This skill answers that in
a bounded amount of time, and its most frequent correct output is **"noise, no action."**

The purpose is to stand between a price move and a decision. Most sharp moves change
nothing about what a business is worth over a decade, and the reflex to act on them is
what converts market volatility into permanent loss.

---

## Step 1 — Establish what actually happened

Before explaining anything, measure it. Explanations attach themselves to any move, and
plausible ones are always available after the fact.

- Magnitude and window: how far, over what period?
- Relative to what? Against the sector and the index. A stock down 6% on a day the sector
  fell 5% has moved 1%, and that is a different question than a 6% idiosyncratic decline.
- Volume against its own average. A large move on ordinary volume is often mechanical;
  heavy volume indicates real repositioning.
- Where does this sit in the stock's own distribution of moves? Some businesses routinely
  move 8% and it means nothing.

Use the `yahoo-finance` MCP tools for price, volume, and sector comparison.

## Step 2 — Find the cause

Work down this list and stop at the first item that genuinely explains the magnitude.

| Check | Where |
|-------|-------|
| Company filing | `sec-edgar` — an 8-K, a new registration, insider Form 4s |
| Earnings or guidance | Company IR, filing |
| Corporate action | Offering, buyback, dividend change, index add or delete, lockup expiry |
| Sector or peer news | A competitor's results routinely move an entire sector |
| Macro | Rates, inflation prints, currency, commodity inputs — `fred` |
| Regulatory or legal | Ruling, investigation, policy change |
| Analyst action | Upgrade, downgrade, initiation, target change |
| Nothing identifiable | Flow, positioning, rebalancing, or no reason at all |

**"No identifiable cause" is a legitimate and common finding.** Say it rather than
manufacturing a narrative. Financial media publishes an explanation for every move
regardless of whether one exists, and adopting that explanation is how you end up
believing something false about your holding.

Beware of explanations that do not fit the magnitude. A downgrade rarely explains 20%.

## Step 3 — Classify

| Class | Definition | Response |
|-------|-----------|----------|
| **Noise** | No change to long-term earning power. Sentiment, flows, macro rotation, analyst opinion. | None. Record and move on. |
| **Repricing** | The business is unchanged; the market changed what it will pay. | None, unless it creates an opportunity at your predetermined price. |
| **New information, thesis intact** | Something real happened; it does not touch a core assumption. | Update the file. Re-examine at the next scheduled review. |
| **New information, thesis affected** | A core assumption is directly implicated. | Full thesis review now — `skills/thesis.md`, Mode B. |
| **Red line** | A predetermined trigger from the thesis has fired. | Execute the action decided in advance. |

The classification governs the response. Most moves land in the first two rows, and the
discipline is in writing that down rather than searching for a reason to act.

## Step 4 — Thesis check

Only if the classification is "affected" or above. Name the specific assumption implicated
and grade it: intact, weakening, impaired, broken.

Then the question that actually decides the outcome:

> **Has the business changed, or has the price changed?**

A price decline with the business intact widens the margin of safety — it argues for
adding, not selling. A price rise with the business impaired argues for selling into
strength. These are the opposite of what the move makes you want to do, which is precisely
why the classification comes before the decision.

## Step 5 — Output

Keep it short. This is triage, not research.

```
MOVE:    -14.2% over 2 sessions (sector -3.1%, volume 4.2x average)
CAUSE:   Q3 guidance cut; FY revenue growth guided 8% from 14%
CLASS:   New information — thesis affected
THESIS:  Assumption 1 (revenue > 12%) — impaired
ACTION:  Full thesis review before any trade
NOTE:    Margin guidance unchanged; the issue appears to be volume, not price
```

If the finding is noise, say so in two lines and stop. That is the skill working, not
failing to find something.

Append anything above "repricing" to `memory/decisions/<COMPANY>.md`. Over time these
entries reveal something useful about your own judgment: how often the moves you found
alarming turned out to matter at all.

---

## Principles

- **Measure before explaining.** A narrative is always available and often invented.
- **Compare against the sector.** Most single-stock moves are largely market or sector.
- **"No cause found" is an answer**, and a more honest one than a borrowed headline.
- **Price moves are not information about value.** They are information about what other
  people did today.
- **The output is usually "no action."** A triage tool that keeps finding reasons to trade
  is not triaging.

> This skill produces research, not advice. See the disclaimer in README.md.
