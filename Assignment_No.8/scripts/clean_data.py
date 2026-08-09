
"""
E-Commerce Analytics System
 Data Cleaning with Pandas

This script:

1. Loads raw CSV files
2. Removes duplicate records
3. Handles missing values
4. Cleans email addresses
5. Cleans product names
6. Fixes date formats
7. Handles invalid quantities
8. Validates primary keys
9. Validates foreign keys
10. Saves cleaned CSV files
11. Generates a cleaning report
"""

from pathlib import Path
import re

import pandas as pd


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"

CLEANED_DIR = BASE_DIR / "data" / "cleaned"

OUTPUT_DIR = BASE_DIR / "output"


# Create required directories
CLEANED_DIR.mkdir(
    parents=True,
    exist_ok=True
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 2. CLEANING REPORT
# ============================================================

cleaning_report = []


def add_report(
    table,
    issue,
    before,
    after,
    action
):
    """
    Add a cleaning operation to the report.
    """

    cleaning_report.append({
        "table": table,
        "issue": issue,
        "rows_before": before,
        "rows_after": after,
        "action": action
    })


# ============================================================
# 3. LOAD RAW DATA
# ============================================================

def load_data():

    print("\nLoading raw CSV files...")

    customers = pd.read_csv(
        RAW_DIR / "customers.csv"
    )

    products = pd.read_csv(
        RAW_DIR / "products.csv"
    )

    orders = pd.read_csv(
        RAW_DIR / "orders.csv"
    )

    order_items = pd.read_csv(
        RAW_DIR / "order_items.csv"
    )

    print("Customers loaded :", len(customers))
    print("Products loaded  :", len(products))
    print("Orders loaded    :", len(orders))
    print("Order items      :", len(order_items))

    return (
        customers,
        products,
        orders,
        order_items
    )


# ============================================================
# 4. CLEAN CUSTOMERS
# ============================================================

def clean_customers(customers):

    print("\n" + "=" * 60)
    print("CLEANING CUSTOMERS")
    print("=" * 60)

    # --------------------------------------------------------
    # Remove duplicate customer IDs
    # --------------------------------------------------------

    before = len(customers)

    customers = customers.drop_duplicates(
        subset=["customer_id"],
        keep="first"
    )

    after = len(customers)

    add_report(
        "customers",
        "duplicate_customer_id",
        before,
        after,
        "Removed duplicate customer records"
    )

    print(
        f"Duplicates removed: {before - after}"
    )


    # --------------------------------------------------------
    # Clean customer name
    # --------------------------------------------------------

    customers["customer_name"] = (
        customers["customer_name"]
        .astype("string")
        .str.strip()
    )


    # --------------------------------------------------------
    # Clean email
    # --------------------------------------------------------

    customers["email"] = (
        customers["email"]
        .astype("string")
        .str.strip()
        .str.lower()
    )


    # --------------------------------------------------------
    # Validate email format
    # --------------------------------------------------------

    email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    valid_email = customers["email"].str.match(
        email_pattern,
        na=False
    )

    invalid_email_count = (
        (~valid_email).sum()
    )

    print(
        f"Invalid emails found: {invalid_email_count}"
    )


    # Replace invalid emails with NULL
    customers.loc[
        ~valid_email,
        "email"
    ] = pd.NA


    add_report(
        "customers",
        "invalid_email",
        invalid_email_count,
        0,
        "Invalid emails replaced with NULL"
    )


    # --------------------------------------------------------
    # Registration date
    # --------------------------------------------------------

    customers["registration_date"] = pd.to_datetime(
        customers["registration_date"],
        errors="coerce"
    )


    invalid_dates = customers[
        "registration_date"
    ].isna().sum()

    print(
        f"Invalid registration dates: {invalid_dates}"
    )


    # Save date in standard format
    customers["registration_date"] = (
        customers["registration_date"]
        .dt.strftime("%Y-%m-%d")
    )


    # --------------------------------------------------------
    # Customer type
    # --------------------------------------------------------

    customers["customer_type"] = (
        customers["customer_type"]
        .astype("string")
        .str.strip()
        .str.upper()
    )


    # --------------------------------------------------------
    # Final customer validation
    # --------------------------------------------------------

    customers = customers[
        customers["customer_id"].notna()
    ]

    return customers


# ============================================================
# 5. CLEAN PRODUCTS
# ============================================================

def clean_products(products):

    print("\n" + "=" * 60)
    print("CLEANING PRODUCTS")
    print("=" * 60)


    # --------------------------------------------------------
    # Remove duplicate product IDs
    # --------------------------------------------------------

    before = len(products)

    products = products.drop_duplicates(
        subset=["product_id"],
        keep="first"
    )

    after = len(products)

    add_report(
        "products",
        "duplicate_product_id",
        before,
        after,
        "Removed duplicate product records"
    )

    print(
        f"Duplicates removed: {before - after}"
    )


    # --------------------------------------------------------
    # Clean product name
    # --------------------------------------------------------

    products["product_name"] = (
        products["product_name"]
        .astype("string")
        .str.strip()
        .str.lower()
        .str.title()
    )


    # --------------------------------------------------------
    # Clean category
    # --------------------------------------------------------

    products["category"] = (
        products["category"]
        .astype("string")
        .str.strip()
        .str.title()
    )


    # --------------------------------------------------------
    # Clean subcategory
    # --------------------------------------------------------

    products["subcategory"] = (
        products["subcategory"]
        .astype("string")
        .str.strip()
        .str.title()
    )


    # --------------------------------------------------------
    # Convert cost price to numeric
    # --------------------------------------------------------

    products["cost_price"] = pd.to_numeric(
        products["cost_price"],
        errors="coerce"
    )


    # --------------------------------------------------------
    # Invalid price
    # --------------------------------------------------------

    invalid_prices = (
        products["cost_price"] <= 0
    ).sum()

    print(
        f"Invalid product prices: {invalid_prices}"
    )


    products.loc[
        products["cost_price"] <= 0,
        "cost_price"
    ] = pd.NA


    return products


# ============================================================
# 6. CLEAN ORDERS
# ============================================================

def clean_orders(
    orders,
    customers
):

    print("\n" + "=" * 60)
    print("CLEANING ORDERS")
    print("=" * 60)


    # --------------------------------------------------------
    # Remove duplicate order IDs
    # --------------------------------------------------------

    before = len(orders)

    orders = orders.drop_duplicates(
        subset=["order_id"],
        keep="first"
    )

    after = len(orders)

    add_report(
        "orders",
        "duplicate_order_id",
        before,
        after,
        "Removed duplicate order records"
    )

    print(
        f"Duplicates removed: {before - after}"
    )


    # --------------------------------------------------------
    # Clean customer ID
    # --------------------------------------------------------

    orders["customer_id"] = (
        orders["customer_id"]
        .astype("string")
        .str.strip()
    )


    # --------------------------------------------------------
    # Convert missing customer IDs
    # --------------------------------------------------------

    missing_customers = (
        orders["customer_id"].isna()
    ).sum()

    print(
        f"Missing customer IDs: {missing_customers}"
    )


    # --------------------------------------------------------
    # Referential integrity
    # --------------------------------------------------------

    valid_customer_ids = set(
        customers["customer_id"]
    )


    valid_customer_reference = (
        orders["customer_id"]
        .isin(valid_customer_ids)
        | orders["customer_id"].isna()
    )


    invalid_customer_references = (
        ~valid_customer_reference
    ).sum()


    print(
        "Invalid customer references:",
        invalid_customer_references
    )


    # Remove invalid customer references
    orders = orders[
        valid_customer_reference
    ]


    # --------------------------------------------------------
    # Handle missing customer IDs
    # --------------------------------------------------------

    # Orders without customers cannot safely be connected
    # to a customer in our relational analytics.
    #
    # We remove these orders from the cleaned customer-order
    # dataset.

    before_missing_removal = len(orders)

    orders = orders[
        orders["customer_id"].notna()
    ]

    after_missing_removal = len(orders)


    add_report(
        "orders",
        "missing_customer_id",
        before_missing_removal,
        after_missing_removal,
        "Removed orders without a customer reference"
    )


    # --------------------------------------------------------
    # Clean order dates
    # --------------------------------------------------------

    orders["order_date"] = pd.to_datetime(
        orders["order_date"],
        errors="coerce",
        dayfirst=False
    )


    invalid_dates = (
        orders["order_date"].isna()
    ).sum()


    print(
        f"Invalid order dates: {invalid_dates}"
    )


    # Remove orders with invalid dates
    orders = orders[
        orders["order_date"].notna()
    ]


    # --------------------------------------------------------
    # Standard date format
    # --------------------------------------------------------

    orders["order_date"] = (
        orders["order_date"]
        .dt.strftime("%Y-%m-%d %H:%M:%S")
    )


    # --------------------------------------------------------
    # Clean order status
    # --------------------------------------------------------

    orders["status"] = (
        orders["status"]
        .astype("string")
        .str.strip()
        .str.upper()
    )


    # --------------------------------------------------------
    # Clean region
    # --------------------------------------------------------

    orders["region_code"] = (
        orders["region_code"]
        .astype("string")
        .str.strip()
        .str.upper()
    )


    return orders


# ============================================================
# 7. CLEAN ORDER ITEMS
# ============================================================

def clean_order_items(
    order_items,
    orders,
    products
):

    print("\n" + "=" * 60)
    print("CLEANING ORDER ITEMS")
    print("=" * 60)


    # --------------------------------------------------------
    # Remove duplicate item IDs
    # --------------------------------------------------------

    before = len(order_items)

    order_items = order_items.drop_duplicates(
        subset=["item_id"],
        keep="first"
    )

    after = len(order_items)


    add_report(
        "order_items",
        "duplicate_item_id",
        before,
        after,
        "Removed duplicate order item records"
    )


    print(
        f"Duplicates removed: {before - after}"
    )


    # --------------------------------------------------------
    # Convert quantity to numeric
    # --------------------------------------------------------

    order_items["quantity"] = pd.to_numeric(
        order_items["quantity"],
        errors="coerce"
    )


    # --------------------------------------------------------
    # Negative quantities
    # --------------------------------------------------------

    negative_quantity_count = (
        order_items["quantity"] < 0
    ).sum()


    print(
        f"Negative quantities: {negative_quantity_count}"
    )


    # In this project, negative quantities are treated
    # as invalid raw records and removed.

    order_items = order_items[
        order_items["quantity"] > 0
    ]


    # --------------------------------------------------------
    # Product ID validation
    # --------------------------------------------------------

    valid_product_ids = set(
        products["product_id"]
    )


    valid_product_reference = (
        order_items["product_id"]
        .isin(valid_product_ids)
    )


    invalid_product_references = (
        ~valid_product_reference
    ).sum()


    print(
        "Invalid product references:",
        invalid_product_references
    )


    order_items = order_items[
        valid_product_reference
    ]


    # --------------------------------------------------------
    # Order ID validation
    # --------------------------------------------------------

    valid_order_ids = set(
        orders["order_id"]
    )


    valid_order_reference = (
        order_items["order_id"]
        .isin(valid_order_ids)
    )


    invalid_order_references = (
        ~valid_order_reference
    ).sum()


    print(
        "Invalid order references:",
        invalid_order_references
    )


    order_items = order_items[
        valid_order_reference
    ]


    # --------------------------------------------------------
    # Unit price
    # --------------------------------------------------------

    order_items["unit_price"] = pd.to_numeric(
        order_items["unit_price"],
        errors="coerce"
    )


    # Remove invalid prices
    order_items = order_items[
        order_items["unit_price"] > 0
    ]


    # --------------------------------------------------------
    # Discount
    # --------------------------------------------------------

    order_items["discount_percent"] = pd.to_numeric(
        order_items["discount_percent"],
        errors="coerce"
    )


    # Keep discount between 0 and 100
    order_items.loc[
        (
            order_items["discount_percent"] < 0
        )
        |
        (
            order_items["discount_percent"] > 100
        ),
        "discount_percent"
    ] = pd.NA


    # --------------------------------------------------------
    # Final data types
    # --------------------------------------------------------

    order_items["quantity"] = (
        order_items["quantity"]
        .astype("int64")
    )


    return order_items


# ============================================================
# 8. FINAL REFERENTIAL INTEGRITY CHECK
# ============================================================

def validate_referential_integrity(
    customers,
    products,
    orders,
    order_items
):

    print("\n" + "=" * 60)
    print("FINAL REFERENTIAL INTEGRITY CHECK")
    print("=" * 60)


    customer_ids = set(
        customers["customer_id"]
    )

    product_ids = set(
        products["product_id"]
    )

    order_ids = set(
        orders["order_id"]
    )


    # --------------------------------------------------------
    # Orders -> Customers
    # --------------------------------------------------------

    invalid_order_customers = (
        ~orders["customer_id"].isin(
            customer_ids
        )
    ).sum()


    print(
        "Invalid Orders -> Customers:",
        invalid_order_customers
    )


    # --------------------------------------------------------
    # Order Items -> Orders
    # --------------------------------------------------------

    invalid_item_orders = (
        ~order_items["order_id"].isin(
            order_ids
        )
    ).sum()


    print(
        "Invalid Order Items -> Orders:",
        invalid_item_orders
    )


    # --------------------------------------------------------
    # Order Items -> Products
    # --------------------------------------------------------

    invalid_item_products = (
        ~order_items["product_id"].isin(
            product_ids
        )
    ).sum()


    print(
        "Invalid Order Items -> Products:",
        invalid_item_products
    )


    # --------------------------------------------------------
    # Final result
    # --------------------------------------------------------

    if (
        invalid_order_customers == 0
        and invalid_item_orders == 0
        and invalid_item_products == 0
    ):

        print("\n✓ Referential integrity PASSED")

        return True

    else:

        print("\n✗ Referential integrity FAILED")

        return False


# ============================================================
# 9. SAVE CLEANED DATA
# ============================================================

def save_cleaned_data(
    customers,
    products,
    orders,
    order_items
):

    print("\n" + "=" * 60)
    print("SAVING CLEANED DATA")
    print("=" * 60)


    customers.to_csv(
        CLEANED_DIR / "customers_clean.csv",
        index=False
    )


    products.to_csv(
        CLEANED_DIR / "products_clean.csv",
        index=False
    )


    orders.to_csv(
        CLEANED_DIR / "orders_clean.csv",
        index=False
    )


    order_items.to_csv(
        CLEANED_DIR / "order_items_clean.csv",
        index=False
    )


    print(
        "✓ customers_clean.csv"
    )

    print(
        "✓ products_clean.csv"
    )

    print(
        "✓ orders_clean.csv"
    )

    print(
        "✓ order_items_clean.csv"
    )


# ============================================================
# 10. SAVE CLEANING REPORT
# ============================================================

def save_cleaning_report():

    report_df = pd.DataFrame(
        cleaning_report
    )


    report_path = (
        OUTPUT_DIR
        / "cleaning_report.csv"
    )


    report_df.to_csv(
        report_path,
        index=False
    )


    print(
        f"\n✓ Cleaning report saved to:"
    )

    print(
        f"  {report_path}"
    )


# ============================================================
# 11. MAIN PIPELINE
# ============================================================

def main():

    print("=" * 70)
    print("E-COMMERCE ANALYTICS SYSTEM")
    print("STAGE 3 - DATA CLEANING WITH PANDAS")
    print("=" * 70)


    # --------------------------------------------------------
    # Load
    # --------------------------------------------------------

    (
        customers,
        products,
        orders,
        order_items
    ) = load_data()


    # --------------------------------------------------------
    # Clean customers
    # --------------------------------------------------------

    customers = clean_customers(
        customers
    )


    # --------------------------------------------------------
    # Clean products
    # --------------------------------------------------------

    products = clean_products(
        products
    )


    # --------------------------------------------------------
    # Clean orders
    # --------------------------------------------------------

    orders = clean_orders(
        orders,
        customers
    )


    # --------------------------------------------------------
    # Clean order items
    # --------------------------------------------------------

    order_items = clean_order_items(
        order_items,
        orders,
        products
    )


    # --------------------------------------------------------
    # Validate relationships
    # --------------------------------------------------------

    integrity_passed = (
        validate_referential_integrity(
            customers,
            products,
            orders,
            order_items
        )
    )


    # --------------------------------------------------------
    # Save cleaned datasets
    # --------------------------------------------------------

    save_cleaned_data(
        customers,
        products,
        orders,
        order_items
    )


    # --------------------------------------------------------
    # Save report
    # --------------------------------------------------------

    save_cleaning_report()


    # ========================================================
    # FINAL SUMMARY
    # ========================================================

    print("\n" + "=" * 70)
    print("COMPLETED")
    print("=" * 70)

    print("\nCleaned row counts:")

    print(
        f"Customers    : {len(customers):,}"
    )

    print(
        f"Products     : {len(products):,}"
    )

    print(
        f"Orders       : {len(orders):,}"
    )

    print(
        f"Order Items  : {len(order_items):,}"
    )


    if integrity_passed:

        print(
            "\n✓ All foreign-key relationships are valid."
        )

    else:

        print(
            "\n⚠ Some foreign-key relationships are invalid."
        )


    print(
        "\nCleaned files are available in:"
    )

    print(
        f"  {CLEANED_DIR}"
    )

    print(
        "\nNext stage:"
    )

    print(
        "  Load cleaned data into SQLite database."
    )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()

