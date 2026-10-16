#!/usr/bin/env python3
"""
NORTH7 Trading Agent — Ready to run.

pip install north7
export NORTH7_API_KEY=your_key
python agent.py
"""
from north7 import North7Client
from datetime import datetime, timezone

def run():
    client = North7Client()  # uses NORTH7_API_KEY env var

    # 1. Market context
    risk = client.risk()
    regime = client.regime()

    print("=" * 50)
    print("NORTH7 TRADING AGENT — %s" % datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"))
    print("=" * 50)
    print()
    print("MARKET CONTEXT")
    print("  Risk Index:  %s/100 (%s)" % (risk.risk_index, risk.label))
    print("  Regime:      %s" % regime.regime)
    print()

    # 2. Get signals
    try:
        signals = client.signals()
    except Exception as e:
        print("  Signals require API key: %s" % str(e)[:60])
        print("  Get one free at north7.ai/developers")
        return

    if not signals:
        print("  No active signals right now. Check back later.")
        return

    # 3. Pick the best signal (highest risk score)
    best = max(signals, key=lambda s: getattr(s, 'risk_score', 0) or 0)

    print("TOP SIGNAL")
    print("  Asset:       %s" % (getattr(best, 'name', None) or getattr(best, 'ticker', '?')))
    print("  Direction:   %s" % (getattr(best, 'direction', None) or getattr(best, 'action', '?')))
    print("  Risk Score:  %s/100" % getattr(best, 'risk_score', '?'))
    print()

    # 4. AI analysis on the top pick
    ticker = getattr(best, 'ticker', None) or getattr(best, 'symbol', None)
    if ticker:
        try:
            analysis = client.analysis(ticker)
            print("AI ANALYSIS")
            if hasattr(analysis, 'summary') and analysis.summary:
                print("  %s" % analysis.summary[:300])
            elif hasattr(analysis, 'reasoning') and analysis.reasoning:
                print("  %s" % analysis.reasoning[:300])
            print()
        except:
            pass

    # 5. Decision
    direction = getattr(best, 'direction', '') or getattr(best, 'action', '') or ''
    score = getattr(best, 'risk_score', 0) or 0

    if score >= 70 and direction.upper() in ('BUY', 'LONG', 'UP'):
        print("DECISION: BUY %s (score %d)" % (ticker, score))
    elif score >= 70 and direction.upper() in ('SELL', 'SHORT', 'DOWN'):
        print("DECISION: SELL %s (score %d)" % (ticker, score))
    else:
        print("DECISION: HOLD (score %d, wait for stronger signal)" % score)

    print("=" * 50)

if __name__ == "__main__":
    run()
