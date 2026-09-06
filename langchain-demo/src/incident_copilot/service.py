from dataclasses import dataclass
from datetime import UTC, datetime
from uuid import uuid4

from .domain import Category, IncidentAssessment, Severity
from .providers import IncidentModel


@dataclass(frozen=True)
class TriageOutcome:
    trace_id: str
    created_at: str
    assessment: IncidentAssessment
    policy_reasons: tuple[str, ...]

    def as_dict(self) -> dict:
        return {
            "trace_id": self.trace_id,
            "created_at": self.created_at,
            "assessment": self.assessment.model_dump(mode="json"),
            "policy_reasons": list(self.policy_reasons),
        }


def enforce_review_policy(assessment: IncidentAssessment) -> tuple[IncidentAssessment, tuple[str, ...]]:
    reasons: list[str] = []
    if assessment.severity in {Severity.P0, Severity.P1}:
        reasons.append("high_severity")
    if assessment.confidence < 0.75:
        reasons.append("low_confidence")
    if len(assessment.missing_information) >= 2:
        reasons.append("material_information_missing")
    if assessment.category == Category.SECURITY_PRIVACY:
        reasons.append("security_or_privacy")

    if reasons and not assessment.needs_human_review:
        assessment = assessment.model_copy(update={"needs_human_review": True})
    return assessment, tuple(reasons)


def triage_incident(incident_text: str, model: IncidentModel) -> TriageOutcome:
    if len(incident_text.strip()) < 10:
        raise ValueError("Incident report must contain at least 10 characters")

    assessment = model.invoke(incident_text)
    assessment, reasons = enforce_review_policy(assessment)
    return TriageOutcome(
        trace_id=str(uuid4()),
        created_at=datetime.now(UTC).isoformat(),
        assessment=assessment,
        policy_reasons=reasons,
    )

