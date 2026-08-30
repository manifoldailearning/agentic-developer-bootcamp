from pydantic import BaseModel, ValidationError

class AgentRequest(BaseModel): # this is a class that inherits from BaseModel
    task: str
    max_steps: int
    temperature: float


request = AgentRequest(task="Solve the problem", max_steps=10, temperature=0.5)
print(request)
print(type(request))
print(type(request.task))
print(type(request.max_steps))
print(type(request.temperature))

print("--------------------------------")
# Parsing / Coercion
request_2 = AgentRequest(task="Solve the problem", max_steps="10", temperature="0.5")
print(request_2)
print(type(request_2))
print(type(request_2.task))
print(type(request_2.max_steps))
print(type(request_2.temperature))
print("--------------------------------")
# invlid input
try:
    request_3 = AgentRequest(task="Solve the problem", max_steps="ten", temperature="0.5")
except ValidationError as e:
    #print(e)
    #print(e.errors())
    for error in e.errors():
        print(f"Location: {error['loc']}")
        print(f"Message: {error['msg']}")
        print(f"Type: {error['type']}")
        print("--------------------------------")

# Assignment:
# create a new class called AgentResponse that inherits from BaseModel
# it should have the following fields:
# - result: str
# - max_steps: int
# - status: str
# - error: str

# On that, test with valid input, invalid input, and missing input.