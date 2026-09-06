import importlib
import sys


REQUIRED = ["pydantic", "langchain", "langchain_openai", "dotenv"]


def main() -> int:
    print(f"Python {sys.version.split()[0]}")
    missing = []
    for name in REQUIRED:
        try:
            importlib.import_module(name)
            print(f"{name:<20} OK")
        except ImportError:
            missing.append(name)
            print(f"{name:<20} MISSING")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())

