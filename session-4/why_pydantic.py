def create_agent(max_steps: int): # by default - no automatic runtime validation
    print(f"Creating agent with max_steps: {max_steps}")
    print(f"type of max_steps: {type(max_steps)}")
    return max_steps*2

result = create_agent("10") # str
print(f"result: {result}")
print(f"type of result: {type(result)}")