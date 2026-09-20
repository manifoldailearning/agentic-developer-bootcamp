"""Concept 3: a schema plus a callable. Registration does not execute it."""
import json
from langchain_core.tools import tool
from langchain_core.utils.function_calling import convert_to_openai_tool
from demo_schema import ImpactInput
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage
load_dotenv()

@tool(args_schema=ImpactInput)
def calculate_incident_impact(failed_requests: int, total_requests: int, baseline_error_rate_pct: float) -> dict:
    """Calculate request failure percentage and percentage-point change from baseline.
    Use counts from the same observation window. This does not calculate unique users or severity.
    """
    rate = failed_requests / total_requests * 100
    return {"error_rate_pct": rate, "change_percentage_points": rate - baseline_error_rate_pct}


model = ChatOpenAI(model="gpt-5.4-mini").bind_tools([calculate_incident_impact])
#print(model.invoke("What is the impact of 60 failed requests out of 1200 total requests, with a baseline error rate of 2%?"))
messages = [HumanMessage(content="What is the impact of 60 failed requests out of 1200 total requests, with a baseline error rate of 2%?")]
output = model.invoke(messages)
print(output)
messages.append(output) # append the output to the messages
print("--------------------------------")
#print(model.invoke("Who is the best actor in the world?"))

# Observations
# 1. Model will propose (not actually call) the tool if it requires for the request
# 2. Model will never execute the tool directly
print(output.tool_calls)
print("--------------------------------")
# Have a hard limit
for call in output.tool_calls:
    print(f"Tool name: {call['name']}")
    print(f"Tool arguments: {call['args']}")
    print("--------------------------------")
    tool_result = calculate_incident_impact.invoke(call['args'])
    print(tool_result)
    print("--------------------------------")
messages.append(ToolMessage(content=tool_result, tool_call_id=call['id']))
output = model.invoke(messages)
print(output)

# Langgraph