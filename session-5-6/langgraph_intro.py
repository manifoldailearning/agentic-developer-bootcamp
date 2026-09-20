from typing import TypedDict
from langgraph.graph import START, END, StateGraph
from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

class State(TypedDict):
    messages: BaseMessage
    counter: int = 0
    output: BaseMessage = None

llm = ChatOpenAI(model="gpt-5.4-mini")

# define node
def call_llm(input: State):
    output = llm.invoke(input["messages"])
    count = input.get("counter", 0) + 1
    # bad practice
    # input["counter"] = count #  not a good practice to mutate the input
    # input["output"] = output #  not a good practice to mutate the input
    return {"output": output, "counter": count} # good practice to return a new state

builder = StateGraph(State)
builder.add_node("call_llm", call_llm)

# define the connections
builder.add_edge(START, "call_llm")
builder.add_edge("call_llm", END)

# compile the graph
graph = builder.compile()

# run the graph
output = graph.invoke({"messages": [HumanMessage(content="What is the capital of France?")],
"counter": 0})
print(output)