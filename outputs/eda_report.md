# Exploratory Data Analysis Report — Retail Sales

## 1. Objective
Explore a retail-sales dataset, understand its structure, check data quality, identify patterns, and communicate findings through charts.

## 2. Dataset
- File: `data/retail_sales_synthetic.csv`
- Records: 1,200 orders
- Columns: 11
- Date range: 2024-01-04 to 2025-12-31
- Important note: This is a **synthetic practice dataset generated for this internship project**. It is not real company or customer data.

## 3. Data quality checks
- Missing values: 0
- Duplicate order IDs: 0
- Data types were reviewed; `order_date` is converted to a datetime field during analysis.
- Sales and profit are numeric measures; discount is represented as a decimal fraction.

## 4. Summary findings
- Total sales: 1,008,639.84
- Total profit: 340,309.85
- Average order sales: 840.53
- Highest-sales category: Technology (644,595.72)
- Highest-sales region: North (291,814.99)
- Highest-sales month: March 2024 (60,601.92)

## 5. Visual analysis
1. `outputs/monthly_sales_trend.png` — shows monthly sales movement and seasonality-like variation.
2. `outputs/sales_by_category.png` — compares sales contribution by category.
3. `outputs/sales_by_region.png` — compares regional sales.
4. `outputs/sales_vs_profit.png` — explores the relationship between sales and profit.

## 6. Conclusion
The analysis summarizes sales performance across time, product categories, and regions. The charts make it easier to compare performance and identify areas for further investigation. These findings are illustrative because the dataset is synthetic.

## 7. Possible next steps
- Replace the sample CSV with an approved real dataset.
- Compare profit margin by category and region.
- Study the impact of discounts on profit.
- Add customer-level retention and repeat-purchase analysis.
