import psycopg2

# Define connection parameters for the source PostgreSQL database
source_db_params = {
    "database": "source_database",
    "user": "source_user",
    "password": "source_password",
    "host": "source_host",
    "port": "source_port"
}

# Define connection parameters for the destination PostgreSQL database
destination_db_params = {
    "database": "destination_database",
    "user": "destination_user",
    "password": "destination_password",
    "host": "destination_host",
    "port": "destination_port"
}

# Establish a connection to the source PostgreSQL database
source_connection = psycopg2.connect(**source_db_params)

# Create a cursor for the source database
source_cursor = source_connection.cursor()

# Establish a connection to the destination PostgreSQL database
destination_connection = psycopg2.connect(**destination_db_params)

# Create a cursor for the destination database
destination_cursor = destination_connection.cursor()

# Define the table name from which you want to copy data
source_table_name = 'source_table'

# Define the destination table name where you want to insert data
destination_table_name = 'destination_table'

# Define the SQL query to select data from the source table
select_query = f"SELECT * FROM {source_table_name}"

# Execute the SELECT query on the source database
source_cursor.execute(select_query)

# Fetch all rows from the source table
rows_to_copy = source_cursor.fetchall()

# Define the SQL query to insert data into the destination table
insert_query = f"INSERT INTO {destination_table_name} VALUES %s"

# Use the copy_expert method to insert data into the destination table
destination_cursor.copy_expert(sql=insert_query, file=rows_to_copy)

# Commit the changes in the destination database
destination_connection.commit()

# Close the cursors and database connections
source_cursor.close()
source_connection.close()
destination_cursor.close()
destination_connection.close()

# Data has been copied from the source table to the destination table
