import unittest

from incident_copilot.domain import IncidentAssessment


VALID = {
    "schema_version": "1.0",
    "incident_id": "INC-1",
    "summary": "Payments fail for a subset of checkout requests.",
    "category": "payments",
    "severity": "P2",
    "affected_services": ["checkout"],
    "business_impact": "Some customers cannot complete checkout.",
    "evidence": [{"claim": "Checkout fails", "source_quote": "checkout requests fail"}],
    "missing_information": [],
    "recommended_team": "payments-on-call",
    "recommended_next_action": "Inspect the payment error rate and recent release.",
    "confidence": 0.8,
    "needs_human_review": False,
}


class DomainTests(unittest.TestCase):
    def test_valid_record_parses(self):
        result = IncidentAssessment.model_validate(VALID)
        self.assertEqual(result.severity.value, "P2")

    def test_invalid_severity_fails(self):
        record = {**VALID, "severity": "urgent"}
        with self.assertRaises(ValueError):
            IncidentAssessment.model_validate(record)

    def test_confidence_must_be_bounded(self):
        record = {**VALID, "confidence": 1.4}
        with self.assertRaises(ValueError):
            IncidentAssessment.model_validate(record)


if __name__ == "__main__":
    unittest.main()

