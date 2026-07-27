#!/usr/bin/env python3
"""rigor.py — exact arithmetic for valuation work.

Mental arithmetic and prose arithmetic are both unauditable, and a single wrong
figure discredits every conclusion built on top of it. Run the numbers here and
paste the output into the report as the verification record.

Everything uses Decimal. Binary floating point is the wrong tool for money: it
cannot represent most decimal fractions exactly, and the error is invisible until
it is embarrassing.

No third-party dependencies.

Commands
--------
  market-cap    Verify a reported market capitalization against price x shares
  multiples     P/E, P/B, earnings yield, dividend yield from first principles
  scenarios     Bear / base / bull outcomes with explicit assumptions
  cross-check   Compare figures from independent sources against tolerance bands

Examples
--------
  python3 tools/rigor.py market-cap --price 178.50 --shares 1.52e9 --reported 271.3e9
  python3 tools/rigor.py multiples --price 178.50 --eps 8.42 --bvps 31.10 --dps 1.20
  python3 tools/rigor.py scenarios --price 178.50 --eps 8.42 \
      --growth 0.03 0.08 0.14 --exit-pe 12 18 25 --years 5
  python3 tools/rigor.py cross-check --label "FY25 revenue" --values 12.41e9 12.37e9
"""

import argparse
import sys
from decimal import Decimal, getcontext, InvalidOperation

getcontext().prec = 28

# Cross-validation tolerance bands. Kept here so every caller uses the same
# thresholds as skills/data-standards.md documents.
AGREEMENT = Decimal("0.01")   # <= 1% : sources agree
CAUTION = Decimal("0.05")     # <= 5% : usable with the gap disclosed


def dec(value):
    """Parse a Decimal, accepting scientific notation like 1.52e9."""
    try:
        return Decimal(str(value))
    except InvalidOperation:
        raise argparse.ArgumentTypeError(f"not a number: {value!r}")


def money(value, places=2):
    """Human-scaled money: 271_300_000_000 -> '271.30B'."""
    v = Decimal(value)
    sign = "-" if v < 0 else ""
    v = abs(v)
    for cutoff, suffix in ((Decimal("1e12"), "T"), (Decimal("1e9"), "B"),
                           (Decimal("1e6"), "M"), (Decimal("1e3"), "K")):
        if v >= cutoff:
            return f"{sign}{(v / cutoff):,.{places}f}{suffix}"
    return f"{sign}{v:,.{places}f}"


def pct(value, places=1):
    return f"{Decimal(value) * 100:.{places}f}%"


def gap(a, b):
    """Relative difference between two figures, using the first as the base."""
    a, b = Decimal(a), Decimal(b)
    if a == 0:
        return None
    return abs(a - b) / abs(a)


def verdict(discrepancy):
    """Map a discrepancy onto the tolerance bands from data-standards.md."""
    if discrepancy is None:
        return "cannot compare (base is zero)"
    if discrepancy <= AGREEMENT:
        return "AGREEMENT — sources consistent, use the higher-tier figure"
    if discrepancy <= CAUTION:
        return "CAUTION — report both figures and the reason for the gap"
    return "REJECT — resolve against the primary filing before using"


def rule(title):
    print("=" * 66)
    print(title)
    print("=" * 66)


# --------------------------------------------------------------------------- #
# market-cap
# --------------------------------------------------------------------------- #

def cmd_market_cap(args):
    computed = args.price * args.shares
    rule("MARKET CAPITALIZATION CHECK")
    print(f"  Share price        {args.price:,.4f} {args.currency}")
    print(f"  Shares outstanding {money(args.shares, 4)}")
    print(f"  Computed           {money(computed)} {args.currency}")

    if args.reported is None:
        print("\n  No reported figure supplied — nothing to verify against.")
        return 0

    d = gap(computed, args.reported)
    print(f"  Reported           {money(args.reported)} {args.currency}")
    print(f"  Discrepancy        {pct(d, 2) if d is not None else 'n/a'}")
    print(f"\n  {verdict(d)}")
    if d is not None and d > CAUTION:
        print("  Common causes: ADR ratio, share class excluded, stale share count,")
        print("                 basic vs diluted, or a currency mismatch.")
    return 0 if (d is not None and d <= CAUTION) else 1


# --------------------------------------------------------------------------- #
# multiples
# --------------------------------------------------------------------------- #

def cmd_multiples(args):
    rule("VALUATION MULTIPLES")
    print(f"  Price              {args.price:,.4f}")

    if args.eps is not None and args.eps != 0:
        pe = args.price / args.eps
        print(f"  EPS                {args.eps:,.4f}")
        print(f"  P/E                {pe:,.2f}x")
        print(f"  Earnings yield     {pct(args.eps / args.price, 2)}")
        if args.eps < 0:
            print("    (negative earnings — P/E carries no meaning here)")
    if args.bvps is not None and args.bvps != 0:
        print(f"  Book value/share   {args.bvps:,.4f}")
        print(f"  P/B                {(args.price / args.bvps):,.2f}x")
    if args.dps is not None:
        print(f"  Dividend/share     {args.dps:,.4f}")
        print(f"  Dividend yield     {pct(args.dps / args.price, 2)}")
        if args.eps is not None and args.eps > 0:
            print(f"  Payout ratio       {pct(args.dps / args.eps, 1)}")

    print("\n  A multiple is a compression of assumptions, not a valuation.")
    print("  Two businesses at the same P/E can be priced very differently.")
    return 0


