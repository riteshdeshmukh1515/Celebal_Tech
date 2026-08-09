
"""
E-Commerce Analytics System
 Load Cleaned Data into SQLite

This script:

1. Creates SQLite database
2. Executes schema.sql
3. Loads cleaned CSV files
4. Enables foreign-key constraints
5. Verifies row counts
6. Verifies table relationships
"""

from pathlib import Path
import sqlite3

import pandas as pd


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

CLEANED_DIR = BASE_DIR / "data" / "cleaned"

SQL_DIR = BASE_DIR / "sql"

DATABASE_PATH = BASE_DIR / "ecommerce.db"

SCHEMA_PATH = SQL_DIR / "schema.sql"


# ============================================================
# 2. DATABASE CONNECTION
# ============================================================

def create_connection():

    print("\nConnecting to SQLite database...")

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    # Enable foreign-key enforcement
    connection.execute(
        "PRAGMA foreign_keys = ON;"
    )

    print("✓ Database connection successful")

    return connection


# ============================================================
# 3. CREATE DATABASE SCHEMA
# ============================================================

def create_schema(connection):

    print("\nCreating database schema...")

    with open(
        SCHEMA_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        schema_sql = file.read()


    connection.executescript(
        schema_sql
    )

    connection.commit()

    print("✓ Database schema created")


# ============================================================
# 4. LOAD CSV FILE
# ============================================================

def load_csv_to_table(
    connection,
    filename,
    table_name
):

    file_path = CLEANED_DIR / filename

    print(
        f"\nLoading {filename}..."
    )

    df = pd.read_csv(
        file_path
    )


    # --------------------------------------------------------
    # Convert dates for SQLite
    # --------------------------------------------------------

    if table_name == "customers":

        if "registration_date" in df.columns:

            df["registration_date"] = (
                pd.to_datetime(
                    df["registration_date"],
                    errors="coerce"
                )
                .dt.strftime("%Y-%m-%d")
            )


    if table_name == "orders":

        if "order_date" in df.columns:

            df["order_date"] = (
                pd.to_datetime(
                    df["order_date"],
                    errors="coerce"
                )
                .dt.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )


    # --------------------------------------------------------
    # Load DataFrame into SQLite
    # --------------------------------------------------------

    df.to_sql(
        table_name,
        connection,
        if_exists="append",
        index=False
    )


    print(
        f"✓ Loaded {len(df):,} rows into {table_name}"
    )


# ============================================================
# 5. GET ROW COUNTS
# ============================================================

def get_row_counts(connection):

    print("\n" + "=" * 60)
    print("DATABASE ROW COUNTS")
    print("=" * 60)


    tables = [
        "customers",
        "products",
        "orders",
        "order_items"
    ]


    counts = {}


    for table in tables:

        cursor = connection.execute(
            f"SELECT COUNT(*) FROM {table}"
        )

        count = cursor.fetchone()[0]

        counts[table] = count

        print(
            f"{table:<15}: {count:,}"
        )


    return counts


# ============================================================
# 6. CHECK FOREIGN KEYS
# ============================================================

def check_foreign_keys(connection):

    print("\n" + "=" * 60)
    print("FOREIGN KEY VALIDATION")
    print("=" * 60)


    cursor = connection.execute(
        "PRAGMA foreign_key_check;"
    )


    violations = cursor.fetchall()


    if not violations:

        print(
            "✓ No foreign-key violations found"
        )

        return True


    print(
        f"✗ Found {len(violations)} foreign-key violations"
    )


    for violation in violations:

        print(violation)


    return False


# ============================================================
# 7. VERIFY RELATIONSHIPS
# ============================================================

def verify_relationships(connection):

    print("\n" + "=" * 60)
    print("RELATIONSHIP VALIDATION")
    print("=" * 60)


    # --------------------------------------------------------
    # Orders without customers
    # --------------------------------------------------------

    query = """
        SELECT COUNT(*)
        FROM orders o
        LEFT JOIN customers c
            ON o.customer_id = c.customer_id
        WHERE c.customer_id IS NULL;
    """


    result = connection.execute(
        query
    ).fetchone()[0]


    print(
        f"Orders without customers: {result}"
    )


    # --------------------------------------------------------
    # Order items without orders
    # --------------------------------------------------------

    query = """
        SELECT COUNT(*)
        FROM order_items oi
        LEFT JOIN orders o
            ON oi.order_id = o.order_id
        WHERE o.order_id IS NULL;
    """


    result = connection.execute(
        query
    ).fetchone()[0]


    print(
        f"Order items without orders: {result}"
    )


    # --------------------------------------------------------
    # Order items without products
    # --------------------------------------------------------

    query = """
        SELECT COUNT(*)
        FROM order_items oi
        LEFT JOIN products p
            ON oi.product_id = p.product_id
        WHERE p.product_id IS NULL;
    """


    result = connection.execute(
        query
    ).fetchone()[0]


    print(
        f"Order items without products: {result}"
    )


    print(
        "\n✓ Relationship validation completed"
    )


# ============================================================
# 8. DATABASE SUMMARY
# ============================================================

def database_summary(connection):

    print("\n" + "=" * 60)
    print("DATABASE TABLES")
    print("=" * 60)


    query = """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        ORDER BY name;
    """


    tables = connection.execute(
        query
    ).fetchall()


    for table in tables:

        print(
            f"✓ {table[0]}"
        )


# ============================================================
# 9. MAIN
# ============================================================

def main():

    print("=" * 70)
    print("E-COMMERCE ANALYTICS SYSTEM")
    print(" LOAD DATA INTO SQLITE")
    print("=" * 70)


    connection = None


    try:

        # ----------------------------------------------------
        # Connect
        # ----------------------------------------------------

        connection = create_connection()


        # ----------------------------------------------------
        # Create schema
        # ----------------------------------------------------

        create_schema(
            connection
        )


        # ----------------------------------------------------
        # Load tables
        # ----------------------------------------------------

        load_csv_to_table(
            connection,
            "customers_clean.csv",
            "customers"
        )


        load_csv_to_table(
            connection,
            "products_clean.csv",
            "products"
        )


        load_csv_to_table(
            connection,
            "orders_clean.csv",
            "orders"
        )


        load_csv_to_table(
            connection,
            "order_items_clean.csv",
            "order_items"
        )


        connection.commit()


        # ----------------------------------------------------
        # Verify
        # ----------------------------------------------------

        get_row_counts(
            connection
        )


        check_foreign_keys(
            connection
        )


        verify_relationships(
            connection
        )


        database_summary(
            connection
        )


        print("\n" + "=" * 70)
        print("STAGE 4 COMPLETED SUCCESSFULLY")
        print("=" * 70)


        print(
            f"\nDatabase created at:"
        )

        print(
            f"  {DATABASE_PATH}"
        )


        print(
            "\nNext stage:"
        )

        print(
            "  SQL analytics using JOINs and aggregations."
        )


    except Exception as error:

        print("\n" + "=" * 70)
        print("DATABASE LOAD FAILED")
        print("=" * 70)

        print(
            f"\nError: {error}"
        )


    finally:

        if connection:

            connection.close()

            print(
                "\nDatabase connection closed."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()

