# Celebal Technologies Summer Internship 2026

# Week 3 
# Assignment_No.3

## Overview

This assignment focuses on applying advanced SQL techniques to analyze the **Sample Superstore** dataset. The data is imported into MySQL, organized into normalized tables, and analyzed using **Subqueries**, **Common Table Expressions (CTEs)**, and **Window Functions** to generate meaningful business insights.

---

## Dataset Information

* **Dataset:** Sample Superstore
* **Database:** MySQL
* **Staging Table:** `superstore_raw`

The raw dataset is normalized into the following tables:

* `customers`
* `products`
* `orders`

---

## Project Structure

```text
Assignment_No.3
│
├── dataset
│   └── Sample - Superstore.csv
│
├── sql
│   ├── 1_create_tables.sql
│   ├── 2_insert_data.sql
│   ├── 3_quires.sql
│   ├── 4_final_query.sql
│   └── 5_mini_project.sql
│
├── Screenshots
│   └── Query Screenshots
│
└── README.md
```

---

## SQL Concepts Demonstrated

This assignment covers the following SQL concepts:

* Data Normalization using `SELECT DISTINCT`
* Subqueries
* Correlated Subqueries
* Common Table Expressions (CTEs)
* Window Functions
* `ROW_NUMBER()`
* `RANK()`
* `DENSE_RANK()`
* INNER JOIN
* Aggregate Functions
* `GROUP BY`
* `ORDER BY`
* Customer Sales Analysis

---

## Assignment Activities

The following tasks were completed during this assignment:

* Imported the Sample Superstore dataset into MySQL Workbench.
* Created a staging table (`superstore_raw`) for the raw data.
* Built separate **customers**, **products**, and **orders** tables from the staging table.
* Applied Subqueries to identify above-average sales and highest-value orders.
* Used Common Table Expressions (CTEs) to simplify customer-level aggregations.
* Implemented Window Functions to rank customers and orders based on sales.
* Combined JOINs, CTEs, and Window Functions to perform customer sales analysis.
* Generated business insights from the sales data.

---

## Customer Sales Analysis

The mini project includes answers to the following business questions:

* Identify the Top 5 customers based on total sales.
* Identify the Bottom 5 customers based on total sales.
* Find customers who placed only one order.
* List customers whose total sales exceed the average customer sales.
* Determine the highest-value order placed by each customer.

---

## Software & Technologies Used

* MySQL Workbench
* MySQL 8
* Git
* GitHub

---

## Learning Outcomes

By completing this assignment, I gained practical experience with:

* Writing advanced SQL queries.
* Using Subqueries and CTEs for complex analysis.
* Applying Window Functions for ranking and reporting.
* Performing customer-centric sales analysis.
* Structuring relational databases from raw datasets.
* Extracting meaningful business insights using SQL.

---

## Author

**Ritesh Deshmukh**

B.Tech – Computer Science Engineering

Sanjivani College of Engineering
