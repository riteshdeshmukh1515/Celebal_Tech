# 🚀 Celebal Technologies CEI 2026

# Week 3

# Assignment No. 3 – SQL Advanced Analytics

---

## 📖 Overview

This assignment focuses on applying **Advanced SQL** concepts to analyze the **Sample Superstore** dataset using **MySQL Workbench**. The project demonstrates the use of **Subqueries**, **Common Table Expressions (CTEs)**, **Window Functions**, and **JOINs** to solve business problems and generate meaningful sales insights.

The Superstore dataset is first imported into a staging table (`superstore_raw`) and then normalized into separate **customers**, **products**, and **orders** tables. Various analytical SQL queries are performed to analyze customer behavior, sales performance, and order trends.

---

## 🎯 Assignment Objective

The primary objective of this assignment is to practice advanced SQL concepts by performing sales analysis on the Superstore dataset.

The tasks completed include:

* Load the Superstore dataset into a staging table (`superstore_raw`).
* Create **customers**, **products**, and **orders** tables using `SELECT DISTINCT`.
* Apply **Subqueries** to identify above-average sales and highest-value orders.
* Use **Common Table Expressions (CTEs)** for customer-level aggregations and intermediate calculations.
* Implement **Window Functions** (`ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`) for customer and order ranking.
* Combine **JOINs**, **CTEs**, and **Window Functions** to perform customer sales analysis.
* Generate customer rankings, identify top and bottom customers, and analyze sales distribution.
* Document business insights obtained from the analysis.

---

## 📂 Dataset Information

* **Dataset:** Sample Superstore
* **Database:** MySQL
* **Staging Table:** `superstore_raw`

The raw dataset is normalized into the following tables:

* `customers`
* `products`
* `orders`

---

## 📁 Project Structure

```text
Assignment_No.3
│
├── dataset
│   └── Sample - Superstore.csv
│
├── sql
│   ├── 1_create_tables.sql
│   ├── 2_insert_data.sql
│   ├── 3_queries.sql
│   ├── 4_final_query.sql
│   └── 5_mini_project.sql
│
├── Screenshots
│   └── Query Screenshots
│
└── README.md
```

---

## 🛠 SQL Concepts Demonstrated

This assignment includes the following SQL concepts:

* Data Normalization using `SELECT DISTINCT`
* Subqueries
* Correlated Subqueries
* Common Table Expressions (CTEs)
* Window Functions
* `ROW_NUMBER()`
* `RANK()`
* `DENSE_RANK()`
* INNER JOIN
* Aggregate Functions (`SUM`, `AVG`, `COUNT`, `MAX`, `MIN`)
* `GROUP BY`
* `HAVING`
* `ORDER BY`
* Customer Sales Analysis

---

## ✅ Assignment Activities

The following tasks were completed during this assignment:

* Imported the Sample Superstore dataset into MySQL Workbench.
* Created the `superstore_raw` staging table.
* Built normalized `customers`, `products`, and `orders` tables using `SELECT DISTINCT`.
* Executed Subqueries to identify above-average sales and highest-value orders.
* Used CTEs to calculate customer-level sales metrics and perform intermediate aggregations.
* Applied Window Functions to rank customers and orders based on sales.
* Combined JOINs, CTEs, and Window Functions to generate customer sales rankings.
* Performed customer sales analysis and documented business insights.

---

## 📊 Customer Sales Analysis

The following business questions were answered during the mini project:

* Identify the Top 5 customers based on total sales.
* Identify the Bottom 5 customers based on total sales.
* Find customers who placed only one order.
* Identify customers whose total sales are above the average customer sales.
* Determine the highest-value order placed by each customer.
* Rank customers based on total sales.
* Analyze region-wise sales performance.
* Identify the highest-performing products.

---

## 📈 Output

The final submission contains:

* SQL Scripts
* Query Results
* Output Screenshots
* Customer Sales Analysis
* Business Insights

---

## 💡 Key Insights

Some important observations from the analysis include:

* A small percentage of customers contributed a significant share of the total revenue.
* High-value orders accounted for a major portion of overall sales.
* Several customers placed only one order, indicating potential opportunities for customer retention.
* Window Functions simplified customer ranking and order analysis.
* CTEs improved the readability and maintainability of complex SQL queries.
* Combining JOINs with CTEs enabled comprehensive customer sales reporting.
* Sales performance varied across regions and product categories.

---

## 💻 Software & Technologies Used

* MySQL Workbench
* MySQL 8
* SQL
* Git
* GitHub

---

## 🎓 Learning Outcomes

Through this assignment, I gained hands-on experience in:

* Importing and managing datasets in MySQL.
* Designing normalized relational database tables.
* Writing advanced SQL queries using Subqueries.
* Using Common Table Expressions (CTEs) for complex data analysis.
* Applying Window Functions for ranking and analytical reporting.
* Performing customer and sales analytics using SQL.
* Extracting meaningful business insights from retail sales data.
* Organizing SQL projects using Git and GitHub.

---

## 👨‍💻 Author

**Ritesh Deshmukh**

B.Tech – Computer Engineering

Sanjivani College of Engineering

**Celebal Technologies CEI 2026**
