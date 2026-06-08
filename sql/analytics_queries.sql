-- ============================================================
-- Service Request Analytics Queries
-- Purpose: Analyze clean service request data after pipeline load
-- ============================================================


-- 1. View all clean service requests
SELECT *
FROM service_requests;


-- 2. Count total clean service requests
SELECT COUNT(*) AS total_clean_requests
FROM service_requests;


-- 3. Count requests by department
SELECT
    department,
    COUNT(*) AS request_count
FROM service_requests
GROUP BY department
ORDER BY request_count DESC;


-- 4. Count requests by priority
SELECT
    priority,
    COUNT(*) AS request_count
FROM service_requests
GROUP BY priority
ORDER BY request_count DESC;


-- 5. Count requests by status
SELECT
    status,
    COUNT(*) AS request_count
FROM service_requests
GROUP BY status
ORDER BY request_count DESC;


-- 6. Average actual cost by department
SELECT
    department,
    ROUND(AVG(actual_cost), 2) AS avg_actual_cost
FROM service_requests
GROUP BY department
ORDER BY avg_actual_cost DESC;


-- 7. Total actual cost by department
SELECT
    department,
    SUM(actual_cost) AS total_actual_cost
FROM service_requests
GROUP BY department
ORDER BY total_actual_cost DESC;


-- 8. Average customer satisfaction by department
SELECT
    department,
    ROUND(AVG(customer_satisfaction_score), 2) AS avg_satisfaction_score
FROM service_requests
GROUP BY department
ORDER BY avg_satisfaction_score DESC;


-- 9. Calculate resolution time in days
SELECT
    request_id,
    department,
    request_type,
    submitted_date,
    resolution_date,
    resolution_date - submitted_date AS resolution_days
FROM service_requests
WHERE resolution_date IS NOT NULL
ORDER BY resolution_days DESC;


-- 10. Average resolution time by assigned team
SELECT
    assigned_team,
    ROUND(AVG(resolution_date - submitted_date), 2) AS avg_resolution_days
FROM service_requests
WHERE resolution_date IS NOT NULL
GROUP BY assigned_team
ORDER BY avg_resolution_days DESC;


-- 11. Cost variance by request
SELECT
    request_id,
    department,
    request_type,
    estimated_cost,
    actual_cost,
    actual_cost - estimated_cost AS cost_variance
FROM service_requests
ORDER BY cost_variance DESC;


-- 12. Requests with actual cost over estimated cost
SELECT
    request_id,
    department,
    request_type,
    estimated_cost,
    actual_cost,
    actual_cost - estimated_cost AS cost_overage
FROM service_requests
WHERE actual_cost > estimated_cost
ORDER BY cost_overage DESC;