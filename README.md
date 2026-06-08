# Cloud Data Quality Pipeline

## Project Summary

This project is a local data quality pipeline built with Python, pandas, and PostgreSQL. I built it to model a realistic business problem: raw operational data comes in messy, inconsistent, and not ready to trust yet.

The pipeline takes raw service request data, cleans and standardizes the values, validates each record against data quality rules, separates rejected records with clear error messages, and loads the clean data into PostgreSQL for SQL analysis.

The goal of this project is to show how raw data can be turned into something more reliable, organized, and usable before it reaches reports, dashboards, databases, or decision-makers.

## Business Problem

Organizations often receive data from multiple systems, departments, or manual entry forms (looking at you Microsoft Forms). Before that data can be trusted for decision-making, it needs to be reviewed for missing values, invalid formats, duplicates, inconsistent categories, and business rule violations.

This project uses a sample service request dataset that includes common data quality issues such as missing fields, invalid dates, duplicate request IDs, negative costs, invalid statuses, and inconsistent text formatting.

## Tech Stack

- Python
- pandas
- CSV files
- VS Code
- Virtual environment
- Git/GitHub

## Pipeline Workflow

The pipeline follows this process:

```text
Raw CSV file
   ↓
Read data with pandas
   ↓
Clean and standardize values
   ↓
Validate records against data quality rules
   ↓
Export valid records to processed data
   ↓
Export rejected records with validation errors
```

## Project Structure
```text
cloud-data-quality-pipeline/
│
├── data/
│   ├── raw/
│   │   └── service_requests.csv
│   ├── processed/
│   │   └── clean_service_requests.csv
│   └── rejected/
│       └── rejected_service_requests.csv
│
├── src/
│   ├── main.py
│   ├── clean.py
│   └── validate.py
│
├── sql/
├── docs/
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
```

## Data Quality Rules

The validation process checks for:

- Missing request IDs
- Duplicate request IDs
- Invalid or missing submitted dates
- Missing departments
- Missing request types
- Invalid priority values
- Invalid status values
- Negative or missing cost values
- Resolution dates that occur before submitted dates
- Customer satisfaction scores outside the allowed range of 1 to 5

## Cleaning Logic

The cleaning step standardizes values that are fixable, such as inconsistent capitalization or formatting.
```text
Examples:

open → Open
OPEN → Open
Complete → Closed
in-progress → In Progress
medium → Medium
LOW → Low
```
## Sample Pipeline Output

When the pipeline runs successfully, it prints a summary like:

Starting service request data quality pipeline...
Loaded 15 raw records.
Valid records exported: 5
Rejected records exported: 10
Clean data saved to: data/processed/clean_service_requests.csv
Rejected data saved to: data/rejected/rejected_service_requests.csv
Pipeline completed successfully.

## How to Run the Project

Create and activate a virtual environment:

py -m venv .venv
.\.venv\Scripts\Activate.ps1

Install dependencies:

python -m pip install -r requirements.txt

Run the pipeline:

python src/main.py
Output Files

## The pipeline creates two output files:

data/processed/clean_service_requests.csv
data/rejected/rejected_service_requests.csv

The rejected records file includes a validation_errors column explaining why each rejected record failed validation.

## PostgreSQL Database Layer

The pipeline loads validated service request records into a PostgreSQL database named `service_request_pipeline`.

The main database table is:

service_requests

## The database schema is defined in:

sql/create_tables.sql

## Additional analytics queries are included in:

sql/analytics_queries.sql

## Reusable reporting views are defined in:

sql/create_views.sql
SQL Analytics Examples

## This project includes SQL queries for:

- Request counts by department
- Request counts by priority
- Request counts by status
- Average actual cost by department
- Total actual cost by department
- Average satisfaction score by department
- Resolution time by request
- Average resolution time by assigned team
- Cost variance between estimated and actual cost

## Automated Tests

This project includes automated tests using `pytest`.

The tests verify that the pipeline correctly:

- Standardizes messy priority and status values
- Removes extra spaces from text fields
- Converts date fields into datetime values
- Converts cost and satisfaction fields into numeric values
- Accepts valid service request records
- Rejects records with missing departments
- Rejects invalid priority values
- Flags duplicate request IDs
- Rejects records where the resolution date occurs before the submitted date

Run tests with:

```powershell
python -m pytest
```

## Why This Project Matters

This project demonstrates important data engineering and data quality skills, including:

- Reading raw data from CSV files
- Cleaning inconsistent business values
- Validating data against business rules
- Separating clean and rejected records
- Creating an audit trail for data quality issues
- Structuring a project for future database and cloud expansion


## Planned future improvements include:

- Load clean records into PostgreSQL
- Create SQL tables and analytics queries
- Add automated tests with pytest
- Add Docker support
- Add GitHub Actions for automated validation
- Build a cloud architecture version using AWS services such as S3, Lambda, Glue, Athena, IAM, and CloudWatch
- Add Terraform infrastructure-as-code examples