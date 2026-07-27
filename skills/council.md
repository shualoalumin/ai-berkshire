---
description: Run a four-analyst value investing council on a company — Buffett, Munger, Graham, and Lynch lenses analyze in parallel, then cross-examine each other.
argument-hint: <ticker or company name>
---

# Council Review

Convene the full council on **$ARGUMENTS**.

Four analysts study the same business through four incompatible lenses, then argue with
each other. The deliverable is not a consensus number. It is a map of where the lenses
agree, where they collide, and what evidence would settle each collision.

## Why four seats

One analytical frame produces one blind spot, and the blind spot is invisible from
inside the frame. A quality-focused analyst talks himself into paying too much. A
deep-value analyst talks himself out of every good business. Running the frames in
parallel and forcing them to attack each other surfaces the blind spots that any single
frame would hide.

| Seat | Lens | Structurally argues *for* | Structurally argues *against* |
|------|------|---------------------------|-------------------------------|
| **Quality** | Buffett | Durable economics, owner earnings, paying up for a great business | Mediocre businesses at any price |
| **Inversion** | Munger | Understanding what kills the business before what grows it | Anything whose incentive structure is rotten |
| **Safety** | Graham | Downside first, balance sheet, statistical cheapness | Paying for a narrative; any thin margin of safety |
| **Growth** | Lynch | The story, the category, growth you can buy at a sane multiple | Slow decliners dressed up as bargains |

The two live fault lines are **Graham vs Lynch** (price discipline against growth
tolerance) and **Buffett vs Munger** (what makes this business great against what makes
it die). If the council never surfaces tension on either axis, the analysis is too
shallow — say so rather than manufacturing agreement.

---

## Step 0 — Recall

Before any new work, check `memory/decisions/<COMPANY>.md` (see
`memory/decisions/README.md`). If prior council records exist, load the most recent one
and open the review by stating:

- when the company was last reviewed, and what the council concluded
- which prior assumptions have since been confirmed or broken
- **the question this review must answer: what has actually changed?**

A review that reaches last quarter's conclusion with no new evidence is not tracking a
business — it is repeating itself. Flag that explicitly if it happens.

If no record exists, note that this is a first review and continue.

## Step 1 — Evidence grade

Before analyzing, grade how knowable this company is. This sets what the council is
allowed to claim.

| Grade | Situation | How the council must adapt |
|-------|-----------|----------------------------|
| **A** | Large cap, long filing history, wide analyst coverage | Consensus is cheap and already priced. Push the seats toward disconfirming evidence and non-consensus reads. Restating the consensus adds nothing. |
| **B** | Recent listing, thin coverage, some primary filings | Every derived figure carries a stated confidence. The chair labels overall evidence sufficiency in the final report. |
| **C** | Obscure, pre-IPO comparables, poor disclosure | Drop the full report format. Answer three or four first-principles questions about the business honestly, and leave the rest blank. |

**The trap:** abundant information feels like certainty and scarce information feels like
risk, but neither is true. Certainty comes from the durability of the business, not the
volume of available material. A heavily covered company can be deeply unpredictable; a
obscure one can be easy to understand. Grade the evidence, then judge the business
separately.

## Step 2 — Seat the analysts

Launch **four analysts in parallel** — one message, four subagent calls, each running in
the background. Every analyst gets the shared brief plus its own seat brief.

### Shared brief (goes to all four)

```
You hold the {SEAT} seat on a value investing council reviewing {COMPANY}.
Evidence grade for this company: {GRADE}.

Ground rules:
- Follow the sourcing and cross-validation rules in skills/data-standards.md.
  Every material figure needs two independent sources; flag any gap above 1%.
- Prefer primary filings (10-K, 10-Q, 20-F, annual report) over commentary.
  Use the sec-edgar and yahoo-finance MCP tools when available.
- Separate fact from inference. Facts carry a source. Inferences are labeled as
  inferences, with the reasoning shown.
- Where the data does not support a conclusion, write "insufficient evidence."
  Do not fill the gap with plausible-sounding narrative.
- Argue your seat honestly. You are not here to be balanced — the other three
  seats provide the balance. But do not misrepresent evidence to win.

Deliver:
1. Your seat's core finding in one paragraph.
2. Supporting analysis with tables for anything numeric.
3. A 1-5 rating on your seat's dimension, with the reasoning for the number.
4. The single strongest argument AGAINST your own conclusion.
5. The specific evidence that would change your mind.

Item 4 is not optional. A seat that cannot argue against itself has not
finished thinking.
```

### Seat briefs

**Quality seat (Buffett lens)**
Judge the business as if buying it whole and never selling.
- What is the actual economic engine? Where does a dollar of revenue come from, and what does it cost to earn the next one?
- Owner earnings: net income plus non-cash charges, minus the capital expenditure genuinely required to hold competitive position. How does that compare to reported earnings?
- Return on incremental invested capital — can the company redeploy profits at a high rate, or does growth require capital it cannot earn back?
- Durability of the advantage: brand, switching costs, network effects, cost position, regulatory position. Test each claim rather than listing it.
- Pricing power: has the company raised prices without losing volume? Show the evidence.
- Rate 1-5 on business quality.

**Inversion seat (Munger lens)**
Start from the failure case and work backwards.
- Describe in concrete detail how this business is destroyed over ten years. Name the mechanism, not a vague risk category.
- Whose incentives govern outcomes here — management, distributors, regulators, employees? Where do those incentives diverge from shareholders'?
- Which cognitive traps make this specific stock attractive right now? Recent price action, a compelling story, social proof from respected holders, commitment from a prior position?
- What must be true for the bull case to work, and what is the probability that all of those things hold simultaneously?
- Where is the accounting doing work — revenue recognition, capitalized costs, adjustments that recur every single year despite being called one-time?
- Rate 1-5 on survivability (5 = very hard to kill).

