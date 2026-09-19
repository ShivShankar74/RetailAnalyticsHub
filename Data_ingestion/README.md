# Task 03 — Retail Data Cleaning & Preprocessing

## Project Overview

This task demonstrates the complete preprocessing workflow for a real-world retail sales dataset using Python and Pandas.

The raw dataset contains more than 12,000 transaction records and includes issues such as missing values, inconsistent data types, unstandardized values, and potential outliers. The objective was to transform this raw data into a structured and analysis-ready dataset.

## Dataset Information

* **Dataset:** Retail Store Sales Dataset
* **Domain:** Retail / Sales Analytics
* **Source Format:** CSV
* **Raw Records:** 12,575
* **Raw Columns:** 11
* **Processing Tool:** Python with Pandas

### Raw Dataset

```text
data/
└── retail_store_sales.csv
```

## Work Performed

The dataset was processed through the following stages:

### 1. Data Loading and Initial Inspection

The CSV file was imported into Pandas and examined to understand:

* Number of records and columns
* Column names
* Data types
* Missing values
* Duplicate records
* Basic statistical information
* Invalid or unusual values

### 2. Data Standardization

The raw data was standardized by:

* Cleaning column names
* Removing unnecessary whitespace
* Normalizing text values
* Converting numerical fields into appropriate data types
* Converting transaction dates into datetime format
* Standardizing discount-related values

### 3. Missing Value Treatment

Missing values were handled according to the type and purpose of each field.

Examples include:

* Unknown labels for missing categorical information
* Median-based replacement for numerical fields
* Default handling for missing discount values
* Recalculation of missing transaction totals

### 4. Duplicate and Invalid Data Handling

Duplicate records were checked and removed where required.

Additional validation was performed for:

* Negative quantities
* Invalid prices
* Incorrect dates
* Invalid discount values
* Inconsistent transaction totals

### 5. Outlier Processing

The Interquartile Range (IQR) method was used to identify unusual observations in numerical columns such as:

* Price per unit
* Quantity

Detected extreme values were capped to reasonable statistical boundaries.

## Feature Engineering

Additional analytical columns were generated from the cleaned dataset:

* `year`
* `month`
* `month_name`
* `average_transaction_value`
* `discount_status`

These fields make the dataset more suitable for future reporting and exploratory analysis.

> **Note:** The original dataset does not contain a separate cost/COGS field. Therefore, a genuine profit or profit-margin calculation cannot be derived without introducing artificial assumptions. Instead, `average_transaction_value` was generated from the available transaction information.

## Final Output

The processed dataset is exported as:

```text
clean_dataset.csv
```

Final dataset status:

| Attribute      | Result |
| -------------- | -----: |
| Records        | 12,575 |
| Columns        |     15 |
| Missing Values |      0 |
| Duplicate Rows |      0 |
| Output Format  |    CSV |

## Project Structure

```text
03_Data_ingestion
│
├── README.md
├── Data_Cleaning_Preprocessing.ipynb
├── clean_dataset.csv
│
└── data/
    └── retail_store_sales.csv
```

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

## Task Outcome

The raw retail dataset was successfully converted into a clean, validated, and analysis-ready dataset. The notebook provides the complete preprocessing workflow, while `clean_dataset.csv` contains the final processed data.
