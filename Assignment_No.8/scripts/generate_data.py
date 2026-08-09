
"""
E-Commerce Analytics System
 Raw Data Generation

This script generates four raw CSV files:

1. customers.csv
2. products.csv
3. orders.csv
4. order_items.csv

The generated data intentionally contains data-quality issues
that will be handled using Pandas.
"""

import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
from faker import Faker


# ============================================================
# 1. CONFIGURATION
# ============================================================

# Reproducibility
RANDOM_SEED = 42

random.seed(RANDOM_SEED)
Faker.seed(RANDOM_SEED)

fake = Faker("en_IN")


# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Raw data directory
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

# Create directory if it does not exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


# Number of records
NUM_CUSTOMERS = 1000
NUM_PRODUCTS = 200
NUM_ORDERS = 5000


# Date range
START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2026, 8, 1)


# ============================================================
# 2. MASTER DATA
# ============================================================

CUSTOMER_TYPES = [
    "REGULAR",
    "PREMIUM",
    "VIP"
]


CATEGORIES = {
    "Electronics": [
        "Smartphones",
        "Laptops",
        "Headphones",
        "Cameras",
        "Accessories"
    ],
    "Clothing": [
        "Shirts",
        "Jeans",
        "Shoes",
        "Jackets",
        "Dresses"
    ],
    "Home": [
        "Furniture",
        "Kitchen",
        "Decor",
        "Lighting",
        "Storage"
    ],
    "Books": [
        "Fiction",
        "Non-Fiction",
        "Technology",
        "Business",
        "Education"
    ]
}


ORDER_STATUSES = [
    "PLACED",
    "SHIPPED",
    "DELIVERED",
    "CANCELLED",
    "RETURNED"
]


REGIONS = [
    "NORTH",
    "SOUTH",
    "EAST",
    "WEST",
    "CENTRAL"
]


PRODUCT_VARIANTS = [
    "Basic",
    "Pro",
    "Plus",
    "Premium",
    "Max"
]


# ============================================================
# 3. HELPER FUNCTIONS
# ============================================================

def random_datetime(start_date, end_date):
    """
    Generate a random datetime between two dates.
    """

    total_seconds = int(
        (end_date - start_date).total_seconds()
    )

    random_seconds = random.randint(
        0,
        total_seconds
    )

    return start_date + timedelta(
        seconds=random_seconds
    )


def create_customer_email(name, number):
    """
    Generate customer email.

    Approximately 2% of emails are intentionally invalid.
    """

    clean_name = (
        name.lower()
        .replace(" ", ".")
        .replace("'", "")
    )

    # Intentionally generate invalid emails
    if random.random() < 0.02:

        invalid_emails = [
            clean_name,
            f"{clean_name}@",
            f"{clean_name}gmail.com",
            f"@gmail.com"
        ]

        return random.choice(invalid_emails)

    return f"{clean_name}{number}@example.com"


def make_messy_product_name(product_name):
    """
    Intentionally introduce inconsistent formatting.
    """

    value = random.random()

    if value < 0.05:
        return f"  {product_name}  "

    if value < 0.10:
        return product_name.upper()

    if value < 0.15:
        return product_name.lower()

    return product_name


def add_duplicate_rows(df, percentage=0.01):
    """
    Add intentional duplicate rows.
    """

    duplicate_count = max(
        1,
        int(len(df) * percentage)
    )

    duplicates = df.sample(
        n=duplicate_count,
        random_state=RANDOM_SEED
    )

    return pd.concat(
        [df, duplicates],
        ignore_index=True
    )


# ============================================================
# 4. GENERATE CUSTOMERS
# ============================================================

def generate_customers():
    """
    Generate customer master data.
    """

    customers = []

    for i in range(1, NUM_CUSTOMERS + 1):

        customer_id = f"CUST{i:05d}"

        customer_name = fake.name()

        email = create_customer_email(
            customer_name,
            i
        )

        registration_date = random_datetime(
            START_DATE,
            END_DATE - timedelta(days=30)
        )

        customer_type = random.choices(
            CUSTOMER_TYPES,
            weights=[70, 25, 5],
            k=1
        )[0]

        customers.append({
            "customer_id": customer_id,
            "customer_name": customer_name,
            "email": email,
            "registration_date": registration_date.strftime(
                "%Y-%m-%d"
            ),
            "customer_type": customer_type
        })

    return pd.DataFrame(customers)


# ============================================================
# 5. GENERATE PRODUCTS
# ============================================================

def generate_products():
    """
    Generate product master data.
    """

    products = []

    product_number = 1

    # Flatten all subcategories
    subcategory_list = []

    for category, subcategories in CATEGORIES.items():

        for subcategory in subcategories:

            subcategory_list.append(
                (category, subcategory)
            )

    while product_number <= NUM_PRODUCTS:

        category, subcategory = random.choice(
            subcategory_list
        )

        variant = random.choice(
            PRODUCT_VARIANTS
        )

        product_name = (
            f"{subcategory} {variant}"
        )

        # Introduce formatting inconsistencies
        product_name = make_messy_product_name(
            product_name
        )

        cost_price = round(
            random.uniform(100, 50000),
            2
        )

        products.append({
            "product_id": f"PROD{product_number:05d}",
            "product_name": product_name,
            "category": category,
            "subcategory": subcategory,
            "cost_price": cost_price
        })

        product_number += 1

    return pd.DataFrame(products)


# ============================================================
# 6. GENERATE ORDERS
# ============================================================

