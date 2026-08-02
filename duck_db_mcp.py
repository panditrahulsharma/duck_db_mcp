from mcp.server.fastmcp import FastMCP
import os
import duckdb
import pandas as pd

# Create MCP server
mcp = FastMCP("DuckDB SQL Server")


# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, 'employee.duckdb')


def main() -> None:
    """Run the MCP server."""
    mcp.run()


@mcp.tool()
def run_sql(sql: str) -> str:
    """
    Execute a SQL query against DuckDB and return the result as a table.

    Tables:
        employee
        salary
        attendance
        department

    Table Schemas:
        employee:
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
        salary:
            salary_id INTEGER PRIMARY KEY,
            employee_id INTEGER,
            basic_salary DECIMAL(10,2),
            bonus DECIMAL(10,2),
            deductions DECIMAL(10,2),
            tax DECIMAL(10,2),
            net_salary DECIMAL(10,2),
            pay_month VARCHAR
        attendance:
            attendance_id INTEGER PRIMARY KEY,
            employee_id INTEGER,
            attendance_date DATE,
            check_in TIME,
            check_out TIME,
            status VARCHAR
        department:
            department_id INTEGER PRIMARY KEY,
            department_name VARCHAR,
            location VARCHAR    

    Args:
        sql: SQL query to execute.

    Returns:
        Query result formatted as a Markdown table.
    """

    try:
        conn = duckdb.connect(DB_PATH)

        df = conn.execute(sql).fetchdf()

        conn.close()

        if df.empty:
            return "✅ Query executed successfully.\n\nNo rows returned."

        return df.to_markdown(index=False)

    except Exception as e:
        return f"❌ SQL Error:\n{e}"


if __name__ == "__main__":
    main()