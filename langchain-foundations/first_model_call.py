from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)

result = model.invoke("What is the Capital of India ?")
print(result)
print("--------------------------------")
print(type(result))
print(result.content)
print(result.usage_metadata)
result = model.invoke("Which country did you generate the response for ?") # by default it is stateless - it does not remember the previous conversation
print(result)
print("--------------------------------")   
print(type(result))
print(result.content)
print(result.usage_metadata)
# https://reference.langchain.com/python/langchain-anthropic/chat_models/ChatAnthropic?_gl=1*2xbiin*_gcl_au*MzcyMzMzNjY4LjE3ODc5ODA1NjE.*_ga*NjY5NzQ0MTA2LjE3ODc5ODA1NjI.*_ga_47WX3HKKY2*czE3ODg1NzU5MTIkbzIkZzEkdDE3ODg1NzU5ODYkajU4JGwwJGgw

# Deepseek - https://docs.langchain.com/oss/python/integrations/chat/deepseek