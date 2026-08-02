# ⚙️ Data Engineering Weekly Assignments

<div align="center">

### **Python • SQL • Spark • Databricks • Data Engineering Concepts**

An **8-Week Structured Learning Repository** for building strong foundations in **Data Engineering** through practical assignments.

**Part of Celebal Technologies Excellence Internship (CEI) 2026**

👨‍💻 **Ritesh Deshmukh**
🎓 *Computer Engineering Student*
📍 *Aspiring Data Engineer*

</div>

---

## 📖 About

This repository contains all the weekly assignments completed during my **8-week Data Engineering Learning Journey**.

The main goal of this repository is to document my:

* Learning progress
* Practical implementations
* Weekly assignments
* Hands-on experience in Data Engineering

The journey begins with **Python Basics** and gradually moves toward:

* SQL Fundamentals
* Subqueries
* Data Engineering Concepts
* Data Cleaning
* Apache Spark
* Databricks
* Pipeline Planning

This repository will be updated regularly after each assignment submission.

---

## 🛠️ Skills & Technologies

| Category                | Technologies     |
| :---------------------- | :--------------- |
| 💻 Programming          | Python           |
| 🗄️ Database            | SQL              |
| 📊 Data Processing      | Pandas, NumPy    |
| ⚡ Big Data              | Apache Spark     |
| ☁️ Platform             | Databricks       |
| 📓 Notebook Environment | Jupyter Notebook |
| 🔧 Version Control      | Git, GitHub      |

---

## 📅 Weekly Progress

|  Week  | Topic                     |    Status   |
| :----: | :------------------------ | :---------: |
| Week 1 | Python Basics             | ✅ Completed |
| Week 2 | SQL Basics                | ✅ Completed |
| Week 3 | Subqueries                | ✅ Completed |
| Week 4 | Data Engineering Concepts | ✅ Completed |
| Week 5 | Data Cleaning             | ✅ Completed |
| Week 6 | Spark Introduction        | ✅ Completed |
| Week 7 | Databricks                | ✅ Completed |
| Week 8 | Planning                  |  🔒 Pending |

---

## 📁 Repository Structure


