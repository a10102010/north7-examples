# NORTH7 Examples

Ready-to-run trading agents and integrations powered by [NORTH7 Market Intelligence API](https://north7.ai).

## Trading Agent

**10 lines. Real signals. No configuration.**

```bash
pip install north7
export NORTH7_API_KEY=your_key
python trading-agent/agent.py
```

Get a free API key at [north7.ai/developers](https://north7.ai/developers) — 1,000 credits, no credit card.

## What's inside

| Example | Description |
|---------|-------------|
| [trading-agent/agent.py](trading-agent/agent.py) | Complete trading agent: risk → signals → AI analysis → BUY/SELL decision |
| [trading-agent/scanner.py](trading-agent/scanner.py) | Multi-asset scanner: stocks + commodities, ranked by score |
| [trading-agent/webhook_agent.py](trading-agent/webhook_agent.py) | Alert bot: Telegram/Slack notifications on high-score signals |
| [langchain/](langchain/) | LangChain tool integration |
| [crewai/](crewai/) | CrewAI agent crew |

## Links

- [API Documentation](https://north7.ai/developers)
- [Python SDK on PyPI](https://pypi.org/project/north7/)
- [MCP Server](https://smithery.ai/server/north7-agent-api)
