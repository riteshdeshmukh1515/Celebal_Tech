
"""
E-Commerce Analytics System
Stage 5: SQL Analytics Runner

Usage:
    python scripts/run_sql.py sql/aggregations.sql
"""

from pathlib import Path
import sqlite3
import sys


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "ecommerce.db"


# ============================================================
# RUN SQL FILE
# ============================================================

def run_sql_file(sql_file):

    sql_path = BASE_DIR / sql_file

    # --------------------------------------------------------
    # Check SQL file
    # --------------------------------------------------------

    if not sql_path.exists():

        print(f"ERROR: SQL file not found:")
        print(sql_path)

        return


    print("=" * 70)
    print(f"Running SQL file: {sql_path.name}")
    print("=" * 70)


    # --------------------------------------------------------
    # Read SQL file
    # --------------------------------------------------------

    with open(
        sql_path,
        "r",
        encoding="utf-8"
    ) as file:

        sql_content = file.read()


    # --------------------------------------------------------
    # Remove SQL comments
    # --------------------------------------------------------

    cleaned_lines = []

    for line in sql_content.splitlines():

        stripped_line = line.strip()

        # Ignore comment lines
        if stripped_line.startswith("--"):
            continue

        cleaned_lines.append(line)


    cleaned_sql = "\n".join(cleaned_lines)


    # --------------------------------------------------------
    # Split SQL statements
    # --------------------------------------------------------

    queries = [

        query.strip()

        for query in cleaned_sql.split(";")

        if query.strip()
    ]


    print(
        f"\nQueries detected: {len(queries)}"
    )


    if len(queries) == 0:

        print("\nERROR: No SQL queries were found.")

        print(
            "\nPlease check that sql/aggregations.sql "
            "contains SQL statements."
        )

        return


    # --------------------------------------------------------
    # Connect to SQLite
    # --------------------------------------------------------

    if not DATABASE_PATH.exists():

        print(
            f"\nERROR: Database not found:"
        )

        print(
            DATABASE_PATH
        )

        print(
            "\nRun this first:"
        )

        print(
            "python scripts/load_database.py"
        )

        return


    connection = sqlite3.connect(
        DATABASE_PATH
    )


    # Enable foreign keys

    connection.execute(
        "PRAGMA foreign_keys = ON;"
    )


    # --------------------------------------------------------
    # Execute queries
    # --------------------------------------------------------

    successful_queries = 0

    failed_queries = 0


    for number, query in enumerate(
        queries,
        start=1
    ):

        try:

            cursor = connection.execute(
                query
            )


            # ------------------------------------------------
            # Check whether query returns rows
            # ------------------------------------------------

            if cursor.description:

                columns = [
                    description[0]
                    for description in cursor.description
                ]

                rows = cursor.fetchall()


                print(
                    "\n" + "-" * 80
                )

                print(
                    f"QUERY {number}"
                )

                print(
                    "-" * 80
                )


                print(
                    " | ".join(columns)
                )

                print(
                    "-" * 80
                )


                # Display first 20 rows

                for row in rows[:20]:

                    print(
                        " | ".join(
                            str(value)
                            for value in row
                        )
                    )


                if len(rows) > 20:

                    print(
                        f"\n... {len(rows) - 20} more rows"
                    )


                if len(rows) == 0:

                    print(
                        "(No results)"
                    )


            else:

                print(
                    f"\nQUERY {number}: "
                    "Executed successfully."
                )


            successful_queries += 1


        except sqlite3.Error as error:

            failed_queries += 1

            print(
                "\n" + "-" * 80
            )

            print(
                f"QUERY {number} FAILED"
            )

            print(
                "-" * 80
            )

            print(
                error
            )


    # --------------------------------------------------------
    # Close connection
    # --------------------------------------------------------

    connection.close()


    # --------------------------------------------------------
    # Final summary
    # --------------------------------------------------------

    print(
        "\n" + "=" * 70
    )

    print(
        "SQL EXECUTION SUMMARY"
    )

    print(
        "=" * 70
    )

    print(
        f"Total queries   : {len(queries)}"
    )

    print(
        f"Successful      : {successful_queries}"
    )

    print(
        f"Failed          : {failed_queries}"
    )

    print(
        "=" * 70
    )


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # Validate command-line argument
    # --------------------------------------------------------

    if len(sys.argv) != 2:

        print(
            "\nUsage:"
        )

        print(
            "python scripts/run_sql.py sql/aggregations.sql"
        )

        sys.exit(1)


    # --------------------------------------------------------
    # Run SQL
    # --------------------------------------------------------

    run_sql_file(
        sys.argv[1]
    )