# --------------------------------------------------------------------------- #
# scenarios
# --------------------------------------------------------------------------- #

def compound(base, rate, years):
    """base * (1 + rate) ** years, exactly, for integer years."""
    factor = Decimal(1)
    for _ in range(years):
        factor *= (Decimal(1) + rate)
    return base * factor


def cagr(start, end, years):
    """Annualized rate from start to end over `years`, via Decimal ln/exp."""
    if start <= 0 or end <= 0:
        return None
    return ((end / start).ln() / Decimal(years)).exp() - Decimal(1)


def cmd_scenarios(args):
    if len(args.growth) != 3 or len(args.exit_pe) != 3:
        print("error: --growth and --exit-pe each need exactly 3 values "
              "(bear base bull)", file=sys.stderr)
        return 2

    rule(f"SCENARIOS — {args.years} year horizon")
    print(f"  Entry price {args.price:,.4f}   Starting EPS {args.eps:,.4f}\n")
    header = (f"  {'':<7}{'growth':>9}{'exit P/E':>10}{'EPS in ' + str(args.years):>12}"
              f"{'value':>12}{'total':>10}{'annualized':>12}")
    print(header)
    print("  " + "-" * (len(header) - 2))

    names = ("bear", "base", "bull")
    values = []
    for name, g, pe in zip(names, args.growth, args.exit_pe):
        future_eps = compound(args.eps, g, args.years)
        value = future_eps * pe
        values.append(value)
        total = (value / args.price) - Decimal(1) if args.price else None
        annual = cagr(args.price, value, args.years)
        print(f"  {name:<7}{pct(g):>9}{pe:>9,.1f}x{future_eps:>12,.2f}"
              f"{value:>12,.2f}{pct(total):>10}"
              f"{(pct(annual) if annual is not None else 'n/a'):>12}")

    spread = max(values) - min(values)
    print(f"\n  Value range {min(values):,.2f} to {max(values):,.2f} "
          f"(spread {spread:,.2f}, {pct(spread / args.price)} of entry price)")
    print("\n  The assumptions above are the valuation. A wide spread is not")
    print("  a defect in the model — it is the honest width of what you know.")
    return 0


# --------------------------------------------------------------------------- #
# cross-check
# --------------------------------------------------------------------------- #

def cmd_cross_check(args):
    if len(args.values) < 2:
        print("error: --values needs at least 2 figures to compare", file=sys.stderr)
        return 2

    rule(f"CROSS-VALIDATION — {args.label}")
    base = args.values[0]
    labels = args.sources or [f"source {i + 1}" for i in range(len(args.values))]
    if len(labels) != len(args.values):
        print("error: --sources count must match --values count", file=sys.stderr)
        return 2

    worst = Decimal(0)
    for label, v in zip(labels, args.values):
        d = gap(base, v)
        marker = "  (base)" if v is base else ""
        shown = pct(d, 2) if d is not None else "n/a"
        if d is not None:
            worst = max(worst, d)
        print(f"  {label:<24}{money(v, 4):>18}{shown:>10}{marker}")

    print(f"\n  Worst discrepancy  {pct(worst, 2)}")
    print(f"  {verdict(worst)}")
    if worst > AGREEMENT:
        print("\n  Diagnose before discarding — see skills/data-standards.md:")
        print("  GAAP vs adjusted, fiscal calendar, currency, consolidation,")
        print("  restatement, share-count basis, or a stale source.")
    return 0 if worst <= CAUTION else 1


# --------------------------------------------------------------------------- #

def main():
    ap = argparse.ArgumentParser(
        description="Exact arithmetic for valuation work.",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)

    p = sub.add_parser("market-cap", help="verify market cap against price x shares")
    p.add_argument("--price", type=dec, required=True)
    p.add_argument("--shares", type=dec, required=True, help="total shares, e.g. 1.52e9")
    p.add_argument("--reported", type=dec, help="market cap as reported elsewhere")
    p.add_argument("--currency", default="USD")
    p.set_defaults(func=cmd_market_cap)

    p = sub.add_parser("multiples", help="P/E, P/B, yields from first principles")
    p.add_argument("--price", type=dec, required=True)
    p.add_argument("--eps", type=dec)
    p.add_argument("--bvps", type=dec, help="book value per share")
    p.add_argument("--dps", type=dec, help="dividend per share")
    p.set_defaults(func=cmd_multiples)

    p = sub.add_parser("scenarios", help="bear / base / bull with stated assumptions")
    p.add_argument("--price", type=dec, required=True)
    p.add_argument("--eps", type=dec, required=True)
    p.add_argument("--growth", type=dec, nargs=3, required=True,
                   metavar=("BEAR", "BASE", "BULL"), help="annual rates, e.g. 0.03 0.08 0.14")
    p.add_argument("--exit-pe", type=dec, nargs=3, required=True,
                   metavar=("BEAR", "BASE", "BULL"))
    p.add_argument("--years", type=int, default=5)
    p.set_defaults(func=cmd_scenarios)

    p = sub.add_parser("cross-check", help="compare independent sources")
    p.add_argument("--label", default="figure", help="what is being compared")
    p.add_argument("--values", type=dec, nargs="+", required=True,
                   help="first value is the base for comparison")
    p.add_argument("--sources", nargs="+", help="optional source names, in the same order")
    p.set_defaults(func=cmd_cross_check)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
