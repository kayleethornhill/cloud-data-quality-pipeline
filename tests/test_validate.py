import pandas as pd

from src.clean import clean_service_requests
from src.validate import validate_service_requests


def test_validate_accepts_valid_record():
    sample_data = pd.DataFrame([
        {
            "request_id": "REQ-3001",
            "submitted_date": "2026-03-01",
            "department": "Engineering",
            "request_type": "Project Update",
            "priority": "High",
            "status": "Open",
            "assigned_team": "Project Controls",
            "region": "North",
            "estimated_cost": 500,
            "actual_cost": 475,
            "resolution_date": "2026-03-05",
            "customer_satisfaction_score": 5,
            "description": "Valid request"
        }
    ])

    cleaned_df = clean_service_requests(sample_data)
    valid_records, rejected_records = validate_service_requests(cleaned_df)

    assert len(valid_records) == 1
    assert len(rejected_records) == 0


def test_validate_rejects_missing_department():
    sample_data = pd.DataFrame([
        {
            "request_id": "REQ-3002",
            "submitted_date": "2026-03-01",
            "department": "",
            "request_type": "Project Update",
            "priority": "High",
            "status": "Open",
            "assigned_team": "Project Controls",
            "region": "North",
            "estimated_cost": 500,
            "actual_cost": 475,
            "resolution_date": "2026-03-05",
            "customer_satisfaction_score": 5,
            "description": "Missing department"
        }
    ])

    cleaned_df = clean_service_requests(sample_data)
    valid_records, rejected_records = validate_service_requests(cleaned_df)

    assert len(valid_records) == 0
    assert len(rejected_records) == 1
    assert "Missing department" in rejected_records.loc[0, "validation_errors"]


def test_validate_rejects_invalid_priority():
    sample_data = pd.DataFrame([
        {
            "request_id": "REQ-3003",
            "submitted_date": "2026-03-01",
            "department": "Finance",
            "request_type": "Report Issue",
            "priority": "urgent",
            "status": "Open",
            "assigned_team": "Analytics",
            "region": "South",
            "estimated_cost": 300,
            "actual_cost": 325,
            "resolution_date": "2026-03-04",
            "customer_satisfaction_score": 4,
            "description": "Invalid priority"
        }
    ])

    cleaned_df = clean_service_requests(sample_data)
    valid_records, rejected_records = validate_service_requests(cleaned_df)

    assert len(valid_records) == 0
    assert len(rejected_records) == 1
    assert "Invalid priority" in rejected_records.loc[0, "validation_errors"]


def test_validate_rejects_duplicate_request_id():
    sample_data = pd.DataFrame([
        {
            "request_id": "REQ-3004",
            "submitted_date": "2026-03-01",
            "department": "Engineering",
            "request_type": "Project Update",
            "priority": "High",
            "status": "Open",
            "assigned_team": "Project Controls",
            "region": "North",
            "estimated_cost": 500,
            "actual_cost": 475,
            "resolution_date": "2026-03-05",
            "customer_satisfaction_score": 5,
            "description": "First duplicate"
        },
        {
            "request_id": "REQ-3004",
            "submitted_date": "2026-03-02",
            "department": "Engineering",
            "request_type": "Project Update",
            "priority": "High",
            "status": "Open",
            "assigned_team": "Project Controls",
            "region": "North",
            "estimated_cost": 500,
            "actual_cost": 475,
            "resolution_date": "2026-03-06",
            "customer_satisfaction_score": 5,
            "description": "Second duplicate"
        }
    ])

    cleaned_df = clean_service_requests(sample_data)
    valid_records, rejected_records = validate_service_requests(cleaned_df)

    assert len(valid_records) == 0
    assert len(rejected_records) == 2
    assert rejected_records["validation_errors"].str.contains("Duplicate request_id").all()


def test_validate_rejects_resolution_date_before_submitted_date():
    sample_data = pd.DataFrame([
        {
            "request_id": "REQ-3005",
            "submitted_date": "2026-03-10",
            "department": "Operations",
            "request_type": "Equipment Request",
            "priority": "Low",
            "status": "Resolved",
            "assigned_team": "Field Support",
            "region": "West",
            "estimated_cost": 900,
            "actual_cost": 850,
            "resolution_date": "2026-03-08",
            "customer_satisfaction_score": 4,
            "description": "Bad date logic"
        }
    ])

    cleaned_df = clean_service_requests(sample_data)
    valid_records, rejected_records = validate_service_requests(cleaned_df)

    assert len(valid_records) == 0
    assert len(rejected_records) == 1
    assert "Resolution date before submitted date" in rejected_records.loc[0, "validation_errors"]