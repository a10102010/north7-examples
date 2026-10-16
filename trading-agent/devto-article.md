---
title: Build a Trading Agent in 10 Lines of Python
published: true
description: A ready-to-run AI trading agent that scans 80+ assets, checks geopolitical risk, and makes BUY/SELL decisions — powered by real market data.
tags: python, ai, trading, api
cover_image:
---

Last month, my AI agent told me to buy Sugar futures. Three weeks later: **+16.5%**.

I didn't write a single line of trading logic. The agent did everything — checked geopolitical risk, analyzed weather anomalies in Brazil, cross-referenced USDA crop data, and decided to go long. I just ran the script.

Here's how to build the same agent in 10 lines of Python.

## The Agent

```python
from north7 import North7Client

client = North7Client()  # free: no key needed for risk/regime
risk = client.risk()
regime = client.regime()

print(f"Risk: {risk.risk_index}/100 ({risk.label})")
print(f"Regime: {regime.regime}")

signals = client.signals()  # needs API key
best = max(signals, key=lambda s: s.risk_score or 0)
print(f"Top signal: {best.ticker} {best.action} (score {best.risk_score})")
```

That's it. Install with `pip install north7`, run it, get a trading decision.

## What it actually does

Behind those 10 lines, the API scans **80+ assets** across stocks, commodities, crypto, and forex. It pulls from:

- **70+ data sources** in 30+ languages
- **NOAA weather data** (drought, flooding, harvest impact)
- **USDA crop reports** and EIA energy stats
- **Geopolitical intelligence** (sanctions, trade wars, conflicts)
- **Technical momentum** and sector rotation

The Risk Index (0-100) tells you how dangerous the market is right now. The Regime (BULL/BEAR/SIDEWAYS/CRISIS) tells you the trend. Signals tell you what to trade.

## The full agent

The [complete trading agent](https://github.com/a10102010/north7-examples/tree/master/trading-agent) adds AI analysis and decision logic:

```python
from north7 import North7Client

client = North7Client()

# 1. Market context
risk = client.risk()
regime = client.regime()

# 2. Get signals + pick the best
signals = client.signals()
best = max(signals, key=lambda s: s.risk_score or 0)

# 3. AI deep-dive on the top pick
analysis = client.analysis(best.ticker)

# 4. Decision
if best.risk_score >= 70 and best.action == "BUY":
    print(f"BUY {best.ticker} — {analysis.summary[:200]}")
elif best.risk_score >= 70 and best.action == "SELL":
    print(f"SELL {best.ticker}")
else:
    print("HOLD — no strong signal")
```

## Run it as a cron job

```bash
# Every morning at 08:00 UTC
0 8 * * * python agent.py >> trades.log 2>&1
```

Or as a **webhook agent** that sends Telegram alerts:

```python
from north7 import North7Client
import requests, time

client = North7Client()

while True:
    signals = client.signals()
    for s in signals:
        if s.risk_score >= 75:
            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                data={"chat_id": CHAT, "text": f"🔔 {s.action} {s.ticker} (score {s.risk_score})"})
    time.sleep(300)  # check every 5 min
```

## Free endpoints (no API key)

You can start without signing up:

```bash
# Risk Index — how dangerous is the market right now?
curl https://north7.ai/v1/risk

# Market Regime — BULL, BEAR, SIDEWAYS, or CRISIS?
curl https://north7.ai/v1/regime
```

For signals and analysis, [get a free API key](https://north7.ai/developers) — 1,000 credits, no credit card.

## MCP for AI agents

If you're building with Claude, GPT, or any LLM that supports [Model Context Protocol](https://modelcontextprotocol.io):

```json
{
  "mcpServers": {
    "north7": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-remote", "https://north7.ai/v1/mcp"]
    }
  }
}
```

Your AI agent can now call `get_risk_index()`, `get_signals()`, `get_analysis()` etc. as tools.

## Why this works

Most financial APIs give you raw data — price feeds, candlesticks, order books. You still need to build the logic that turns data into decisions.

NORTH7 gives you **decision-ready signals**. The AI has already analyzed the data, cross-referenced sources, and assigned confidence scores. Your agent just needs to act on them.

The Sugar trade? The agent spotted a +174% rainfall anomaly in São Paulo (threatening Brazil's harvest) combined with -99% precipitation in India. It cross-referenced historical patterns and found that similar setups led to +8-16% moves within 3 weeks. The signal came out at $17.40. Sugar hit $20.27.

## Get started

```bash
pip install north7
```

- [GitHub: ready-to-run examples](https://github.com/a10102010/north7-examples)
- [API Documentation](https://north7.ai/developers)
- [Python SDK on PyPI](https://pypi.org/project/north7/)

---

*Built by [NORTH7](https://north7.ai) — AI Trading Intelligence from Vienna, Austria.*
