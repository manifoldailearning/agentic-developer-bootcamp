import argparse
import json
from pathlib import Path

from dotenv import load_dotenv

from .providers import FixtureModel, LangChainOpenAIModel
from .service import triage_incident


ROOT = Path(__file__).resolve().parents[2]


def load_cases(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def evaluate_case(case: dict, assessment: dict) -> list[str]:
    failures: list[str] = []
    if assessment["severity"] not in case["expected_severity_any_of"]:
        failures.append("severity")
    if assessment["needs_human_review"] != case["expected_human_review"]:
        failures.append("human_review")
    searchable = json.dumps(assessment).lower()
    if case["forbidden_claim"].lower() in searchable:
        failures.append("unsupported_claim")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the small Week 1 golden dataset")
    parser.add_argument("--mock", action="store_true")
    args = parser.parse_args()

    cases = load_cases(ROOT / "data" / "evaluation_cases.jsonl")
    if args.mock:
        live_model = None
    else:
        load_dotenv()
        live_model = LangChainOpenAIModel()

    passed = 0
    for case in cases:
        model = (
            FixtureModel(ROOT / "fixtures" / "mock_assessments.json", case["case_id"])
            if args.mock
            else live_model
        )
        outcome = triage_incident(case["text"], model)
        assessment = outcome.assessment.model_dump(mode="json")
        failures = evaluate_case(case, assessment)
        status = "PASS" if not failures else f"FAIL ({', '.join(failures)})"
        print(f"{case['case_id']:<20} {status}")
        passed += not failures

    print(f"\n{passed}/{len(cases)} cases passed")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())

