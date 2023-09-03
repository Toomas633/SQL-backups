import mysql.connector
from mysql.connector import Error
import os
import datetime

def mysql_dump(name, address, username, password):
    db_config = {
        'host': 'sql.toomas633.com',
        'user': username,
        'password': password,
        'database': 'mysql'
    }
    connection = None
    current_date = datetime.date.today()
    formatted_date = current_date.strftime('%d-%m-%Y')
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]
            for table in tables:
                os.makedirs(f"dumps/{name}/{formatted_date}/", exist_ok=True)
                dump_file = os.path.join(
                    f"dumps/{name}/{formatted_date}/", f"{table}.sql")
                dump_cmd = f"mysqldump -h {db_config['host']} -u {db_config['user']} -p{db_config['password']} {db_config['database']}{table} > {dump_file}"
                os.system(dump_cmd)
            return True
    except Error as e:
        return str(e)
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()