import subprocess

# Database connection information
db_host = "your_database_host"
db_port = "your_database_port"
db_user = "your_database_user"
db_password = "your_database_password"

# Path to store the dump file
dump_file_path = "path_to_store_dump_file.sql"

# Construct the pg_dumpall command
pg_dumpall_command = [
    "pg_dumpall",
    f"--host={db_host}",
    f"--port={db_port}",
    f"--username={db_user}",
    f"--file={dump_file_path}",
]

# If your database requires a password, add it to the command
if db_password:
    pg_dumpall_command.append(f"--password={db_password}")

# Execute the pg_dumpall command
subprocess.run(pg_dumpall_command)

print("All databases dump created successfully.")
