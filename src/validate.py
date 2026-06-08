import pandas as pd


VALID_PRIORITIES = {"Low", "Medium", "High", "Critical"}
VALID_STATUSES = {"Open", "In Progress", "Resolved", "Closed"}


def validate_service_requests(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Validates service request records.

    Returns:
        valid_records: records that passed all validation checks
        rejected_records: records that failed one or more validation checks
    """

    validated_df = df.copy()
    validated_df["validation_errors"] = ""

    for index, row in validated_df.iterrows():
        errors = []

        if pd.isna(row["request_id"]) or str(row["request_id"]).strip() == "":
            errors.append("Missing request_id")

        if pd.isna(row["submitted_date"]):
            errors.append("Invalid or missing submitted_date")

        if pd.isna(row["department"]) or str(row["department"]).strip() == "":
            errors.append("Missing department")

        if pd.isna(row["request_type"]) or str(row["request_type"]).strip() == "":
            errors.append("Missing request_type")

        if row["priority"] not in VALID_PRIORITIES:
            errors.append("Invalid priority")

        if row["status"] not in VALID_STATUSES:
            errors.append("Invalid status")

        if pd.isna(row["estimated_cost"]) or row["estimated_cost"] < 0:
            errors.append("Invalid estimated_cost")

        if pd.isna(row["actual_cost"]) or row["actual_cost"] < 0:
            errors.append("Invalid actual_cost")

        if not pd.isna(row["resolution_date"]) and not pd.isna(row["submitted_date"]):
            if row["resolution_date"] < row["submitted_date"]:
                errors.append("Resolution date before submitted date")

        if (
            pd.isna(row["customer_satisfaction_score"])
            or row["customer_satisfaction_score"] < 1
            or row["customer_satisfaction_score"] > 5
        ):
            errors.append("Invalid customer_satisfaction_score")

        validated_df.at[index, "validation_errors"] = "; ".join(errors)

    # Now I need to flag duplicate request IDs
    duplicate_mask = validated_df["request_id"].duplicated(keep=False)

    for index in validated_df[duplicate_mask].index:
        existing_errors = validated_df.at[index, "validation_errors"]

        if existing_errors:
            validated_df.at[index, "validation_errors"] = (
                existing_errors + "; Duplicate request_id"
            )
        else:
            validated_df.at[index, "validation_errors"] = "Duplicate request_id"

    rejected_records = validated_df[validated_df["validation_errors"] != ""].copy()
    valid_records = validated_df[validated_df["validation_errors"] == ""].copy()

    valid_records = valid_records.drop(columns=["validation_errors"])

    return valid_records, rejected_records