import mysql.connector
from mysql.connector import Error

# Database configuration
db_config = {
    'host': 'your_host',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}

# Create a connection to the database
try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        cursor = connection.cursor()

        # Get the list of all tables in the database
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]

        # Create a dump for each table
        for table in tables:
            dump_cmd = f"mysqldump -h {db_config['host']} -u {db_config['user']} -p{db_config['password']} {db_config['database']} {table} > {table}.sql"
            os.system(dump_cmd)

        print("Database dumped successfully!")

except Error as e:
    print("Error:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
