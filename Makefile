PYTHON ?= python3
UV ?= uv

.PHONY: init venv install-deps setup-db all

init:
	$(UV) init

venv:
	$(UV) venv

install-deps:
	$(UV) add "mcp[cli]" fastmcp duckdb pandas tabulate

setup-db:
	$(PYTHON) seed_employee_db.py

all: init venv install-deps setup-db
