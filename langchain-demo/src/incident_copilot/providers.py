import json
import os
from pathlib import Path
from typing import Protocol

from .domain import IncidentAssessment
from .prompts import SYSTEM_PROMPT, human_prompt


class IncidentModel(Protocol):
    def invoke(self, incident_text: str) -> IncidentAssessment:
        """Return one validated assessment."""


class FixtureModel:
    """Deterministic model substitute for teaching and offline tests."""

    def __init__(self, fixture_path: Path, case_id: str):
        records = json.loads(fixture_path.read_text(encoding="utf-8"))
        if case_id not in records:
            raise KeyError(f"No fixture for case {case_id!r}")
        self._record = records[case_id]

    def invoke(self, incident_text: str) -> IncidentAssessment:
        del incident_text
        return IncidentAssessment.model_validate(self._record)


class LangChainOpenAIModel:
    """LangChain adapter kept behind a small application boundary."""

    def __init__(self, model_name: str | None = None):
        from langchain.chat_models import init_chat_model

        selected_model = model_name or os.getenv("OPENAI_MODEL")
        if not selected_model:
            raise RuntimeError("Set OPENAI_MODEL in .env before using live mode")

        model = init_chat_model(
            f"openai:{selected_model}",
            temperature=0,
            timeout=30,
            max_retries=2,
        )
        self._model = model.with_structured_output(
            IncidentAssessment,
            method="json_schema",
            include_raw=True,
        )

    def invoke(self, incident_text: str) -> IncidentAssessment:
        try:
            result = self._model.invoke(
                [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": human_prompt(incident_text)},
                ]
            )
        except Exception as exc:
            raise RuntimeError(f"Model call failed: {exc}") from exc

        if result.get("parsing_error") is not None:
            raise RuntimeError(f"Structured output failed: {result['parsing_error']}")
        parsed = result.get("parsed")
        if parsed is None:
            raise RuntimeError("The model returned no parsed assessment")
        return parsed
