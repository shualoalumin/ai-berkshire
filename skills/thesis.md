---
description: Write an investment thesis with sell conditions defined before purchase, then track it quarterly against evidence with a health score.
argument-hint: <ticker or company name> [new | review]
---

# Thesis

Establish or review the investment thesis for **$ARGUMENTS**.

Most investment processes end at the purchase. That is where the hard part starts. Without
a written thesis, three predictable failures follow: holding a broken business because
selling would confirm a mistake, panic-selling an intact business because the price fell,
and — most commonly — no longer remembering precisely why you bought.

The fix is unglamorous. Write down what you believe and what would prove you wrong,
**before** you own it, while your judgment is still uncontaminated by the position.

---

## Step 0 — Recall

Read `memory/decisions/<COMPANY>.md` if it exists. A prior council review supplies the
raw material for the thesis, especially its unresolved conflicts — those are usually the
assumptions most worth tracking.

## Mode selection

Look for `research/<COMPANY>/thesis.md`.

- Absent → **Mode A: establish**
- Present → **Mode B: review**

---

# Mode A — Establish the thesis

## A1. The thesis in five sentences

If this cannot be completed cleanly, the decision is not ready. That is the test, not an
exercise.

```
I am buying <COMPANY> at <PRICE> because:

1. The business earns money by ________, and I understand that mechanism.
2. Its advantage is ________, and the evidence it is holding or widening is ________.
3. Management is trustworthy with capital because ________.
4. At today's price I am paying ________ of my estimate of intrinsic value,
   and the margin of safety comes from ________.
5. If I am wrong, the downside is limited because ________.
```

Vagueness in any sentence points to unfinished work, not to a writing problem. "It's a
great company" is not sentence 1.

## A2. Assumptions

Decompose the thesis into claims that reality can contradict. Typically three to seven —
fewer suggests shallow thinking, more suggests the thesis is unfocused.

| # | Assumption | How it is tested | Frequency | Status |
|---|-----------|------------------|-----------|:------:|
| 1 | Revenue compounds above 12% | Quarterly revenue growth | Quarterly | intact |
| 2 | Gross margin holds above 60% | Quarterly gross margin | Quarterly | intact |
| 3 | Buybacks continue below intrinsic value | Cash flow statement, average repurchase price | Quarterly | intact |
| 4 | No competitor matches the distribution advantage | Competitor filings, market share data | Semi-annual | intact |

A good assumption is falsifiable and cheap to check. "Management remains excellent" fails
both tests; "return on incremental capital stays above 15%" passes both.

## A3. Red lines

Conditions that force a re-evaluation — decided now, in calm conditions, because they will
be needed in the opposite circumstances.

| # | Red line | Severity | Predetermined action |
|---|----------|----------|---------------------|
| 1 | Evidence of dishonest disclosure or accounting manipulation | Terminal | Exit in full, immediately, no waiting for clarification |
| 2 | Core revenue declines two consecutive quarters absent a known cycle | Severe | Halve the position, reopen the full review |
| 3 | A competitor demonstrably replicates the advantage | Severe | Re-underwrite from scratch; exit if the advantage is gone |
| 4 | Leverage exceeds <X>x EBITDA outside a stated plan | Severe | Reassess survivability before doing anything else |
| 5 | Unplanned insider selling at scale | Warning | Investigate; no automatic action |

The distinction that matters most: **a falling price is not a red line.** A price decline
with the thesis intact is an opportunity. A price rise with the thesis broken is a gift
you should take. The thesis, not the quote, is the trigger.

## A4. Valuation anchors

| | At purchase | Bear | Base | Bull |
|---|---|---|---|---|
| Price | | | | |
| EPS or owner earnings | | | | |
| Multiple | | | | |
| Implied value | | | | |
| Margin of safety | | | | |

Generate with `tools/rigor.py scenarios` and paste the output. The point is to record what
you assumed, so that later you can find out which assumption was wrong — not to project
false precision.

