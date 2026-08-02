## install the library
    1. uv init
    2. uv venv
    3. uv add "mcp[cli]" fastmcp duckdb pandas tabulate
    4. make setup-db

## NOTE:
  while creating an api make sure you have write the proper doc string otherwise the result may be wrong

## Test server
    mcp dev duck_db_mcp.py 
    uv run mcp dev duck_db_mcp.py     

## install mcp server 
  mcp install duck_db_mcp.py
  
## test sql
```sql
  SELECT
    e.first_name,
    e.last_name,
    d.department_name,
    s.net_salary
FROM employee e
JOIN department d
    ON e.department_id = d.department_id
JOIN salary s
    ON e.employee_id = s.employee_id
```

## claude Desktop MCP config
  mcp install duck_db_mcp.py

```json
 
    "DuckDB SQL Server": {
      "command": "/opt/homebrew/bin/uv",
      "args": [
        "run",
        "--frozen",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/Users/rahulkumar/Desktop/AI/mcp_server_learning/duck_db_mcp/duck_db_mcp.py"
      ],
        "env": {
        "VIRTUAL_ENV": "/Users/rahulkumar/Desktop/AI/mcp_server_learning/duck_db_mcp/.venv",
        "PATH": "/Users/rahulkumar/Desktop/AI/mcp_server_learning/duck_db_mcp/.venv/bin:/opt/homebrew/bin:/usr/bin:/bin"
      }
    }


```
# duck_db_mcp
# duck_db_mcp
