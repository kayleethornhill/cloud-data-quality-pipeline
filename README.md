# Project Summary

This project is a local data quality pipeline built with Python, pandas, and PostgreSQL. I built it to model a realistic business problem: raw operational data often comes in messy, inconsistent, incomplete, and not ready to trust yet.

The pipeline takes raw service request data, cleans and standardizes the values, validates each record against data quality rules, separates rejected records with clear validation error messages, generates a data quality report, and loads the clean records into PostgreSQL for SQL analysis.

The goal of this project is to show how raw data can be turned into something more reliable, organized, and usable before it reaches reports, dashboards, databases, or decision-makers.

## Business Problem

Organizations often receive data from multiple systems, departments, or manual entry forms — looking at you, Microsoft Forms. Before that data can be trusted for decision-making, it needs to be reviewed for missing values, invalid formats, duplicates, inconsistent categories, and business rule violations.

This project uses a sample service request dataset that includes common data quality issues such as missing fields, invalid dates, duplicate request IDs, negative costs, invalid statuses, invalid customer satisfaction scores, and inconsistent text formatting.

## Tech Stack
Python
pandas
PostgreSQL
SQL
SQLAlchemy
python-dotenv
pytest
CSV files
VS Code
Git/GitHub

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
   ↓
Generate a data quality report
   ↓
Load clean records into PostgreSQL
   ↓
Run SQL analytics queries and reporting views
```

## Project Structure
```text
cloud-data-quality-pipeline/
│
├── data/
│   ├── raw/
│   │   └── service_requests.csv
│   ├── processed/
│   │   └── .gitkeep
│   └── rejected/
│       └── .gitkeep
│
├── docs/
│
├── logs/
│   └── .gitkeep
│
├── reports/
│   └── .gitkeep
│
├── samples/
│   ├── clean_service_requests_sample.csv
│   ├── rejected_service_requests_sample.csv
│   ├── data_quality_report_sample.txt
│   └── sql_query_results_sample.md
│
├── sql/
│   ├── analytics_queries.sql
│   ├── create_tables.sql
│   └── create_views.sql
│
├── src/
│   ├── main.py
│   ├── clean.py
│   ├── validate.py
│   └── load.py
│
├── tests/
│   ├── test_clean.py
│   └── test_validate.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```
## Data Quality Rules

The validation process checks for:

Missing request IDs
Duplicate request IDs
Invalid or missing submitted dates
Missing departments
Missing request types
Invalid priority values
Invalid status values
Negative or missing cost values
Resolution dates that occur before submitted dates
Customer satisfaction scores outside the allowed range of 1 to 5

Rejected records are exported with a validation_errors column explaining exactly why each record failed validation.

## Cleaning Logic

The cleaning step standardizes values that are fixable, such as inconsistent capitalization, extra spaces, or alternate formatting.
```text
Examples:

open → Open
OPEN → Open
Complete → Closed
in-progress → In Progress
medium → Medium
LOW → Low
```
The cleaning step also converts date fields into datetime values and converts cost and satisfaction fields into numeric values.

## Sample Pipeline Output

When the pipeline runs successfully, it prints a summary like:

Starting service request data quality pipeline...
Loaded 15 raw records.
Data quality report saved to: reports/data_quality_report.txt
Loaded 5 records into PostgreSQL table: service_requests
Valid records exported: 5
Rejected records exported: 10
Clean data saved to: data/processed/clean_service_requests.csv
Rejected data saved to: data/rejected/rejected_service_requests.csv
Pipeline completed successfully.
Sample Outputs

The samples/ folder includes example outputs from a successful pipeline run so the results can be reviewed without running the project locally.

clean_service_requests_sample.csv shows records that passed all validation checks.
rejected_service_requests_sample.csv shows records that failed validation, including validation error messages.
data_quality_report_sample.txt summarizes total records, valid records, rejected records, rejection rate, and validation error counts.
sql_query_results_sample.md shows example SQL query results from the cleaned PostgreSQL data.

The live output folders under data/processed/, data/rejected/, reports/, and logs/ are generated when the pipeline runs and are ignored by Git to keep the repository clean.

## PostgreSQL Database Layer

The project includes a PostgreSQL database layer so clean records can be stored and analyzed after validation.

The sql/ folder contains scripts used to create the database table, create reusable reporting views, and analyze the cleaned service request data.

create_tables.sql creates the main service_requests table.
create_views.sql creates reusable summary views for department, priority, team resolution, and cost variance analysis.
analytics_queries.sql contains business-focused SQL queries for request volume, cost, resolution time, and customer satisfaction.

## SQL Analytics Examples

This project includes SQL queries for:

- Viewing all clean service request records
- Counting total clean service requests
- Request counts by department
- Request counts by priority
- Request counts by status
- Average actual cost by department
- Total actual cost by department
- Average satisfaction score by department
- Resolution time by request
- Average resolution time by assigned team
- Cost variance between estimated and actual cost
- Requests where actual cost exceeded estimated cost

Sample SQL outputs are included in:

samples/sql_query_results_sample.md
Data Quality Reporting

The pipeline generates a data quality report each time it runs.

The report includes:

- Total records processed
- Valid records
- Rejected records
- Rejection rate
- Validation error counts

A sample report is included in:

samples/data_quality_report_sample.txt
Logging

The project uses Python logging to track pipeline execution.

The log captures major pipeline events, including:

Pipeline start
Raw record count
Cleaning completion
Valid and rejected record counts
Output file creation
Report creation
PostgreSQL load status
Pipeline errors, if they occur

Live log files are generated in the logs/ folder and ignored by Git.

## Automated Tests

This project includes automated tests using pytest.

The tests verify that the pipeline correctly:

Standardizes messy priority and status values
Removes extra spaces from text fields
Converts date fields into datetime values
Converts cost and satisfaction fields into numeric values
Accepts valid service request records
Rejects records with missing departments
Rejects invalid priority values
Flags duplicate request IDs
Rejects records where the resolution date occurs before the submitted date

Run tests with:

python -m pytest
How to Run the Project

Create and activate a virtual environment:

py -m venv .venv
.\.venv\Scripts\Activate.ps1

Install dependencies:

python -m pip install -r requirements.txt

Create a .env file in the project root with your PostgreSQL connection details:

DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name

Create the PostgreSQL table by running:

sql/create_tables.sql

Then run the pipeline:

python src/main.py
Output Files Created When the Pipeline Runs

The pipeline creates live output files in the following locations:

data/processed/clean_service_requests.csv
data/rejected/rejected_service_requests.csv
reports/data_quality_report.txt
logs/pipeline.log

The live output files are ignored by Git because they are regenerated when the pipeline runs. Portfolio-friendly examples are stored in the samples/ folder.

## Why This Project Matters

This project demonstrates important data quality, data engineering, and analytics skills, including:

Reading raw data from CSV files
Cleaning inconsistent business values
Validating records against business rules
Separating clean and rejected records
Creating a data quality audit trail
Generating data quality reports
Loading clean data into PostgreSQL
Writing SQL analytics queries
Creating reusable SQL reporting views
Using environment variables for database connection settings
Adding automated tests with pytest
Structuring a project for future database, cloud, and automation expansion