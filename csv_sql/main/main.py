from alive_progress import alive_bar
import mysql.connector
from csv_sql.main.utils import *
from mysql.connector import Error
import os
from urllib.parse import urlparse

limit = 4

try:
	connection = mysql.connector.connect(host='localhost',
										 port='3306',
										 database='cartmigration_ver3_test_113',
										 user='root',
										 password='aA123456',
										 auth_plugin='mysql_native_password')
	if connection.is_connected():
		db_Info = connection.get_server_info()
		print("Connected to MySQL Server version ", db_Info)
		cursor = connection.cursor()
		columns, row = read_csv_file(file_name='products.csv')
		prepare_table, table_query = create_table(database='cartmigration_ver3_test_112', table_name='table', columns=columns)
		cursor.execute(prepare_table, multi=True)
		result = cursor.execute(table_query)
		print("Table created successfully ")
		with alive_bar(len(row)) as bar:
			for data in row:
				insert_query = create_insert_query(table='table',columns=columns, data=row)
				if insert_query == '':
					break
				cursor.execute(insert_query, multi=True)
		connection.commit()
		bar()

except Error as e:
	print("Error while connecting to MySQL", e)
	a = 1

finally:
	if connection.is_connected():
		cursor.close()
		connection.close()
		print("MySQL connection is closed")
