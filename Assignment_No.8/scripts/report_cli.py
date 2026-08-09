
import argparse
import sqlite3
import sys
from pathlib import Path

from tabulate import tabulate


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "ecommerce.db"


# ============================================================
# REPORT QUERIES
# ============================================================

REPORT_QUERIES = {

    # --------------------------------------------------------
    # REVENUE REPORT
    # --------------------------------------------------------

    "revenue": """
        SELECT
            strftime('%Y-%m', o.order_date) AS month,
            ROUND(
                SUM(oi.quantity * oi.unit_price),
                2
            ) AS revenue
        FROM orders o
        JOIN order_items oi
            ON o.order_id = oi.order_id
        GROUP BY month
        ORDER BY month;
    """,

    # --------------------------------------------------------
    # TOP CUSTOMERS
    # --------------------------------------------------------

    "top_customers": """
        SELECT
            c.customer_id,
            c.customer_name,
            COUNT(DISTINCT o.order_id) AS total_orders,
            ROUND(
                SUM(
                    oi.quantity * oi.unit_price
                ),
                2
            ) AS total_spend
        FROM customers c
        JOIN orders o
            ON c.customer_id = o.customer_id
        JOIN order_items oi
            ON o.order_id = oi.order_id
        GROUP BY
            c.customer_id,
            c.customer_name
        ORDER BY total_spend DESC
        LIMIT 10;
    """,

    # --------------------------------------------------------
    # TOP PRODUCTS
    # --------------------------------------------------------

    "top_products": """
        SELECT
            p.product_id,
            p.product_name,
            p.category,
            SUM(oi.quantity) AS units_sold,
            ROUND(
                SUM(
                    oi.quantity * oi.unit_price
                ),
                2
            ) AS revenue
        FROM products p
        JOIN order_items oi
            ON p.product_id = oi.product_id
        GROUP BY
            p.product_id,
            p.product_name,
            p.category
        ORDER BY revenue DESC
        LIMIT 10;
    """,

    # --------------------------------------------------------
    # AVERAGE ORDER VALUE
    # --------------------------------------------------------

    "aov": """
        WITH order_totals AS (
            SELECT
                o.order_id,
                o.customer_id,
                SUM(
                    oi.quantity * oi.unit_price
                ) AS order_value
            FROM orders o
            JOIN order_items oi
                ON o.order_id = oi.order_id
            GROUP BY
                o.order_id,
                o.customer_id
        )

        SELECT
            ROUND(
                AVG(order_value),
                2
            ) AS average_order_value
        FROM order_totals;
    """,

    # --------------------------------------------------------
    # CUSTOMER SEGMENTS
    # --------------------------------------------------------

    "segments": """
        WITH customer_metrics AS (

            SELECT
                o.customer_id,

                COUNT(
                    DISTINCT o.order_id
                ) AS total_orders,

                SUM(
                    oi.quantity * oi.unit_price
                ) AS total_spend

            FROM orders o

            JOIN order_items oi
                ON o.order_id = oi.order_id

            GROUP BY o.customer_id
        )

        SELECT

            CASE
                WHEN total_orders = 1
                    THEN 'One-Time'

                WHEN total_orders BETWEEN 2 AND 5
                    THEN 'Occasional'

                ELSE 'Loyal'
            END AS frequency_segment,

            COUNT(*) AS customer_count,

            ROUND(
                AVG(total_spend),
                2
            ) AS average_spend

        FROM customer_metrics

        GROUP BY frequency_segment

        ORDER BY customer_count DESC;
    """,

    # --------------------------------------------------------
    # RFM REPORT
    # --------------------------------------------------------

    "rfm": """
        WITH dataset_date AS (

            SELECT
                MAX(
                    date(order_date)
                ) AS latest_date
            FROM orders
        ),

        customer_metrics AS (

            SELECT

                o.customer_id,

                MAX(
                    date(o.order_date)
                ) AS last_purchase_date,

                COUNT(
                    DISTINCT o.order_id
                ) AS frequency,

                SUM(
                    oi.quantity * oi.unit_price
                ) AS monetary

            FROM orders o

            JOIN order_items oi
                ON o.order_id = oi.order_id

            GROUP BY o.customer_id
        ),

        rfm_metrics AS (

            SELECT

                cm.customer_id,

                CAST(
                    julianday(dd.latest_date)
                    -
                    julianday(
                        cm.last_purchase_date
                    )
                    AS INTEGER
                ) AS recency,

                cm.frequency,

                cm.monetary

            FROM customer_metrics cm

            CROSS JOIN dataset_date dd
        ),

        rfm_scores AS (

            SELECT

                customer_id,

                recency,

                frequency,

                monetary,

                NTILE(5) OVER (
                    ORDER BY recency DESC
                ) AS r_score,

                NTILE(5) OVER (
                    ORDER BY frequency
                ) AS f_score,

                NTILE(5) OVER (
                    ORDER BY monetary
                ) AS m_score

            FROM rfm_metrics
        )

        SELECT

            customer_id,

            recency,

            frequency,

            ROUND(
                monetary,
                2
            ) AS monetary,

            r_score,

            f_score,

            m_score,

            (
                r_score
                +
                f_score
                +
                m_score
            ) AS rfm_score

        FROM rfm_scores

        ORDER BY rfm_score DESC

        LIMIT 20;
    """,

    # --------------------------------------------------------
    # RETENTION / COHORT REPORT
    # --------------------------------------------------------

    "retention": """
        WITH first_purchase AS (

            SELECT
                customer_id,
                MIN(
                    date(order_date)
                ) AS first_purchase_date

            FROM orders

            GROUP BY customer_id
        ),

        cohorts AS (

            SELECT

                customer_id,

                strftime(
                    '%Y-%m',
                    first_purchase_date
                ) AS cohort_month

            FROM first_purchase
        ),

        monthly_activity AS (

            SELECT DISTINCT

                o.customer_id,

                strftime(
                    '%Y-%m',
                    o.order_date
                ) AS activity_month

            FROM orders o
        )

        SELECT

            c.cohort_month,

            ma.activity_month,

            COUNT(
                DISTINCT ma.customer_id
            ) AS active_customers

        FROM cohorts c

        JOIN monthly_activity ma

            ON c.customer_id =
               ma.customer_id

        GROUP BY

            c.cohort_month,
            ma.activity_month

        ORDER BY

            c.cohort_month,
            ma.activity_month;
    """,

    # --------------------------------------------------------
    # CATEGORY REVENUE
    # --------------------------------------------------------

    "category": """
        SELECT

            p.category,

            SUM(
                oi.quantity
            ) AS units_sold,

            ROUND(
                SUM(
                    oi.quantity * oi.unit_price
                ),
                2
            ) AS revenue

        FROM products p

        JOIN order_items oi

            ON p.product_id = oi.product_id

        GROUP BY p.category

        ORDER BY revenue DESC;
    """
}


