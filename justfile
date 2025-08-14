set shell := ["bash", "-uc"]

# --- Paths & settings ---
PROJECT := "your-project"
PACKAGE := "your_project"

# --- Setup & env ---
setup:
    # Initialize virtual env and install deps (uv)
    uv venv
    uv sync --all-extras
    pre-commit install

lint:
    uv run ruff check .
    uv run ruff format --check .
    uv run mypy src

fmt:
    uv run ruff format .
    uv run ruff check --fix .

test:
    uv run pytest

api:
    ./scripts/dev_api.sh "{{PACKAGE}}.api.app:app"

seed:
    uv run python scripts/seed_data.py

nb:
    uv run python -m ipykernel install --user --name "{{PROJECT}}" --display-name "{{PROJECT}}"

clean:
    rm -rf .uv .venv dist build .pytest_cache .mypy_cache .ruff_cache

