"""NORTH7 + LangChain: Market Analysis Agent"""
from north7 import North7Client
from langchain_core.tools import tool
from langchain_anthropic import ChatAnthropic
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
import os

client = North7Client(api_key=os.environ["NORTH7_API_KEY"])

@tool
def get_risk_index() -> dict:
    """Returns global market risk index 0-100 with active crises and market regime."""
    return client.risk()

@tool
def get_sector_radar() -> dict:
    """Returns breadth score for 11 US sectors with rotation signals."""
    return client.sector_radar()

@tool
def analyze_stock(ticker: str) -> dict:
    """Returns AI analysis for a stock: fundamentals, technicals, sentiment, assessment."""
    return client.analysis(ticker)

tools = [get_risk_index, get_sector_radar, analyze_stock]
llm = ChatAnthropic(model="claude-haiku-4-5-20251001")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a market analyst. Use the tools to assess current market conditions."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])
agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
result = executor.invoke({"input": "Check the current market risk, analyze the tech sector, and give me a quick take on AAPL."})
print(result["output"])
