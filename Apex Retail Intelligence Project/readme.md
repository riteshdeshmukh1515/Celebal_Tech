# 🛒 APEX Retail Intelligence — End-to-End Data Engineering Pipeline

An end-to-end **Retail Data Engineering and Analytics Pipeline** built using **Databricks, PySpark, Delta Lake, SQL, and Unity Catalog**.

The project demonstrates how raw retail data can be transformed into clean, validated, reliable, and analytics-ready data using modern data engineering practices.

---

## 📌 Table of Contents

* [Project Overview](#-project-overview)
* [Objectives](#-objectives)
* [Technology Stack](#-technology-stack)
* [Project Workflow](#-project-workflow)
* [Dataset](#-dataset)
* [Data Engineering Process](#-data-engineering-process)
* [Data Quality](#-data-quality)
* [Delta Lake and MERGE](#-delta-lake-and-merge)
* [SCD Type 1 and Type 2](#-scd-type-1-and-type-2)
* [Gold Star Schema](#-gold-star-schema)
* [Unity Catalog](#-unity-catalog)
* [Analytics and KPI Reporting](#-analytics-and-kpi-reporting)
* [RFM Analysis](#-rfm-analysis)
* [Cohort Retention Analysis](#-cohort-retention-analysis)
* [Data Reconciliation](#-data-reconciliation)
* [Final Pipeline Validation](#-final-pipeline-validation)
* [Project Structure](#-project-structure)
* [How to Run](#-how-to-run)
* [Key Learnings](#-key-learnings)
* [Future Improvements](#-future-improvements)
* [Conclusion](#-conclusion)

---

# 📖 Project Overview

The **APEX Retail Data Engineering Pipeline** processes retail customer, product, and sales data through multiple stages of data transformation and validation.

The pipeline starts with raw CSV data and transforms it into structured analytical datasets using PySpark and Delta Lake.

The final Gold layer follows a **Star Schema** containing customer, product, promotion, and date dimensions connected to a sales fact table.

The project also performs business analytics such as:

* Sales KPI reporting
* Customer analysis
* Product analysis
* Revenue analysis
* RFM customer segmentation
* Cohort retention analysis
* Data reconciliation
* Final data-quality auditing

---

# 🎯 Objectives

The primary objectives of the project are:

1. Build an end-to-end retail data engineering pipeline.
2. Process raw CSV files using PySpark.
3. Convert raw data into Parquet format.
4. Perform data cleaning and validation.
5. Implement incremental processing.
6. Use Delta Lake for reliable data storage.
7. Implement Delta MERGE operations.
8. Implement SCD Type 1 and Type 2 concepts.
9. Generate surrogate keys for dimension tables.
10. Build a Gold-layer Star Schema.
11. Register analytical tables in Unity Catalog.
12. Perform sales and customer analytics.
13. Implement RFM analysis.
14. Implement cohort retention analysis.
15. Perform end-to-end reconciliation.
16. Implement final pipeline auditing and validation.

---

# 🛠️ Technology Stack

| Technology        | Purpose                                   |
| ----------------- | ----------------------------------------- |
| **Databricks**    | Data engineering and analytics platform   |
| **PySpark**       | Distributed data processing               |
| **Python**        | Pipeline and transformation logic         |
| **SQL**           | Data querying and validation              |
| **Delta Lake**    | Reliable transactional storage            |
| **Unity Catalog** | Table registration and governance         |
| **Parquet**       | Columnar data storage                     |
| **GitHub**        | Version control and project documentation |

---

# 🔄 Project Workflow

```text
                    Raw CSV Data
                         │
                         ▼
              Raw / Inbound Processing
                         │
                         ▼
                 CSV Validation
                         │
                         ▼
                 Parquet Conversion
                         │
                         ▼
                Data Cleaning & DQ
                         │
                         ▼
               Incremental Processing
                         │
                         ▼
                    Delta Lake
                         │
                         ▼
                  Delta MERGE
                         │
                         ▼
                SCD Type 1 / Type 2
                         │
                         ▼
              Surrogate Key Generation
                         │
                         ▼
                   GOLD LAYER
                         │
                         ▼
                  Star Schema
                         │
                         ▼
                  Unity Catalog
                         │
                         ▼
              KPI & Business Analytics
                         │
                         ▼
                RFM + Cohort Analysis
                         │
                         ▼
             Reconciliation & Validation
                         │
                         ▼
                 Final Pipeline Audit
```

---

# 📊 Dataset

The project works with three major business entities:

### 👤 Customer Data

Contains customer attributes such as:

* Customer ID
* Age
* Gender
* Income Bracket
* Loyalty Program
* Membership Years
* Churn Status
* Marital Status
* Number of Children
* Education Level
* Occupation
* ZIP Code
* City
* State

### 📦 Product Data

Contains product master information used for product-level analysis.

### 🧾 Sales Data

Contains retail transaction information such as:

* Transaction ID
* Transaction Date
* Customer ID
* Product ID
* Quantity
* Unit Price
* Discount
* Payment Method
* Store Location
* Transaction Hour
* Day of Week
* Week of Year
* Month
* Total Sales
* Promotion ID
* Promotion Type
* Holiday/Season Information
* Weekend Indicator

---

# 🏗️ Data Engineering Process

## 1. Raw / Inbound Processing

The pipeline begins by ingesting raw CSV files.

### Activities

* CSV ingestion
* Schema inspection
* Column validation
* Data type inspection
* Raw data organization
* Initial quality checks
* Parquet conversion

---

## 2. Parquet Processing

Raw CSV datasets are converted into Parquet format.

Parquet provides:

* Columnar storage
* Efficient compression
* Faster analytical queries
* Better performance compared with raw CSV

---

## 3. Data Cleaning

Data cleaning was performed for customer, product, and sales datasets.

### Customer Cleaning

* Data type correction
* NULL validation
* Duplicate validation
* Customer ID validation
* Attribute validation

### Product Cleaning

* Product ID validation
* Product attribute validation
* NULL checks
* Duplicate checks

### Sales Cleaning

* Transaction ID validation
* Transaction date validation
* Quantity validation
* Price validation
* Discount validation
* Revenue validation
* Duplicate transaction detection

---

# 🔍 Data Quality Validation

Data quality checks were performed throughout the pipeline.

The project validates:

```text
NULL Values
Duplicate Records
Primary Keys
Transaction IDs
Data Types
Foreign Keys
Quantity
Revenue
Reference Integrity
```

The final pipeline validation confirmed:

```text
Customer Data Quality : PASS
Product Data Quality  : PASS
Sales Data Quality    : PASS
```

---

# ⚡ Incremental Processing

Incremental processing was implemented to avoid unnecessarily processing the complete dataset during every execution.

The pipeline identifies new or changed records and processes them accordingly.

This approach improves:

* Processing efficiency
* Scalability
* Pipeline performance
* Maintainability

---

# 🧱 Delta Lake

Delta Lake is used for reliable data storage and transformation.

The project uses Delta Lake features including:

* ACID transactions
* Schema management
* Reliable writes
* Incremental processing
* MERGE operations
* Historical data management

---

# 🔀 Delta MERGE

Delta MERGE was implemented for incremental insert/update processing.

The general workflow is:

```text
Incoming Data
      │
      ▼
Compare with Existing Data
      │
      ├── Existing Record → UPDATE
      │
      └── New Record      → INSERT
```

This enables efficient incremental data processing.

---

# 🕒 SCD Type 1 and Type 2

Slowly Changing Dimension techniques were applied to dimension processing.

## SCD Type 1

SCD Type 1 updates the existing value without maintaining historical versions.

```text
Old Value
    ↓
Updated Value
```

## SCD Type 2

SCD Type 2 preserves historical versions of dimension records.

```text
Customer Version 1
        ↓
Customer Updated
        ↓
Customer Version 2
```

This allows historical analysis of changing customer or dimension attributes.

---

# 🔑 Surrogate Keys

Surrogate keys were generated for the Gold dimensions.

The major surrogate keys include:

```text
customer_sk
product_sk
promotion_sk
date_sk
```

These keys provide stable relationships between dimensions and the `fact_sales` table.

---

# ⭐ Gold Star Schema

The final analytical model follows a **Star Schema**.

```text
                    dim_customer
                         │
                         │
                         ▼
dim_product ───────► fact_sales ◄─────── dim_promotion
                         │
                         │
                         ▼
                      dim_date
```

## Dimension Tables

### `dim_customer`

Customer master dimension containing customer attributes and `customer_sk`.

### `dim_product`

Product master dimension containing product attributes and `product_sk`.

### `dim_promotion`

Promotion dimension containing promotion information and `promotion_sk`.

### `dim_date`

Date dimension containing calendar attributes and `date_sk`.

## Fact Table

### `fact_sales`

Contains transaction-level sales information and foreign keys connecting the fact table to the dimensions.

---

# 🧩 Unknown Dimension Handling

During data-quality validation, some sales records referenced dimension values that were not available in the master data.

Instead of leaving foreign keys NULL, the project uses an **Unknown Dimension Member**.

### Unknown Product

```text
product_sk = -1
```

### Unknown Date

```text
date_sk = -1
```

This maintains referential integrity while preserving the original transaction.

For example, 64 transactions contained:

```text
transaction_date = "-"
```

These invalid dates were not replaced with an artificial date.

Instead, they were assigned:

```text
date_sk = -1
```

while the original source value was retained for auditing.

---

# 🗂️ Unity Catalog

The Gold tables are registered under:

```text
apex_retail.gold
```

The main Gold tables are:

```text
dim_customer
dim_product
dim_promotion
dim_date
fact_sales
gold_kpi
sales_gold
```

Unity Catalog provides centralized management and governance of the analytical tables.

---

# 📈 Gold KPI Reporting

Business-ready KPIs were generated from the Gold layer.

## Overall KPIs

* Total Revenue
* Total Transactions
* Total Quantity Sold
* Average Order Value

## Business Analysis

* Revenue by Store
* Revenue by Promotion
* Monthly Revenue
* Payment Method Analysis
* Customer Revenue Analysis
* Product Revenue Analysis
* Top Products

A dedicated KPI table was created:

```text
gold_kpi
```

---

# 👥 Customer Analytics

Customer-level analysis was performed using the fact and customer dimension.

Metrics include:

* Transaction frequency
* Total revenue
* Quantity purchased
* Customer contribution
* Customer-level performance

---

# 🎯 RFM Analysis

RFM analysis was implemented to segment customers based on three dimensions.

### Recency

How recently a customer purchased.

### Frequency

How frequently a customer purchased.

### Monetary

How much revenue a customer generated.

RFM analysis helps identify:

* High-value customers
* Loyal customers
* Recent customers
* At-risk customers
* Low-engagement customers

---

# 📅 Cohort Retention Analysis

Cohort analysis was implemented to evaluate customer retention over time.

Customers were grouped based on their first purchase period.

The retention matrix uses:

```text
cohort_month
cohort_month_number
retention_percentage
```

This analysis helps understand:

* Customer retention
* Repeat purchases
* Cohort performance
* Customer engagement over time

---

# 🔄 Data Reconciliation

Reconciliation was performed between the processed sales data and the final fact table.

The following metrics were compared:

* Record count
* Total quantity
* Total revenue

Final result:

```text
Sales Reconciliation : PASS
```

Customer and product reconciliation checks were also performed.

---

# 🔐 Final Data Quality Validation

The final `fact_sales` table was checked for NULL foreign keys.

Final validation:

```text
NULL Customer SKs  : 0
NULL Product SKs   : 0
NULL Promotion SKs : 0
NULL Date SKs      : 0
```

Transaction validation:

```text
NULL Transaction IDs      : 0
Duplicate Transaction IDs : 0
```

This confirms the final fact table maintains referential and transaction-level integrity.

---

# 🧪 Final Pipeline Audit

The final audit validates the complete pipeline.

The following checks are included:

```text
Customer Data Quality
Product Data Quality
Sales Data Quality
Star Schema Foreign Keys
Transaction Validation
Sales Reconciliation
Gold Table Structure
```

Expected final result:

```text
============================================================
          APEX RETAIL FINAL PIPELINE AUDIT
============================================================

Customer Data Quality      : PASS
Product Data Quality       : PASS
Sales Data Quality         : PASS
Star Schema Foreign Keys   : PASS
Transaction Validation     : PASS
Sales Reconciliation       : PASS
Gold Table Structure       : PASS

============================================================
FINAL PIPELINE STATUS: PASS
APEX RETAIL PIPELINE COMPLETED SUCCESSFULLY
============================================================
```

---

# 📁 Project Structure

Recommended GitHub repository structure:

```text
APEX-Retail-Data-Engineering/
│
├── README.md
│
├── notebooks/
│   └── updated_Apex_retail_intelligence.py
│   └── Apex_retail_intelligence.py
│
├── Dataset/

│
├── screenshots/
|
├── Output/
│
└── docs/
    └── APEX_Retail_Detailed_Documentation.pdf
```

> Large raw datasets and complete Delta/Parquet storage files should generally not be committed to GitHub. Use sample data where appropriate.

---

# ▶️ How to Run

## Prerequisites

You need:

* Databricks workspace
* Compute/cluster
* Unity Catalog access
* PySpark
* Delta Lake support
* SQL support

## Step 1 — Create the Catalog and Schema

The project uses:

```text
Catalog: apex_retail
Schema : gold
```

## Step 2 — Upload the Notebook

Upload:

```text
notebooks/APEX_Retail_Data_Engineering.py
```

to Databricks.

## Step 3 — Configure Input Data

Provide the required customer, product, and sales CSV files.

## Step 4 — Execute the Notebook

Run the notebook sequentially from:

```text
Raw → Processing → Validation → Gold → Analytics → Audit
```

## Step 5 — Verify Gold Tables

Run:

```sql
SHOW TABLES IN apex_retail.gold;
```

Expected tables include:

```text
dim_customer
dim_product
dim_promotion
dim_date
fact_sales
gold_kpi
sales_gold
```

## Step 6 — Run Final Audit

Execute the final pipeline validation cell.

The target result is:

```text
FINAL PIPELINE STATUS: PASS
```

---

# 📸 Execution Evidence

The project includes screenshots demonstrating important pipeline stages.

Recommended screenshots:

| Screenshot     | Purpose                       |
| -------------- | ----------------------------- |
| Raw Processing | CSV ingestion and processing  |
| Data Quality   | NULL and duplicate validation |
| Delta MERGE    | Insert/update processing      |
| SCD            | SCD Type 1/2 processing       |
| Star Schema    | Gold data model               |
| KPI Reporting  | Business KPIs                 |
| RFM            | Customer segmentation         |
| Cohort         | Retention matrix              |
| Final Audit    | Final PASS result             |

---

# 🧠 Key Learnings

This project provided practical experience with:

* PySpark DataFrames
* Spark transformations
* Spark SQL
* Data cleaning
* Data-quality frameworks
* Incremental data processing
* Delta Lake
* Delta MERGE
* SCD Type 1
* SCD Type 2
* Surrogate key generation
* Dimensional modeling
* Star Schema
* Unity Catalog
* KPI development
* Customer segmentation
* RFM analysis
* Cohort analysis
* Data reconciliation
* Pipeline auditing

---

# 🚀 Future Improvements

Possible improvements include:

1. Implement a dedicated Bronze layer for raw Delta ingestion.
2. Add automated pipeline scheduling.
3. Add Databricks Workflows for orchestration.
4. Add automated data-quality monitoring.
5. Add alerts for failed validation checks.
6. Create Power BI/Tableau dashboards.
7. Add CI/CD using GitHub Actions.
8. Add automated unit and integration tests.
9. Add data lineage and governance documentation.
10. Add performance optimization using partitioning and Z-Ordering where appropriate.

---

# 🏆 Conclusion

The **APEX Retail Data Engineering Pipeline** demonstrates a complete data engineering workflow from raw retail data to business-ready analytics.

The project combines:

```text
PySpark
+
Databricks
+
Delta Lake
+
SQL
+
Unity Catalog
+
Dimensional Modeling
+
Data Quality
+
Business Analytics
```

The final Gold layer provides reliable data for:

* Sales reporting
* Revenue analysis
* Customer analysis
* Product analysis
* Promotion analysis
* KPI reporting
* RFM segmentation
* Cohort retention analysis

The pipeline also includes reconciliation and final data-quality auditing to ensure that the transformed data remains accurate and reliable.

---

# ✅ Project Status

```text
============================================================
              APEX RETAIL PROJECT
============================================================

Raw Processing              : COMPLETED
Data Cleaning               : COMPLETED
Data Quality                : PASS
Incremental Processing      : COMPLETED
Delta Lake                  : COMPLETED
Delta MERGE                 : COMPLETED
SCD Type 1                  : COMPLETED
SCD Type 2                  : COMPLETED
Surrogate Keys              : COMPLETED
Gold Star Schema            : COMPLETED
Unity Catalog               : COMPLETED
KPI Reporting               : COMPLETED
RFM Analysis                : COMPLETED
Cohort Retention            : COMPLETED
Data Reconciliation         : PASS
Final Data Quality          : PASS
Final Pipeline Audit        : PASS

============================================================
        APEX RETAIL PIPELINE COMPLETED SUCCESSFULLY
============================================================
```

---

## 👨‍💻 Author

**Ritesh Deshmukh**

Data Engineering Project
Built using Databricks, PySpark, Delta Lake, SQL, and Unity Catalog.
