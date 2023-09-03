import sqlite3
import os
import shutil
import zipfile

import mysqldump


def check_connection(name, type, address, username, password):
    if (type == 'mysql'):
        status = mysqldump.mysql_dump(name, address, username, password)
        if (status == True):
            return save_connection(name, type, address, username, password)
        else:
            return status
    elif (type == 'postgres'):
        return save_connection(name, type, address, username, password)
    elif (type == 'mariadb'):
        return save_connection(name, type, address, username, password)
    else:
        return "Unknown type"


def save_connection(name, type, address, username, password):
    try:
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        data_to_insert = (type, address, username, password, name)
        cursor.execute(
            "INSERT INTO databases (type, address, username, password, name) VALUES (?, ?, ?, ?, ?)", data_to_insert)
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        return e


def zip_folder(folder, date):
    zip_filename = os.path.join(folder, f"{date}.zip")
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as archive:
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                archive.write(file_path, os.path.relpath(file_path, folder))

    shutil.rmtree(folder)
