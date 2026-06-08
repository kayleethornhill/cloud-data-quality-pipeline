import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


PROCESSED_DATA_PATH = Path("data/processed/clean_service_requests.csv")


def get_database_engine():
    """
    Creates a database connection engine using environment variables.
    """

    load_dotenv()

    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    connection_string = (
        f"postgresql+psycopg2://{db_user}:{db_password}"
        f"@{db_host}:{db_port}/{db_name}"
    )

    return create_engine(connection_string)


def load_clean_data_to_postgres() -> None:
    """
    Loads the cleaned service request CSV into PostgreSQL.
    """

    print("Loading clean service request data into PostgreSQL...")

    df = pd.read_csv(PROCESSED_DATA_PATH)

    engine = get_database_engine()

    df.to_sql(
        "service_requests",
        engine,
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(df)} records into PostgreSQL table: service_requests")