def generate_orders(customers):
    """
    Generate order-level data.

    Approximately 5% of customer IDs are intentionally NULL.
    Approximately 3% of dates use a different format.
    """

    orders = []

    customer_ids = customers[
        "customer_id"
    ].tolist()

    for i in range(1, NUM_ORDERS + 1):

        order_id = f"ORD{i:06d}"

        # Intentionally create NULL customer IDs
        if random.random() < 0.05:

            customer_id = None

        else:

            customer_id = random.choice(
                customer_ids
            )

        order_datetime = random_datetime(
            START_DATE,
            END_DATE
        )

        # Intentionally create inconsistent date formats
        if random.random() < 0.03:

            order_date = order_datetime.strftime(
                "%d-%m-%Y"
            )

        else:

            order_date = order_datetime.strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        status = random.choices(
            ORDER_STATUSES,
            weights=[10, 20, 50, 10, 10],
            k=1
        )[0]

        region_code = random.choice(
            REGIONS
        )

        orders.append({
            "order_id": order_id,
            "customer_id": customer_id,
            "order_date": order_date,
            "status": status,
            "region_code": region_code
        })

    return pd.DataFrame(orders)


# ============================================================
# 7. GENERATE ORDER ITEMS
# ============================================================

def generate_order_items(orders, products):
    """
    Generate line-item level data.

    Each order contains between 1 and 5 products.

    Approximately 3% of quantities are intentionally negative
    to simulate returns/incorrect data.
    """

    order_items = []

    product_ids = products[
        "product_id"
    ].tolist()

    # Create lookup for faster access
    product_lookup = products.set_index(
        "product_id"
    ).to_dict("index")

    item_number = 1

    for _, order in orders.iterrows():

        number_of_items = random.randint(
            1,
            5
        )

        selected_products = random.sample(
            product_ids,
            number_of_items
        )

        for product_id in selected_products:

            # Intentionally create negative quantity
            if random.random() < 0.03:

                quantity = -random.randint(
                    1,
                    3
                )

            else:

                quantity = random.randint(
                    1,
                    5
                )

            cost_price = product_lookup[
                product_id
            ]["cost_price"]

            # Selling price is greater than cost
            unit_price = round(
                cost_price * random.uniform(
                    1.10,
                    1.80
                ),
                2
            )

            discount_percent = round(
                random.uniform(
                    0,
                    40
                ),
                2
            )

            order_items.append({
                "item_id": f"ITEM{item_number:07d}",
                "order_id": order["order_id"],
                "product_id": product_id,
                "quantity": quantity,
                "unit_price": unit_price,
                "discount_percent": discount_percent
            })

            item_number += 1

    return pd.DataFrame(order_items)


# ============================================================
# 8. MAIN PIPELINE
# ============================================================

def main():

    print("=" * 70)
    print("E-COMMERCE ANALYTICS SYSTEM")
    print("STAGE 2 - RAW DATA GENERATION")
    print("=" * 70)


    # --------------------------------------------------------
    # Customers
    # --------------------------------------------------------

    print("\n[1/4] Generating customers...")

    customers = generate_customers()

    print(
        f"      Generated {len(customers):,} customers"
    )


    # --------------------------------------------------------
    # Products
    # --------------------------------------------------------

    print("\n[2/4] Generating products...")

    products = generate_products()

    print(
        f"      Generated {len(products):,} products"
    )


    # --------------------------------------------------------
    # Orders
    # --------------------------------------------------------

    print("\n[3/4] Generating orders...")

    orders = generate_orders(
        customers
    )

    print(
        f"      Generated {len(orders):,} orders"
    )


    # --------------------------------------------------------
    # Order Items
    # --------------------------------------------------------

    print("\n[4/4] Generating order items...")

    order_items = generate_order_items(
        orders,
        products
    )

    print(
        f"      Generated {len(order_items):,} order items"
    )


    # ========================================================
    # INTRODUCE DUPLICATES
    # ========================================================

    print("\nIntroducing intentional duplicate records...")

    customers = add_duplicate_rows(
        customers,
        percentage=0.01
    )

    products = add_duplicate_rows(
        products,
        percentage=0.01
    )

    orders = add_duplicate_rows(
        orders,
        percentage=0.01
    )


    # ========================================================
    # SAVE CSV FILES
    # ========================================================

    print("\nSaving CSV files...")

    customers.to_csv(
        RAW_DATA_DIR / "customers.csv",
        index=False
    )

    products.to_csv(
        RAW_DATA_DIR / "products.csv",
        index=False
    )

    orders.to_csv(
        RAW_DATA_DIR / "orders.csv",
        index=False
    )

    order_items.to_csv(
        RAW_DATA_DIR / "order_items.csv",
        index=False
    )


    # ========================================================
    # FINAL SUMMARY
    # ========================================================

    print("\n" + "=" * 70)
    print("DATA GENERATION COMPLETED SUCCESSFULLY")
    print("=" * 70)

    print("\nGenerated files:")

    print(
        f"  customers.csv     : {len(customers):,} rows"
    )

    print(
        f"  products.csv      : {len(products):,} rows"
    )

    print(
        f"  orders.csv        : {len(orders):,} rows"
    )

    print(
        f"  order_items.csv   : {len(order_items):,} rows"
    )

    print(
        f"\nFiles location:"
    )

    print(
        f"  {RAW_DATA_DIR}"
    )

    print("\nIntentional data-quality issues:")

    print("  ✓ Duplicate customer records")
    print("  ✓ Duplicate product records")
    print("  ✓ Duplicate order records")
    print("  ✓ Missing customer IDs")
    print("  ✓ Invalid email addresses")
    print("  ✓ Inconsistent product names")
    print("  ✓ Inconsistent date formats")
    print("  ✓ Negative quantities")

    print("\nNext stage:")
    print("  Run the Pandas data-cleaning pipeline.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()

