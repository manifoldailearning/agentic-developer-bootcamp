import json
from langchain_core.tools import tool
from langchain_core.utils.function_calling import convert_to_openai_tool
from demo_schema import ImpactInput
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage
load_dotenv()

model = ChatOpenAI(model="gpt-5.4-mini")
messages = [HumanMessage(content="Who is the PM of India?")]
output = model.invoke(messages)
print(output)
print("--------------------------------")
messages.append(output)
messages.append(HumanMessage(content="What is his age?"))
output = model.invoke(messages)
print(output)
