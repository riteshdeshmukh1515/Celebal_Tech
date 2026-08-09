from pathlib import Path


# ============================================================
# PROJECT ROOT
# ============================================================

BASE_DIR = Path(__file__).resolve().parent


# ============================================================
# DIRECTORIES
# ============================================================

directories = [
    "data/raw",
    "data/cleaned",
    "scripts",
    "sql",
    "tests",
    "output/sample_reports",
]


# ============================================================
# FILES
# ============================================================

files = [
    "scripts/generate_data.py",
    "scripts/clean_data.py",
    "scripts/load_database.py",
    "scripts/report_cli.py",

    "sql/schema.sql",
    "sql/aggregations.sql",
    "sql/window_functions.sql",
    "sql/cohort_analysis.sql",

    "tests/test_edge_cases.py",

    "README.md",
    ".gitignore",
    "requirements.txt",
]


# ============================================================
# CREATE DIRECTORIES
# ============================================================

print("=" * 60)
print("E-COMMERCE ANALYTICS SYSTEM SETUP")
print("=" * 60)

print("\nCreating directories...\n")

for directory in directories:

    path = BASE_DIR / directory

    path.mkdir(
        parents=True,
        exist_ok=True
    )

    print(f"[OK] {directory}")


# ============================================================
# CREATE FILES
# ============================================================

print("\nCreating files...\n")

for file in files:

    path = BASE_DIR / file

    if not path.exists():

        path.touch()

        print(f"[OK] {file}")

    else:

        print(f"[EXISTS] {file}")


# ============================================================
# CREATE .GITIGNORE CONTENT
# ============================================================

gitignore_path = BASE_DIR / ".gitignore"

gitignore_content = """# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Virtual environment
venv/

# SQLite database
*.db

# VS Code
.vscode/

# OS files
.DS_Store
Thumbs.db
"""

gitignore_path.write_text(
    gitignore_content,
    encoding="utf-8"
)


# ============================================================
# CREATE REQUIREMENTS.TXT
# ============================================================

requirements_path = BASE_DIR / "requirements.txt"

requirements_content = """pandas
faker
tabulate
"""

requirements_path.write_text(
    requirements_content,
    encoding="utf-8"
)


# ============================================================
# COMPLETION MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("PROJECT STRUCTURE CREATED SUCCESSFULLY")
print("=" * 60)

print("""
Next steps:

1. Create virtual environment
2. Activate virtual environment
3. Install requirements
4. Start data generation
""")