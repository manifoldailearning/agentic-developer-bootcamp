from pydantic import BaseModel, ValidationError, Field
from typing import Literal

class AgentRequest(BaseModel): # this is a class that inherits from BaseModel
    task: str # required field
    description: str | None # required field, but None is allowed
    max_steps: int = 5 # default value
    temperature: float | None # required field, but None is allowed

# request = AgentRequest(task="Solve the problem")
# print(request)
# print(type(request))
# print(type(request.task))
# print(type(request.description))
# print(type(request.max_steps))
# print(type(request.temperature))
# print("--------------------------------")

request = AgentRequest(task="Solve the problem", description=None, temperature=None)
print(request)
print(type(request))
print(type(request.task))
print(type(request.description))
print(type(request.max_steps))
print(type(request.temperature))
print("--------------------------------")

# Field Constraints
class AgentRequest(BaseModel): # this is a class that inherits from BaseModel
    task: str = Field(min_length=10, max_length=500, description="The task to solve")
    description: str | None = Field(default=None, description="The description of the task")
    max_steps: int = Field(default=5, ge=1,le = 100, description="The maximum number of steps to solve the task")
    temperature: float | None = Field(default=None, description="The temperature of the task")
    status: Literal["pending", "running", "completed", "failed"] = Field(default="pending", description="The status of the task")

request = AgentRequest(task="Solve the problem", description=None, temperature=None, status="waiting")
print(request)
print(type(request))
print(type(request.task))
print(type(request.description))
print(type(request.max_steps))
print(type(request.temperature))
print(type(request.status))
print("--------------------------------")

# Assignment:
# create a new class called AgentResponse that inherits from BaseModel
# it should have the following fields:
# - result: str
# - max_steps: int
# - status: str
# - error: str
# - traceback: str
# - traceback: str