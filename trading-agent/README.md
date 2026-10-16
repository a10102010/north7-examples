# NORTH7 Trading Agent

A ready-to-run AI trading agent powered by [NORTH7 Market Intelligence](https://north7.ai).

**10 lines of code. Real signals. No configuration.**

## What it does

Every run, the agent:
1. Checks the **Risk Index** (0-100) — how dangerous is the market?
2. Reads the **Regime** (BULL/BEAR/SIDEWAYS) — what's the trend?
3. Scans **Trading Signals** — which assets have momentum?
4. Analyzes the best signal with **AI** — should you buy?
5. Outputs a clear **BUY / SELL / HOLD** decision with reasoning

## Quick Start

```bash
pip install north7
export NORTH7_API_KEY=your_key  # get one free at north7.ai/developers
python agent.py
```

## Get a Free API Key

1. Go to [north7.ai/developers](https://north7.ai/developers)
2. Click "Get Started Free"
3. Get 1,000 free credits (no credit card)

## Example Output

```
═══════════════════════════════════════════════
NORTH7 TRADING AGENT — 2026-10-16 08:00 UTC
═══════════════════════════════════════════════

MARKET CONTEXT
  Risk Index:  72/100 (ELEVATED)
  Regime:      BULL (VIX 16.87)

TOP SIGNAL
  Asset:       Sugar (SB)
  Direction:   BUY
  Risk Score:  79/100
  Confidence:  HIGH

AI ANALYSIS
  Weather anomaly in Brazil (+174% rain vs normal)
  threatens harvest. India drought (-99% precipitation).
  Historical pattern: similar setups led to +8-16% moves
  within 3 weeks.

DECISION: BUY SB
  Entry:  21.06
  Stop:   19.80 (-6%)
  Target: 22.70 (+8%)
═══════════════════════════════════════════════
```

## Run as a Cron Job

```bash
# Every day at 08:00 UTC
0 8 * * * cd /path/to/trading-agent && python agent.py >> agent.log 2>&1
```

## Advanced: Multi-Asset Scanner

```bash
python scanner.py  # scans all signals, ranks by score, outputs top 5
```

## Advanced: Webhook Alerts

```bash
python webhook_agent.py  # sends Telegram/Slack alerts on new signals
```

## License

MIT — use it, modify it, profit from it.

## Links

- [NORTH7 API Docs](https://north7.ai/developers)
- [Python SDK](https://pypi.org/project/north7/)
- [MCP Server](https://smithery.ai/server/north7-agent-api)
