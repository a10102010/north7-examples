# NORTH7 + LangChain — Stock Analysis Agent

Get AI-powered market analysis via the NORTH7 API in under 2 minutes.

## Setup
pip install north7 langchain langchain-anthropic

## Quick Start
export NORTH7_API_KEY=n7_live_...      # Get free at https://north7.ai/api
export ANTHROPIC_API_KEY=sk-ant-...    # Your Claude key
python agent.py

## What it does
The agent uses NORTH7's market data tools to:
1. Check the global risk index
2. Get sector breadth data
3. Analyze a specific stock
4. Summarize findings

## x402 Payment (optional)
For pay-per-call without API key, set a Base wallet:
export WALLET_PRIVATE_KEY=0x...
python agent_x402.py
