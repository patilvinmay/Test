import pandas as pd
import re

# ==========================================
# INPUT / OUTPUT FILES
# ==========================================
input_csv = r"C:\Input\queries.csv"
output_csv = r"C:\Output\state_column_analysis.csv"

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

# Convert to uppercase
state_columns = [col.upper() for col in state_columns]

# ==========================================
# READ INPUT CSV
# ==========================================
df = pd.read_csv(input_csv)

results = []

# ==========================================
# FUNCTION TO EXTRACT OUTERMOST SELECT
# ==========================================
def extract_outer_select(sql):

    sql = str(sql)

    # Remove line breaks
    sql_clean = re.sub(r"\s+", " ", sql)

    # Track bracket depth
    depth = 0
    select_pos = -1
    from_pos = -1

    tokens = re.finditer(r"\(|\)|SELECT|FROM", sql_clean, re.IGNORECASE)

    for match in tokens:

        token = match.group().upper()

        if token == "(":
            depth += 1

        elif token == ")":
            depth -= 1

        elif token == "SELECT" and depth == 0 and select_pos == -1:
            select_pos = match.end()

        elif token == "FROM" and depth == 0 and select_pos != -1:
            from_pos = match.start()
            break

    if select_pos != -1 and from_pos != -1:
        return sql_clean[select_pos:from_pos]

    return ""

# ==========================================
# PROCESS QUERIES
# ==========================================
for index, row in df.iterrows():

    query_name = row["query_name"]
    sql_query = row["query"]

    try:

        outer_select = extract_outer_select(sql_query).upper()

        matched_columns = []

        for col in state_columns:

            # Exact word match
            pattern = rf"\b{re.escape(col)}\b"

            if re.search(pattern, outer_select, re.IGNORECASE):
                matched_columns.append(col)

        results.append({
            "query_name": query_name,
            "state_column_found": "YES" if matched_columns else "NO",
            "matched_columns": ", ".join(matched_columns),
            "outer_select_clause": outer_select
        })

    except Exception as e:

        results.append({
            "query_name": query_name,
            "state_column_found": "ERROR",
            "matched_columns": str(e),
            "outer_select_clause": ""
        })

# ==========================================
# SAVE OUTPUT
# ==========================================
output_df = pd.DataFrame(results)

output_df.to_csv(output_csv, index=False)

print(f"\nDone.")
print(f"Output File: {output_csv}")
