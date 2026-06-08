-- ============================================================
-- Service Request Analytics Views
-- Purpose: Create reusable reporting views from clean data
-- ============================================================


DROP VIEW IF EXISTS vw_department_summary;

CREATE VIEW vw_department_summary AS
SELECT
    department,
    COUNT(*) AS request_count,
    ROUND(AVG(actual_cost), 2) AS avg_actual_cost,
    SUM(actual_cost) AS total_actual_cost,
    ROUND(AVG(customer_satisfaction_score), 2) AS avg_satisfaction_score
FROM service_requests
GROUP BY department;


DROP VIEW IF EXISTS vw_priority_summary;

CREATE VIEW vw_priority_summary AS
SELECT
    priority,
    COUNT(*) AS request_count,
    ROUND(AVG(actual_cost), 2) AS avg_actual_cost,
    ROUND(AVG(customer_satisfaction_score), 2) AS avg_satisfaction_score
FROM service_requests
GROUP BY priority;


DROP VIEW IF EXISTS vw_team_resolution_summary;

CREATE VIEW vw_team_resolution_summary AS
SELECT
    assigned_team,
    COUNT(*) AS request_count,
    ROUND(AVG(resolution_date - submitted_date), 2) AS avg_resolution_days,
    ROUND(AVG(actual_cost), 2) AS avg_actual_cost
FROM service_requests
WHERE resolution_date IS NOT NULL
GROUP BY assigned_team;


DROP VIEW IF EXISTS vw_cost_variance;

CREATE VIEW vw_cost_variance AS
SELECT
    request_id,
    department,
    request_type,
    estimated_cost,
    actual_cost,
    actual_cost - estimated_cost AS cost_variance
FROM service_requests;