# Vision

Where this project is going, and what has to be true before each step.

---

## What this is

A research system, not a signal generator. It does not predict prices. It enforces a
process: understand the business, judge the advantage, examine management, demand a margin
of safety, write down what would prove you wrong, and then check afterwards whether you
were right.

The scarce thing in investing is not information — that has been free and abundant for
years. It is **discipline applied consistently over long periods**, which is precisely
what humans are worst at and what a well-designed tool can genuinely help with.

## What makes it different

There are open-source projects that assign investing personas to language models, and
projects that run structured agent debates. This one is built around three choices that
are unusual in combination:

**Disagreement is an output, not a defect.** Most multi-agent systems reconcile their
agents into a single recommendation. That reconciliation is where the information dies. A
company that is excellent on quality and terrible on margin of safety is a specific,
actionable situation; a 3.2 out of 5 is not.

**The process is a gate, not a scorer.** The checklist is designed so most candidates fail
early. Systems that always produce a rating always produce a reason to act, and acting is
usually the mistake.

**Judgments are scored.** `scripts/ledger.py` exists so that claims about this system can
eventually be checked rather than asserted. Wrong calls go in the ledger with the right
ones.

## Distribution

Two paths, which can run in parallel.

### Plugin (available now)

```
/plugin marketplace add shualoalumin/value-council
```

Free and open source. The purpose is reach and feedback, not revenue. Issues from real
users will find the weaknesses in these skills faster than any amount of internal review.

While the project iterates, `plugin.json` deliberately omits `version`, so installs track
the git commit and every push reaches users. At the first stable release, pin a semantic
version and start a changelog.

### Hosted service (later)

The same skills deployed as a managed agent behind an API, for users who want the research
without installing a developer tool. This requires: an agent definition, deployment
tooling, usage metering, and a front end. It should not be started until the free tier has
demonstrated that people actually want this.

## Revenue, if it goes that way

| Tier | What it is | Precondition |
|------|-----------|--------------|
| **Free** | The plugin, all ten skills, the tools | Available now |
| **Research** | Published reports, tracked theses, the public ledger | Enough reports to be worth subscribing to |
| **Hosted** | The API service above | Free tier proves demand |
| **Institutional** | Private data sources, custom lenses, white label | A hosted service with real users |

Order matters. Free reach, then a credible ledger, then anything paid. Charging before
there is a track record inverts the sequence and produces a product that has to be sold
rather than one people want.

## Trust

This product is only worth anything if its output can be trusted, which means the
infrastructure for trust comes before the infrastructure for revenue.

1. **Publish the ledger, including the losses.** A public record showing a 50% hit rate is
   worth more than a marketing claim of 90%, because one of them can be checked.
2. **Enforce the sourcing rules mechanically.** `scripts/check.py` gates the repository;
   `skills/data-standards.md` gates the research.
3. **Keep the disclaimer everywhere and mean it.** This produces research and education,
   never advice.
4. **Stay on the right side of the regulatory line.** Publishing research methodology and
   educational tooling is very different from providing personalized investment
   recommendations for compensation, which is a regulated activity in essentially every
   jurisdiction. Before any paid tier that could be construed as advice, get a legal
   opinion for the relevant jurisdictions. The safe products are the methodology and the
   tooling — do not drift into individualized buy and sell instructions for money without
   that opinion in hand.

## Near-term

- [ ] Publish the plugin and verify the install path end to end
- [ ] Run the council on real companies; fix what breaks in practice
- [ ] Start the ledger with actual judgments and score it quarterly
- [ ] Add a worked example to the README once one exists that is honest
- [ ] Consider a `research/` template so output formatting is consistent

## Non-goals

- Price prediction, technical analysis, or anything with a holding period under a year
- Automated trading, or any execution capability
- Portfolio optimization by statistical correlation — shared dependency is the thing that
  matters, and it is not in the covariance matrix
- Volume. Ten skills that work beat thirty that mostly do

---

> This document describes intent, not commitments or timelines.
