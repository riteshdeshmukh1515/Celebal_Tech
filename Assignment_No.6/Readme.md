# 🚀 Spark Architecture & Data Processing using PySpark

## 📌 Assignment Objective

The objective of this assignment is to understand Apache Spark architecture and perform efficient data processing using PySpark. The assignment demonstrates Spark DataFrame operations, lazy evaluation, DAG execution, schema handling, data transformations, filtering, null value handling, performance optimization, and building an end-to-end ETL pipeline.

---

# 📂 Dataset

**Dataset Name:** Hotel Booking Demand Dataset

**Source:** Kaggle

https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand

**File Used:**

- hotel_bookings.csv

---

# 🎯 Learning Objectives

- Understand Apache Spark Architecture
- Learn Driver, Cluster Manager, and Executors
- Understand Spark Execution Modes
- Learn Lazy Evaluation
- Understand DAG (Directed Acyclic Graph)
- Read CSV files using Spark
- Infer Schema Automatically
- Explore DataFrames
- Select and Filter Data
- Rename Columns
- Cast Data Types
- Create New Columns
- Handle Missing Values
- Remove Duplicate Records
- Perform Aggregation
- Understand Wide Transformations
- Understand Shuffle Operations
- Learn Predicate Pushdown
- Compare CSV and Parquet File Formats
- Build an ETL Pipeline
- Save Processed Data
- Follow Spark Performance Best Practices

---

# 🛠 Technologies Used

- Python
- Apache Spark
- PySpark
- Google Colab
- Kaggle Dataset

---

# 📁 Project Structure

```
ASSIGNMENT_NO.6/
│
├── Dataset/
│   └── hotel_bookings.csv
│
├── Notebook/
│   └── CEI_Assignment_No_6.ipynb
│
├── Output/
│   ├── CSV/
│   └── PARQUET/
│
└── Readme.md
```

---

# 📚 Assignment Workflow

## Step 1
Install PySpark

## Step 2
Create Spark Session

## Step 3
Read Hotel Booking Dataset

## Step 4
Explore Dataset

- Display Records
- Print Schema
- Count Rows
- Describe Dataset

## Step 5
Understand Spark Architecture

- Driver
- Cluster Manager
- Executors

## Step 6
Understand Lazy Evaluation

- Transformations
- Actions

## Step 7
View DAG Execution Plan

- explain(True)

## Step 8
Perform DataFrame Transformations

- Select Columns
- Filter Records
- Rename Columns
- Cast Data Types
- Add New Columns

## Step 9
Handle Missing Values

- fillna()
- dropna()

## Step 10
Aggregation

- groupBy()
- avg()
- count()

## Step 11
Wide Transformations

- groupBy()
- Shuffle

## Step 12
Predicate Pushdown

- Filter Optimization

## Step 13
CSV vs Parquet Comparison

- Read Performance
- Storage Efficiency

## Step 14
Build ETL Pipeline

Read → Transform → Filter → Write

## Step 15
Save Processed Data

- CSV
- Parquet

---

# 📊 Spark Concepts Covered

- Spark Architecture
- Driver Program
- Cluster Manager
- Executors
- Spark Session
- Lazy Evaluation
- DAG (Directed Acyclic Graph)
- Transformations
- Actions
- Narrow Transformations
- Wide Transformations
- Shuffle
- Predicate Pushdown
- Schema Inference
- DataFrame API
- ETL Pipeline

---

# ⚡ DataFrame Operations Performed

- select()
- filter()
- withColumn()
- withColumnRenamed()
- cast()
- fillna()
- dropna()
- dropDuplicates()
- orderBy()
- distinct()
- groupBy()
- agg()
- explain()
- write.csv()
- write.parquet()

---

# 📈 Performance Optimization Techniques

- Lazy Evaluation
- DAG Optimization
- Predicate Pushdown
- Wide Transformations
- Shuffle Awareness
- Schema Inference
- Column Selection
- Avoid collect() on Large Datasets
- Use show() for Preview
- Store Analytical Data in Parquet Format

---

# 📄 Output Generated

- Processed CSV File
- Processed Parquet File
- ETL Pipeline Output
- Execution Plan (DAG)
- Aggregated Results
- Performance Comparison (CSV vs Parquet)

---

# 📌 Key Observations

- Spark executes transformations lazily and performs computation only when an action is triggered.
- The Driver Program creates the execution plan while Executors perform the actual computations.
- Wide transformations such as groupBy() involve shuffle operations, making them more expensive than narrow transformations.
- Predicate Pushdown reduces the amount of data read from storage, improving performance.
- Parquet provides faster read performance and better compression compared to CSV.
- Selecting only required columns and filtering data early improves Spark job efficiency.

---

# ✅ Conclusion

This assignment successfully demonstrates Apache Spark's architecture, execution model, DataFrame operations, data cleaning, transformation techniques, and performance optimization. Using the Hotel Booking Demand dataset, an end-to-end ETL pipeline was developed to read, transform, filter, and save data in both CSV and Parquet formats. The assignment also highlights Spark best practices for handling large-scale data efficiently.

---

## 👨‍💻 Author

**Name:** Ritesh Deshmukh

**Technology:** PySpark | Apache Spark | Python

**Platform:** Google Colab

**Dataset:** Hotel Booking Demand Dataset (Kaggle)