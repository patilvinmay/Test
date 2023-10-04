import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',  # Change to your database host
    'port': '5432',       # Change to your database port
}

# SQL query to select data from the PostgreSQL table
sql_query = "SELECT * FROM your_table_name"

# File path to save the text file
file_path = 'data.txt'

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object
    cur = conn.cursor()

    # Execute the SQL query
    cur.execute(sql_query)

    # Fetch all the results
    results = cur.fetchall()

    # Open a text file for writing
    with open(file_path, 'w') as file:
        # Write the column headers as the first line (optional)
        column_names = [desc[0] for desc in cur.description]
        file.write(','.join(column_names) + '\n')

        # Write the data to the file
        for row in results:
            file.write(','.join(map(str, row)) + '\n')

    print("Data exported to", file_path)

except psycopg2.Error as e:
    print("Error:", e)

finally:
    # Close the database connection
    if conn:
        conn.close()
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')
