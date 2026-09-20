from typing import TypedDict, Annotated
from langgraph.graph import START, END, StateGraph
from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.types import interrupt,Command
from dotenv import load_dotenv
import sqlite3
import uuid
load_dotenv()

class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    agent_message: str
    approval_message: str
    #output: BaseMessage = None

llm = ChatOpenAI(model="gpt-5.4-mini")

def agent_node(input: State):
    print("Agent is determining the Eligibility if the refund")
    return {"agent_message": "Agent Approves the Refund because the order is eligible within refund period with allowed reason"}

def approval_node(input: State):
    print("Node Execution started with state: ", input)
    value = interrupt(f"As per the Agent analysis here: {input['agent_message']}, please approve the refund or not?")
    return {"approval_message": value}

def refund_node(input: State):
    print("Node Execution started with state: ", input)
    return {"messages": ToolMessage(content="Refund is approved", tool_call_id="refund_call")}

builder = StateGraph(State)
builder.add_node("agent", agent_node)
builder.add_node("approval", approval_node)
builder.add_node("refund", refund_node)
builder.add_edge(START, "agent")
builder.add_edge("agent", "approval")
builder.add_edge("approval", "refund")
builder.add_edge("refund", END)

conn = sqlite3.connect("checkpoint.db", check_same_thread=False)
memory = SqliteSaver(conn)

graph = builder.compile(checkpointer=memory)

#  generate a unique id
thread_id = str(uuid.uuid4()) # random uuid for the thread
thread_1 = {"configurable": {"thread_id": thread_id}}

output = graph.invoke({"messages": [HumanMessage(content="I want to refund the order")], "counter": 0}, thread_1)
print("--------------------------------")
print("Execution so far")
print(output)
print("--------------------------------")
result = graph.invoke(Command(resume="Accepted"), thread_1)
print(result)
print("--------------------------------")