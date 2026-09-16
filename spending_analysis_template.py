"""
Monthly Spending Analyzer — PRACTICE TEMPLATE
------------------------------------------------
Use my_spending.csv (columns: date, category, amount) to answer:
  1. How much did I spend in a given month?
  2. What are my top spending categories?

Fill in each function below. No solutions included — this is for
you to work through yourself.
"""

from collections import defaultdict
from datetime import datetime

CSV_PATH = "my_spending.csv"


# ---------------------------------------------------------------
# 1. LOAD THE DATA
# ---------------------------------------------------------------
def load_from_csv(path):
    """
    Read the CSV at `path` and return a list of dicts like:
        {"date": "2026-09-01", "category": "Groceries", "amount": 450.00}

    Hints:
      - Use the csv module (csv.DictReader)
      - Remember to convert "amount" from string to float
    """
    # TODO: implement
    pass


# ---------------------------------------------------------------
# 2. TOTAL SPEND FOR A MONTH
# ---------------------------------------------------------------
def total_spend_for_month(data, year, month):
    """
    Return the total amount spent in the given year/month.

    Hints:
      - Parse each transaction's "date" string into a datetime
        (datetime.strptime)
      - Only add up amounts where the year and month match
    """
    # TODO: implement
    pass


# ---------------------------------------------------------------
# 3. SPEND BROKEN DOWN BY CATEGORY
# ---------------------------------------------------------------
def spend_by_category(data, year=None, month=None):
    """
    Return a dict of {category: total_amount}, optionally filtered
    to a specific year/month.

    Hints:
      - Use a defaultdict(float) to accumulate totals
      - Skip a transaction if year/month is given and doesn't match
    """
    # TODO: implement
    pass


# ---------------------------------------------------------------
# 4. TOP N CATEGORIES
# ---------------------------------------------------------------
def top_categories(data, year=None, month=None, n=5):
    """
    Return the top n categories as a list of (category, amount) tuples,
    sorted highest spend first.

    Hints:
      - Reuse spend_by_category() to get the totals
      - sorted(..., key=..., reverse=True) is your friend
    """
    # TODO: implement
    pass


# ---------------------------------------------------------------
# 5. RUN IT
# ---------------------------------------------------------------
if __name__ == "__main__":
    YEAR, MONTH = 2026, 9  # <-- change to the month you want to check

    transactions = load_from_csv(CSV_PATH)

    total = total_spend_for_month(transactions, YEAR, MONTH)
    print(f"Total spend for {YEAR}-{MONTH:02d}: R{total:,.2f}")

    print("\nSpend by category:")
    for cat, amt in spend_by_category(transactions, YEAR, MONTH).items():
        print(f"  {cat:<15} R{amt:,.2f}")

    print("\nTop 3 categories:")
    for cat, amt in top_categories(transactions, YEAR, MONTH, n=3):
        print(f"  {cat:<15} R{amt:,.2f}")
