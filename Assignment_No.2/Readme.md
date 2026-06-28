
# 🛒   Sales Data Analysis Assignment

## 📌 Introduction

This repository contains my **SQL-based Data Analysis Assignment**, focused on analyzing an **E-Commerce Sales Database** named **ShopEase**.

Here, **ShopEase** is simply used as the **database name** for the assignment dataset .

The purpose of this assignment is to apply SQL concepts in a structured way and solve practical business-related queries using relational data.

The database contains sales-related information such as:

- Customer details
- Product information
- Order records
- Order item details

Using this dataset, the assignment focuses on extracting meaningful insights by applying SQL operations like filtering, aggregation, joins, sorting, and transactions.

This assignment is designed to strengthen practical SQL knowledge and simulate real-world sales data analysis scenarios.

---

## 🎯 Objective

The objective of this assignment is to analyze e-commerce sales data using SQL and perform:

- Data loading into SQL database
- Table exploration and schema understanding
- Data filtering using `WHERE`
- Aggregation using `GROUP BY`
- Sorting and limiting results
- Joining multiple tables
- Business use-case solving
- Data validation
- Transaction handling

---

## 📚 SQL Concepts Covered

This assignment covers:

### 1. SQL Basics

- SELECT
- DISTINCT
- Primary Keys
- Constraints
- UNIQUE
- CHECK
- NOT NULL

---

### 2. Filtering & Optimization

- WHERE clause
- BETWEEN
- AND / OR
- NOT
- Index optimization
- Query optimization (SARGable queries)

---

### 3. Aggregation

- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()
- GROUP BY
- HAVING

---

### 4. Joins & Relationships

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- Foreign Keys

---

### 5. Advanced SQL

- CASE statements
- Conditional aggregation
- Transactions
- ACID properties

---

## 🗂 Database Structure

The database consists of 4 tables:

### customers

Stores customer details.

Fields:

- customer_id
- first_name
- last_name
- email
- city
- state
- join_date
- is_premium

---

### products

Stores product information.

Fields:

- product_id
- product_name
- category
- brand
- unit_price
- stock_qty

---

### orders

Stores order details.

Fields:

- order_id
- customer_id
- order_date
- status
- total_amount

---

### order_items

Stores item-level order details.

Fields:

- item_id
- order_id
- product_id
- quantity
- unit_price
- discount_pct

---

## 🔗 Database Relationships

```text
customers (1) -------- (N) orders
orders (1) ----------- (N) order_items
products (1) --------- (N) order_items
````

Foreign Keys:

* `orders.customer_id → customers.customer_id`
* `order_items.order_id → orders.order_id`
* `order_items.product_id → products.product_id`

---

## 📂 Assignment Structure

The assignment is divided into five sections:

### Section A — SQL Basics

Focus:

* Data retrieval
* Constraints
* Primary keys

File:

```text
section_a_sql_basics.sql
```

---

### Section B — Filtering & Optimization

Focus:

* Filtering records
* Using indexes
* Query optimization

File:

```text
section_b_filtering_optimization.sql
```

---

### Section C — Aggregation

Focus:

* Summarizing data
* Revenue calculations
* Category analysis

File:

```text
section_c_aggregation.sql
```

---

### Section D — Joins & Relationships

Focus:

* Combining tables
* Understanding relationships
* Foreign key validations

File:

```text
section_d_joins_relationships.sql
```

---

### Section E — Advanced Concepts

Focus:

* CASE statements
* Transactions
* ACID properties

File:

```text
section_e_advanced_concepts.sql
```

---

## ⚙ Workflow

This assignment follows:

1. Create database
2. Create tables
3. Add indexes
4. Insert sample data
5. Validate records
6. Run section-wise queries
7. Analyze outputs
8. Document insights

---

## 📈 Analysis Goals

Using SQL queries, this assignment answers questions like:

* How many total orders exist?
* What is the total delivered revenue?
* Which product categories are expensive?
* Which customers belong to a specific state?
* What products are premium or budget?
* How are orders distributed by status?

---

## 🛠 Tools Used

* MySQL Workbench
* SQL
* GitHub

---

## 📁 Project Structure

```text

ASSIGNMENT_NO.2
│
├── Database_setup/                      # Database initialization files
│   ├── shopease_database_setup.pdf     # Documentation for database schema, tables, and setup process
│   └── shopease.sql                    # Main SQL file containing database creation, table creation, indexes, and sample data
│
├── Section_A/                          # SQL Basics (SELECT, Constraints, Primary Keys)
│   ├── basic_queries.sql               # Basic SQL queries for data retrieval and constraint validation
│   └── section_a_documentation.pdf     # Explanation and outputs for Section A queries
│
├── Section_B/                          # Filtering & Optimization (WHERE, Indexes)
│   ├── filtering_queries.sql           # Queries using WHERE clause, date filtering, and optimization concepts
│   └── section_b_documentation.pdf     # Documentation and results for Section B
│
├── Section_C/                          # Aggregation (GROUP BY, SUM, COUNT, AVG, MIN, MAX)
│   ├── aggregation_queries.sql         # Aggregate queries for sales analysis and summaries
│   └── section_c_documentation.pdf     # Explanation and outputs for Section C
│
├── Section_D/                          # Joins & Relationships
│   ├── joins_queries.sql               # INNER JOIN, LEFT JOIN, RIGHT JOIN, and foreign key queries
│   └── section_d_documentation.pdf     # Documentation and outputs for Section D
│
├── Section_E/                          # Advanced Concepts (CASE, ACID, Transactions)
│   ├── advanced_queries.sql            # CASE statements, transaction handling, and advanced SQL concepts
│   └── section_e_documentation.pdf     # Explanation and outputs for Section E
│
└── Readme.md                           # Project overview, objectives, workflow, and documentation
```


---

## 🎓 Learning Outcomes

After completing this assignment, I gained hands-on experience in:

* Writing SQL queries
* Understanding relational databases
* Using filters and aggregations
* Working with joins
* Handling transactions
* Maintaining data consistency
* Solving business queries using SQL

---

## ✅ Conclusion

This assignment helped strengthen my SQL fundamentals by working on a structured e-commerce sales dataset.

It provided practical exposure to querying, analyzing, and validating relational data, which is essential for data analytics and data engineering roles.

```
```
