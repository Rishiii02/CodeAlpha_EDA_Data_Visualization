"""
CodeAlpha Internship — Task 3: Interactive Data Visualization Dashboard
Run: streamlit run dashboard.py
"""
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parent
df = pd.read_csv(ROOT / "data" / "retail_sales_synthetic.csv", parse_dates=["order_date"])

st.set_page_config(page_title="Retail Sales Dashboard", page_icon="📊", layout="wide")
st.title("📊 Retail Sales Analytics Dashboard")
st.caption("CodeAlpha Internship | EDA + Data Visualization | Synthetic practice dataset")

with st.sidebar:
    st.header("Filters")
    regions = st.multiselect("Region", sorted(df.region.unique()), default=sorted(df.region.unique()))
    categories = st.multiselect("Category", sorted(df.category.unique()), default=sorted(df.category.unique()))
    date_range = st.date_input("Order date range", value=(df.order_date.min().date(), df.order_date.max().date()))

filtered = df[df.region.isin(regions) & df.category.isin(categories)]
if isinstance(date_range, tuple) and len(date_range) == 2:
    filtered = filtered[(filtered.order_date.dt.date >= date_range[0]) & (filtered.order_date.dt.date <= date_range[1])]

if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Sales", f"{filtered.sales.sum():,.0f}")
c2.metric("Total Profit", f"{filtered.profit.sum():,.0f}")
c3.metric("Orders", f"{len(filtered):,}")
c4.metric("Average Order Sales", f"{filtered.sales.mean():,.0f}")

left, right = st.columns(2)
monthly = filtered.assign(month=filtered.order_date.dt.to_period("M").dt.to_timestamp()).groupby("month", as_index=False).sales.sum()
left.plotly_chart(px.line(monthly, x="month", y="sales", markers=True, title="Monthly Sales Trend"), use_container_width=True)
category = filtered.groupby("category", as_index=False).sales.sum().sort_values("sales", ascending=False)
right.plotly_chart(px.bar(category, x="category", y="sales", title="Sales by Category"), use_container_width=True)

left, right = st.columns(2)
region = filtered.groupby("region", as_index=False).sales.sum().sort_values("sales", ascending=False)
left.plotly_chart(px.bar(region, x="region", y="sales", title="Sales by Region"), use_container_width=True)
right.plotly_chart(px.scatter(filtered, x="sales", y="profit", color="category", hover_data=["product", "region"], title="Sales vs Profit"), use_container_width=True)

st.subheader("Filtered data")
st.dataframe(filtered.sort_values("order_date", ascending=False), use_container_width=True)
st.download_button("Download filtered CSV", filtered.to_csv(index=False).encode("utf-8"), "filtered_retail_sales.csv", "text/csv")
st.info("Dataset is synthetic and intended for learning/demo purposes, not business reporting.")
