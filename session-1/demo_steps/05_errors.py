from pathlib import Path


try:
    Path("data/missing-ticket.txt").read_text(encoding="utf-8")
except FileNotFoundError as error:
    print(f"Could not continue: {error}")
