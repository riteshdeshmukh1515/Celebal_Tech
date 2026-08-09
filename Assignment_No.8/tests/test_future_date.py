
import sqlite3


def test_future_date():

    print("=" * 70)
    print("EDGE CASE TEST: FUTURE ORDER DATE")
    print("=" * 70)

    connection = sqlite3.connect(":memory:")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE orders (
            order_id TEXT PRIMARY KEY,
            customer_id TEXT,
            order_date TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO orders
        VALUES (
            'ORD99999',
            'CUST99999',
            '2030-01-01'
        )
    """)

    cursor.execute("""
        SELECT
            order_id,
            order_date
        FROM orders
        WHERE date(order_date) > date('now')
    """)

    result = cursor.fetchone()

    if result:

        print(
            f"Future order detected: "
            f"{result[0]} | {result[1]}"
        )

        print()
        print(
            "PASS: Future date successfully detected."
        )

    else:

        print(
            "FAIL: Future date was not detected."
        )

    connection.close()


if __name__ == "__main__":
    test_future_date()

