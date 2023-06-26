SQL_QUERY="SELECT * FROM <your_table> LIMIT 10;"

# Connect to Snowflake and execute the SQL query
snowsql -a "$SNOWSQL_ACCOUNT" -u "$SNOWSQL_USER" -p "$SNOWSQL_PASSWORD" -w "$SNOWSQL_WAREHOUSE" -d "$SNOWSQL_DATABASE" -s "$SNOWSQL_SCHEMA" -q "$SQL_QUERY"
