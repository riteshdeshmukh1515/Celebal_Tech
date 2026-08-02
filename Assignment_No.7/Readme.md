# Assignment No. 7: Delta Lake Incremental Data Processing

## Student Information

**Name:** Ritesh Deshmukh

**Course:** Data Engineering Internship

**Assignment Number:** 7

**Assignment Title:** Delta Lake Incremental Data Processing

**Tools & Technologies:** Azure Databricks, Apache Spark (PySpark), Delta Lake, Unity Catalog, Git, GitHub

---

# Objective

The objective of this assignment is to perform **incremental data processing using Delta Lake** in Azure Databricks.

The assignment demonstrates how to load data into a Delta table, clean the data, create an incremental dataset, perform the MERGE (UPSERT) operation, validate the processed data, and display the final results.

---

# Assignment Objectives

- Load a CSV dataset into a Delta table.
- Perform data cleaning by handling null values and removing duplicate records.
- Create a second dataset to simulate incremental data.
- Perform the MERGE (UPSERT) operation.
- Validate the processed data.
- Display the final dataset and summary statistics.

---

# Tools and Technologies Used

- Azure Databricks
- Apache Spark (PySpark)
- Delta Lake
- Unity Catalog Volumes
- CSV Dataset
- Git & GitHub

---

# Dataset

**Dataset Name:** Sample Superstore

The dataset contains retail sales information, including:

- Order Details
- Customer Details
- Product Details
- Sales
- Quantity
- Discount
- Profit
- Region
- Category
- Sub-Category

---

# File Structure

```text
ASSIGNMENT_NO.7/
│
├── Data/
│   ├── Sample - Superstore.csv
│   └── Superstore_Incremental.csv
│
├── Notebook/
│   └── Delta_Lake_Assignment.ipynb
│
├── Screenshots/
│   ├── Screenshot 2026-08-02 231417.png
│   ├── Screenshot 2026-08-02 231440.png
│   ├── Screenshot 2026-08-02 231450.png
│   ├── Screenshot 2026-08-02 231503.png
│   ├── Screenshot 2026-08-02 231518.png
│   ├── Screenshot 2026-08-02 231539.png
│   ├── Screenshot 2026-08-02 231552.png
│   ├── Screenshot 2026-08-02 231604.png
│   ├── Screenshot 2026-08-02 231615.png
│   ├── Screenshot 2026-08-02 231647.png
│   ├── Screenshot 2026-08-02 231710.png
│   ├── Screenshot 2026-08-02 231724.png
│   ├── Screenshot 2026-08-02 231735.png
│   ├── Screenshot 2026-08-02 231749.png
│   └── Screenshot 2026-08-02 231802.png
│
└── README.md
```

---

# Assignment Workflow

## Step 1: Load the Dataset

- Uploaded the **Sample - Superstore.csv** file to Azure Databricks.
- Loaded the CSV dataset into a Spark DataFrame.
- Verified the schema and displayed sample records.

---

## Step 2: Data Cleaning

Performed the following preprocessing steps:

- Checked for null values.
- Removed rows containing null values.
- Removed duplicate records.
- Renamed column names by replacing spaces with underscores for Delta Lake compatibility.

Example:

| Original | Updated |
|----------|----------|
| Row ID | Row_ID |
| Order ID | Order_ID |
| Order Date | Order_Date |
| Ship Date | Ship_Date |
| Customer ID | Customer_ID |
| Customer Name | Customer_Name |
| Postal Code | Postal_Code |
| Product ID | Product_ID |
| Product Name | Product_Name |

---

## Step 3: Create a Delta Table

The cleaned dataset was stored in Delta Lake format.

### Delta Lake Features

- ACID Transactions
- Schema Enforcement
- Schema Validation
- Reliable Data Storage
- Time Travel
- Incremental Processing
- MERGE Support

---

## Step 4: Create Incremental Dataset

A second dataset named **Superstore_Incremental.csv** was created.

The dataset contains:

- Existing records for updating.
- New records for insertion.

---

## Step 5: Load Incremental Dataset

The incremental dataset was loaded into a Spark DataFrame.

The schema was verified before performing the merge operation.

---

## Step 6: Perform MERGE (UPSERT)

The MERGE operation was performed using Delta Lake.

The merge compares records using **Row_ID**.

### MERGE Logic

- Update records when **Row_ID** already exists.
- Insert records when **Row_ID** does not exist.

This enables efficient incremental data processing without reloading the complete dataset.

---

## Step 7: Validate the Results

The following validations were performed:

- Verified total record count.
- Checked duplicate Row_ID values.
- Displayed the updated Delta table.
- Generated summary statistics.

---

# Output

The assignment successfully demonstrates:

- Dataset Loading
- Data Cleaning
- Delta Table Creation
- Incremental Dataset Loading
- MERGE (UPSERT)
- Record Updates
- New Record Insertions
- Data Validation
- Summary Statistics
- Final Dataset Display

---

# Learning Outcomes

After completing this assignment, I gained practical experience in:

- Working with Apache Spark DataFrames.
- Data cleaning using PySpark.
- Creating Delta tables.
- Understanding Delta Lake architecture.
- Performing incremental data processing.
- Using MERGE (UPSERT) operations.
- Validating processed datasets.
- Working with Azure Databricks.

---

# Conclusion

This assignment successfully demonstrates incremental data processing using Delta Lake in Azure Databricks.

The Sample Superstore dataset was cleaned and stored as a Delta table. An incremental dataset was then merged into the existing Delta table using the MERGE (UPSERT) operation, allowing existing records to be updated and new records to be inserted efficiently.

The validation process confirmed that the data was updated correctly without creating duplicate records. This assignment provided practical experience in implementing Delta Lake features commonly used in modern data engineering workflows.

---

# Author

**Name:** Ritesh Deshmukh

**Assignment:** Assignment No. 7 – Delta Lake Incremental Data Processing

**Tools Used:** Azure Databricks, Apache Spark (PySpark), Delta Lake
