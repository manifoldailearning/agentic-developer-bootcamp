import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "support-ticket.txt"
OUTPUT_PATH = PROJECT_ROOT / "output" / "ticket.json"
ALLOWED_PRIORITIES = {"low", "medium", "high"}
# changes

def parse_ticket(text: str) -> dict:
    ticket = {
        "customer": "",
        "issue": "",
        "priority": "medium",
        "tags": [],
    }

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or ":" not in line:
            continue

        key, value = line.split(":", maxsplit=1)
        key = key.strip().lower()
        value = value.strip()

        if key == "tags":
            ticket["tags"] = [tag.strip() for tag in value.split(",") if tag.strip()]
        elif key in {"customer", "issue", "priority"}:
            ticket[key] = value

    if not ticket["customer"] or not ticket["issue"]:
        raise ValueError("customer and issue are required")

    priority = str(ticket["priority"]).lower()
    if priority not in ALLOWED_PRIORITIES:
        raise ValueError(f"priority must be one of {ALLOWED_PRIORITIES}")
    ticket["priority"] = priority
    return ticket


def main() -> int:
    try:
        text = INPUT_PATH.read_text(encoding="utf-8")
        ticket = parse_ticket(text)
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_PATH.write_text(json.dumps(ticket, indent=2), encoding="utf-8")
    except FileNotFoundError as error:
        print(f"Input error: {error}")
        return 1
    except ValueError as error:
        print(f"Data error: {error}")
        return 1

    print(f"Created: {OUTPUT_PATH.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
