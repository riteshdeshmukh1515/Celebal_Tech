# E-Commerce Order Analytics System

## 📌 Project Overview

The **E-Commerce Order Analytics System** is an end-to-end data engineering and analytics project built using **Python, Pandas, SQLite, and SQL**.

The project demonstrates a complete data pipeline starting from realistic e-commerce data generation and continuing through data validation, cleaning, database loading, SQL analytics, customer segmentation, RFM analysis, cohort analysis, and command-line reporting.

The system is designed to simulate a real-world e-commerce analytics workflow where raw data contains quality issues that must be identified, cleaned, validated, and transformed into business-ready information.

---

## 🎯 Objective

The objective of this project is to design and develop an end-to-end e-commerce order analytics system combining **Python and SQL**.

The system demonstrates:

- Dataset generation
- Data quality validation
- Data cleaning using Pandas
- Handling missing values
- Duplicate detection and removal
- Data type validation
- Referential integrity validation
- Relational database design
- SQLite database loading
- SQL joins and aggregations
- Window functions
- CTE-based analysis
- Cohort analysis
- Customer retention analysis
- Customer segmentation
- RFM analysis
- CLI-based reporting
- Edge-case testing
- Business-oriented analytics

---

# 🏗️ System Architecture

```text
                    ┌────────────────────────┐
                    │  Python Data Generation│
                    │      Faker / Random    │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │      Raw CSV Files      │
                    │                        │
                    │ customers.csv          │
                    │ products.csv           │
                    │ orders.csv             │
                    │ order_items.csv        │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │   Raw Data Validation   │
                    │  Data Quality Checks    │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │   Pandas Data Cleaning  │
                    │                        │
                    │ Missing Values         │
                    │ Duplicates             │
                    │ Data Types             │
                    │ Referential Integrity  │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │    Cleaned CSV Files   │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │     SQLite Database     │
                    │                        │
                    │ customers              │
                    │ products               │
                    │ orders                 │
                    │ order_items            │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │      SQL Analytics      │
                    │                        │
                    │ Aggregations           │
                    │ Window Functions       │
                    │ CTEs                   │
                    │ Cohort Analysis        │
                    │ Retention Analysis     │
                    │ RFM Analysis           │
                    │ Customer Segmentation  │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │    Python CLI Tool      │
                    │                        │
                    │ Revenue                │
                    │ Top Customers          │
                    │ Top Products           │
                    │ AOV                    │
                    │ Segments               │
                    │ RFM                    │
                    │ Retention              │
                    │ Category               │
                    └────────────────────────┘
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Data generation, cleaning, validation and CLI development |
| **Pandas** | Data cleaning and transformation |
| **Faker** | Realistic customer and product data generation |
| **Random** | Randomized test data generation and data inconsistencies |
| **SQLite** | Relational database |
| **SQL** | Business analytics and reporting |
| **Window Functions** | Ranking, running totals, moving averages and comparisons |
| **CTEs** | Multi-step SQL analysis |
| **Tabulate** | CLI table formatting |
| **Git** | Version control |
| **GitHub** | Project submission and repository management |

---

# 📂 Project Structure

```text
ASSIGNMENT_NO.8/
│
├── data/
│   ├── cleaned/
│   │   ├── customers_clean.csv
│   │   ├── order_items_clean.csv
│   │   ├── orders_clean.csv
│   │   └── products_clean.csv
│   │
│   └── raw/
│       ├── customers.csv
│       ├── order_items.csv
│       ├── orders.csv
│       └── products.csv
│
├── output/
│   ├── sample_reports/
│   │   ├── category.txt
│   │   ├── retention.txt
│   │   ├── revenue.txt
│   │   ├── rfm.txt
│   │   ├── segments.txt
│   │   ├── top_customers.txt
│   │   └── top_products.txt
│   │
│   └── cleaning_report.csv
│
├── scripts/
│   ├── check_raw_data.py
│   ├── clean_data.py
│   ├── generate_data.py
│   ├── load_database.py
│   ├── report_cli.py
│   └── run_sql.py
│
├── sql/
│   ├── aggregations.sql
│   ├── cohort_analysis.sql
│   ├── customer_segmentation.sql
│   ├── schema.sql
│   └── window_functions.sql
│
├── tests/
│   ├── test_edge_cases.py
│   ├── test_future_date.py
│   └── test_single_customer.py
│
├── Screenshots/
│
├── .gitignore
├── ecommerce.db
├── README.md
├── requirements.txt
└── setup_project.py
```

> **Note:** The `venv/` directory is used locally for the Python virtual environment and should not be committed to GitHub.

---

# 🔄 Data Engineering Pipeline

## Step 1 — Generate Realistic Data

Python is used to generate realistic e-commerce datasets using Faker and randomization.

The following datasets are generated:

- Customers
- Products
- Orders
- Order Items

The generated raw data intentionally contains data-quality problems such as:

- Missing values
- Duplicate records
- Invalid dates
- Mismatched IDs
- Referential integrity issues
- Data type inconsistencies

### Run

```bash
python scripts/generate_data.py
```

The generated files are stored in:

```text
data/raw/
```

---

# Step 2 — Validate Raw Data

Before cleaning, the raw datasets can be checked using the raw-data validation script.

The validation process checks the generated CSV files for potential data-quality issues.

### Run

```bash
python scripts/check_raw_data.py
```

This step helps identify issues before the data is processed further.

---

# Step 3 — Clean Data Using Pandas

Pandas is used to transform the raw datasets into clean, analysis-ready datasets.

The cleaning process includes:

- Handling missing values
- Removing duplicate records
- Converting data types
- Validating IDs
- Handling invalid dates
- Validating customer IDs
- Validating product IDs
- Validating order IDs
- Checking referential integrity
- Exporting cleaned datasets
- Generating a cleaning report

### Run

```bash
python scripts/clean_data.py
```

The cleaned datasets are stored in:

```text
data/cleaned/
```

The cleaning report is stored in:

```text
output/cleaning_report.csv
```

---

# Step 4 — Load Data into SQLite

The cleaned datasets are loaded into a relational SQLite database.

The database file is:

```text
ecommerce.db
```

The database contains the following tables:

```text
customers
products
orders
order_items
```

### Run

```bash
python scripts/load_database.py
```

The relationships between the tables are:

```text
customers
    │
    │ customer_id
    ▼
