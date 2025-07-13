import polars as pl

data = pl.read_csv(
    "machine-readable-business-employment-data-mar-2025-quarter.csv",
    ignore_errors=True
)

print(data)