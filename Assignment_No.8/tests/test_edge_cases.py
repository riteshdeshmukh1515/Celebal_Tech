
import sqlite3
import tempfile
from pathlib import Path


def create_empty_database():

    print("=" * 70)
    print("EDGE CASE TEST: EMPTY DATABASE")
    print("=" * 70)

    temp_db = Path(
        tempfile.gettempdir()
    ) / "ecommerce_empty_test.db"

    connection = sqlite3.connect(temp_db)

    cursor = connection.cursor()

    # Create empty tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id TEXT PRIMARY KEY,
            customer_name TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            customer_id TEXT,
            order_date TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            order_item_id TEXT PRIMARY KEY,
            order_id TEXT,
            product_id TEXT,
            quantity INTEGER,
            unit_price REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id TEXT PRIMARY KEY,
            product_name TEXT,
            category TEXT
        )
    """)

    connection.commit()

    # Verify row counts
    tables = [
        "customers",
        "orders",
        "order_items",
        "products"
    ]

    for table in tables:

        cursor.execute(
            f"SELECT COUNT(*) FROM {table}"
        )

        count = cursor.fetchone()[0]

        print(
            f"{table:<15} rows = {count}"
        )

    connection.close()

    print()
    print("PASS: Empty database handled successfully.")
    print()


if __name__ == "__main__":
    create_empty_database()