orders
    │
    │ order_id
    ▼
order_items
    │
    │ product_id
    ▼
products
```

### Main relationships

```text
customers.customer_id
        ↓
orders.customer_id

orders.order_id
        ↓
order_items.order_id

products.product_id
        ↓
order_items.product_id
```

The database schema is defined in:

```text
sql/schema.sql
```

---

# Step 5 — SQL Analytics: Joins and Aggregations

SQL joins and aggregations are used to generate business-level insights.

The project calculates:

- Total revenue per customer
- Total revenue per category
- Monthly revenue
- Top products by quantity sold
- Top products by revenue
- Top customers
- Average Order Value (AOV)
- Customer-level order statistics

### Run

```bash
python scripts/run_sql.py sql/aggregations.sql
```

The analysis demonstrates the use of:

- `INNER JOIN`
- `LEFT JOIN`
- `GROUP BY`
- `SUM()`
- `COUNT()`
- `AVG()`
- `ORDER BY`

---

# Step 6 — Window Functions and CTEs

Window functions are used for advanced analytical calculations.

The project demonstrates:

- Customer ranking
- Lifetime Value ranking
- Running revenue
- Moving averages
- Previous-month comparisons
- Revenue growth
- Product ranking
- Customer order sequencing

Window functions include:

```sql
RANK()
```

```sql
DENSE_RANK()
```

```sql
SUM() OVER()
```

```sql
AVG() OVER()
```

```sql
LAG()
```

```sql
ROW_NUMBER()
```

```sql
NTILE()
```

### Run

```bash
python scripts/run_sql.py sql/window_functions.sql
```

The analysis includes examples such as:

- Ranking customers by lifetime value
- Calculating cumulative revenue
- Calculating three-month moving averages
- Comparing current-month revenue with previous-month revenue
- Calculating month-over-month growth
- Ranking products within categories

---

# Step 7 — Cohort and Retention Analysis

Customers are grouped into cohorts based on their first purchase month.

The cohort analysis identifies:

- Customer cohorts
- First purchase month
- Monthly customer activity
- Repeat customers
- Retention rates
- Churn behavior
- Customer activity across months

### Run

```bash
python scripts/run_sql.py sql/cohort_analysis.sql
```

The results help answer questions such as:

- How many customers return after their first purchase?
- Which cohorts have the highest retention?
- How does customer retention change over time?
- Which customers appear to have churned?

---

# Step 8 — Customer Segmentation and RFM Analysis

Customer segmentation is performed using purchase frequency, spending behavior and RFM metrics.

## Purchase Frequency Segmentation

Customers are classified into:

```text
One-Time
Occasional
Loyal
```

## Spend Tier Segmentation

Customers are classified into:

```text
Low
Medium
High
```

## RFM Analysis

RFM analysis uses:

```text
R = Recency
F = Frequency
M = Monetary
```

### Recency

Measures how recently the customer made a purchase.

### Frequency

Measures how frequently the customer placed orders.

### Monetary

Measures how much the customer spent.

Example RFM segments include:

```text
Champions
Loyal Customers
Potential Loyalists
Regular Customers
At Risk
Lost
```

### Run

```bash
python scripts/run_sql.py sql/customer_segmentation.sql
```

---

# Step 9 — CLI Reporting Tool

A Python command-line interface is provided for dynamically generating business reports.

### Display available reports

```bash
python scripts/report_cli.py --help
```

Available reports:

```text
revenue
top_customers
top_products
aov
segments
rfm
retention
category
```

---

## 📊 Available Reports

| Report | Description |
|---|---|
| `revenue` | Monthly revenue analysis |
| `top_customers` | Highest-value customers |
| `top_products` | Best-selling products |
| `aov` | Average Order Value |
| `segments` | Customer purchase-frequency segmentation |
| `rfm` | RFM customer analysis |
| `retention` | Cohort and retention analysis |
| `category` | Revenue by product category |

---

## Revenue Report

```bash
python scripts/report_cli.py --report revenue
```

---

## Top Customers Report

```bash
python scripts/report_cli.py --report top_customers
```

---

## Top Products Report

```bash
python scripts/report_cli.py --report top_products
```

---

## Average Order Value Report

```bash
python scripts/report_cli.py --report aov
```

---

## Customer Segmentation Report

```bash
python scripts/report_cli.py --report segments
```

---

## RFM Analysis Report

```bash
python scripts/report_cli.py --report rfm
```

---

## Retention Report

```bash
python scripts/report_cli.py --report retention
```

---

## Category Revenue Report

```bash
python scripts/report_cli.py --report category
```

---

# 🧪 Step 10 — Edge Case Testing

The project includes tests for different edge cases to improve reliability.

The tests cover:

- Invalid CLI input
- Empty database
- Single customer
- Future-dated orders

---

## Invalid CLI Input

An invalid report name is rejected by the CLI.

Example:

```bash
python scripts/report_cli.py --report abc
```

The CLI validates the available report choices and displays an appropriate error message.

Valid reports are:

```text
revenue
top_customers
top_products
aov
segments
rfm
retention
category
```

---

## Empty Database Test

The project contains an empty-database edge-case test.

Run:

```bash
python tests/test_edge_cases.py
```

This verifies that the system can handle a database containing no records.

---

## Single Customer Test

Run:

```bash
python tests/test_single_customer.py
```

This tests the system with a minimal scenario containing a single customer and order.

---

## Future Date Test

Run:

```bash
python tests/test_future_date.py
```

This test verifies the detection and handling of future-dated orders.

---

# 📊 Sample Reports

Sample CLI outputs are stored in:

```text
output/sample_reports/
```

Available sample reports:

```text
category.txt
retention.txt
revenue.txt
rfm.txt
segments.txt
top_customers.txt
top_products.txt
```

These files provide examples of the analytical results generated by the system.

---

# 📄 Cleaning Report

The data-cleaning process generates a cleaning report:

```text
output/cleaning_report.csv
```

The report provides information about the data-quality processing performed during the cleaning stage.

---

# 📸 Screenshots

Screenshots demonstrating the project execution are maintained in:

```text
Screenshots/
```

Recommended screenshots for the final submission include:

1. Data generation
2. Raw data validation
3. Data cleaning
4. SQLite database loading
5. SQL aggregation results
6. Window-function results
7. Cohort/retention results
8. RFM/customer segmentation
9. CLI reports
10. Edge-case testing

---

# 📦 Installation

## 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd ASSIGNMENT_NO.8
```

