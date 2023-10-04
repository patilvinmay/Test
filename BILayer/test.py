import pandas as pd
from sqlalchemy import create_engine

# Sample DataFrame
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
}

df = pd.DataFrame(data)

# Replace placeholders with your PostgreSQL database credentials and connection details
DATABASE_URI = "postgresql://username:password@hostname:port/database_name"
engine = create_engine(DATABASE_URI)

# Define the table name
table_name = 'your_table_name'

# Write the DataFrame to the PostgreSQL table
df.to_sql(table_name, engine, if_exists='replace', index=False)
