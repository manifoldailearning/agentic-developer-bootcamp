"""Concept 1: ordinary Python arithmetic. No model, framework or project import."""
def calculate_incident_impact(failed_requests, total_requests, baseline_error_rate_pct):
    rate = failed_requests / total_requests * 100
    return {"error_rate_pct": rate, "change_percentage_points": rate - baseline_error_rate_pct}


if __name__ == "__main__":
    print(calculate_incident_impact(240, 1200, 2.0))
    print("Who selected the function and arguments? The developer did.")
    print("This first version has no validation. Predict what total_requests=0 would do.")
