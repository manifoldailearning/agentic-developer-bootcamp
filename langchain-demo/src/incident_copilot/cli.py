import argparse
import json
import sys
from pathlib import Path

from dotenv import load_dotenv

from .providers import FixtureModel, LangChainOpenAIModel
from .service import triage_incident


ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))


def resolve_from_root(path: Path) -> Path:
    return path if path.is_absolute() else ROOT / path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Triage one operational incident report")
    parser.add_argument("incident_file", type=Path)
    parser.add_argument("--mock", action="store_true", help="Use a deterministic fixture")
    parser.add_argument("--case-id", default="payments-502")
    parser.add_argument("--output", type=Path, default=ROOT / "output" / "triage.json")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    load_dotenv(ROOT / ".env")
    try:
        incident_file = resolve_from_root(args.incident_file)
        incident_text = incident_file.read_text(encoding="utf-8")
        if args.mock:
            model = FixtureModel(ROOT / "fixtures" / "mock_assessments.json", args.case_id)
        else:
            model = LangChainOpenAIModel()

        outcome = triage_incident(incident_text, model)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(outcome.as_dict(), indent=2), encoding="utf-8")
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"Triage failed: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(outcome.as_dict(), indent=2))
    print(f"\nSaved {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
