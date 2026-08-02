# 📘 Assignment No. 7 – Delta Lake Incremental Data Processing

<p align="center">

![Azure Databricks](https://img.shields.io/badge/Azure-Databricks-red?style=for-the-badge&logo=databricks)
![Apache Spark](https://img.shields.io/badge/Apache-Spark-orange?style=for-the-badge&logo=apachespark)
![Delta Lake](https://img.shields.io/badge/Delta-Lake-blue?style=for-the-badge)
![PySpark](https://img.shields.io/badge/PySpark-Python-green?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

</p>

---

# 👨‍🎓 Student Information

| **Details** | **Information** |
|-------------|-----------------|
| **Name** | Ritesh Deshmukh |
| **Assignment No.** | 7 |
| **Assignment Title** | Delta Lake Incremental Data Processing |
| **Technology** | Azure Databricks, PySpark, Delta Lake |
| **Dataset** | Sample Superstore |

---

# 🎯 Assignment Objective

The objective of this assignment is to implement **Incremental Data Processing using Delta Lake** in **Azure Databricks**.

The assignment demonstrates how to:

- 📂 Load a CSV dataset into a Delta table
- 🧹 Clean the dataset
- 📊 Create an incremental dataset
- 🔄 Perform the MERGE (UPSERT) operation
- ✅ Validate the processed data
- 📈 Display the final dataset and summary

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Azure Databricks | Cloud Analytics Platform |
| Apache Spark (PySpark) | Data Processing |
| Delta Lake | Incremental Data Processing |
| Unity Catalog | Data Storage |
| Git & GitHub | Version Control |

---

# 📂 Dataset Information

### Dataset Name

**Sample Superstore Dataset**

### Dataset Description

The dataset contains retail sales information including:

- Customer Details
- Product Details
- Order Information
- Sales
- Quantity
- Discount
- Profit
- Region
- Category
- Sub-Category

---

# 📁 Project Structure

```text
ASSIGNMENT_NO.7/
│
├── 📂 Data/
│   ├── Sample - Superstore.csv
│   └── Superstore_Incremental.csv
│
├── 📂 Notebook/
│   └── Delta_Lake_Assignment.ipynb
│
├── 📂 Screenshots/
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
└── 📄 README.md
```

---

# 🚀 Assignment Workflow

## Step 1: Loading the Dataset

The Sample Superstore dataset was uploaded into Azure Databricks and stored in Unity Catalog Volumes. Using PySpark, the CSV file was read into a Spark DataFrame with the header option enabled and schema inferred automatically.

The dataset was then displayed to verify that all records were successfully loaded.

**Tasks Performed**

- Uploaded CSV file
- Read CSV using Spark
- Displayed first 20 rows
- Verified schema
- Counted total records

---

## Step 2: Data Cleaning

Before storing the dataset into Delta Lake, several preprocessing operations were performed to improve data quality.

The following cleaning operations were completed:

- Checked for missing (null) values.
- Removed rows containing null values.
- Removed duplicate records.
- Renamed columns by replacing spaces with underscores.

Example:

| Original Column | Updated Column |
|-----------------|----------------|
| Row ID | Row_ID |
| Order ID | Order_ID |
| Order Date | Order_Date |
| Customer Name | Customer_Name |
| Product Name | Product_Name |

Renaming the columns ensures compatibility with Delta Lake because column names containing spaces are not supported without enabling column mapping.

---

## Step 3: Creating the Delta Table

After cleaning the data, the DataFrame was stored in Delta format.

A Delta table acts as the master dataset for future updates.

Unlike normal CSV files, Delta tables support reliable updates, versioning, and transactional operations.

### Benefits of Delta Lake

- ACID Transactions
- Schema Enforcement
- Schema Validation
- Time Travel
- Efficient Data Updates
- Incremental Processing
- High Performance

---

## Step 4: Creating an Incremental Dataset

To simulate real-world scenarios where new data arrives regularly, a second dataset named **Superstore_Incremental.csv** was created.

The incremental dataset contains two types of records:

### Existing Records

Existing Row_ID values with modified Sales, Profit, or Quantity values.

These records demonstrate update operations.

### New Records

Completely new Row_ID values.

These records demonstrate insert operations.

This simulates how new business data is received daily in production systems.

---

## Step 5: Loading the Incremental Dataset

The incremental dataset was uploaded into Azure Databricks and loaded into a Spark DataFrame.

Before performing the merge operation, the schema and sample records were verified to ensure compatibility with the Delta table.

---

## Step 6: Performing the MERGE (UPSERT) Operation

The MERGE operation is one of the most powerful features of Delta Lake.

Instead of deleting and reloading the complete dataset, MERGE compares records based on a matching key.

In this assignment, **Row_ID** was used as the matching column.

### MERGE Logic

If the Row_ID already exists in the Delta table:

➡ Update the existing record.

If the Row_ID does not exist:

➡ Insert the new record.

This approach significantly improves processing efficiency and minimizes unnecessary computation.

---

## Step 7: Validation

After the MERGE operation, several validation checks were performed.

### Record Count

The total number of records was verified to ensure that new records were inserted successfully.

### Duplicate Check

Duplicate Row_ID values were checked to ensure that MERGE updated existing records instead of creating duplicates.

### Summary Statistics

Descriptive statistics were generated for numerical columns including:

- Sales
- Quantity
- Discount
- Profit

### Final Dataset

The updated Delta table was displayed to verify that all updates and insertions were completed successfully.

---

# ✨ Delta Lake Features Demonstrated

This assignment demonstrates several important Delta Lake features.

| Feature | Description |
|----------|-------------|
| ACID Transactions | Ensures reliable updates and consistency |
| MERGE (UPSERT) | Updates existing records and inserts new records |
| Schema Enforcement | Prevents invalid data |
| Incremental Processing | Processes only changed data |
| Delta Tables | Reliable storage for Spark workloads |
| Data Validation | Ensures data quality |

---

# 📊 Results

The assignment successfully completed all required tasks.

✔ Loaded the dataset into Azure Databricks

✔ Performed data cleaning

✔ Created a Delta table

✔ Created an incremental dataset

✔ Loaded incremental records

✔ Performed MERGE (UPSERT)

✔ Updated existing records

✔ Inserted new records

✔ Validated processed data

✔ Displayed the final dataset

---

# 📚 Learning Outcomes

After completing this assignment, I gained practical knowledge of:

- Reading CSV files using PySpark
- Data cleaning using Spark DataFrames
- Delta Lake architecture
- Creating Delta tables
- Incremental data processing
- MERGE (UPSERT) operations
- Data validation techniques
- Azure Databricks environment
- Real-world ETL workflow implementation

---

# 🎯 Conclusion

This assignment successfully demonstrates the implementation of incremental data processing using Delta Lake in Azure Databricks.

The Sample Superstore dataset was first cleaned and stored as a Delta table. A second dataset containing updated and new records was then merged into the existing Delta table using the MERGE (UPSERT) operation.

The validation process confirmed that existing records were updated correctly, new records were inserted successfully, and no duplicate records were created.

Through this assignment, I gained practical experience in working with Delta Lake features such as ACID transactions, schema enforcement, and incremental data processing. These concepts are fundamental in designing reliable and scalable modern data engineering pipelines.



## 🚀 Thank You!

**Assignment No. 7 – Delta Lake Incremental Data Processing**

**Developed by Ritesh Deshmukh**

</div>
