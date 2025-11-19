# Data Analysis Tool

Python scripts for analyzing and visualizing sales data from CSV files.

## Features

### Analysis (analyze_csv.py)
- Load and explore CSV data (shape, columns, data types)
- Clean data: handle missing values, check for duplicates
- Calculate new columns: revenue, month, day name
- Analyze: revenue by category/region, top customers/products
- Filter: high-value orders, pending/cancelled orders
- Generate pivot tables and correlations
- Export cleaned data to CSV

### Visualization (visualize_sales.py)
- 12 different chart types (bar, pie, line, scatter, histogram, etc.)
- Seaborn plots: box plots, heatmaps, count plots
- Complete sales dashboard

## Requirements

- Python 3.x
- pandas
- numpy
- seaborn
- matplotlib

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```bash
python analyze_csv.py
python visualize_sales.py
```

Make sure `sales_data.csv` is in the same directory.

## Output

- `outputs/sales_data_cleaned.csv` - Cleaned dataset
- `outputs/revenue_by_category.csv` - Revenue summary
- `outputs/charts/` - 12 visualization charts (PNG)