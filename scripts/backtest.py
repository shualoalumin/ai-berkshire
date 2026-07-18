#!/usr/bin/env python3
"""backtest.py — 判断验证回测：把历史判断与真实股价结果对账。

发掘报告合并路线图 Phase 4。与 ai-hedge-fund 的"LLM 重放式回测"不同，
本工具验证的是**本仓库已经产生的真实判断**——实盘交易、团队分析结论——
在其后的真实市场表现，让"框架有效"从叙事变成可复算的数字。

数据哲学（与 momentum_backtest_v2.py 一脉相承）：
  行情 API 在部分环境不可用（代理/风控），因此**离线价格注入是一等公民**，
  在线拉取（Yahoo chart API）仅作为本地环境的便利通道。零外部依赖。

用法：
  # 模式一：从实盘记录自动提取买入信号（默认路径 实盘记录/实盘操作记录.md）
  python3 scripts/backtest.py --from-trades --prices prices.json

  # 模式二：自定义信号清单
  python3 scripts/backtest.py --signals signals.json --prices prices.json

  # 本地环境可尝试在线取现价（无代理限制时）
  python3 scripts/backtest.py --from-trades --online

signals.json 格式：
  [{"date": "2026-04-21", "ticker": "PDD", "action": "buy",
    "price": 103.66, "source": "实盘记录", "note": "首次建仓"}]
  action: buy（买入判断，涨=判断对） / pass（否决判断，跌=判断对）

prices.json 格式：
  {"asof": "2026-07-18",
   "current":    {"PDD": 85.88, "SPY": 743.29},
   "historical": {"SPY": {"2026-04-21": 705.00}}}   # 可选：基准的信号日价格
  historical 中给出基准（默认 SPY）信号日价格时，输出超额收益；否则只算绝对收益。
"""

import argparse
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRADES_MD = os.path.join(ROOT, "实盘记录", "实盘操作记录.md")
BENCHMARK = "SPY"

TICKER_RE = re.compile(r"\b([A-Z]{1,5})\b|(\d{4,6})\.(HK|SH|SZ)")
PRICE_RE = re.compile(r"\$?([0-9]+(?:\.[0-9]+)?)")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


def parse_trades(path):
    """从实盘操作记录的 Markdown 表格提取买入信号。"""
    signals = []
    if not os.path.exists(path):
        print(f"❌ 找不到实盘记录: {path}")
        return signals
    with open(path, encoding="utf-8") as f:
        for line in f:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 4 or not DATE_RE.match(cells[0]):
                continue
            date, target, action_cell, price_cell = cells[0], cells[1], cells[2], cells[3]
            if "买入" not in action_cell:
                continue  # 只回测直接买入；期权等复杂头寸价格口径不同，跳过
            m = TICKER_RE.search(target)
            if not m:
                continue
            ticker = m.group(1) or f"{m.group(2)}.{m.group(3)}"
            pm = PRICE_RE.search(price_cell)
            if not pm:
                print(f"⚠️  跳过 {date} {ticker}：无法解析价格「{price_cell}」")
                continue
            signals.append({
                "date": date, "ticker": ticker, "action": "buy",
                "price": float(pm.group(1)), "source": "实盘记录",
                "note": cells[6] if len(cells) > 6 else "",
            })
    return signals


def fetch_online(tickers):
    """本地环境便利通道：Yahoo chart API 取最新收盘价。受限环境会失败并提示离线模式。"""
    current = {}
    for t in tickers:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=5d&interval=1d"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as r:
                data = json.load(r)
            closes = data["chart"]["result"][0]["indicators"]["quote"][0]["close"]
            current[t] = next(c for c in reversed(closes) if c is not None)
        except Exception as e:
            print(f"⚠️  在线获取 {t} 失败（{e.__class__.__name__}）。"
                  f"请改用 --prices prices.json 离线注入价格。")
    return current


