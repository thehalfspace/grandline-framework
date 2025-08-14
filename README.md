# Your Project

Reusable scientific project template (Python) with FastAPI + Polars, uv, ruff, mypy, pytest, pre-commit, containers, and Open OnDemand app.

### Start a new project from this template:
```sh
cp -r project-template my-new-project
cd my-new-project
```

### Initialize env & install
```sh
uv venv
uv sync --all-extras
pre-commit install
```

### Add runtime deps later as needed
```sh
uv add numpy scipy
# or dev tools
uv add --group dev black
```

# Layout

- `src/your_project`: package code
- `assets/`: logs, figures, metadata
- `data/`: raw/interim/processed datasets
- `notebooks/`: Jupyter notebooks
- `scripts/`: CLI utilities (dev server, seeding, etc.)
- `container/`: Docker & Apptainer
- `ood-apps/`: Open OnDemand interactive app template

# Dev Tasks

- `just setup` – create venv, install deps, enable pre-commit
- `just api` – run FastAPI dev server
- `just fmt / just lint` – format & lint
- `just test` – run tests

## Quickstart
```bash
uv venv
uv sync --all-extras
pre-commit install
just seed
just api
```


