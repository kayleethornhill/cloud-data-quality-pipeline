import pandas as pd

from src.clean import clean_service_requests


def test_clean_service_requests_standardizes_priority_and_status():
    sample_data = pd.DataFrame([
        {
            "request_id": " REQ-2001 ",
            "submitted_date": "2026-02-01",
            "department": "Engineering",
            "request_type": "System Access",
            "priority": "HIGH",
            "status": "in-progress",
            "assigned_team": "Infrastructure",
            "region": "North",
            "estimated_cost": "500",
            "actual_cost": "450",
            "resolution_date": "2026-02-03",
            "customer_satisfaction_score": "5",
            "description": " Test request "
        }
    ])

    cleaned_df = clean_service_requests(sample_data)

    assert cleaned_df.loc[0, "request_id"] == "REQ-2001"
    assert cleaned_df.loc[0, "priority"] == "High"
    assert cleaned_df.loc[0, "status"] == "In Progress"
    assert cleaned_df.loc[0, "description"] == "Test request"


def test_clean_service_requests_converts_dates_and_numbers():
    sample_data = pd.DataFrame([
        {
            "request_id": "REQ-2002",
            "submitted_date": "2026-02-01",
            "department": "Finance",
            "request_type": "Report Issue",
            "priority": "medium",
            "status": "open",
            "assigned_team": "Analytics",
            "region": "South",
            "estimated_cost": "300",
            "actual_cost": "325",
            "resolution_date": "2026-02-04",
            "customer_satisfaction_score": "4",
            "description": "Report issue"
        }
    ])

    cleaned_df = clean_service_requests(sample_data)

    assert pd.api.types.is_datetime64_any_dtype(cleaned_df["submitted_date"])
    assert pd.api.types.is_datetime64_any_dtype(cleaned_df["resolution_date"])
    assert pd.api.types.is_numeric_dtype(cleaned_df["estimated_cost"])
    assert pd.api.types.is_numeric_dtype(cleaned_df["actual_cost"])
    assert pd.api.types.is_numeric_dtype(cleaned_df["customer_satisfaction_score"])