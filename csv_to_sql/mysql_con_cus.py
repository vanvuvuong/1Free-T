import mysql.connector
import os
from alive_progress import alive_bar
from mysql.connector import Error
from urllib.parse import urlparse

import create_query

try:
    connection = mysql.connector.connect(
        user='root',
        password='1111',
        host='127.0.0.1',
        database='csv_to_sql',
        auth_plugin='mysql_native_password'
    )
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        data_dump = create_query.create_tbl('export_rubinia', 'export.rubinia.com.csv', ',')
        result = cursor.execute(data_dump['query'])

        print("Table created")
        with alive_bar(len(data_dump['data'])) as bar:
            for row in data_dump['data']:

                insert_query = create_query.create_insert_query('export_rubinia', row)
                if insert_query == '':
                    continue
                cursor.execute(insert_query)
                connection.commit()
                bar()

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
