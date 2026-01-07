# Case 5 — Data Pipeline: Raw to Clean to Report

This project demonstrates a simple data pipeline for processing subscription data.

## Description
The pipeline loads raw subscription data, validates and cleans it, and produces
an aggregated revenue report. The goal is to show a clear separation between
raw data, cleaned data, and analytical outputs.

## Data Structure
data/
├── raw/
│   └── subscriptions_raw.csv
├── clean/
│   └── subscriptions_clean.csv
└── reports/
└── revenue_report.csv

## Validation Rules
A row is considered valid if:
- plan is not empty
- months is a positive number
- price is a positive number

Invalid rows are excluded from further processing.

## Processing Steps
1. Load raw CSV data
2. Convert numeric columns and handle invalid values
3. Filter valid records using boolean masks
4. Save cleaned data to data/clean
5. Calculate revenue (`months * price`)
6. Aggregate revenue and months by subscription plan
7. Save the final report to data/reports

## Output
- Cleaned dataset ready for reuse
- Aggregated revenue report by subscription plan

## Technologies
- Python
- pandas
- pathlib

## Author
Sabira