# CodeAlpha Internship — Data Analytics (Tasks 2 & 3)

This repository contains two connected internship tasks:

- **Task 2: Exploratory Data Analysis (EDA)** — inspect the dataset, validate data quality, calculate descriptive statistics, and identify patterns.
- **Task 3: Data Visualization** — communicate findings with charts and an interactive Streamlit dashboard.

## Dataset
`data/retail_sales_synthetic.csv` contains 1,200 generated retail order records. It is **synthetic practice data**, not actual CodeAlpha/company/customer data. Replace it with an approved dataset if your internship coordinator requires a real-world source, and update the report accordingly.

## Project structure
```text
CodeAlpha_EDA_Data_Visualization/
├── data/
│   └── retail_sales_synthetic.csv
├── outputs/
│   ├── eda_report.md
│   ├── monthly_sales_trend.png
│   ├── sales_by_category.png
│   ├── sales_by_region.png
│   └── sales_vs_profit.png
├── analysis.py
├── dashboard.py
├── requirements.txt
└── README.md
```

## Setup (Windows)
1. Install Python 3.10 or newer.
2. Open this folder in File Explorer.
3. Click the address bar, type `cmd`, and press Enter.
4. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run Task 2 — EDA
```bash
python analysis.py
```
The script prints data-quality checks and summary statistics, and saves charts in `outputs/`.

## Run Task 3 — Interactive dashboard
```bash
streamlit run dashboard.py
```
A browser tab opens with filters for region, category, and date range.

## Tools used
Python, Pandas, Matplotlib, Plotly, and Streamlit.

## Before submission
- Run both tasks on your computer and review the results.
- Read `outputs/eda_report.md` and be prepared to explain the charts.
- If your supervisor expects a real dataset, replace the synthetic CSV with a permitted public dataset and rerun the analysis.
- Add your name and internship details to this README if required by your coordinator.
