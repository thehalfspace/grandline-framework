FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# system deps for polars & builds
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:/root/.local/bin:${PATH}"

COPY pyproject.toml ./
RUN uv pip install --system -e ".[dev]"

COPY src/ ./src/
COPY scripts/ ./scripts/
EXPOSE 8000
CMD ["uvicorn", "your_project.api.app:app", "--host", "0.0.0.0", "--port", "8000"]

