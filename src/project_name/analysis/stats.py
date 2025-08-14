from __future__ import annotations
import polars as pl
from pathlib import Path

def simple_summary(parquet_path: Path) -> dict:
    df = pl.read_parquet(parquet_path)
    numeric = [c for c, dt in zip(df.columns, df.dtypes) if "Float" in str(dt) or "Int" in str(dt)]
    return {col: {"mean": float(df[col].mean()), "std": float(df[col].std())} for col in numeric}

