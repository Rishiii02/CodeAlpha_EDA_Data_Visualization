"""
CodeAlpha Internship — Task 2: Exploratory Data Analysis
Run: python analysis.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "retail_sales_synthetic.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["order_date"])
print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate order IDs:", df["order_id"].duplicated().sum())
print("\nNumeric summary:\n", df[["units_sold", "unit_price", "discount", "sales", "profit"]].describe())
print("\nSales by category:\n", df.groupby("category")["sales"].sum().sort_values(ascending=False))
print("\nSales by region:\n", df.groupby("region")["sales"].sum().sort_values(ascending=False))

monthly = df.assign(month=df.order_date.dt.to_period("M").dt.to_timestamp()).groupby("month", as_index=False).sales.sum()
plots = [
    ("monthly_sales_trend.png", monthly.month, monthly.sales, "Monthly Sales Trend", "Month", "Sales", "line"),
]
for filename, x, y, title, xlabel, ylabel, kind in plots:
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker="o")
    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel)
    plt.xticks(rotation=45); plt.tight_layout()
    plt.savefig(OUT / filename, dpi=150); plt.close()

for column, filename, title in [
    ("category", "sales_by_category.png", "Sales by Product Category"),
    ("region", "sales_by_region.png", "Sales by Region"),
]:
    values = df.groupby(column)["sales"].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 5)); plt.bar(values.index, values.values)
    plt.title(title); plt.xlabel(column.title()); plt.ylabel("Sales")
    plt.tight_layout(); plt.savefig(OUT / filename, dpi=150); plt.close()

plt.figure(figsize=(8, 5)); plt.scatter(df.sales, df.profit, alpha=.45)
plt.title("Sales vs Profit"); plt.xlabel("Sales"); plt.ylabel("Profit")
plt.tight_layout(); plt.savefig(OUT / "sales_vs_profit.png", dpi=150); plt.close()
print("\nCharts saved in outputs/.")
