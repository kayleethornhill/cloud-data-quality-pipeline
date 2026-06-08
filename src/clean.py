import pandas as pd


def clean_service_requests(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and standardizes service request data.

    This function handles values that are fixable, such as inconsistent
    capitalization or alternate spellings of known business values.
    """

    cleaned_df = df.copy()

    # Standardize text fields by stripping extra spaces
    text_columns = [
        "request_id",
        "department",
        "request_type",
        "priority",
        "status",
        "assigned_team",
        "region",
        "description",
    ]

    for column in text_columns:
        cleaned_df[column] = cleaned_df[column].astype("string").str.strip()

    # Standardize the priority values
    priority_mapping = {
        "low": "Low",
        "medium": "Medium",
        "high": "High",
        "critical": "Critical",
    }

    cleaned_df["priority"] = (
        cleaned_df["priority"]
        .str.lower()
        .map(priority_mapping)
        .fillna(cleaned_df["priority"])
    )

    # Standardize what the status values are
    status_mapping = {
        "open": "Open",
        "inprogress": "In Progress",
        "in progress": "In Progress",
        "in-progress": "In Progress",
        "resolved": "Resolved",
        "closed": "Closed",
        "complete": "Closed",
    }

    cleaned_df["status"] = (
        cleaned_df["status"]
        .str.lower()
        .str.replace("-", " ", regex=False)
        .str.replace(" ", "", regex=False)
        .map(status_mapping)
        .fillna(cleaned_df["status"])
    )

    # Convert dates
    cleaned_df["submitted_date"] = pd.to_datetime(
        cleaned_df["submitted_date"],
        errors="coerce"
    )

    cleaned_df["resolution_date"] = pd.to_datetime(
        cleaned_df["resolution_date"],
        errors="coerce"
    )

    # Convert number columns
    numeric_columns = [
        "estimated_cost",
        "actual_cost",
        "customer_satisfaction_score",
    ]

    for column in numeric_columns:
        cleaned_df[column] = pd.to_numeric(cleaned_df[column], errors="coerce")

    return cleaned_df