**Safety seat (Graham lens)**
Assume the story is wrong and ask what is left.
- Balance sheet first: cash, total debt, maturity schedule, off-balance-sheet obligations, interest coverage. Can it survive two bad years without raising capital?
- Earnings quality: how do cash flows track reported earnings over five years? Persistent divergence is the finding.
- Valuation without growth assumptions — what is this worth on current earning power alone?
- Downside scenario: what does the business look like at trough margins and a trough multiple? How far below today's price is that?
- Margin of safety: state it as a percentage, and state plainly whether it exists.
- Rate 1-5 on margin of safety.

**Growth seat (Lynch lens)**
Understand the story and then price it.
- Classify the company: fast grower, stalwart, cyclical, turnaround, or asset play. The classification determines which metrics matter and what a fair multiple is.
- What is the growth engine — units, price, new markets, new products? Which is durable and which is a one-time step?
- How long is the runway? Show the arithmetic on market size and current penetration rather than citing a total addressable market figure.
- Growth at a reasonable price: relate the multiple to the sustainable growth rate. Be explicit that this heuristic breaks down for cyclicals and for very high or very low growth rates.
- Ground-level evidence: product reviews, hiring patterns, app rankings, store traffic, developer activity — whatever observable signal fits this business.
- Rate 1-5 on growth quality (durable and reasonably priced, not merely fast).

## Step 3 — Collect

Track arrival of the four reports and show the user progress as each lands, with two or
three headline findings from each. Wait for all four before proceeding.

## Step 4 — Cross-examination

**This step is the point of the council.** Four reports stapled together is a document;
four reports that have been forced to collide is an analysis.

The chair extracts **two or three genuine conflicts** — points where seats reached
opposing conclusions from the same evidence. For each one:

1. State the conflict as a question with a real answer (`Is the current multiple
   supported by the growth runway?`), not as a topic (`valuation`).
2. Quote the bull side: which seat, what evidence, what reasoning.
3. Quote the bear side: same.
4. **Press both sides.** Ask the optimistic seat for the strongest disconfirming
   evidence. Ask the skeptical seat what it is discounting that a fair reading would
   credit. Where the conflict turns on a checkable fact rather than a judgment, send a
   follow-up question to the relevant analyst and wait for the answer.
5. Rule — and be willing not to. If the evidence genuinely does not settle it, record
   it as **unresolved** and say what evidence would settle it.

| Conflict | Bull side (seat, evidence) | Bear side (seat, evidence) | Ruling | If unresolved: what would settle it |
|----------|---------------------------|---------------------------|--------|-------------------------------------|

An unresolved conflict is a legitimate and often the most valuable output. Averaging two
opposing views into a lukewarm middle destroys the information the disagreement carried.
Resist that.

Once cross-examination is complete, shut down the four analysts.

## Step 5 — Chair's synthesis

Write the report in this order:

**1. Verdict** — one paragraph. What the business is, what it is worth, what the council
concluded, and the confidence level. A reader who stops here should have the answer.

**2. Council scorecard**

| Seat | Dimension | Rating | Core finding |
|------|-----------|:------:|--------------|
| Quality | Business quality | /5 | |
| Inversion | Survivability | /5 | |
| Safety | Margin of safety | /5 | |
| Growth | Growth quality | /5 | |

Report the four ratings and their spread. **Do not average them.** A company rated 5/2/1/5
is a completely different proposition from one rated 3/3/3/3, and a single mean would
hide that. Where the spread is wide, that dispersion is the finding.

**3. The numbers** — key financial and operating figures, latest two years side by side,
each sourced.

**4. Cross-examination record** — the table from Step 4, in full.

**5. The case both ways** — five to seven points per side, retaining only arguments that
survived cross-examination. Mark unresolved conflicts explicitly.

**6. Pre-purchase gate** — run `skills/checklist.md` and report the pass/fail result.

**7. What to do** — a clear stance (buy / watch / pass) with the price range that would
change it, and the specific developments that would trigger a re-review in either
direction.

**8. Limits of this analysis** — evidence grade, what could not be verified, and where
the council was reasoning rather than measuring. Be concrete.

## Step 6 — Record

Save to `research/<COMPANY>/council-<YYYY-MM-DD>.md`.

Append a record to `memory/decisions/<COMPANY>.md` per `memory/decisions/README.md`:
date, the four ratings, the verdict, and the unresolved conflicts. The next review starts
from that record — which is what makes the next review a continuation rather than a
repetition.

---

## Standing rules

1. **Launch the four analysts in one message.** Sequential launches waste time and let
   later analysts anchor on earlier findings.
2. **The chair does not analyze during Steps 2-3.** The chair's job is cross-examination
   and synthesis, and doing analysis early biases both.
3. **Ratings are not averaged.** Ever. The spread carries information.
4. **Disagreement is preserved.** If the seats cannot be reconciled on the evidence, the
   report says so.
5. **Silence beats speculation.** "Insufficient evidence" is a finding. A framework
   filled in with plausible guesses looks like analysis and is worse than a blank.
6. **No position taken in advance.** Assemble the evidence, then let the conclusion
   follow. If the conclusion was obvious before the work started, the work was decorative.

> This skill produces research, not advice. See the disclaimer in README.md.
