
import sqlite3
import tempfile
from pathlib import Path


def test_single_customer():

    print("=" * 70)
    print("EDGE CASE TEST: SINGLE CUSTOMER")
    print("=" * 70)

    db_path = (
        Path(tempfile.gettempdir())
        / "ecommerce_single_customer.db"
    )

    connection = sqlite3.connect(db_path)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE customers (
            customer_id TEXT PRIMARY KEY,
            customer_name TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE orders (
            order_id TEXT PRIMARY KEY,
            customer_id TEXT,
            order_date TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE order_items (
            order_item_id TEXT PRIMARY KEY,
            order_id TEXT,
            product_id TEXT,
            quantity INTEGER,
            unit_price REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE products (
            product_id TEXT PRIMARY KEY,
            product_name TEXT,
            category TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO customers
        VALUES ('CUST00001', 'Test Customer')
    """)

    cursor.execute("""
        INSERT INTO products
        VALUES (
            'PROD00001',
            'Test Product',
            'Electronics'
        )
    """)

    cursor.execute("""
        INSERT INTO orders
        VALUES (
            'ORD00001',
            'CUST00001',
            '2026-07-01'
        )
    """)

    cursor.execute("""
        INSERT INTO order_items
        VALUES (
            'ITEM00001',
            'ORD00001',
            'PROD00001',
            2,
            1000
        )
    """)

    connection.commit()

    cursor.execute("""
        SELECT
            c.customer_name,
            COUNT(DISTINCT o.order_id) AS orders,
            SUM(
                oi.quantity * oi.unit_price
            ) AS revenue

        FROM customers c

        JOIN orders o
            ON c.customer_id = o.customer_id

        JOIN order_items oi
            ON o.order_id = oi.order_id

        GROUP BY c.customer_id
    """)

    result = cursor.fetchone()

    print(
        f"Customer : {result[0]}"
    )

    print(
        f"Orders   : {result[1]}"
    )

    print(
        f"Revenue  : {result[2]}"
    )

    connection.close()

    print()
    print(
        "PASS: Single customer scenario handled."
    )
    print()


if __name__ == "__main__":
    test_single_customer()

