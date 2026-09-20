from typing import TypedDict, Annotated
from langgraph.graph import START, END, StateGraph
from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
checkpoint = MemorySaver()
import uuid
load_dotenv()

class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    counter: int = 0
    #output: BaseMessage = None

llm = ChatOpenAI(model="gpt-5.4-mini")

# define node
def call_llm(input: State):
    output = llm.invoke(input["messages"])
    count = input.get("counter", 0) + 1
    # bad practice
    # input["counter"] = count #  not a good practice to mutate the input
    # input["output"] = output #  not a good practice to mutate the input
    # input["messages"].append(output) # not a good practice to mutate the input
    return {"messages": output, "counter": count} # good practice to return a new state

builder = StateGraph(State)
builder.add_node("call_llm", call_llm)

# define the connections
builder.add_edge(START, "call_llm")
builder.add_edge("call_llm", END)

# compile the graph
graph = builder.compile(checkpointer=checkpoint)

#
#  generate a unique id
thread_id = str(uuid.uuid4()) # random uuid for the thread
thread_1 = {"configurable": {"thread_id": thread_id}}

# run the graph
output = graph.invoke({"messages": [HumanMessage(content="Who is PM of India?")],
"counter": 0}, thread_1)
print(output)
print("--------------------------------")
get_state = graph.get_state(thread_1)
print(get_state)
print("--------------------------------")
# run the graph
output = graph.invoke({"messages": [HumanMessage(content="What is his age?")],
"counter": 0}, thread_1)
print(output)