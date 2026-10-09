# RetailAnalyticsHub

An end-to-end retail analytics project that transforms raw business data into measurable KPIs, data-quality insights, interactive dashboards, statistical findings, and executive-level business recommendations.

The project demonstrates a complete analytics workflow, from data profiling and preprocessing to visualization, business intelligence, and management decision support.

## 🚀 Live Interactive Dashboard

Explore the deployed Streamlit application:

**[Retail Analytics Hub — Live Dashboard](https://retailanalyticsapp-z294pv9u3tzjse8cihqgrw.streamlit.app/)**

## Tasks Completed

### Task 02 — KPI Dictionary & Data Quality Contract

#### Objective

Translate business requirements into measurable KPIs and establish a testable framework for assessing retail data quality and reliability.

#### Work Performed

* Defined 10 business-oriented KPIs.
* Documented KPI formulas, calculation logic, and data grain.
* Specified relevant filters and business conditions.
* Identified KPI ownership and refresh frequency.
* Profiled data completeness, uniqueness, validity, consistency, and freshness.
* Implemented data-quality checks using Python and Pandas.
* Checked duplicate records and missing values.
* Validated dates, quantities, and discount values.
* Defined measurable quality thresholds.
* Documented failure-handling and escalation procedures.

#### Deliverables

```text
02_KPI_Data_Quality/
├── README.md
├── KPI_Dictionary_and_DQ_Contract.xlsx
├── Retail_Data_Profile.ipynb
├── Data_Quality_Contract.md
└── data/
    ├── retail-orders-raw.csv
    └── retail-data-dictionary.csv
```

---

### Task 03 — Data Cleaning & Preprocessing

#### Objective

Prepare the retail dataset for reliable downstream analysis by identifying inconsistencies, handling missing or invalid values, and producing a cleaned analytical dataset.

#### Work Performed

* Loaded and inspected the raw retail dataset.
* Reviewed column structures and data types.
* Identified missing, inconsistent, and duplicate records.
* Standardized relevant date fields.
* Validated numerical columns and business constraints.
* Examined invalid or unexpected values.
* Applied appropriate data-cleaning transformations.
* Prepared the cleaned dataset for further analysis.
* Documented cleaning steps and important observations.

#### Deliverables

```text
03_Data_Cleaning/
├── README.md
├── Retail_Data_Cleaning.ipynb
├── cleaned_retail_data.csv
└── data/
    └── retail-orders-raw.csv
```

---

### Task 04 — Exploratory Data Analysis & Statistical Insights

#### Objective

Perform Exploratory Data Analysis (EDA) and statistical testing to discover patterns, relationships, outliers, and potential business opportunities in the retail dataset.

#### Work Performed

* Calculated descriptive statistics, including mean, median, standard deviation, minimum, maximum, and quartiles.
* Analyzed distributions of relevant numerical variables.
* Created histograms and box plots to explore distributions and potential outliers.
* Generated correlation matrices and heatmaps.
* Used scatter plots for multivariate analysis.
* Compared sales and profitability across product categories and regions, where the required fields were available.
* Formulated three business hypotheses.
* Applied Pearson correlation analysis to numerical relationships.
* Applied one-way ANOVA for category-level comparisons.
* Documented statistical results and business interpretations.
* Summarized key analytical findings.

#### Hypotheses Tested

1. **Discount vs. Profit:** Examined the relationship between discount levels and profit.
2. **Quantity vs. Sales:** Examined the relationship between order quantity and sales.
3. **Category vs. Profit:** Examined whether average profit differed across product categories.

*Note: Statistical tests and conclusions must be interpreted according to the actual dataset columns and the results produced by the notebook.*

#### Deliverables

```text
04_Exploratory_Data_Analysis/
├── README.md
├── Retail_EDA_Statistical_Insights.ipynb
└── data/
    └── retail-orders-raw.csv
```

---

### Task 05 — Interactive Business Intelligence Dashboard

#### Objective

Develop and deploy an interactive dashboard that presents retail performance metrics, trends, and category-level insights in an accessible format for business analysis.

#### Work Performed

* Developed an interactive dashboard using Streamlit and Plotly.
* Integrated the retail dataset for interactive exploration.
* Displayed important business KPIs and summary metrics.
* Created visualizations for retail performance analysis.
* Enabled users to explore sales and transaction patterns.
* Presented category-level and payment-method insights where supported by the dataset.
* Organized dashboard elements to improve readability and usability.
* Deployed the application on Streamlit Community Cloud.

#### Executive Dashboard Metrics

The reported dashboard metrics include:

* Total Revenue
* Total Transactions
* Unique Customers
* Average Order Value
* Units Sold
* Discount-Applied Transactions

#### Live Deployment

**[Open Retail Analytics Hub Dashboard](https://retailanalyticsapp-z294pv9u3tzjse8cihqgrw.streamlit.app/)**

#### Deliverables

```text
05_Interactive_Dashboard/
├── README.md
├── app.py
├── requirements.txt
└── data/
    └── retail-orders-clean.csv
```

*The file structure above is a representative layout; adjust the filenames to match the actual deployed repository.*

---

### Task 06 — Executive Decision Report & Capstone Presentation

#### Objective

Consolidate the findings from Tasks 02–05 into an executive-ready Business Intelligence report that supports data-driven management decisions and business improvement planning.

#### Work Performed

* Consolidated key findings from the analytics workflow.
* Prepared an executive KPI summary.
* Identified high-performing product categories.
* Reviewed annual performance and payment-method preferences.
* Evaluated discount usage as an area for further investigation.
* Developed strategic recommendations for category-level discounting, inventory planning, and recurring BI monitoring.
* Documented dataset limitations to avoid unsupported business conclusions.
* Prepared scenario-based ROI projections for planning.
* Connected the analytical outcomes with the deployed interactive dashboard.

#### Executive KPIs

| KPI                           | Reported Value |
| ----------------------------- | -------------: |
| Total Revenue                 |     ₹16,36,956 |
| Total Transactions            |         12,575 |
| Unique Customers              |             25 |
| Average Order Value           |        ₹130.18 |
| Units Sold                    |         69,828 |
| Discount-Applied Transactions |          33.6% |

*These figures are reported project metrics and should be reconciled with the final analytical dataset and dashboard before formal business use.*

#### Key Findings

* **Category Performance:** Butchers was identified as the highest-revenue category.
* **Annual Performance:** 2024 was identified as the strongest full year in the supplied dataset.
* **Payment Preferences:** Cash was the largest payment channel by revenue.
* **Discount Usage:** Discount usage should be monitored through controlled experiments to evaluate its business impact.
* **Data Limitations:** Profit, Customer Acquisition Cost (CAC), churn, and geographic fields are not available in the supplied dataset; therefore, these metrics have not been fabricated.

#### Strategic Recommendations

1. **Optimize Category-Level Discounting:** Evaluate discount effectiveness by category and compare business outcomes before expanding promotions.
2. **Improve Inventory and Promotions:** Use category-level performance insights to inform inventory planning and promotional priorities.
3. **Institutionalize BI Monitoring:** Maintain recurring dashboard reviews and data-quality checks to track performance and identify anomalies.

#### ROI Projection

The ROI projection uses scenario-based assumptions to evaluate potential business improvements.

**Important:** Projected ROI figures are planning assumptions, not historically measured returns. Actual pilot results should replace these assumptions before investment approval.

#### Deliverables

```text
06_Executive_Decision_Report/
├── README.md
├── Executive_Decision_Report.pdf
├── Final_Analytical_Notebook.ipynb
└── ROI_Projection.xlsx
```

*The capstone presentation should also be included if required by the internship submission guidelines.*

---

## Technology & Tools

* **Programming Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn, Plotly
* **Statistical Analysis:** SciPy
* **Interactive Dashboard:** Streamlit
* **Development Environment:** Jupyter Notebook
* **Documentation & Reporting:** Markdown, Microsoft Excel, PDF
* **Version Control:** Git and GitHub
* **Deployment:** Streamlit Community Cloud

## Analytics Workflow

```text
Raw Retail Dataset
        │
        ▼
Task 02: KPI Definition
        │
        ▼
Data Quality Profiling
        │
        ▼
Data Quality Contract
        │
        ▼
Task 03: Data Cleaning
        │
        ▼
Task 04: Exploratory Data Analysis
        │
        ▼
Statistical Analysis & Hypothesis Testing
        │
        ▼
Task 05: Interactive BI Dashboard
        │
        ▼
Task 06: Executive Decision Report
        │
        ▼
Business Recommendations & ROI Scenarios
```

## Repository Structure

```text
RetailAnalyticsHub/
│
├── README.md
│
├── 02_KPI_Data_Quality/
│   ├── README.md
│   ├── KPI_Dictionary_and_DQ_Contract.xlsx
│   ├── Retail_Data_Profile.ipynb
│   ├── Data_Quality_Contract.md
│   └── data/
│       ├── retail-orders-raw.csv
│       └── retail-data-dictionary.csv
│
├── 03_Data_Cleaning/
│   ├── README.md
│   ├── Retail_Data_Cleaning.ipynb
│   ├── cleaned_retail_data.csv
│   └── data/
│       └── retail-orders-raw.csv
│
├── 04_Exploratory_Data_Analysis/
│   ├── README.md
│   ├── Retail_EDA_Statistical_Insights.ipynb
│   └── data/
│       └── retail-orders-raw.csv
│
├── 05_Interactive_Dashboard/
│   ├── README.md
│   ├── app.py
│   ├── requirements.txt
│   └── data/
│       └── retail-orders-clean.csv
│
└── 06_Executive_Decision_Report/
    ├── README.md
    ├── Executive_Decision_Report.pdf
    ├── Final_Analytical_Notebook.ipynb
    └── ROI_Projection.xlsx
```

*Ensure the repository structure matches the files actually committed to GitHub. Do not create duplicate or placeholder files solely to match this example.*

## Key Skills Demonstrated

* Data Analytics and Business Intelligence
* KPI Definition and Business Metrics
* Data Profiling and Quality Assessment
* Data Cleaning and Preprocessing
* Exploratory Data Analysis
* Statistical Analysis and Hypothesis Testing
* Correlation Analysis and ANOVA
* Data Visualization and Dashboard Development
* Python and Pandas
* Streamlit and Plotly
* Business Insight Generation
* Executive Reporting and Documentation
* Scenario-Based ROI Planning
* Git, GitHub, and Cloud Deployment

## Expected Outcomes

The project demonstrates how raw retail data can be transformed into structured analytical outputs and business-oriented insights.

* Establish measurable KPIs and data-quality expectations.
* Prepare data for consistent analysis.
* Explore statistical patterns and potential business relationships.
* Present key performance indicators through an interactive dashboard.
* Communicate findings and recommendations in an executive report.
* Use scenario-based projections to support planning without presenting assumptions as historical facts.

## Conclusion

RetailAnalyticsHub demonstrates an end-to-end retail analytics workflow, combining data-quality assessment, preprocessing, exploratory and statistical analysis, interactive Business Intelligence, and executive decision support.

The project provides a reproducible analytical foundation for understanding retail performance, identifying opportunities for improvement, and communicating findings to stakeholders.

### Areas of Interest

* Data Analytics
* Business Intelligence
* Artificial Intelligence
* Machine Learning
* Data Science
* Python Development

## Repository Status

| Task    | Description                                       | Status    |
| ------- | ------------------------------------------------- | --------- |
| Task 02 | KPI Dictionary & Data Quality Contract            | Completed |
| Task 03 | Data Cleaning & Preprocessing                     | Completed |
| Task 04 | Exploratory Data Analysis & Statistical Insights  | Completed |
| Task 05 | Interactive Business Intelligence Dashboard       | Completed |
| Task 06 | Executive Decision Report & Capstone Presentation | Completed |

**Overall Project Status:** Completed

**Live Dashboard:** [Retail Analytics Hub](https://retailanalyticsapp-z294pv9u3tzjse8cihqgrw.streamlit.app/)
