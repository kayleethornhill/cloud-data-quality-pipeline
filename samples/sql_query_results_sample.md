# SQL Query Results Sample

These are example results from running the PostgreSQL analytics queries after the clean service request records were loaded into the `service_requests` table.

The goal of these queries is to show how cleaned data can be used for business analysis after it has passed validation.

---

## Total Clean Requests

```sql
SELECT COUNT(*) AS total_clean_requests
FROM service_requests;
total_clean_requests
5
Requests by Department
SELECT
    department,
    COUNT(*) AS request_count
FROM service_requests
GROUP BY department
ORDER BY request_count DESC;
department	request_count
Engineering	2
Finance	1
HR	1
Operations	1
Requests by Priority
SELECT
    priority,
    COUNT(*) AS request_count
FROM service_requests
GROUP BY priority
ORDER BY request_count DESC;
priority	request_count
Medium	2
Critical	1
High	1
Low	1
Requests by Status
SELECT
    status,
    COUNT(*) AS request_count
FROM service_requests
GROUP BY status
ORDER BY request_count DESC;
status	request_count
Closed	2
In Progress	2
Open	1
Cost Variance by Request
SELECT
    request_id,
    department,
    request_type,
    estimated_cost,
    actual_cost,
    actual_cost - estimated_cost AS cost_variance
FROM service_requests
ORDER BY cost_variance DESC;
request_id	department	request_type	estimated_cost	actual_cost	cost_variance
REQ-1002	Finance	Report Issue	300.00	325.00	25.00
REQ-1011	HR	System Access	450.00	425.00	-25.00
REQ-1001	Engineering	System Access	500.00	450.00	-50.00
REQ-1013	Engineering	Project Update	700.00	650.00	-50.00
REQ-1003	Operations	Equipment Request	1200.00	1100.00	-100.00
What These Results Show

The SQL layer confirms that the cleaned data can be used for analysis after the pipeline runs. The queries summarize request volume, priority distribution, status, department activity, and cost variance across valid service request records.


## Step 3: Check the values against your pgAdmin results

The tables above are based on the clean records we saw earlier. If your pgAdmin results are slightly different, change the sample file to match your actual query results.

The important thing is not that the numbers are huge. The important thing is that you are showing:

```text
Python cleaned the data
Validation separated good/bad records
PostgreSQL stored the good records
SQL can analyze the clean records