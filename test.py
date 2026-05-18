import pandas as pd
from sqlglot import parse_one

# ==========================================
# INPUT / OUTPUT FILES
# ==========================================
input_csv = r"C:\Input\queries.csv"
output_csv = r"C:\Output\state_analysis_output.csv"

# ==========================================
# POSSIBLE STATE COLUMN NAMES
# ==========================================
state_columns = [
    "SECTN_CD",
    "LOC_ST",
    "STATE",
    "STATE_CD",
    "ST_CD",
    "REGION_STATE"
]

# ==========================================
# READ INPUT CSV
# ==========================================
# Expected columns:
# query_id, query_text, username
df = pd.read_csv(input_csv)

# ==========================================
# STORE RESULTS
# ==========================================
results = []

# ==========================================
# PROCESS EACH QUERY
# ==========================================
for index, row in df.iterrows():

    query_id = row["query_id"]
    query_text = str(row["query_text"])
    username = row["username"]

    state_found = "NO"
    state_column_name = ""

    try:

        # Parse SQL
        tree = parse_one(query_text, dialect="snowflake")

        # Get ONLY outermost select columns
        outer_columns = [
            projection.sql()
            for projection in tree.expressions
        ]

        # Search for state columns
        for col in outer_columns:

            for state_col in state_columns:

                if state_col.upper() in col.upper():

                    state_found = "YES"
                    state_column_name = state_col
                    break

            if state_found == "YES":
                break

    except Exception as e:
        state_found = "ERROR"
        state_column_name = str(e)

    # Save output row
    results.append({
        "query_id": query_id,
        "query_text": query_text,
        "username": username,
        "state_column_name": state_column_name,
        "state_found_yes_no": state_found
    })

# ==========================================
# CREATE OUTPUT CSV
# ==========================================
output_df = pd.DataFrame(results)

output_df.to_csv(output_csv, index=False)

print(f"\nOutput saved to:\n{output_csv}")
