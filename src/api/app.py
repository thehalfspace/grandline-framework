from __future__ import annotations
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import polars as pl
from pathlib import Path

app = FastAPI(title="Your Project API", version="0.1.0")

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "processed"

class Summary(BaseModel):
    rows: int
    cols: int
    columns: list[str]

@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/table/{name}", response_model=Summary)
def table_summary(name: str) -> Summary:
    path = DATA_DIR / f"{name}.parquet"
    if not path.exists():
        raise HTTPException(status_code=404, detail=f"{path} not found")
    df = pl.read_parquet(path)
    return Summary(rows=df.height, cols=df.width, columns=[str(c) for c in df.columns])

@app.get("/preview/{name}")
def preview(name: str, n: int = 5) -> dict:
    path = DATA_DIR / f"{name}.parquet"
    if not path.exists():
        raise HTTPException(status_code=404, detail=f"{path} not found")
    df = pl.read_parquet(path).head(n)
    # Return JSON-safe preview
    return {"data": df.to_dict(as_series=False)}