def run(signals, prices, asof):
    current = prices.get("current", {})
    historical = prices.get("historical", {})
    bench_now = current.get(BENCHMARK)

    rows, rets, excesses, wins = [], [], [], 0
    for s in signals:
        tk, entry = s["ticker"], s.get("price")
        now = current.get(tk)
        if now is None or entry is None:
            rows.append((s["date"], tk, s["action"], entry, "—", "—", "—", "缺价格"))
            continue
        ret = (now - entry) / entry * 100

        bench_entry = historical.get(BENCHMARK, {}).get(s["date"])
        if bench_entry and bench_now:
            bench_ret = (bench_now - bench_entry) / bench_entry * 100
            excess = ret - bench_ret
            excesses.append(excess)
            excess_s = f"{excess:+.1f}%"
        else:
            excess_s = "—"

        correct = ret > 0 if s["action"] == "buy" else ret < 0
        wins += correct
        rets.append(ret)
        rows.append((s["date"], tk, s["action"], f"{entry:.2f}", f"{now:.2f}",
                     f"{ret:+.1f}%", excess_s, "✅ 判断成立" if correct else "❌ 判断未成立"))

    print("=" * 78)
    print(f"判断验证回测  (截至 {asof}，基准 {BENCHMARK})")
    print("=" * 78)
    print(f"{'信号日':<11}{'标的':<9}{'判断':<6}{'入场价':>9}{'现价':>9}"
          f"{'收益':>9}{'超额':>9}  结果")
    print("-" * 78)
    for r in rows:
        print(f"{r[0]:<11}{r[1]:<9}{r[2]:<6}{str(r[3]):>9}{str(r[4]):>9}"
              f"{str(r[5]):>9}{str(r[6]):>9}  {r[7]}")
    print("-" * 78)

    n = len(rets)
    if n:
        print(f"  有效信号: {n}   判断成立率: {wins}/{n} ({wins / n * 100:.0f}%)   "
              f"平均收益: {sum(rets) / n:+.1f}%")
        if excesses:
            print(f"  平均超额收益(vs {BENCHMARK}): {sum(excesses) / len(excesses):+.1f}%")
        else:
            print(f"  超额收益: 未提供基准信号日价格（prices.json 的 historical.{BENCHMARK}），只算绝对收益")
    else:
        print("  无有效信号。")
    print("\n  ⚠️ 提醒：价值投资的验证周期以年计，短期回测结果≠框架有效性结论；")
    print("     样本少时尤其如此。本工具的意义是让每笔判断可对账，而非制造虚假精确。")
    return 0 if n else 1


def main():
    ap = argparse.ArgumentParser(description="判断验证回测")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--from-trades", action="store_true", help="从实盘记录提取买入信号")
    src.add_argument("--signals", help="信号清单 JSON 路径")
    ap.add_argument("--trades-file", default=TRADES_MD, help="实盘记录路径")
    ap.add_argument("--prices", help="离线价格 JSON 路径（推荐）")
    ap.add_argument("--online", action="store_true", help="尝试在线取现价（本地环境）")
    args = ap.parse_args()

    if args.from_trades:
        signals = parse_trades(args.trades_file)
    else:
        with open(args.signals, encoding="utf-8") as f:
            signals = json.load(f)
    if not signals:
        print("❌ 未提取到任何信号。")
        return 1

    prices, asof = {"current": {}, "historical": {}}, "在线最新"
    if args.prices:
        with open(args.prices, encoding="utf-8") as f:
            prices = json.load(f)
        asof = prices.get("asof", "未标注")
    elif args.online:
        tickers = sorted({s["ticker"] for s in signals} | {BENCHMARK})
        prices["current"] = fetch_online(tickers)
    else:
        print("❌ 需要 --prices 或 --online 之一提供现价。")
        return 1

    return run(signals, prices, asof)


if __name__ == "__main__":
    sys.exit(main())
