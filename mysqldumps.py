import mysql.connector
from mysql.connector import Error
import os
import datetime

def mysql_dump(name, address, username, password):
    db_config = {
        'host': address,
        'user': username,
        'password': password,
        'database': 'mysql'
    }
    
    current_date = datetime.date.today()
    formatted_date = current_date.strftime('%d-%m-%Y')
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]
            for table in tables:
                os.makedirs('dumps/' + name + '/', exist_ok=True)
                dump_file = os.path.join('dumps/' + name + '/', formatted_date + ".sql")
                dump_cmd = f"mysqldump -h {db_config['host']} -u {db_config['user']} -p{db_config['password']} {db_config['database']} {' '.join(tables)} > {dump_file}"
                os.system(dump_cmd)
            return True
    except Error as e:
        return e
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
mysql_dump('testmysql', 'sql.toomas633.com', 'toomas', 'Toomas2001')