import argparse
import sys
import re

import mysql.connector
from alive_progress import alive_bar
from mysql.connector import Error

from libs import create_query
from libs.get_config import *

parser = argparse.ArgumentParser(prog='mysql_con_cus')
parser.add_argument('--file', help='Name of csv file')
parser.add_argument('--deli', help='Delimiter')
args = parser.parse_args()
csv_file = args.file
deli = args.deli
table_name = csv_file.replace('files/', '').split('.csv')[0]
table_name = re.sub('[^a-zA-Z0-9]', '', table_name)

if not csv_file or not table_name:
    print("Missing the argument to run the code. Please do the -h or --help to see details.")
    sys.exit()

config = get_config()
try:
    connection = mysql.connector.connect(
        user=config['user'],
        password=config['password'],
        host=config['host'],
        database=config['database'],
        charset="utf8mb4",
        auth_plugin='mysql_native_password'
    )
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute('SET NAMES utf8mb4')
        cursor.execute("SET CHARACTER SET utf8mb4")
        cursor.execute("SET character_set_connection=utf8mb4") 
        cursor.execute("SET collation_connection=utf8mb4_general_ci") 
        cursor.execute(f"DROP TABLE IF EXISTS {table_name} ;")
        data_dump = create_query.create_tbl(table_name, csv_file, deli=deli)
        result = cursor.execute(data_dump['query'])

        print("Table created")
        with alive_bar(len(data_dump['data'])) as bar:
            for row in data_dump['data']:

                insert_query = create_query.create_insert_query(table_name, row)
                if insert_query == '':
                    continue
                cursor.execute(insert_query)
                connection.commit()
                bar()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
except Error as e:
    print("Error while connecting to MySQL", e)
    # cursor.close()
    # connection.close()
    # print("MySQL connection is closed")

# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")
