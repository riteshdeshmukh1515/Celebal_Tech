# 🚀 Assignment No. 5 - Apache Spark DataFrame Operations using PySpark

## 📌 Objective

The objective of this assignment is to understand the fundamentals of **Apache Spark** and perform various data processing tasks using **PySpark DataFrames**. The assignment demonstrates data loading, data cleaning, transformation, filtering, aggregation, grouping, schema modification, and building a complete data processing pipeline.

---

# 📖 About Apache Spark

Apache Spark is an open-source distributed computing framework designed for processing large-scale data efficiently. Unlike Hadoop MapReduce, Spark performs most computations in memory, making it significantly faster for iterative algorithms and real-time analytics.

### Advantages of Apache Spark

* In-memory processing for faster execution
* Distributed computing across multiple machines
* Easy-to-use DataFrame API
* Supports SQL, Machine Learning, Streaming, and Graph Processing
* Fault-tolerant architecture
* Optimized query execution using the Catalyst Optimizer

---

# 📚 Assignment Learning Outcomes

After completing this assignment, the following concepts were learned:

* Understanding the limitations of MapReduce
* Advantages of Apache Spark over MapReduce
* Creating a Spark Session
* Working with Spark DataFrames
* Loading CSV datasets
* Exploring datasets
* Data cleaning techniques
* Handling missing values
* Removing duplicate records
* Applying filtering conditions
* Transforming data using Spark functions
* Modifying DataFrame schema
* Performing aggregation functions
* Grouping data using `groupBy()`
* Understanding wide transformations and shuffle operations
* Building a complete ETL (Extract, Transform, Load) pipeline
* Saving processed data

---

# 🛠 Technologies Used

* Python 3
* Apache Spark (PySpark)
* Google Colab
* Kaggle Titanic Dataset

---

# 📂 Dataset Information

**Dataset Name:** Titanic Dataset

**Source:** Kaggle

The dataset contains passenger information from the Titanic disaster and includes demographic details, ticket information, passenger class, fare, survival status, and other related attributes.

### Dataset Columns

* PassengerId
* Survived
* Pclass
* Name
* Sex
* Age
* SibSp
* Parch
* Ticket
* Fare
* Cabin
* Embarked

---

# 📁 Project Structure

```text
Assignment_No.5/
│── Dataset/
│   └── Titanic-Dataset.csv
│
│── notebook/
│   └── Assignment_06_Apache_Spark_DataFrame_Operations(1).ipynb
|   └── Assignment_06_Apache_Spark_DataFrame_Operations(1).pdf
│
│── output/
│   └── Spark Output.csv
│
└── Week- 5 Question_Documentation.pdf
│
└── README.md
```

---

# ⚙ Installation

## Step 1: Open Google Colab

Create a new Google Colab notebook.

## Step 2: Install PySpark

```python
!pip install pyspark
```

## Step 3: Import Required Libraries

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
```

## Step 4: Create Spark Session

```python
spark = SparkSession.builder \
    .appName("Titanic Spark Assignment") \
    .master("local[*]") \
    .getOrCreate()
```

---

# 📊 Operations Performed

## 1. Data Loading

* Uploaded Titanic CSV file
* Loaded CSV into Spark DataFrame
* Displayed sample records
* Displayed schema
* Displayed dataset dimensions

---

## 2. Data Exploration

Performed the following operations:

* Displayed first records
* Printed schema
* Displayed column names
* Generated summary statistics

---

## 3. Data Cleaning

The following cleaning operations were performed:

* Removed duplicate records
* Identified missing values
* Filled missing Age values using average age
* Replaced missing Cabin values with **"Not Assigned"**
* Replaced missing Embarked values with **"Unknown"**

---

## 4. Data Transformation

Performed several transformation operations including:

* Renamed columns
* Changed data types
* Created a new calculated column (`FareWithTax`)
* Verified updated schema

---

## 5. Data Filtering

Applied different filtering conditions such as:

* Passengers between 20 and 40 years of age
* Female passengers
* First-class passengers
* Passengers with ticket fare greater than 100
* Multiple filtering conditions

---

## 6. Aggregation

Performed various aggregation operations:

* Count
* Sum
* Average
* Minimum
* Maximum

These operations helped summarize the dataset and generate statistical insights.

---

## 7. GroupBy Operations

Grouped data using different attributes such as:

* Gender
* Passenger Class
* Embarked Port

Applied aggregation functions including:

* Count
* Average
* Sum

---

## 8. Sorting

Sorted the dataset by:

* Age
* Ticket Fare
* Passenger Class

Displayed the highest-paying passengers.

---

## 9. Wide Transformations

Implemented wide transformations using:

* `groupBy()`

### Shuffle Concept

During `groupBy()`, Spark redistributes data between partitions.

This redistribution is called **Shuffle**.

Although shuffle enables grouping and aggregation, it increases network communication and execution time.

---

## 10. Complete ETL Pipeline

A complete data processing pipeline was created consisting of:

1. Load Dataset
2. Remove Duplicate Records
3. Handle Missing Values
4. Rename Columns
5. Filter Records
6. Perform Aggregation
7. Display Results
8. Save Output

---

# 📤 Output

The processed data was successfully saved as CSV inside:

```text
Spark_Output/
```

The output contains grouped passenger statistics after data cleaning and transformation.

---

# 📈 Key Insights

* The Titanic dataset contains missing values in the **Age**, **Cabin**, and **Embarked** columns.
* Duplicate checking confirmed there were no duplicate records in the dataset.
* Missing values were successfully handled using Spark DataFrame functions.
* Filtering operations allowed focused analysis on selected passenger groups.
* Aggregation functions generated meaningful statistical summaries.
* GroupBy operations provided insights into passenger class distribution and fare collection.
* Wide transformations demonstrated Spark's distributed processing capabilities.
* The complete ETL pipeline showed how Spark can efficiently clean, transform, analyze, and store data.

---

# ✅ Conclusion

This assignment successfully demonstrated the core capabilities of Apache Spark DataFrames. Various data engineering tasks including loading, cleaning, transforming, filtering, aggregating, grouping, sorting, and schema modification were performed using PySpark.

The assignment also highlighted the advantages of Spark over traditional MapReduce by utilizing in-memory processing, distributed computation, and optimized execution.

Overall, this project provided practical experience in building a complete Spark-based data processing pipeline and strengthened the understanding of modern big data processing techniques.

---

# 👨‍💻 Author

**Name:** Ritesh Deshmukh

**Course:** B.Tech Computer Engineering

**Assignment:** Assignment No. 5 – Apache Spark DataFrame Operations using PySpark

**Platform:** Google Colab

**Technology:** Apache Spark (PySpark)