---

## 2. Create a Virtual Environment

On Windows:

```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

```bash
venv\Scripts\activate
```

After activation, the terminal should display:

```text
(venv)
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Complete Project

Run the project in the following order.

## 1. Generate Data

```bash
python scripts/generate_data.py
```

---

## 2. Validate Raw Data

```bash
python scripts/check_raw_data.py
```

---

## 3. Clean Data

```bash
python scripts/clean_data.py
```

---

## 4. Load Data into SQLite

```bash
python scripts/load_database.py
```

---

## 5. Run SQL Aggregations

```bash
python scripts/run_sql.py sql/aggregations.sql
```

---

## 6. Run Window Functions

```bash
python scripts/run_sql.py sql/window_functions.sql
```

---

## 7. Run Cohort Analysis

```bash
python scripts/run_sql.py sql/cohort_analysis.sql
```

---

## 8. Run Customer Segmentation and RFM

```bash
python scripts/run_sql.py sql/customer_segmentation.sql
```

---

## 9. Run CLI Reports

For example:

```bash
python scripts/report_cli.py --report revenue
```

```bash
python scripts/report_cli.py --report top_customers
```

```bash
python scripts/report_cli.py --report top_products
```

```bash
python scripts/report_cli.py --report aov
```

```bash
python scripts/report_cli.py --report segments
```

```bash
python scripts/report_cli.py --report rfm
```

```bash
python scripts/report_cli.py --report retention
```

