import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',  # Change to your database host
    'port': '5432',       # Change to your database port
}

# Path to your text file
file_path = 'data.txt'

# Name of the table to insert data into
table_name = 'my_table'

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object
    cur = conn.cursor()

    # Prepare a SQL statement for copying data from the file to the table
    copy_sql = sql.SQL("COPY {} FROM stdin WITH CSV HEADER").format(
        sql.Identifier(table_name)
    )

    # Open the file and execute the COPY command
    with open(file_path, 'r') as file:
        cur.copy_expert(sql=copy_sql, file=file)

    # Commit the transaction
    conn.commit()

    print("Data inserted successfully!")

except psycopg2.Error as e:
    print("Error:", e)

finally:
    # Close the database connection
    if conn:
        conn.close()
