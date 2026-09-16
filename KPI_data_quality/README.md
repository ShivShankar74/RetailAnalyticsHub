Task 02 — KPI Dictionary & Data Quality Contract
Objective
Translate a retail business requirement into measurable KPIs and a testable agreement about what trustworthy data means.
Decision Owner
Head of Commerce / Operations Manager
Dataset
Retail Orders dataset supplied by RabTech Academy.
Expected grain: one row per unique `order\_id`
Deliverables
`KPI\_Dictionary\_and\_DQ\_Contract.xlsx` — KPI definitions, DQ rules, source dictionary and contract
`Retail\_Data\_Profile.ipynb` — executable data-quality profiling notebook
`Data\_Quality\_Contract.md` — human-readable quality agreement
`data/retail-orders-raw.csv` — original raw dataset
`data/retail-data-dictionary.csv` — supplied column definitions
KPIs
10 KPIs are defined:
Gross Sales
Discount Amount
Net Sales
Orders
Units Sold
Average Order Value (AOV)
Paid Order Rate
Refund Rate
Average Discount %
Units per Order
Data Quality Dimensions
Completeness
Uniqueness
Validity
Consistency
Freshness
How to Run
Open `Retail\_Data\_Profile.ipynb` in Jupyter Notebook or Google Colab.
Keep the `data` folder beside the notebook.
Run all cells.
Review the quality-check results and final contract decision.
Contract Decision
Critical data-quality failures block KPI publication until the affected records are corrected or quarantined and the profile passes again.
