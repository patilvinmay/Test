import pandas as pd
from sqlglot import parse_one, exp

# ==========================================
# INPUT CSV
# ==========================================
# Example CSV format:
#
# query_name,query
# q1,"SELECT customer_id, SECTN_CD FROM table1"
# q2,"SELECT * FROM table2"
#
input_csv = r"C:\Input\queries.csv"

# ==========================================
# OUTPUT CSV
# ==========================================
output_csv = r"C:\Output\state_column_analysis.csv"

# ==========================================
# POSSIBLE STATE COLUMN NAMES
# ==========================================
state_columns = {
    "SECTN_CD",
    "LOC_ST",
    "STATE",
    "STATE_CD",
    "ST_CD",
    "REGION_STATE"
}

# Convert to uppercase for matching
state_columns = {col.upper() for col in state_columns}

# ==========================================
# READ INPUT
# ==========================================
df = pd.read_csv(input_csv)

# ==========================================
# OUTPUT RESULTS
# ==========================================
results = []

# ==========================================
# PROCESS EACH QUERY
# ==========================================
for index, row in df.iterrows():

    query_name = str(row["query_name"])
    sql_query = str(row["query"])

    found_state_column = "NO"
    matched_columns = []

    try:
        # Parse SQL
        tree = parse_one(sql_query, dialect="snowflake")

        # ONLY OUTERMOST SELECT
        outer_select_columns = []

        for projection in tree.expressions:

            # Direct column
            if isinstance(projection, exp.Column):
                col_name = projection.name.upper()
                outer_select_columns.append(col_name)

            # Alias handling
            elif isinstance(projection, exp.Alias):

                # Example:
                # SELECT LOC_ST AS STATE_CODE

                inner_expression = projection.this

                if isinstance(inner_expression, exp.Column):
                    col_name = inner_expression.name.upper()
                    outer_select_columns.append(col_name)

        # Check against probable state columns
        for col in outer_select_columns:
            if col in state_columns:
                found_state_column = "YES"
                matched_columns.append(col)

    except Exception as e:
        found_state_column = f"ERROR: {str(e)}"

    # Store result
    results.append({
        "query_name": query_name,
        "state_column_found": found_state_column,
        "matched_state_columns": ", ".join(matched_columns)
    })

# ==========================================
# SAVE OUTPUT
# ==========================================
output_df = pd.DataFrame(results)

output_df.to_csv(output_csv, index=False)

print(f"\nAnalysis Complete.")
print(f"Output saved to:\n{output_csv}")
