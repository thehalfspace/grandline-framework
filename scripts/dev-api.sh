#!/usr/bin/env bash
set -euo pipefail
# Launch FastAPI dev server (reload) via uvicorn
# Usage: ./scripts/dev_api.sh your_project.api.app:app
APP_PATH="${1:-your_project.api.app:app}"
exec uv run uvicorn "$APP_PATH" --host 0.0.0.0 --port 8000 --reload

