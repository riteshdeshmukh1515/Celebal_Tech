# 📘 Assignment No. 1  
# 🛒 Shopping Dataset Analysis using Python

---

## 📌 Introduction

This assignment focuses on performing **Exploratory Data Analysis (EDA)** on a shopping dataset.  
The main purpose of this assignment is to understand the dataset, clean the data, perform different types of analysis, and generate meaningful insights using Python.

This assignment helps in improving practical knowledge of:

- Data handling
- Data cleaning
- Data analysis
- Data visualization
- Feature engineering

It also provides hands-on experience with real-world shopping data.

---

## 🎯 Objective of the Assignment

The main objectives of this assignment are:

✔ Load and inspect the shopping dataset  
✔ Understand dataset structure and content  
✔ Identify and handle missing values  
✔ Convert price-related columns into proper numeric format  
✔ Remove duplicate entries  
✔ Create new derived columns for better analysis  
✔ Perform Exploratory Data Analysis (EDA)  
✔ Generate insights from data  
✔ Visualize patterns and trends using charts  

---

## 📂 Dataset Information

### Dataset Used:
**combined_dataset.csv**

The dataset contains product-level information related to shopping items.

### Important Columns in Dataset:

| Column Name | Description |
|---|---|
| title | Product name |
| category | Product category |
| initial_price | Original price of product |
| final_price | Discounted price |
| discount | Discount value |
| rating | Product rating |
| ratings_count | Number of customer ratings |

This dataset is useful for analyzing:

- Product pricing
- Customer ratings
- Product popularity
- Discount patterns
- Category performance

---

## 🛠 Libraries Used

The following Python libraries were used in this assignment:

### 1. Pandas
Used for:
- Loading dataset
- Data cleaning
- Data manipulation

```python
import pandas as pd
```

---

### 2. NumPy
Used for:
- Numerical calculations
- Array operations

```python
import numpy as np
```

---

### 3. Matplotlib
Used for:
- Basic plotting
- Data visualization

```python
import matplotlib.pyplot as plt
```

---

### 4. Seaborn
Used for:
- Advanced visualizations
- Better chart styling

```python
import seaborn as sns
```

---

# 🚀 Concepts Covered in This Assignment

This assignment covers the following concepts:

- Data Loading
- Data Inspection
- Data Cleaning
- Missing Value Handling
- Data Type Conversion
- Duplicate Removal
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Univariate Analysis
- Bivariate Analysis
- Category-Level Analysis
- Data Visualization
- Business Insight Generation

---

# 📋 Steps Performed

---

# Step 1: Data Loading

The dataset was loaded into a Pandas DataFrame.

### Tasks performed:

✔ Imported required libraries  
✔ Loaded CSV file  
✔ Checked shape of dataset  
✔ Checked column names  

Example:

```python
df = pd.read_csv("combined_dataset.csv")
```

Purpose:
To bring data into the notebook for analysis.

---

# Step 2: Initial Dataset Inspection

This step helps in understanding the dataset.

### Operations performed:

### Viewing first 5 rows:

```python
df.head()
```

Purpose:
To check sample data.

---

### Viewing last 5 rows:

```python
df.tail()
```

Purpose:
To check ending records.

---

### Checking dataset information:

```python
df.info()
```

Purpose:
To understand:
- Number of rows
- Number of columns
- Data types

---

### Checking missing values:

```python
df.isnull().sum()
```

Purpose:
To identify null values.

---

### Statistical summary:

```python
df.describe()
```

Purpose:
To analyze:
- Mean
- Minimum
- Maximum
- Standard deviation

---

# Step 3: Data Cleaning

Data cleaning is important before analysis.

### Cleaning performed:

✔ Converted price columns into numeric  
✔ Removed ₹ symbol  
✔ Removed commas  
✔ Removed quotes  
✔ Filled missing values  
✔ Removed duplicate rows  

Example:

```python
df['final_price'] = df['final_price'].str.replace('₹','')
```

Purpose:
To make price columns usable for calculations.

---

# Step 4: Feature Engineering

New useful columns were created.

---

## 1. Price Difference

Formula:

```python
price_difference = initial_price - final_price
```

Purpose:
To find actual discount amount.

---

## 2. Popularity Score

Formula:

```python
popularity_score = rating * ratings_count
```

Purpose:
To measure product popularity.

---

## 3. Discount Percentage

Formula:

```python
discount_percentage = (price_difference / initial_price) * 100
```

Purpose:
To calculate percentage discount.

---

# Step 5: Exploratory Data Analysis (EDA)

EDA helps in understanding data patterns.

---

## 📊 Univariate Analysis

Univariate analysis means analyzing one variable.

### Performed:

- Final Price Distribution
- Rating Distribution
- Category Count

Charts used:

✔ Histogram  
✔ Boxplot  
✔ Violin Plot  

Purpose:
To understand distribution of single variables.

---

## 🔗 Bivariate Analysis

Bivariate analysis means analyzing relationship between two variables.

### Performed:

- Price vs Rating
- Discount vs Ratings Count
- Initial Price vs Final Price

Charts used:

✔ Scatter Plot  
✔ Line Plot  

Purpose:
To identify relationships.

---

## 🏷 Category-Level Analysis

Category-level analysis means grouped analysis by category.

### Performed:

- Average Price by Category
- Average Rating by Category
- Total Ratings Count by Category
- Discount Analysis by Category

Charts used:

✔ Bar Chart  
✔ Pie Chart  

Purpose:
To compare category performance.

---

# 📈 Data Visualizations Used

The following charts were used:

- Histogram
- Bar Chart
- Boxplot
- Pie Chart
- Scatter Plot
- Line Plot
- Violin Plot

These charts helped in better understanding of the data.

---

# 💡 Key Findings

After analysis, the following findings were observed:

✔ Some categories have very high average prices  
✔ Products with high discounts receive more engagement  
✔ Highly rated products are generally more popular  
✔ Some categories dominate the shopping dataset  
✔ Price and ratings have moderate relationship  

---

# 📊 Business Insights

This analysis can help businesses in:

- Improving pricing strategies
- Increasing product engagement
- Understanding customer preferences
- Identifying top-performing categories
- Designing better discount strategies

---

# ✅ Conclusion

This assignment helped in learning:

- How to work with real-world datasets
- How to clean messy data
- How to perform EDA
- How to visualize data effectively
- How to derive meaningful insights

Overall, this assignment improved practical understanding of **Python for Data Analysis**.

---

# 👨‍💻 Submitted By

**Ritesh Deshmukh**