## A5. Save

Write to `research/<COMPANY>/thesis.md`: date, entry price, position size, the five
sentences, assumptions, red lines, anchors, and an empty review log.

## A6. Record

Append to `memory/decisions/<COMPANY>.md`: date, thesis summary, and the assumption list.
Future reviews of this and of similar companies start from here.

---

# Mode B — Review

Run quarterly, and after any earnings release or material event.

## B1. Load

Read the existing thesis: the five sentences, assumptions, red lines, anchors, and the
prior review. Note explicitly what the last review said to watch.

## B2. Gather

Per `skills/data-standards.md`: latest filing, material events since the last review,
current price and multiples, insider transactions, and relevant competitor developments.

## B3. Test each assumption

| # | Assumption | Prior | Evidence this period | Now | Δ |
|---|-----------|:-----:|---------------------|:---:|:-:|
| 1 | Revenue > 12% | intact | Q4 growth 11.2% | weakening | ▼ |
| 2 | GM > 60% | intact | 61.4% | intact | — |

Four states, applied strictly:

- **intact** — evidence supports the assumption
- **weakening** — still within tolerance, trend adverse
- **impaired** — evidence contradicts the assumption
- **broken** — the assumption is falsified

Grade against the assumption as originally written. Silently loosening a threshold to keep
a status at "intact" is the most common way this process fails, and it fails invisibly.
If the original threshold now looks wrong, say so explicitly and record the change as an
amendment with its reasoning.

## B4. Check red lines

| # | Red line | Triggered | Evidence |
|---|----------|:---------:|----------|

Any trigger goes at the top of the report with its predetermined action. What you decided
in advance carries more weight than what you feel now, because now you own it.

## B5. Update valuation

| | At purchase | Prior review | Now | Δ |
|---|---|---|---|---|
| Price | | | | |
| Multiple | | | | |
| Estimated value | | | | |
| Margin of safety | | | | |

Separate the two questions: has the *business* changed, or has the *price* changed? They
call for opposite responses and are constantly confused.

## B6. Health score

```
health = 10 − 3×(broken) − 2×(impaired) − 1×(weakening) − 5×(red lines triggered)
clamped to [1, 10]
```

| Score | Reading | Indicated action |
|:-----:|---------|------------------|
| 9-10 | Thesis stronger than at purchase | Consider adding |
| 7-8 | Core intact, minor erosion | Hold |
| 5-6 | Real damage, central logic survives | Hold, tighten monitoring |
| 3-4 | Multiple assumptions impaired | Reduce |
| 1-2 | Red line triggered or thesis broken | Exit |

The formula is a discipline device, not an oracle. It exists to make you write down the
grades before you consult your feelings about the position. Where you override it, record
the override and its reasoning — that record is what makes the next review honest.

## B7. Conclude

Answer three questions plainly:

1. **Is the thesis intact?** intact / weakening / impaired / broken
2. **What action?** add / hold / reduce / exit
3. **When is the next review, and what specifically is being watched?**

## B8. Log

Append to `research/<COMPANY>/thesis.md`:

| Date | Health | What changed | Action |
|------|:------:|--------------|--------|

And to `memory/decisions/<COMPANY>.md`, including the back-check on the previous review's
watch list. Over time this record answers a question no single review can: **are your
assumptions the kind that turn out to be right?** That is a more valuable finding than any
one company's outcome.

---

## Principles

- **Write sell conditions before buying.** Decisions made without a position are better
  than decisions made with one.
- **Make assumptions falsifiable.** If nothing could contradict it, tracking it is theater.
- **Act on red lines.** "Let's give it another quarter" is how small mistakes become large
  ones.
- **A broken thesis is not a falling price**, and a falling price is not a broken thesis.
- **Record errors in specific terms.** A thesis that was wrong is information; a thesis
  quietly rewritten to have been right is worse than nothing.

> This skill produces research, not advice. See the disclaimer in README.md.
