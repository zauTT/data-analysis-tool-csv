import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("=" * 60)
print("SALES DATA VISUALIZATION")
print("=" * 60)

df = pd.read_csv('/Users/zautt/Desktop/Projects/data-analysis-tool-csv/outputs/sales_data_cleaned.csv')

df['date'] = pd.to_datetime(df['date'])
df['quantity'].fillna(1, inplace=True)
df['revenue'] = df['quantity'] * df['price']
df['month'] = df['date'].dt.strftime('%B')

print("\n✓ Data Loaded and prepared")
print(f"  Total records: {len(df)}")
print(f"  Date range: {df['date'].min()} to {df['date'].max()}")

os.makedirs('outputs/charts', exist_ok=True)

print("\n" + "=" * 60)
print("CHART1: Revenue by category (Bar Chart)")
print("=" * 60)

plt.figure(figsize=(10, 6))

category_revenue = df.groupby('category')['revenue'].sum().sort_values(ascending=False)

bars = plt.bar(category_revenue.index, category_revenue.values, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'${height:,.0f}',
             ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.title('Total Revenue by Product Category', fontsize=16, fontweight='bold')
plt.xlabel('Category', fontsize=12, fontweight='semibold')
plt.ylabel('Revenue ($)', fontsize=12, fontweight='semibold')
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

plt.grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('outputs/charts/01_revenue_by_category.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 01_revenue_by_category.png")
plt.close()

print("\n" + "=" * 60)
print("CHART2: Market share by Category (Pie Chart)")
print("=" * 60)

plt.figure(figsize=(10, 8))

colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
explode = (0.1, 0, 0)

plt.pie(category_revenue.values,
        labels=category_revenue.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        shadow=False,
        textprops={'fontsize': 12, 'fontweight': 'bold'})

plt.title('Market Share by Category', fontsize=16, fontweight='semibold', loc='left')
plt.axis('equal')

plt.tight_layout()
plt.savefig('outputs/charts/02_market_share_pie.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 02_market_share_pie.png")
plt.close()

print("\n" + "=" * 60)
print("CHART 3: Revenue by Region (Horizontal Bar)")
print("=" * 60)

plt.figure(figsize=(10, 6))

region_revenue = df.groupby('region')['revenue'].sum().sort_values()

bars = plt.barh(region_revenue.index, region_revenue.values, color='#95E1D3')

for i, (bar, value) in enumerate(zip(bars, region_revenue.values)):
    plt.text(value, i, f'  ${value:,.0f}', 
             va='center', fontsize=11, fontweight='bold')

plt.title('Total Revenue by Region', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Revenue ($)', fontsize=12, fontweight='semibold')
plt.ylabel('Region', fontsize=12, fontweight='semibold')
plt.grid(axis='x', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('outputs/charts/03_revenue_by_region.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 03_revenue_by_region.png")
plt.close()

print("\n" + "=" * 60)
print("CHART 4: Revenue Trend Over Time (Line Chart)")
print("=" * 60)

plt.figure(figsize=(12, 6))

daily_revenue = df.groupby('date')['revenue'].sum().reset_index()

plt.plot(daily_revenue['date'], daily_revenue['revenue'],
        marker='o', linewidth=2, markersize=6, color='#E74C3C')

plt.title('Daily Revenue Trend', fontsize=16, fontweight='semibold', pad=20)
plt.xlabel('Date', fontsize=12, fontweight='semibold')
plt.ylabel('Revenue ($)', fontsize=12, fontweight='semibold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, linestyle='--')

avg_revenue = daily_revenue['revenue'].mean()
plt.axhline(y=avg_revenue, color='green', linestyle='--', linewidth=2,
            label=f'Average: ${avg_revenue:.2f}')
plt.legend(fontsize=11)

plt.tight_layout()
plt.savefig('outputs/charts/04_revenue_trend.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 04_revenue_trend.png")
plt.close()

print("\n" + "=" * 60)
print("CHART 5: Orders by Status per Region (Grouped Bar)")
print("=" * 60)

plt.figure(figsize=(12, 6))

status_region = df.groupby(['region', 'status']).size().unstack(fill_value=0)

status_region.plot(kind='bar', figsize=(12, 6), width=0.8)

plt.title('Order Status Distribution by Region', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Region', fontsize=12, fontweight='semibold')
plt.ylabel('Number of Orders', fontsize=12, fontweight='semibold')
plt.xticks(rotation=0, fontsize=11)
plt.legend(title='Status', fontsize=10, title_fontsize=11)
plt.grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('outputs/charts/05_status_by_region.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 05_status_by_region.png")
plt.close()

print("\n" + "=" * 60)
print("CHART 6: Price vs Quantity (Scatter Plot)")
print("=" * 60)

plt.figure(figsize=(10, 6))

categories = df['category'].unique()
colors_map = {'Electronics': '#FF6B6B', 'Furniture': '#4ECDC4', 'Stationery': '#45B7D1'}

for category in categories:
    subset = df[df['category'] == category]
    plt.scatter(subset['quantity'], subset['price'],
    label=category, alpha=0.6, s=100,
    color=colors_map.get(category, 'gray'))

plt.title('Price vs Quantity Relationship', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Quantity', fontsize=12, fontweight='semibold')
plt.ylabel('Price ($)', fontsize=12, fontweight='semibold')
plt.legend(title='Category', fontsize=10, title_fontsize=11)
plt.grid(True, alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('outputs/charts/06_price_vs_quantity.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 06_price_vs_quantity.png")
plt.close()

print("\n" + "=" * 60)
print("CHART 7: Price Distribution (Histogram)")
print("=" * 60)

plt.figure(figsize=(10, 6))

plt.hist(df['price'], bins=15, color='#9B59B6', edgecolor='black', alpha=0.7)

plt.title('Distribution of Product Prices', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Price ($)', fontsize=12, fontweight='semibold')
plt.ylabel('Frequency (Number of Orders)', fontsize=12, fontweight='semibold')
plt.grid(axis='y', alpha=0.3, linestyle='--')

median_price = df['price'].median()
mean_price = df['price'].mean()
plt.axvline(median_price, color='red', linestyle='--', linewidth=2,
            label=f'Median: ${median_price:.2f}')
plt.axvline(mean_price, color='green', linestyle='--', linewidth=2,
            label=f'Mean: ${mean_price:.2f}')
plt.legend(fontsize=11)

plt.tight_layout()
plt.savefig('outputs/charts/07_price_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 07_price_distribution.png")
plt.close()

print("\n" + "=" * 60)
print("CHART 8: Price Range by Category (Box Plot - SEABORN)")
print("=" * 60)

plt.figure(figsize=(10, 6))

sns.boxplot(data=df, x='category', y='price', palette='Set2')

plt.title('Price Range by Category', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Category', fontsize=12, fontweight='semibold')
plt.ylabel('Price ($)', fontsize=12, fontweight='semibold')
plt.xticks(fontsize=12)
plt.grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('outputs/charts/08_price_boxplot.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 08_price_boxplot.png")
plt.close()

print("\n" + "=" * 60)
print("CHART 9: Revenue Heatmap - Category vs Region (SEABORN)")
print("=" * 60)

plt.figure(figsize=(10, 6))

pivot = df.pivot_table(values='revenue', index='category', columns='region', aggfunc='sum', fill_value=0)

sns.heatmap(pivot, annot=True, fmt='.0f', cmap='YlOrRd', linewidths=0.5, 
            cbar_kws={'label': 'Revenue ($)'})

plt.title('Revenue Heatmap: Category vs Region', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Region', fontsize=12, fontweight='semibold')
plt.ylabel('Category', fontsize=12, fontweight='semibold')

plt.tight_layout()
plt.savefig('outputs/charts/09_revenue_heatmap.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 09_revenue_heatmap.png")
plt.close()

print("\n" + "=" * 60)
print("CHART 10: Order Count by Status (Count Plot - SEABORN)")
print("=" * 60)

plt.figure(figsize=(10, 6))

sns.countplot(data=df, x='status', palette='viridis', order=df['status'].value_counts().index)

plt.title('Order Count by Status', fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Order Status", fontsize=12, fontweight='semibold')
plt.ylabel("Count", fontsize=12, fontweight='semibold')
plt.xticks(fontsize=11, rotation=0)
plt.grid(axis='y', alpha=0.3, linestyle='--')

ax =plt.gca()
for container in ax.containers:
    ax.bar_label(container, fontsize=11, fontweight='semibold')

plt.tight_layout()
plt.savefig('outputs/charts/10_status_countplot.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 10_status_countplot.png")
plt.close()

print("\n" + "=" * 60)
print("CHART 11: Revenue Composition by Region (Stacked Bar)")
print("=" * 60)

plt.figure(figsize=(12, 6))

stacked_data = df.pivot_table(values='revenue', index='region', columns='category', aggfunc='sum', fill_value=0)

stacked_data.plot(kind='bar', stacked=True, figsize=(12, 6), 
                   color=['#FF6B6B', '#4ECDC4', '#45B7D1'])

plt.title('Revenue Composition by Region', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Region', fontsize=12, fontweight='semibold')
plt.ylabel('Revenue ($)', fontsize=12, fontweight='semibold')
plt.legend(title='Category', fontsize=10, title_fontsize=11)
plt.grid(axis='y',alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('outputs/charts/11_stacked_revenue.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 11_stacked_revenue.png")
plt.close()

print("\n" + "=" * 60)
print("CHART 12: Complete Dashboard (Multiple Subplots)")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Sales Analytics Dashboard', fontsize=20, fontweight='bold', y=0.995)

category_revenue.plot(kind='bar', ax=axes[0, 0], color='#FF6B6B')
axes[0, 0].set_title('Revenue by category', fontsize=14, fontweight='semibold')
axes[0, 0].set_xlabel('Category', fontsize=11)
axes[0, 0].set_ylabel('Revenue ($)', fontsize=11)
axes[0, 0].tick_params(axis='x', rotation=0)
axes[0, 0].grid(axis='y', alpha=0.3)

region_revenue_sorted = df.groupby('region')['revenue'].sum().sort_values(ascending=False)
region_revenue_sorted.plot(kind='bar', ax=axes[0, 1], color='#4ECDC4')
axes[0, 1].set_title('Revenue by Region', fontsize=14, fontweight='semibold')
axes[0, 1].set_xlabel('Region', fontsize=11)
axes[0, 1].set_ylabel('Revenue ($)', fontsize=11)
axes[0, 1].tick_params(axis='x', rotation=0)
axes[0, 1].grid(axis='y', alpha=0.3)

status_counts = df['status'].value_counts()
status_counts.plot(kind='pie', ax=axes[1, 0], autopct='%1.1f%%', 
                   colors=['#95E1D3', '#FFEAA7', '#DFE6E9', '#FF7675'])
axes[1, 0].set_title('Order Status Distribution', fontsize=14, fontweight='bold')
axes[1, 0].set_ylabel('')

daily_revenue = df.groupby('date')['revenue'].sum()
axes[1, 1].plot(daily_revenue.index, daily_revenue.values, marker='o', 
                linewidth=2, markersize=5, color='#6C5CE7')
axes[1, 1].set_title('Daily Revenue Trend', fontsize=14, fontweight='bold')
axes[1, 1].set_xlabel('Date', fontsize=11)
axes[1, 1].set_ylabel('Revenue ($)', fontsize=11)
axes[1, 1].tick_params(axis='x', rotation=45)
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('outputs/charts/12_dashboard.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 12_dashboard.png")
plt.close()

print("\n" + "=" * 60)
print("VISUALIZATION COMPLETE! 🎉")
print("=" * 60)
