import unittest

from incident_copilot.domain import IncidentAssessment
from incident_copilot.service import enforce_review_policy, triage_incident
from test_domain import VALID


class FakeModel:
    def __init__(self, record: dict):
        self.record = record

    def invoke(self, incident_text: str) -> IncidentAssessment:
        self.last_input = incident_text
        return IncidentAssessment.model_validate(self.record)


class ServiceTests(unittest.TestCase):
    def test_p0_always_requires_review(self):
        assessment = IncidentAssessment.model_validate(
            {**VALID, "severity": "P0", "needs_human_review": False}
        )
        hardened, reasons = enforce_review_policy(assessment)
        self.assertTrue(hardened.needs_human_review)
        self.assertIn("high_severity", reasons)

    def test_low_confidence_requires_review(self):
        assessment = IncidentAssessment.model_validate(
            {**VALID, "confidence": 0.3, "needs_human_review": False}
        )
        hardened, reasons = enforce_review_policy(assessment)
        self.assertTrue(hardened.needs_human_review)
        self.assertIn("low_confidence", reasons)

    def test_normal_p2_can_remain_unreviewed(self):
        assessment = IncidentAssessment.model_validate(VALID)
        hardened, reasons = enforce_review_policy(assessment)
        self.assertFalse(hardened.needs_human_review)
        self.assertEqual(reasons, ())

    def test_service_rejects_empty_report(self):
        with self.assertRaises(ValueError):
            triage_incident("  ", FakeModel(VALID))

    def test_service_returns_traceable_envelope(self):
        outcome = triage_incident("Checkout requests fail after release", FakeModel(VALID))
        self.assertTrue(outcome.trace_id)
        self.assertEqual(outcome.assessment.category.value, "payments")


if __name__ == "__main__":
    unittest.main()

