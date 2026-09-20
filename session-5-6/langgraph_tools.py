import json
from langchain_core.tools import tool
from langchain_core.utils.function_calling import convert_to_openai_tool
from demo_schema import ImpactInput
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage, BaseMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt,Command
from langchain_community.tools import DuckDuckGoSearchRun
from typing import TypedDict, Annotated
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph import START, END, StateGraph
import sqlite3
import uuid
load_dotenv()

@tool(args_schema=ImpactInput)
def calculate_incident_impact(failed_requests: int, total_requests: int, baseline_error_rate_pct: float) -> dict:
    """Calculate request failure percentage and percentage-point change from baseline.
    Use counts from the same observation window. This does not calculate unique users or severity.
    """
    rate = failed_requests / total_requests * 100
    return {"error_rate_pct": rate, "change_percentage_points": rate - baseline_error_rate_pct}


TOOLS = [calculate_incident_impact, DuckDuckGoSearchRun()]

model = ChatOpenAI(model="gpt-5.4-mini").bind_tools(TOOLS) # bind both the tools

class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def assistant(state: State):
    return {"messages": [model.invoke(state["messages"])]}

builder = StateGraph(State)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(TOOLS))
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition) # tools ? : END
builder.add_edge("tools","assistant")
builder.add_edge("assistant", END)

graph = builder.compile(checkpointer=MemorySaver())

#  generate a unique id
thread_id = str(uuid.uuid4()) # random uuid for the thread
thread_1 = {"configurable": {"thread_id": thread_id}}

output = graph.invoke({"messages": [HumanMessage(content="What is the impact of 60 failed requests out of 1200 total requests, with a baseline error rate of 2%?")]}, thread_1)
print(output)
print("--------------------------------")
output = graph.invoke({"messages": [HumanMessage(content="What is the latest news on the stock market?")]}, thread_1)
print(output)
print("--------------------------------")
print(graph.get_graph().draw_ascii())