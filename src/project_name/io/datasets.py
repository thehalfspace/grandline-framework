from __future__ import annotations
from pathlib import Path
import polars as pl

ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"

def csv_to_parquet(csv_name: str, parquet_name: str | None = None) -> Path:
    csv_path = DATA_RAW / f"{csv_name}.csv"
    parquet_name = parquet_name or csv_name
    out = DATA_PROCESSED / f"{parquet_name}.parquet"
    out.parent.mkdir(parents=True, exist_ok=True)
    df = pl.read_csv(csv_path)
    df.write_parquet(out)
    return out

