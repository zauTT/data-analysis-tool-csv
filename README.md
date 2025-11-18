# Data Analysis Tool

A Python script for analyzing sales data from CSV files.

## Features

- Load and explore CSV data (shape, columns, data types)
- Clean data: handle missing values, check for duplicates
- Calculate new columns: revenue, month, day name
- Analyze: revenue by category/region, top customers/products
- Filter: high-value orders, pending/cancelled orders
- Generate pivot tables and correlations
- Export cleaned data to CSV

## Requirements

- Python 3.x
- pandas
- numpy

## Usage

```bash
python analyze_csv.py
```

Make sure `sales_data.csv` is in the same directory.

## Output

- `outputs/sales_data_cleaned.csv` - Cleaned dataset
- `outputs/revenue_by_category.csv` - Revenue summary