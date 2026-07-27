---
description: Comprehensive single-company research — seven sequential modules from business model through valuation, building one integrated picture rather than four parallel views.
argument-hint: <ticker or company name>
---

# Deep Dive

Produce a full research report on **$ARGUMENTS**.

This is the single-analyst counterpart to `skills/council.md`. The council runs four
lenses in parallel and makes them argue; the deep dive runs one analyst sequentially,
where each module builds on the last. Use the deep dive when you want a coherent
narrative and a complete picture of a business. Use the council when you want the
disagreements surfaced.

Work through the modules **in order**. Later modules depend on earlier findings — you
cannot judge whether a margin is defensible before you understand what produces it.

---

## Step 0 — Recall and scope

Check `memory/decisions/<COMPANY>.md`. If prior work exists, state what changed since,
and let that question shape the emphasis of this report.

Grade evidence availability (A/B/C, as defined in `skills/council.md`) and let it govern
what this report is allowed to claim.

Follow `skills/data-standards.md` throughout: primary filings first, two sources for
every material figure, `tools/rigor.py` for arithmetic.

---

## Module 1 — The business

Everything downstream depends on getting this right, and it is the module most often
rushed.

- **The core transaction.** Who pays, for what, how often, and why they choose this
  provider over the alternative.
- **Revenue decomposition.** By segment, geography, and type — recurring versus one-time,
  subscription versus transactional. Recurring revenue with high retention deserves a
  different multiple than project revenue that must be won again each year.
- **Unit economics.** What one customer, store, subscriber, or contract costs to acquire
  and what it returns over its life. Payback period matters more than lifetime-value
  ratios, which are easy to inflate with optimistic churn assumptions.
- **The cost structure.** Fixed versus variable, and the operating leverage that follows.
- **The flywheel, if there is one.** Describe the actual causal loop and where it can
  break. Most claimed flywheels are ordinary scale economics with a diagram.

Close the module with a plain-language statement of what this business fundamentally is,
in two sentences.

## Module 2 — Industry and competition

- **Market structure.** Size, growth, concentration, and where the profit pool actually
  sits — which is often not where the revenue sits.
- **Position.** Share and its trend. Share gained through price cuts is not the same
  finding as share gained at stable prices.
- **The named competitors.** Two or three, analyzed individually rather than listed.
  What is each one's strategy, and what would it take for them to attack this company's
  core?
- **Value chain.** Who captures the economics up and down the chain, and is that
  distribution stable? Suppliers or channels with power extract margin over time.
- **Structural change.** Technology, regulation, distribution, or consumer behavior shifts
  that could redraw the industry. Distinguish changes underway from changes speculated
  about.

## Module 3 — The advantage, and how it ends

- Name the mechanism and produce evidence for it (use the test table in
  `skills/checklist.md`, Gate 3).
- Direction matters more than existence: is the advantage widening, holding, or eroding?
  Show the metric that demonstrates it.
- **Then invert.** Write the specific story of how this advantage is destroyed over ten
  years. Name the agent and the mechanism. If you cannot construct a plausible one, you do
  not yet understand the business well enough to own it.

## Module 4 — Financial history

Five years minimum, longer for cyclicals. Tables, sourced.

- Revenue, gross profit, operating income, net income, and the growth rates of each.
- Margin progression, with an explanation of every material inflection.
- ROIC and return on incremental invested capital.
- Cash flow: operating, capex split into maintenance and growth where determinable, and
  free cash flow.
- The cash conversion question: does net income become cash? Persistent divergence is
  the single most reliable early warning in fundamental analysis.
- Balance sheet: leverage, maturities, liquidity, off-balance-sheet obligations.
- Share count: is the per-share claim growing or shrinking?

## Module 5 — Management

Summarize here; run `skills/management.md` for the full treatment.

- The capital allocation record, in numbers.
- Whether stated plans matched subsequent outcomes.
- What incentive compensation actually rewards.
- Insider ownership bought versus granted.

## Module 6 — Risk

Distinguish the three kinds, because they call for different responses:

| Kind | Definition | Response |
|------|-----------|----------|
| **Business** | Something that permanently impairs earning power | Size the position for it or avoid |
| **Balance sheet** | Something that forces action at the worst time | Usually disqualifying |
| **Valuation** | The business is fine; the price assumed too much | Wait, with a target |

For each material risk: the mechanism, an honest likelihood, the severity if it occurs,
and the observable signal that would tell you it is happening. A risk with no observable
signal cannot be monitored, only survived — size accordingly.

## Module 7 — Valuation

- Intrinsic value from owner earnings, with assumptions stated explicitly.
- Scenarios via `tools/rigor.py scenarios`; report the range and what drives its width.
- **Reverse the DCF:** what does today's price require the business to do? This is usually
  the most informative single number in the report, because it converts a valuation debate
  into a testable claim about the business.
- Comparison to the company's own history and to peers, with the reason for any premium
  or discount.
- Margin of safety, stated as a number.

---

## Report structure

1. **Verdict** — one paragraph, the answer up front
2. **The business in brief** — what it does and how it makes money
3. **Key figures** — two-year comparison table, sourced
4. **Modules 1-7** — the analysis
5. **The case both ways** — bull and bear, each argued at its strongest
6. **Valuation and what to do** — stance, price range, triggers
7. **What could make this wrong** — the evidence that would overturn the conclusion
8. **Limits** — evidence grade, what could not be verified, where inference substituted
   for measurement

## Save and record

Write to `research/<COMPANY>/deep-dive-<YYYY-MM-DD>.md` and append a summary to
`memory/decisions/<COMPANY>.md`.

---

## Standing rules

- **Modules run in order.** Skipping to valuation is the most common failure mode in
  equity research and produces confident numbers built on an unexamined business.
- **Fact and inference stay visually distinct.** A reader must be able to tell at a glance
  which is which.
- **Gaps are stated as gaps.** A blank field is information. A field filled with a
  plausible guess is a liability that looks like an asset.
- **The strongest bear case is written by you.** If the bear section is weaker than the
  bull section, the report is advocacy.

> This skill produces research, not advice. See the disclaimer in README.md.
