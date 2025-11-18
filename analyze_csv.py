import pandas as pd
import numpy as np

df = pd.read_csv('sales_data.csv')

print("show first 5 rows")
print(df.head())

print("show last 5 rows")
print(df.tail())

print("\nRow and column count")
print(f"  {df.shape[0]} rows and {df.shape[1]} columns")

print("\nall column names:")
print(f"{list(df.columns)}")

print("\ndata type of each column")
print(df.dtypes)

print("\nSummary:")
df.info()

print("\nCalculate statistics:")
print(df.describe())

print('=' * 60)
print(" ")
print('=' * 60)

print("\nCount how many empty/missing values are in each column")
missing = df.isnull().sum()
print(missing)

print("\nChecking for duplicates")
duplicates = df.duplicated().sum()
print(f"   Total duplicate rows: {duplicates}")

df_clean = df.copy() # copy of the dataframe for cleaning

df_clean['quantity'] = df_clean['quantity'].fillna(1) # For any missing quantity, filled it with 1

print(f"\nRemaining missing values in quantity: {df_clean['quantity'].isnull().sum()}")

print('=' * 60)
print(" ")
print('=' * 60)

df_clean['date'] = pd.to_datetime(df_clean['date'])
print("✅ Converted to datetime format")

df_clean['revenue'] = df_clean['quantity'] * df_clean['price']
print("✅ Created 'revenue' column (quantity * price)")

df_clean['month'] = df_clean['date'].dt.month
print("✅ Extracted month from date")

df_clean['day_name'] = df_clean['date'].dt.day_name()
print("✅ Extracted day_name")

print("\n📊 New columns added:")
print(df_clean[['order_id', 'quantity', 'price', 'revenue', 'month', 'day_name']].head())

print(" ")
print('=' * 60)
print(" ")
print('=' * 60)

print("Revenue by category:")
revenue_by_category = df_clean.groupby('category')['revenue'].sum().sort_values(ascending=False)
print(revenue_by_category)

print("\nOrders by status:")
orders_by_status = df_clean['status'].value_counts()
print(orders_by_status)

print("\nTop 5 customers by spending:")
top_customers = df_clean[df_clean['customer_id'].notna()].groupby('customer_name').agg({
    'revenue': 'sum',
    'order_id': 'count'
}).rename(columns={'order_id': 'num_orders'}).sort_values('revenue', ascending=False).head()
print(top_customers)

print("\nRevenue by region:")
revenue_by_region = df_clean.groupby('region').agg({
    'revenue': 'sum',
    'order_id': 'count',
    'quantity': 'sum'
}).rename(columns={'order_id': 'num_orders'})
revenue_by_region['avg_order_value'] = revenue_by_region['revenue'] / revenue_by_region['num_orders']
print(revenue_by_region.round(2))

print("\nTop 5 most popular products:")
top_products = df_clean.groupby('product').agg({
    'quantity': 'sum',
    'order_id': 'count',
    'revenue': 'sum'
}).rename(columns={'order_id': 'times_ordered'}).sort_values('times_ordered', ascending=False).head()
print(top_products)

print("\nRevenue by month:")
monthly_revenue = df_clean.groupby('month')['revenue'].sum()
print(monthly_revenue)

print("\n📊 Overall statistics:")
print(f"  Total Revenue: ${df_clean['revenue'].sum():,.2f}")
print(f"  Average Order Value: ${df_clean['revenue'].mean():,.2f}")
print(f"  Total Orders: {len(df_clean)}")
print(f"  Total items sold: {df_clean['quantity'].sum():.0f}")

print(" ")
print('=' * 60)
print(" ")
print('=' * 60)

print("\nHigh value orders:")
high_value = df_clean[df_clean['revenue'] > 500][['order_id', 'product', 'revenue', 'customer_name']]
print(high_value)

print("\nElectronics in North Region:")
electronics_north = df_clean[(df_clean['category'] == 'Electronics') & (df_clean['region'] == 'North')][
    ['order_id', 'product', 'price', 'customer_name']
]
print(electronics_north)

print("\n⚠️ Orders that are Pending or Cancelled:")
problematic_orders = df_clean[df_clean['status'].isin(['Pending', 'Cancelled'])][
    ['order_id', 'customer_name', 'status', 'revenue']
]
print(problematic_orders)

print(" ")
print('=' * 60)
print(" ")
print('=' * 60)

print("\n📊 Pivot Table: Revenue by Category and Region:")
pivot = df_clean.pivot_table(
    values='revenue',
    index='category',
    columns='region',
    aggfunc='sum',
    fill_value=0
)
print(pivot.round(2))

print("\nCorrelation between Quantity and Revenue:")
correlation = df_clean[['quantity', 'price', 'revenue']].corr()
print(correlation.round(3))

print(" ")
print('=' * 60)
print(" ")
print('=' * 60)

df_clean.to_csv("/Users/zautt/Desktop/Projects/data-analysis-tool-csv/outputs/sales_data_cleaned.csv", index=False)
print("✅ Category summary saved to: /outputs/sales_data_cleaned.csv")

revenue_by_category.to_csv("/Users/zautt/Desktop/Projects/data-analysis-tool-csv/outputs/revenue_by_category.csv")
print("✅ Category summary saved to: revenue_by_category.csv")

print('=' * 60)
print("                        ✅✅✅")
print('=' * 60)