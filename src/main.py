from pathlib import Path

import pandas as pd

from clean import clean_service_requests
from validate import validate_service_requests
from load import load_clean_data_to_postgres

# this script does the first full pipeline

RAW_DATA_PATH = Path("data/raw/service_requests.csv")
PROCESSED_DATA_PATH = Path("data/processed/clean_service_requests.csv")
REJECTED_DATA_PATH = Path("data/rejected/rejected_service_requests.csv")


def main() -> None:
    """
    Runs the local service request data quality pipeline.
    """

    print("Starting service request data quality pipeline...")

    df = pd.read_csv(RAW_DATA_PATH)

    print(f"Loaded {len(df)} raw records.")

    cleaned_df = clean_service_requests(df)

    valid_records, rejected_records = validate_service_requests(cleaned_df)

    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    REJECTED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    valid_records.to_csv(PROCESSED_DATA_PATH, index=False)
    rejected_records.to_csv(REJECTED_DATA_PATH, index=False)
    
    load_clean_data_to_postgres()

    print(f"Valid records exported: {len(valid_records)}")
    print(f"Rejected records exported: {len(rejected_records)}")

    print(f"Clean data saved to: {PROCESSED_DATA_PATH}")
    print(f"Rejected data saved to: {REJECTED_DATA_PATH}")

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()