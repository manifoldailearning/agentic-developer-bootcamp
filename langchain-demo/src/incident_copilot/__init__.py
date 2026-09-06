"""Incident Triage Copilot teaching package."""

from .domain import IncidentAssessment
from .service import TriageOutcome, triage_incident

__all__ = ["IncidentAssessment", "TriageOutcome", "triage_incident"]

