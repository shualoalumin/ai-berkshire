#!/usr/bin/env python3
"""ledger.py — score past judgments against what the market actually did.

A research process that never checks its own output is indistinguishable from one
that produces nothing. This reconciles recorded judgments — buy calls, passes —
against subsequent prices, and reports the hit rate, the average return, and the
excess over a benchmark.

It is deliberately unflattering. Every judgment goes in the ledger, including the
ones that were wrong, because a ledger that only records wins measures nothing.

Design note on data: price APIs are blocked in many sandboxed and corporate
environments, so **offline price injection is the primary mode**. Live fetching is
a convenience for local use, not a dependency. No third-party packages.

Usage
-----
  python3 scripts/ledger.py --signals signals.json --prices prices.json
  python3 scripts/ledger.py --signals signals.json --online

signals.json
------------
  [
    {"date": "2025-03-14", "ticker": "ACME", "action": "buy",  "price": 42.10,
     "source": "council", "note": "passed gate, 4/5 quality"},
    {"date": "2025-06-02", "ticker": "WIDG", "action": "pass", "price": 88.00,
     "source": "checklist", "note": "failed gate 5 — leverage"}
  ]

  action "buy"  -> the judgment was right if the price rose
  action "pass" -> the judgment was right if the price fell

prices.json
-----------
  {
    "asof": "2026-07-27",
    "current":    {"ACME": 51.30, "WIDG": 71.40, "SPY": 743.29},
    "historical": {"SPY": {"2025-03-14": 705.00, "2025-06-02": 719.50}}
  }

  Supplying benchmark prices at each signal date enables excess-return
  reporting. Without them the ledger reports absolute returns only.
"""

import argparse
import json
import sys
import urllib.request

BENCHMARK = "SPY"


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def fetch_live(tickers):
    """Convenience path for local runs. Fails loudly and suggests offline mode."""
    prices = {}
    for ticker in tickers:
        url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
               f"?range=5d&interval=1d")
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(request, timeout=15) as response:
                payload = json.load(response)
            closes = payload["chart"]["result"][0]["indicators"]["quote"][0]["close"]
            prices[ticker] = next(c for c in reversed(closes) if c is not None)
        except Exception as exc:
            print(f"  warn  live fetch failed for {ticker} ({type(exc).__name__}); "
                  f"use --prices to inject prices offline", file=sys.stderr)
    return prices


def score(signals, prices, asof):
    current = prices.get("current", {})
    historical = prices.get("historical", {})
    benchmark_now = current.get(BENCHMARK)

    rows = []
    buy_returns = []      # returns you would actually have earned
    buy_excesses = []     # those returns net of the benchmark
    pass_moves = []       # what the passes did afterwards, tracked separately
    scored = 0
    correct = 0

    for signal in signals:
        ticker = signal["ticker"]
        entry = signal.get("price")
        action = signal.get("action", "buy")
        now = current.get(ticker)

        if entry in (None, 0) or now is None:
            rows.append((signal["date"], ticker, action, entry, None, None, None,
                         "no price"))
            continue

        change = (now - entry) / entry * 100

        # Buy and pass calls are not commensurable. A pass that avoided a 19%
        # decline did not earn -19%; averaging the two together produces a
        # number that means nothing. Keep them in separate books.
        benchmark_then = historical.get(BENCHMARK, {}).get(signal["date"])
        excess = None
        if action == "buy":
            buy_returns.append(change)
            if benchmark_then and benchmark_now:
                benchmark_change = (benchmark_now - benchmark_then) / benchmark_then * 100
                excess = change - benchmark_change
                buy_excesses.append(excess)
        else:
            pass_moves.append(change)

        was_right = change > 0 if action == "buy" else change < 0
        scored += 1
        correct += was_right
        rows.append((signal["date"], ticker, action, entry, now, change, excess,
                     "right" if was_right else "wrong"))

    print("=" * 78)
    print(f"JUDGMENT LEDGER — prices as of {asof}, benchmark {BENCHMARK}")
    print("=" * 78)
    print(f"  {'date':<12}{'ticker':<9}{'call':<7}{'entry':>10}{'now':>10}"
          f"{'return':>10}{'excess':>10}  result")
    print("  " + "-" * 74)

    for date, ticker, action, entry, now, change, excess, result in rows:
        entry_s = f"{entry:,.2f}" if entry is not None else "-"
        now_s = f"{now:,.2f}" if now is not None else "-"
        change_s = f"{change:+.1f}%" if change is not None else "-"
        excess_s = f"{excess:+.1f}%" if excess is not None else "-"
        print(f"  {date:<12}{ticker:<9}{action:<7}{entry_s:>10}{now_s:>10}"
              f"{change_s:>10}{excess_s:>10}  {result}")

    print("  " + "-" * 74)

    if not scored:
        print("  No scorable judgments — every signal is missing a price.")
        return 1

    print(f"  scored {scored}   right {correct}/{scored} ({correct / scored * 100:.0f}%)")

    if buy_returns:
        print(f"  buy calls  ({len(buy_returns)}): average return "
              f"{sum(buy_returns) / len(buy_returns):+.1f}%")
        if buy_excesses:
            print(f"             average excess over {BENCHMARK}: "
                  f"{sum(buy_excesses) / len(buy_excesses):+.1f}% "
                  f"(on {len(buy_excesses)} of {len(buy_returns)})")
        else:
            print(f"             excess unavailable — add historical.{BENCHMARK} prices "
                  f"at each signal date")

    if pass_moves:
        print(f"  passes     ({len(pass_moves)}): average subsequent move "
              f"{sum(pass_moves) / len(pass_moves):+.1f}% "
              f"(negative means the decline was avoided)")

    print()
    print("  Read this carefully. A value process is judged over years, and a small")
    print("  sample of short holding periods says almost nothing about whether the")
    print("  method works. What this ledger does establish is that every judgment was")
    print("  recorded and scored, which is the part most processes skip.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Score past judgments against outcomes.")
    parser.add_argument("--signals", required=True, help="path to the signals JSON file")
    parser.add_argument("--prices", help="path to an offline prices JSON file (preferred)")
    parser.add_argument("--online", action="store_true",
                        help="attempt to fetch current prices (local use only)")
    args = parser.parse_args()

    signals = load(args.signals)
    if not signals:
        print("No signals in file.", file=sys.stderr)
        return 1

    if args.prices:
        prices = load(args.prices)
        asof = prices.get("asof", "unspecified")
    elif args.online:
        tickers = sorted({s["ticker"] for s in signals} | {BENCHMARK})
        prices = {"current": fetch_live(tickers), "historical": {}}
        asof = "live"
    else:
        print("Supply either --prices or --online.", file=sys.stderr)
        return 2

    return score(signals, prices, asof)


if __name__ == "__main__":
    sys.exit(main())
