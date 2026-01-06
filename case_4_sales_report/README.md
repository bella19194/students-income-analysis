# Case 4 — Sales Revenue Report

This project demonstrates a simple data processing pipeline using pandas.

## Description
The script loads raw sales data, validates it, calculates revenue, and generates
an aggregated report by product.

## Input Data
data/sales_raw.csv contains raw sales records, including invalid rows.

A row is considered valid if:
- product is not empty
- quantity is a positive number
- price is a positive number

## Processing Steps
1. Load raw CSV data
2. Convert numeric columns and handle invalid values
3. Filter valid rows using boolean masks
4. Calculate revenue per order
5. Aggregate revenue and quantity by product
6. Identify the most profitable product

## Output
- Aggregated revenue report by product
- Total revenue
- Top product by revenue

## Technologies
- Python
- pandas

## Author
Sabira