```bash
python scripts/report_cli.py --report category
```

---

## 10. Run Edge-Case Tests

```bash
python tests/test_edge_cases.py
```

```bash
python tests/test_single_customer.py
```

```bash
python tests/test_future_date.py
```

---

# 🔁 Complete Pipeline Summary

```text
1. Generate Data
       ↓
2. Validate Raw Data
       ↓
3. Clean Data using Pandas
       ↓
4. Export Cleaned CSV Files
       ↓
5. Load Data into SQLite
       ↓
6. Run SQL Aggregations
       ↓
7. Run Window Functions and CTEs
       ↓
8. Perform Cohort Analysis
       ↓
9. Perform Customer Segmentation
       ↓
10. Perform RFM Analysis
       ↓
11. Generate CLI Reports
       ↓
12. Run Edge-Case Tests
       ↓
13. Document and Submit
```

---

# 📈 Business Insights Generated

The system can answer important e-commerce business questions such as:

- Which customers generate the most revenue?
- Which products sell the most units?
- Which products generate the highest revenue?
- Which categories generate the most revenue?
- What is the monthly revenue trend?
- What is the Average Order Value?
- Which customers are loyal?
- Which customers are one-time buyers?
- Which customers have high monetary value?
- Which customers are at risk of churn?
- Which customers have recently purchased?
- How well are customer cohorts being retained?
- Which customer segments should be targeted for marketing campaigns?
- Which customers should be prioritized for retention campaigns?

---

# 🎯 Key Data Engineering Concepts Demonstrated

This project demonstrates practical knowledge of:

### Data Engineering

- ETL pipeline development
- Data generation
- Data ingestion
- Data cleaning
- Data validation
- Data quality management
- Referential integrity
- Data transformation

### Python

- Python scripting
- Pandas
- Faker
- File handling
- Exception handling
- CLI development
- Argument parsing
- Automated testing

### Database

- Relational database design
- SQLite
- Primary keys
- Foreign keys
- Constraints
- Table relationships

### SQL

- SELECT
- WHERE
- GROUP BY
- ORDER BY
- JOINs
- Aggregations
- CTEs
- Window functions
- RANK
- DENSE_RANK
- ROW_NUMBER
- NTILE
- LAG
- Running totals
- Moving averages

### Analytics

- Revenue analysis
- Product analysis
- Customer analysis
- Cohort analysis
- Retention analysis
- Customer segmentation
- RFM analysis
- Churn analysis
- Average Order Value

### Software Engineering

- Modular project structure
- Command-line interface
- Input validation
- Error handling
- Edge-case testing
- Documentation
- Version control

---

# 🔐 Data Quality and Reliability

The project intentionally introduces data-quality problems during data generation to simulate real-world data engineering scenarios.

The pipeline then identifies and handles these problems during the validation and cleaning stages.

Examples include:

```text
Missing values
Duplicate records
Invalid dates
Invalid IDs
Mismatched foreign keys
Incorrect data types
Empty datasets
Future-dated records
```

This demonstrates that the project is not only focused on analytics but also on building a reliable data pipeline.

---

# 📁 Output Files

The project produces the following major outputs:

```text
data/raw/
    ├── customers.csv
    ├── products.csv
    ├── orders.csv
    └── order_items.csv

data/cleaned/
    ├── customers_clean.csv
    ├── products_clean.csv
    ├── orders_clean.csv
    └── order_items_clean.csv

output/
    ├── cleaning_report.csv
    └── sample_reports/
        ├── category.txt
        ├── retention.txt
        ├── revenue.txt
        ├── rfm.txt
        ├── segments.txt
        ├── top_customers.txt
        └── top_products.txt

ecommerce.db
```

---

# 🚀 Future Improvements

The current system can be extended with additional data engineering and analytics capabilities such as:

- PostgreSQL integration
- MySQL integration
- Apache Spark processing
- Delta Lake integration
- Data visualization dashboards
- Power BI integration
- Apache Airflow orchestration
- Cloud storage integration
- Automated data pipelines
- Incremental data loading
- Real-time analytics
- Advanced customer prediction models

---

# 👨‍💻 Author

**Ritesh Deshmukh**

**E-Commerce Order Analytics System**

A data engineering project demonstrating an end-to-end workflow using:

**Python + Pandas + SQLite + SQL + Data Analytics**

---

## ⭐ Project Summary

This project demonstrates how raw e-commerce data can be transformed into meaningful business insights through a structured data engineering pipeline.

```text
Raw Data
   ↓
Validation
   ↓
Cleaning
   ↓
Database
   ↓
SQL Analytics
   ↓
Customer Segmentation
   ↓
RFM & Cohort Analysis
   ↓
CLI Reports
   ↓
Business Insights
```

**End-to-end E-Commerce Data Engineering & Analytics Pipeline**