from pathlib import Path
from functions_and_flow_v2 import greeting
# Path("data/missing-ticket.txt").read_text(encoding="utf-8")

try:
    Path("data/missing-ticket.txt").read_text(encoding="utf-8")
except FileNotFoundError as error:
    print(f"File is not found, please check the directory if it exists: {error}")
    print(greeting("User"))


except Exception as error:
    print(f"Could not continue: {error}")
