import argparse
import sys

import mysql.connector
from alive_progress import alive_bar
from mysql.connector import Error

from libs import create_query
from libs.get_config import *

parser = argparse.ArgumentParser(prog='mysql_con_cus')
parser.add_argument('--file', help='Name of csv file')
parser.add_argument('--name', help='Table name to save the database')
args = parser.parse_args()
csv_file = getattr(args, 'file')
name = getattr(args, 'name')
if not csv_file or not name:
    print("Missing the argument to run the code. Please do the -h or --help to see details.")
    sys.exit()
config = get_config()
try:
    connection = mysql.connector.connect(
        user=config['user'],
        password=config['password'],
        host=config['host'],
        database=config['database'],
        auth_plugin='mysql_native_password'
    )
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        data_dump = create_query.create_tbl(name, csv_file, ',')
        result = cursor.execute(data_dump['query'])

        print("Table created")
        with alive_bar(len(data_dump['data'])) as bar:
            for row in data_dump['data']:

                insert_query = create_query.create_insert_query(name, row)
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
