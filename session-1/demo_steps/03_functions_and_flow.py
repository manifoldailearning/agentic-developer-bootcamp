ALLOWED_PRIORITIES = {"low", "medium", "high"}


def normalise_priority(value: str) -> str:
    priority = value.strip().lower()
    if priority not in ALLOWED_PRIORITIES:
        raise ValueError(f"Unsupported priority: {value}")
    return priority


def parse_line(line: str) -> tuple[str, str]:
    key, value = line.split(":", maxsplit=1)
    return key.strip().lower(), value.strip()


key, value = parse_line("Priority: HIGH")
print(key)
print(normalise_priority(value))
