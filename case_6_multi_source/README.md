# Case 6 — Sales Data Ingestion & Reporting

This case demonstrates a full data ingestion pipeline for sales data coming from multiple CSV files with different schemas.

## What the pipeline does
- Reads multiple raw CSV files from data/raw
- Normalizes column names to a unified schema
- Selects only required columns
- Cleans invalid data (non-numeric, empty, negative values)
- Calculates revenue per product
- Generates an aggregated revenue report
- Saves clean data and report to separate folders

## Input
- data/raw/*.csv — raw sales files with different column names

## Output
- data/clean/sales_clean.csv — cleaned and validated sales data
- data/reports/monthly_report.csv — aggregated revenue report by product

## Technologies
- Python
- pandas
- pathlib

## Author
Sabira