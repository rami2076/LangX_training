# Import relevant functionality
from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

import getpass
import os

if not os.environ.get("ANTHROPIC_API_KEY"):
    os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("Enter API key for Anthropic: ")

if not os.environ.get("TAVILY_API_KEY"):
    os.environ["TAVILY_API_KEY"] = getpass.getpass("Enter API key for TAVILY: ")

print("################")
print("Loaded API Keys.")
print("################")

# Create the agent
memory = MemorySaver()
model = ChatAnthropic(model_name="claude-3-7-sonnet-latest")
search = TavilySearchResults(max_results=3)
tools = [search]
agent_executor = create_react_agent(model, tools, checkpointer=memory)

# Use the agent
# config = {"configurable": {"thread_id": "abc123"}}
config = {"configurable": {"thread_id": "abc1234"}}
for step in agent_executor.stream(
        {"messages": [HumanMessage(content="whats the weather where I live?")]},
        config,
        stream_mode="values",
):
    step["messages"][-1].pretty_print()
# for step in agent_executor.stream(
#         {"messages": [HumanMessage(content="I live in matsudo in Japan")]},
#         config,
#         stream_mode="values",
# ):
#     step["messages"][-1].pretty_print()