```text
```text
Celebal_Tech (data-engineering-assignments)/
│
├── README.md
│
├── Assignment-01/
│   ├── analysis1.ipynb
│   ├── README.md
│   └── data/
│
├── Assignment-02/
│   ├── Database_setup/
│   │   ├── shopease.sql
│   │   └── shopease_database_setup.pdf
│   │
│   ├── Section_A/
│   │   ├── basic_queries.sql
│   │   └── section_a_documentation.pdf
│   │
│   ├── Section_B/
│   │   ├── filtering_queries.sql
│   │   └── section_b_documentation.pdf
│   │
│   ├── Section_C/
│   │   ├── aggregation_queries.sql
│   │   └── section_c_documentation.pdf
│   │
│   ├── Section_D/
│   │   ├── joins_queries.sql
│   │   └── section_d_documentation.pdf
│   │
│   ├── Section_E/
│   │   ├── advanced_queries.sql
│   │   └── section_e_documentation.pdf
│   │
│   └── README.md
│
├── Assignment-03/
│   ├── dataset/
│   │   └── Sample - Superstore.csv
│   │
│   ├── sql/
│   │   ├── 1_create_tables.sql
│   │   ├── 2_insert_data.sql
│   │   ├── 3_queries.sql
│   │   ├── 4_final_query.sql
│   │   └── 5_mini_project.sql
│   │
│   ├── Screenshots/
│   │   └── Query Screenshots/
│   │
│   └── README.md
│
├── Assignment-04/
│   ├── Screenshots/
│   ├── Assignment_No.4_Report.pdf
│   ├── Sample - Superstore.csv
│   └── README.md
│
├── Assignment-05/
│   ├── Dataset/
│   │   └── Titanic-Dataset.csv
│   │
│   ├── Notebook/
│   │   ├── Assignment_05_Apache_Spark_DataFrame_Operations.ipynb
│   │   └── Assignment_05_Apache_Spark_DataFrame_Operations.pdf
│   │
│   ├── Output/
│   │   └── Spark_Output.csv
│   │
│   ├── Week-5_Question_Documentation.pdf
│   └── README.md
│
├── Assignment-06/
│   ├── Dataset/
│   │   └── hotel_bookings.csv
│   │
│   ├── Notebook/
│   │   └── CEI_Assignment_No_6.ipynb
│   │
│   ├── Output/
│   │   ├── CSV/
│   │   │   ├── part-00000-*.csv
│   │   │   ├── _SUCCESS
│   │   │   └── ...
│   │   │
│   │   └── PARQUET/
│   │       ├── part-00000-*.parquet
│   │       ├── _SUCCESS
│   │       └── ...
│   │
│   └── README.md
│
├── Assignment-07/
│   ├── Dataset/
│   │   ├── Sample - Superstore.csv
│   │   └── Superstore_Incremental.csv
│   │
│   ├── Notebook/
│   │   └── Delta_Lake_Assignment.ipynb
│   │
│   ├── Screenshots/
|   |
│   └── README.md
│
└── Assignment-08/
```



# 📌 Week 1 (Assignment No. 1)



## Python Basics & Data Exploration

This assignment focuses on building strong fundamentals in **Python Programming** and performing **Exploratory Data Analysis (EDA)** on a shopping dataset.

---

## 📚 Topics Covered in Assignment No. 1

| Topic                       | Description                                      |
| :-------------------------- | :----------------------------------------------- |
| 🐍 Python Basics            | Variables, Data Types, Loops, Functions          |
| 📂 Data Loading             | Reading CSV files using Pandas                   |
| 🔍 Data Inspection          | Using `head()`, `tail()`, `info()`, `describe()` |
| 🧹 Data Cleaning            | Handling Missing Values, Duplicates, Formatting  |
| ⚙️ Feature Engineering      | Creating Derived Columns                         |
| 📊 Univariate Analysis      | Analysis of Single Variables                     |
| 🔗 Bivariate Analysis       | Relationship Between Two Variables               |
| 🏷️ Category-Level Analysis | Group-wise Analysis and Insights                 |
| 📈 Data Visualization       | Histograms, Boxplots, Scatterplots, Bar Charts   |

---
# 📌 Week 2 (Assignment No. 2)

## SQL-Based Sales Data Analysis

This assignment focuses on building strong fundamentals in **SQL** and performing **sales data analysis** using filtering, aggregation, joins, and business queries on an e-commerce dataset.

---

## 📚 Topics Covered in Assignment No. 2

| Topic | Description |
| :--- | :--- |
| 🗄️ Database Setup | Creating database, tables, and relationships |
| 🔑 Constraints & Keys | Primary Keys, Foreign Keys, UNIQUE, CHECK |
| 📂 Data Loading | Inserting sample records into relational tables |
| 🔍 Data Exploration | Using SELECT, DISTINCT, and schema inspection |
| 🎯 Data Filtering | Applying `WHERE`, `BETWEEN`, `AND`, `NOT` conditions |
| ⚡ Query Optimization | Understanding indexes and SARGable queries |
| 📊 Aggregation | Using `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()` |
| 🧮 Grouping Data | Applying `GROUP BY` and `HAVING` for summaries |
| 🔗 Table Joins | INNER JOIN, LEFT JOIN, RIGHT JOIN operations |
| 🏷️ Business Queries | Customer insights, sales trends, product analysis |
| ⚙️ CASE Statements | Conditional categorization and logic handling |
| 🔄 Transactions | COMMIT, ROLLBACK, and transaction management |
| 🛡️ ACID Properties | Understanding Atomicity, Consistency, Isolation, Durability |

---
# 📌 Week 3 (Assignment No. 3)

## SQL Advanced Analytics

This assignment focuses on applying **Advanced SQL** concepts to analyze the **Sample Superstore** dataset. The project demonstrates how to perform customer and sales analytics using **Subqueries**, **Common Table Expressions (CTEs)**, **Window Functions**, and **JOINs** to solve real-world business problems and generate meaningful insights.

---

## 📚 Topics Covered in Assignment No. 3

| Topic                              | Description                                                                     |
| :--------------------------------- | :------------------------------------------------------------------------------ |
| 🗄️ Database Setup                 | Creating the database and importing the Superstore dataset into MySQL           |
| 📂 Data Normalization              | Creating `customers`, `products`, and `orders` tables using `SELECT DISTINCT`   |
| 🔍 Data Exploration                | Exploring the dataset using `SELECT`, `DISTINCT`, and summary queries           |
| 🧩 Subqueries                      | Finding above-average sales, highest-value orders, and nested query analysis    |
| 🔄 Common Table Expressions (CTEs) | Simplifying complex queries and performing intermediate aggregations            |
| 📊 Customer Sales Analysis         | Calculating total sales, profit, and quantity for each customer                 |
| 📈 Window Functions                | Using `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()` for ranking and segmentation |
| 🔗 JOIN Operations                 | Combining customer, product, and order tables for comprehensive analysis        |
| 🏆 Customer Ranking                | Ranking customers based on total sales and identifying top performers           |
| 📉 Sales Distribution              | Identifying top customers, bottom customers, and above-average customers        |
| 🛍️ Order Analysis                 | Finding highest-value orders and customers with only one order                  |
| 📌 Business Insights               | Generating actionable insights from customer and sales data using SQL           |

---
# 📌 Week 4 (Assignment No. 4)

## Azure Cloud Fundamentals & Data Pipeline Implementation using Azure Data Factory (ADF)

This assignment focuses on understanding **Microsoft Azure Cloud Services** and building an **end-to-end data pipeline** using **Azure Blob Storage** and **Azure Data Factory (ADF)**. It covers creating Azure resources, configuring storage, designing ETL pipelines, validating metadata, managing access using IAM, and monitoring pipeline execution.

---

## 📚 Topics Covered in Assignment No. 4

| Topic | Description |
| :--- | :--- |
| ☁️ Azure Cloud Fundamentals | Understanding Azure Portal, Resource Groups, and Cloud Services |
| 📁 Resource Group | Creating and managing Azure resources in a logical container |
| 💾 Azure Storage Account | Creating Storage Accounts and managing cloud storage |
| 📦 Azure Blob Storage | Creating Blob Containers and uploading CSV datasets |
| 🏗️ Azure Data Factory (ADF) | Creating and exploring Azure Data Factory Studio |
| 🔗 Linked Services | Connecting Azure Data Factory with Azure Blob Storage |
| 📄 Datasets | Configuring Source and Destination datasets |
| 📋 Get Metadata Activity | Retrieving file metadata such as Exists, Size, and Last Modified |
| 📂 Copy Data Activity | Copying data from the input Blob container to the destination container |
| ⚙️ Pipeline Development | Designing and validating an end-to-end ETL pipeline |
| ▶️ Pipeline Execution | Running pipelines using Debug and Trigger options |
| 📊 Pipeline Monitoring | Monitoring execution status and activity logs |
| 🔐 Azure IAM (RBAC) | Assigning Reader, Contributor, and Storage Blob Data Contributor roles |
| ✅ End-to-End Data Pipeline | Implementing and validating a complete Blob → ADF → Blob data pipeline |
| 📈 Cloud Data Engineering | Understanding practical cloud-based ETL workflow and data movement |

---
# 📌 Week 5 (Assignment No. 5 )
##  Apache Spark DataFrame Operations

## 📖 Overview

This assignment focuses on learning the fundamentals of **Apache Spark** and performing **DataFrame operations** using **PySpark**. The Titanic dataset is used to explore Spark DataFrames, perform data cleaning, apply transformations, and generate analytical insights. The assignment also highlights the advantages of Spark's in-memory processing over traditional Hadoop MapReduce.

---

## 🎯 Objectives 

- Understand the basics of Apache Spark and PySpark.
- Learn how to create and work with Spark DataFrames.
- Read and analyze CSV datasets using Spark.
- Perform data cleaning and preprocessing.
- Apply filtering, sorting, grouping, and aggregation operations.
- Remove duplicate records based on selected columns.
- Export processed data to CSV format.
- Compare Apache Spark with Hadoop MapReduce.

---

## 📚 Topics Covered in Assignment No. 5

| Topic | Description |
| :--- | :--- |
| ⚡ Introduction to Apache Spark | Understanding Apache Spark architecture and its advantages over Hadoop MapReduce |
| 🏗️ Spark Environment Setup | Setting up Apache Spark using PySpark and Jupyter Notebook |
| 📂 Loading CSV Data | Reading the Titanic dataset into a Spark DataFrame |
| 📊 Spark DataFrames | Creating, exploring, and performing operations on DataFrames |
| 🔍 Data Exploration | Viewing schema, displaying records, and generating summary statistics |
| 🧹 Data Cleaning | Handling missing values and removing duplicate records |
| 📝 Column Operations | Selecting, renaming, adding, and dropping DataFrame columns |
| 🔄 Filtering & Sorting | Filtering records based on conditions and sorting data |
| 📈 Aggregation | Performing aggregate functions such as count, sum, average, min, and max |
| 👥 GroupBy Operations | Grouping data and generating summarized insights |
| 🛠️ Data Transformation | Applying transformations using Spark DataFrame APIs |
| 💾 Writing Output | Exporting processed DataFrames as CSV files |
| 🚀 In-Memory Processing | Understanding Spark's in-memory computation for faster processing |
| ⚖️ Spark vs MapReduce | Comparing Spark with traditional Hadoop MapReduce architecture |
| ✅ End-to-End Spark Workflow | Building a complete Spark DataFrame pipeline from data loading to output generation |


# 📌 Week 6 (Assignment No. 6)
## Apache Spark Architecture & Data Processing using PySpark

## 📖 Overview

This assignment focuses on understanding **Apache Spark Architecture** and performing efficient **data processing using PySpark**. The **Hotel Booking Demand** dataset is used to explore Spark DataFrames, perform schema handling, data transformations, filtering, null value handling, performance optimization, and build an end-to-end ETL pipeline. The assignment also demonstrates Spark concepts such as **Lazy Evaluation**, **DAG (Directed Acyclic Graph)**, **Wide Transformations**, **Shuffle**, **Predicate Pushdown**, and compares **CSV** and **Parquet** file formats.

---

## 🎯 Objectives

- Understand Apache Spark Architecture.
- Learn the roles of Driver, Cluster Manager, and Executors.
- Understand Spark Execution Modes.
- Learn Lazy Evaluation and DAG (Directed Acyclic Graph).
- Read CSV and Parquet files with proper schema handling.
- Perform DataFrame filtering and column selection.
- Modify DataFrames by renaming columns, casting data types, and creating new columns.
- Handle missing values efficiently.
- Understand Wide Transformations and Shuffle operations.
- Learn Predicate Pushdown optimization.
- Compare CSV and Parquet file formats.
- Build an end-to-end ETL pipeline (Read → Transform → Filter → Write).
- Save processed data in CSV and Parquet formats.
- Follow Spark best practices for processing large datasets.

---

## 📚 Topics Covered in Assignment No. 6

| Topic | Description |
| :--- | :--- |
| ⚡ Apache Spark Architecture | Understanding Driver Program, Cluster Manager, and Executors |
| 🏗️ Spark Environment Setup | Setting up Apache Spark using PySpark in Google Colab |
| 🚀 Spark Execution Modes | Learning Local Mode, Standalone, YARN, and Kubernetes execution modes |
| 🔄 Lazy Evaluation | Understanding how Spark delays execution until an action is triggered |
| 📊 DAG (Directed Acyclic Graph) | Viewing Spark execution plans using `explain(True)` |
| 📂 Reading CSV Data | Loading the Hotel Booking Demand dataset with schema inference |
| 📁 Reading Parquet Files | Reading processed Parquet files for optimized analytics |
| 📋 Schema Handling | Exploring DataFrame schema and automatic data type inference |
| 📊 Data Exploration | Displaying records, schema, statistics, rows, and columns |
| 🔍 Filtering & Selection | Filtering records and selecting required columns |
| 📝 DataFrame Modifications | Renaming columns, casting data types, and creating calculated columns |
| 🧹 Missing Value Handling | Using `fillna()` and `dropna()` to handle null values |
| 🔄 Data Transformations | Applying Spark DataFrame transformations and actions |
| 📈 Aggregation & GroupBy | Performing aggregation using `groupBy()`, `count()`, `avg()`, and other functions |
| 🔀 Wide Transformations | Understanding shuffle operations during `groupBy()` and other wide transformations |
| 🚀 Predicate Pushdown | Optimizing query execution by pushing filters closer to the data source |
| 📄 CSV vs Parquet | Comparing storage format, compression, and query performance |
| 🔁 ETL Pipeline | Building a complete Read → Transform → Filter → Write pipeline |
| 💾 Writing Output | Saving processed datasets in CSV and Parquet formats |
| ⚡ Spark Performance | Understanding performance optimization techniques and best practices |
| ✅ End-to-End Spark Workflow | Implementing a complete Spark data processing workflow using PySpark |
---

# 📌 Week 7 (Assignment No. 7)
## Delta Lake Incremental Data Processing using Azure Databricks

## 📖 Overview

This assignment focuses on implementing **Incremental Data Processing using Delta Lake** in **Azure Databricks**. The **Sample Superstore** dataset is used to demonstrate how to load data into a Delta table, perform data cleaning, create an incremental dataset, and efficiently update existing records while inserting new records using the **MERGE (UPSERT)** operation.

The assignment also explores key Delta Lake features such as **ACID Transactions**, **Schema Enforcement**, **Schema Validation**, and efficient data management for modern data engineering pipelines. Finally, the processed data is validated using row count, duplicate checks, and summary statistics to ensure data quality and consistency.

---

## 🎯 Objectives

- Understand the fundamentals of Delta Lake.
- Learn the benefits of Delta Lake over traditional file formats.
- Load CSV data into a Spark DataFrame.
- Perform data cleaning by handling null values and removing duplicate records.
- Rename column names for Delta Lake compatibility.
- Create and store data as a Delta Table.
- Create an incremental dataset to simulate new incoming records.
- Perform MERGE (UPSERT) operations to update and insert records.
- Validate the processed data using row count and duplicate checks.
- Generate summary statistics for the final dataset.
- Build an end-to-end Incremental ETL pipeline using Delta Lake.
- Gain practical experience with Azure Databricks and Delta Lake.

---

## 📚 Topics Covered in Assignment No. 7

| Topic | Description |
| :--- | :--- |
| 🏗️ Introduction to Delta Lake | Understanding Delta Lake architecture and its advantages |
| ☁️ Azure Databricks | Working with Databricks notebooks and Unity Catalog Volumes |
| 📂 Loading CSV Data | Importing the Sample Superstore dataset into a Spark DataFrame |
| 📊 Data Exploration | Displaying records, schema, row count, and understanding the dataset |
| 🧹 Data Cleaning | Handling null values and removing duplicate records |
| 📝 Column Renaming | Renaming columns by replacing spaces with underscores for Delta compatibility |
| 💾 Delta Table Creation | Creating and storing data in Delta Lake format |
| 📁 Incremental Dataset | Creating a second dataset containing updated and new records |
| 📥 Loading Incremental Data | Reading incremental CSV data into a Spark DataFrame |
| 🔀 MERGE (UPSERT) | Updating existing records and inserting new records using Delta Lake MERGE |
| 🔑 Primary Key Matching | Matching records using the **Row_ID** column |
| ⚡ ACID Transactions | Ensuring reliable and consistent data updates |
| 🛡️ Schema Enforcement | Preventing invalid or incompatible data from being written |
| 📋 Data Validation | Validating row count, duplicate records, and processed data |
| 📈 Summary Statistics | Generating descriptive statistics for numerical columns |
| 🚀 Incremental ETL Pipeline | Building a complete Read → Clean → Load → MERGE → Validate workflow |
| 📦 Delta Table Management | Managing Delta tables for efficient storage and querying |
| ⚙️ Delta Lake Best Practices | Understanding efficient storage, updates, and data reliability |
| 🎯 End-to-End Delta Lake Workflow | Implementing a complete incremental data processing solution using Azure Databricks |

---


## 🎯 Learning Goals
This structured learning journey is designed to:

✔ Strengthen programming fundamentals with Python  
✔ Master SQL concepts and query writing  
✔ Understand relational database design and optimization  
✔ Perform data cleaning, filtering, and aggregation  
✔ Learn data analysis using business-oriented SQL queries  
✔ Build a strong foundation in Data Engineering concepts  
✔ Explore Apache Spark and distributed data processing  
✔ Work with Databricks for scalable data workflows  
✔ Understand ETL pipelines and data architecture  
✔ Develop end-to-end real-world data solutions  

---

## 🚀 Current Progress

```text
✅ Assignment No. 1 Completed
✅ Assignment No. 2 Completed
✅ Assignment No. 3 Completed
✅ Assignment No. 4 Completed
✅ Assignment No. 5 Completed
✅ Assignment No. 6 Completed
✅ Assignment No. 7 Completed
⏳ Next: Assignment No. 8
```

---

## 📌 Future Scope

Future assignments will cover:

• Databricks Workflow Management

• Data Warehousing Concepts

• Real-Time Data Processing

• Data Pipeline Architecture

• End-to-End Data Engineering Projects

---

## 👨‍💻 Author

**Ritesh Deshmukh**

*Computer Engineering Student*

*Aspiring Data Engineer*

---

<div align="center">

⭐ **This repository will be updated weekly as new assignments are completed.**

</div>
