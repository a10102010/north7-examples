"""NORTH7 + CrewAI: Market Analysis Crew"""
from north7 import North7Client
from crewai import Agent, Task, Crew
from crewai.tools import tool
import os

client = North7Client(api_key=os.environ["NORTH7_API_KEY"])

@tool("Risk Index")
def get_risk_index() -> dict:
    """Returns global market risk index 0-100 with active crises and market regime."""
    return client.risk()

@tool("Sector Radar")
def get_sector_radar() -> dict:
    """Returns breadth score for 11 US sectors with rotation signals."""
    return client.sector_radar()

@tool("Stock Analysis")
def analyze_stock(ticker: str) -> dict:
    """Returns AI analysis for a stock: fundamentals, technicals, sentiment, assessment."""
    return client.analysis(ticker)

analyst = Agent(
    role="Market Analyst",
    goal="Assess current market conditions and identify opportunities",
    backstory="Senior analyst with access to NORTH7 market intelligence.",
    tools=[get_risk_index, get_sector_radar, analyze_stock],
    verbose=True,
)

task1 = Task(
    description="Check the global risk index and sector rotation. Summarize the market environment in 3 sentences.",
    expected_output="Market summary with risk level and top/bottom sectors.",
    agent=analyst,
)

task2 = Task(
    description="Analyze AAPL and give a one-paragraph assessment.",
    expected_output="Stock assessment with key metrics.",
    agent=analyst,
)

crew = Crew(agents=[analyst], tasks=[task1, task2], verbose=True)
result = crew.kickoff()
print(result)
