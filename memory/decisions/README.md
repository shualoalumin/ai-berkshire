# Decision Memory

A running record of what the council concluded about each company, so that the next
review starts from the last one instead of from nothing.

## The problem this solves

Research without memory repeats itself. The same three failures recur:

- A company is analyzed again six months later and the prior reasoning is never checked
  against what happened.
- A business rejected on valuation is rediscovered and re-argued from scratch, complete
  with the same debate.
- Positions are taken and closed, and nothing about the outcome flows back into how the
  next company is analyzed.

The individual analyses can all be excellent and the process still learns nothing.

## Layout

```
memory/decisions/
├── README.md         this file — the contract
└── <COMPANY>.md      one append-only file per company, newest entry first
```

Company files are gitignored by default. This record is personal and often contains
positions; publish it deliberately or not at all.

## Entry format

Newest first. Append, never rewrite — an edited record cannot show you where your
judgment drifted.

```markdown
## 2026-07-27 · council

**Ratings**: quality 4/5 · survivability 3/5 · safety 2/5 · growth 4/5
**Verdict**: Good business, demanding price. Watch below $XX.

**Unresolved conflicts**
| Conflict | Bull side | Bear side | Ruling |
|----------|-----------|-----------|--------|
| Does the runway support the multiple? | Growth seat: penetration at 12% | Safety seat: needs 9 years of 20% | Unresolved — settled by FY27 cohort data |

**Assumptions carried forward**
1. Incremental ROIC stays above 15%
2. Gross margin holds above 60%

**Back-check on the previous entry**
- 2026-01: "distribution advantage is widening" -> confirmed; competitor exited two markets
- 2026-01: "margin expansion continues" -> weakened; margin flat for two quarters

---
```

The **back-check** is the part that matters. Everything else is a summary; the back-check
is the only field that measures your judgment rather than restating it.

## When to write

| Trigger | Skill | What gets recorded |
|---------|-------|--------------------|
| Council review completes | `council.md` | Ratings, verdict, unresolved conflicts |
| Gate is run | `checklist.md` | Pass or the gate that failed, and why |
| Thesis established | `thesis.md` A6 | Thesis summary, assumptions, red lines |
| Thesis reviewed | `thesis.md` B8 | Health score, assumption changes, back-check |
| Material price move | `pulse.md` | Anything classified above "repricing" |

Record rejections as carefully as purchases. Whether your passes were right is a real
question about your process, and the only way to answer it is to have written them down.

## When to read

Every analytical skill checks this directory before starting work. If a record exists,
the review opens by stating what was concluded last time and what has changed since.

**The rule that makes this useful:** memory is not for reusing conclusions. It is for
forcing the question *what changed?* If a review six months later reaches the same
conclusion with no new evidence, that is not consistency — it is a process that has
stopped looking. Say so in the report.

## Relationship to other records

Three different records, three different jobs. None substitutes for another.

| Record | Answers | Written when |
|--------|---------|--------------|
| `memory/decisions/<COMPANY>.md` | What did the analysis conclude, and was it right? | Every analytical skill run |
| `research/<COMPANY>/thesis.md` | Why do I own this, and what would make me sell? | At purchase, reviewed quarterly |
| `signals.json` → `scripts/ledger.py` | What did the judgments actually return? | When judgments are scored |

Together they close the loop: analysis produces a judgment, the judgment produces a
thesis, the thesis produces an outcome, and the outcome feeds back into the next
analysis. Each piece alone is a document; connected, they are a process that can improve.
