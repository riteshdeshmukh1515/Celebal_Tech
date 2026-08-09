import pandas as pd
from pathlib import Path


# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Raw data directory
RAW_DIR = BASE_DIR / "data" / "raw"


print("=" * 60)
print("RAW DATA VALIDATION")
print("=" * 60)


# ------------------------------------------------------------
# Load files
# ------------------------------------------------------------

customers = pd.read_csv(RAW_DIR / "customers.csv")
products = pd.read_csv(RAW_DIR / "products.csv")
orders = pd.read_csv(RAW_DIR / "orders.csv")
order_items = pd.read_csv(RAW_DIR / "order_items.csv")


# ------------------------------------------------------------
# Row counts
# ------------------------------------------------------------

print("\nROW COUNTS")
print("-" * 60)

print(f"Customers    : {len(customers):,}")
print(f"Products     : {len(products):,}")
print(f"Orders       : {len(orders):,}")
print(f"Order Items  : {len(order_items):,}")


# ------------------------------------------------------------
# Duplicate checks
# ------------------------------------------------------------

print("\nDUPLICATE RECORDS")
print("-" * 60)

print(
    "Duplicate customers:",
    customers["customer_id"].duplicated().sum()
)

print(
    "Duplicate products:",
    products["product_id"].duplicated().sum()
)

print(
    "Duplicate orders:",
    orders["order_id"].duplicated().sum()
)


# ------------------------------------------------------------
# Missing values
# ------------------------------------------------------------

print("\nMISSING VALUES")
print("-" * 60)

print(
    "Missing customer IDs in orders:",
    orders["customer_id"].isna().sum()
)


# ------------------------------------------------------------
# Negative quantities
# ------------------------------------------------------------

print("\nINVALID QUANTITIES")
print("-" * 60)

print(
    "Negative quantities:",
    (order_items["quantity"] < 0).sum()
)


# ------------------------------------------------------------
# Invalid emails
# ------------------------------------------------------------

print("\nINVALID EMAILS")
print("-" * 60)

invalid_emails = customers[
    ~customers["email"].str.contains(
        "@",
        na=False
    )
]

print(
    "Invalid emails:",
    len(invalid_emails)
)


# ------------------------------------------------------------
# Product name inconsistencies
# ------------------------------------------------------------

print("\nPRODUCT NAME SAMPLE")
print("-" * 60)

print(
    products["product_name"].head(10).to_string(
        index=False
    )
)


# ------------------------------------------------------------
# Completion
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("RAW DATA CHECK COMPLETED")
print("=" * 60)