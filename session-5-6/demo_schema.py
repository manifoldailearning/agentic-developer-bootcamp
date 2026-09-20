"""Concept 2: Pydantic validates tool INPUTS, just as Week 1 validated outputs."""
import json
from pydantic import BaseModel, ConfigDict, Field, StrictInt, ValidationError, model_validator


class ImpactInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    failed_requests: StrictInt = Field(ge=0, description="Failed requests in the observed window")
    total_requests: StrictInt = Field(gt=0, description="All requests in that same window")
    baseline_error_rate_pct: float = Field(ge=0, le=100, strict=True, allow_inf_nan=False,
                                           description="Baseline percentage: 2.0 means 2 percent")

    @model_validator(mode="after")
    def check_counts(self):
        if self.failed_requests > self.total_requests:
            raise ValueError("failed requests cannot exceed total requests")
        return self


if __name__ == "__main__":
    print(json.dumps(ImpactInput.model_json_schema(), indent=2))
    for total in (1200, 0, "1200"):
        try:
            values = ImpactInput(failed_requests=240, total_requests=total, baseline_error_rate_pct=2.0)
            print("ACCEPTED", values.model_dump())
        except ValidationError:
            print("REJECTED total_requests:", repr(total))
    print("Cross-field checks live in Python. JSON Schema alone does not encode our count relationship.")
