from pathlib import Path
import duckdb

DB_PATH = Path(__file__).with_name("employee.duckdb")

STATEMENTS = [
    """
    DROP TABLE IF EXISTS salary;
    DROP TABLE IF EXISTS attendance;
    DROP TABLE IF EXISTS employee;
    DROP TABLE IF EXISTS department;
    """,
    """
    CREATE TABLE department (
        department_id INTEGER PRIMARY KEY,
        department_name VARCHAR,
        location VARCHAR
    );
    """,
    """
    CREATE TABLE employee (
        employee_id INTEGER PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        email VARCHAR,
        phone VARCHAR,
        hire_date DATE,
        department_id INTEGER,
        job_title VARCHAR,
        manager_id INTEGER,
        status VARCHAR
    );
    """,
    """
    CREATE TABLE attendance (
        attendance_id INTEGER PRIMARY KEY,
        employee_id INTEGER,
        attendance_date DATE,
        check_in TIME,
        check_out TIME,
        status VARCHAR
    );
    """,
    """
    CREATE TABLE salary (
        salary_id INTEGER PRIMARY KEY,
        employee_id INTEGER,
        basic_salary DECIMAL(10,2),
        bonus DECIMAL(10,2),
        deductions DECIMAL(10,2),
        tax DECIMAL(10,2),
        net_salary DECIMAL(10,2),
        pay_month VARCHAR
    );
    """,
    """
    INSERT INTO department (department_id, department_name, location) VALUES
    (1, 'Engineering', 'Madrid'),
    (2, 'Human Resources', 'Barcelona'),
    (3, 'Finance', 'Valencia'),
    (4, 'Sales', 'Seville'),
    (5, 'IT Support', 'Bilbao');
    """,
    """
    INSERT INTO employee (
        employee_id,
        first_name,
        last_name,
        email,
        phone,
        hire_date,
        department_id,
        job_title,
        manager_id,
        status
    ) VALUES
    (101, 'Rahul', 'Kumar', 'rahul.kumar@company.com', '600111111', '2023-01-15', 1, 'Data Engineer', 105, 'Active'),
    (102, 'Alice', 'Johnson', 'alice.johnson@company.com', '600111112', '2022-05-20', 1, 'Senior Data Engineer', 105, 'Active'),
    (103, 'Bob', 'Smith', 'bob.smith@company.com', '600111113', '2021-09-10', 2, 'HR Specialist', 106, 'Active'),
    (104, 'Carol', 'White', 'carol.white@company.com', '600111114', '2020-03-18', 3, 'Financial Analyst', 107, 'Active'),
    (105, 'David', 'Brown', 'david.brown@company.com', '600111115', '2019-07-01', 1, 'Engineering Manager', NULL, 'Active'),
    (106, 'Emma', 'Davis', 'emma.davis@company.com', '600111116', '2018-11-12', 2, 'HR Manager', NULL, 'Active'),
    (107, 'Frank', 'Wilson', 'frank.wilson@company.com', '600111117', '2017-08-22', 3, 'Finance Manager', NULL, 'Active'),
    (108, 'Grace', 'Lee', 'grace.lee@company.com', '600111118', '2024-02-01', 4, 'Sales Executive', 109, 'Active'),
    (109, 'Henry', 'Taylor', 'henry.taylor@company.com', '600111119', '2018-04-10', 4, 'Sales Manager', NULL, 'Active'),
    (110, 'Ivy', 'Martin', 'ivy.martin@company.com', '600111120', '2023-10-05', 5, 'System Administrator', NULL, 'Active');
    """,
    """
    INSERT INTO attendance (
        attendance_id,
        employee_id,
        attendance_date,
        check_in,
        check_out,
        status
    ) VALUES
    (1, 101, '2026-07-20', '09:00:00', '18:00:00', 'Present'),
    (2, 102, '2026-07-20', '09:10:00', '18:15:00', 'Present'),
    (3, 103, '2026-07-20', '09:00:00', '17:45:00', 'Present'),
    (4, 104, '2026-07-20', NULL, NULL, 'Leave'),
    (5, 105, '2026-07-20', '08:45:00', '18:30:00', 'Present'),
    (6, 106, '2026-07-20', '09:05:00', '18:00:00', 'Present'),
    (7, 107, '2026-07-20', '09:15:00', '18:10:00', 'Present'),
    (8, 108, '2026-07-20', '09:00:00', '18:05:00', 'Present'),
    (9, 109, '2026-07-20', '08:50:00', '18:20:00', 'Present'),
    (10, 110, '2026-07-20', NULL, NULL, 'Work From Home'),
    (11, 101, '2026-07-21', '09:05:00', '18:00:00', 'Present'),
    (12, 102, '2026-07-21', NULL, NULL, 'Sick Leave'),
    (13, 103, '2026-07-21', '09:00:00', '18:00:00', 'Present'),
    (14, 104, '2026-07-21', '09:10:00', '18:10:00', 'Present'),
    (15, 110, '2026-07-21', '09:00:00', '18:00:00', 'Present');
    """,
    """
    INSERT INTO salary (
        salary_id,
        employee_id,
        basic_salary,
        bonus,
        deductions,
        tax,
        net_salary,
        pay_month
    ) VALUES
    (1, 101, 6500.00, 500.00, 150.00, 1200.00, 5650.00, '2026-07'),
    (2, 102, 7800.00, 800.00, 200.00, 1500.00, 6900.00, '2026-07'),
    (3, 103, 4200.00, 200.00, 100.00, 700.00, 3600.00, '2026-07'),
    (4, 104, 5000.00, 300.00, 150.00, 900.00, 4250.00, '2026-07'),
    (5, 105, 9500.00, 1200.00, 250.00, 2200.00, 8250.00, '2026-07'),
    (6, 106, 8800.00, 900.00, 200.00, 1900.00, 7600.00, '2026-07'),
    (7, 107, 9200.00, 1000.00, 250.00, 2100.00, 7850.00, '2026-07'),
    (8, 108, 4500.00, 700.00, 100.00, 800.00, 4300.00, '2026-07'),
    (9, 109, 9000.00, 1500.00, 300.00, 2300.00, 7900.00, '2026-07'),
    (10, 110, 6000.00, 400.00, 150.00, 1000.00, 5250.00, '2026-07');
    """,
]


def main() -> None:
    conn = duckdb.connect(DB_PATH)
    for statement in STATEMENTS:
        conn.execute(statement)

    row_count = conn.execute("SELECT COUNT(*) FROM employee").fetchone()[0]
    conn.close()

    print(f"Database ready at {DB_PATH}")
    print(f"Inserted {row_count} employees")


if __name__ == "__main__":
    main()
