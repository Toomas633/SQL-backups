import os
import mysql.connector

# Database connection details
host = 'your_remote_host'
user = 'your_username'
password = 'your_password'

# Path to save the dump file
dump_path = 'path_to_save_dump_file.sql'

# Connect to the database server
try:
    connection = mysqldumps.connector.connect(host=host, user=user, password=password)
    cursor = connection.cursor()

    # Get a list of all databases on the server
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()

    # Create a dump for each database
    for database in databases:
        database_name = database[0]
        dump_command = f"mysqldump -h {host} -u {user} -p{password} {database_name} > {dump_path}"
        os.system(dump_command)

    print("Dump created successfully!")

except mysqldumps.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
