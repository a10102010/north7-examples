#!/usr/bin/env python3
"""
NORTH7 Multi-Asset Scanner — Scans all signals, ranks by score.

pip install north7
export NORTH7_API_KEY=your_key
python scanner.py
"""
from north7 import North7Client
from datetime import datetime, timezone

def run():
    client = North7Client()

    risk = client.risk()
    regime = client.regime()

    print("=" * 65)
    print("NORTH7 SCANNER — %s" % datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"))
    print("  Risk: %s (%s) | Regime: %s" % (risk.risk_index, risk.label, regime.regime))
    print("=" * 65)

    # Stock signals
    try:
        signals = client.signals()
        if signals:
            ranked = sorted(signals, key=lambda s: getattr(s, 'risk_score', 0) or 0, reverse=True)
            print("\n  STOCKS (top 5 by risk score)")
            print("  %-8s %-6s %5s  %s" % ("Ticker", "Action", "Score", "Name"))
            print("  " + "-" * 45)
            for s in ranked[:5]:
                print("  %-8s %-6s %5s  %s" % (
                    getattr(s, 'ticker', '?'),
                    getattr(s, 'action', getattr(s, 'direction', '?')),
                    getattr(s, 'risk_score', '?'),
                    getattr(s, 'name', '')[:25]
                ))
    except Exception as e:
        print("\n  Signals: %s" % str(e)[:50])

    # Commodity signals
    try:
        commodities = client.commodities()
        if commodities:
            ranked = sorted(commodities, key=lambda s: getattr(s, 'risk_score', 0) or 0, reverse=True)
            print("\n  COMMODITIES (top 5 by risk score)")
            print("  %-8s %-6s %5s  %s" % ("Ticker", "Action", "Score", "Name"))
            print("  " + "-" * 45)
            for s in ranked[:5]:
                print("  %-8s %-6s %5s  %s" % (
                    getattr(s, 'instrument', '?'),
                    getattr(s, 'action', getattr(s, 'direction', '?')),
                    getattr(s, 'risk_score', '?'),
                    getattr(s, 'commodity', '')[:25]
                ))
    except Exception as e:
        print("\n  Commodities: %s" % str(e)[:50])

    print("\n" + "=" * 65)

if __name__ == "__main__":
    run()
