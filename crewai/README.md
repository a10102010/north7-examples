# NORTH7 + CrewAI — Market Analysis Crew

Get AI-powered market analysis via the NORTH7 API with CrewAI agents.

## Setup
pip install north7 crewai crewai-tools

## Quick Start
export NORTH7_API_KEY=n7_live_...      # Get free at https://north7.ai/api
export OPENAI_API_KEY=sk-...           # CrewAI default LLM
python crew.py

## What it does
A one-agent crew that:
1. Checks the global risk index and sector rotation
2. Analyzes a specific stock (AAPL)
3. Summarizes findings across both tasks

## x402 Payment (optional)
For pay-per-call without API key, set a Base wallet:
export WALLET_PRIVATE_KEY=0x...
