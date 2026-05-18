import pandas as pd
from sqlglot import parse_one

# ==========================================
# INPUT CSV
# ==========================================
# Example CSV:
#
# query_name,query
# q1,"SELECT a.LOC_ST FROM sales a"
#
input_csv = r"C:\Input\queries.csv"

# ==========================================
# READ CSV
# ==========================================
df = pd.read_csv(input_csv)

# ==========================================
# STATE COLUMNS
# ==========================================
state_cols = ["LOC_ST", "SECTN_CD", "STATE_CD"]

# ==========================================
# PROCESS EACH QUERY
# ==========================================
for index, row in df.iterrows():

    query_name = row["query_name"]
    sql = row["query"]

    print(f"\nProcessing: {query_name}")

    try:

        # Parse SQL
        tree = parse_one(sql, dialect="snowflake")

        # Get ONLY outermost SELECT columns
        columns = [projection.sql() for projection in tree.expressions]

        print("Outer Select Columns:")
        print(columns)

        # Check for state columns
        found = []

        for col in columns:
            for state_col in state_cols:

                if state_col.upper() in col.upper():
                    found.append(state_col)

        if found:
            print("State Columns Found:", found)
        else:
            print("No State Column Found")

    except Exception as e:
        print("Error:", e)
