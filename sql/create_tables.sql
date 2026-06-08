DROP TABLE IF EXISTS service_requests;

CREATE TABLE service_requests (
    request_id VARCHAR(20) PRIMARY KEY,
    submitted_date DATE NOT NULL,
    department VARCHAR(100) NOT NULL,
    request_type VARCHAR(100) NOT NULL,
    priority VARCHAR(20) NOT NULL,
    status VARCHAR(30) NOT NULL,
    assigned_team VARCHAR(100),
    region VARCHAR(50),
    estimated_cost NUMERIC(10, 2),
    actual_cost NUMERIC(10, 2),
    resolution_date DATE,
    customer_satisfaction_score INTEGER,
    description TEXT
);