# ============================================================
# DATABASE CONNECTION
# ============================================================

def connect_database():
    """
    Connect to the SQLite database.
    """

    try:

        connection = sqlite3.connect(
            DATABASE_PATH
        )

        return connection

    except sqlite3.Error as error:

        print()
        print("ERROR: Could not connect to database.")
        print(f"Details: {error}")
        print()

        sys.exit(1)


# ============================================================
# EXECUTE REPORT
# ============================================================

def run_report(report_name):
    """
    Execute the selected report and print results.
    """

    if report_name not in REPORT_QUERIES:

        print()
        print(
            f"ERROR: Unknown report '{report_name}'."
        )

        print()
        print("Available reports:")

        for report in REPORT_QUERIES:
            print(f"  - {report}")

        print()

        sys.exit(1)

    connection = connect_database()

    try:

        cursor = connection.cursor()

        query = REPORT_QUERIES[
            report_name
        ]

        cursor.execute(query)

        rows = cursor.fetchall()

        column_names = [
            description[0]
            for description in cursor.description
        ]

        print()
        print("=" * 80)
        print(
            f"REPORT: {report_name.upper()}"
        )
        print("=" * 80)

        if not rows:

            print()
            print(
                "No data found for this report."
            )
            print()

            return

        print()

        print(
            tabulate(
                rows,
                headers=column_names,
                tablefmt="grid"
            )
        )

        print()

        print(
            f"Rows returned: {len(rows)}"
        )

        print()

    except sqlite3.Error as error:

        print()
        print(
            "ERROR: Failed to execute report."
        )
        print(
            f"Details: {error}"
        )
        print()

        sys.exit(1)

    finally:

        connection.close()


# ============================================================
# COMMAND-LINE ARGUMENTS
# ============================================================

def main():

    parser = argparse.ArgumentParser(

        description=(
            "E-Commerce Analytics "
            "CLI Reporting Tool"
        )
    )

    parser.add_argument(

        "--report",

        required=True,

        choices=REPORT_QUERIES.keys(),

        help=(
            "Report to execute"
        )
    )

    args = parser.parse_args()

    run_report(
        args.report
    )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()

