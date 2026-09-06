from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field


class Severity(str, Enum):
    P0 = "P0"
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"


class Category(str, Enum):
    PAYMENTS = "payments"
    AUTHENTICATION = "authentication"
    INVENTORY = "inventory"
    FULFILMENT = "fulfilment"
    SECURITY_PRIVACY = "security-privacy"
    OTHER = "other"


class Team(str, Enum):
    PAYMENTS = "payments-on-call"
    IDENTITY = "identity-on-call"
    FULFILMENT = "fulfilment-platform"
    SECURITY = "security-incident-response"
    OPERATIONS = "operations"


class EvidenceItem(BaseModel):
    claim: str = Field(min_length=1, description="A conclusion supported by the input")
    source_quote: str = Field(
        min_length=1,
        description="A short exact excerpt from the incident report supporting the claim",
    )


class IncidentAssessment(BaseModel):
    """The machine-readable contract returned by the model."""

    schema_version: Literal["1.0"] = "1.0"
    incident_id: str | None = Field(
        default=None,
        description="Incident identifier from the input, or null when absent",
    )
    summary: str = Field(min_length=10, max_length=280)
    category: Category
    severity: Severity
    affected_services: list[str] = Field(default_factory=list, max_length=8)
    business_impact: str = Field(min_length=5, max_length=300)
    evidence: list[EvidenceItem] = Field(min_length=1, max_length=6)
    missing_information: list[str] = Field(default_factory=list, max_length=8)
    recommended_team: Team
    recommended_next_action: str = Field(min_length=10, max_length=400)
    confidence: float = Field(ge=0, le=1)
    needs_human_review: bool

