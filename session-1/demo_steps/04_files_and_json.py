import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
input_path = root / "data" / "support-ticket.txt"
output_path = root / "output" / "step-04-ticket.json"

text = input_path.read_text(encoding="utf-8")
lines = [line for line in text.splitlines() if line.strip()]

ticket = {"line_count": len(lines), "first_line": lines[0]}
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(ticket, indent=2), encoding="utf-8")

print(f"Created: {output_path}")
