from typing import Literal
from pydantic import BaseModel, ValidationError, Field

# define the contract
class SupportTicket(BaseModel):
    ticket_id: int
    customer_name: str
    issue: str = Field(min_length=10, max_length=500, description="The issue to solve")
    priority: Literal["low", "medium", "high"] 
    resolved: bool = False

# imagnoe this came from an api, LLM or external systems
candidate = {
    "ticket_id": "123456",
    "customer_name": "John Doe",
    "issue": "I am having trouble with my account",
    "priority": "high",
    "resolved": False
}

# Validate the external data
ticket = SupportTicket.model_validate(candidate)

# convert the validated data to JSON
json_text = ticket.model_dump_json(indent=2)

print(f"validated pydantic object: {ticket}")
print(f"JSON: {json_text}")