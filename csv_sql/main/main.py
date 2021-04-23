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
										 database='cartmigration_ver3_test_112',
										 user='root',
										 password='aA123456',
										 auth_plugin='mysql_native_password')
	if connection.is_connected():
		db_Info = connection.get_server_info()
		print("Connected to MySQL Server version ", db_Info)
		cursor = connection.cursor()
		columns, row = read_csv_file(file_name='products-backup.csv')
		data_dump = create_table(database='cartmigration_ver3_test_112', table_name='table', columns=columns)
		result = cursor.execute(data_dump)
		print("Table created successfully ")
		with alive_bar(len(row)) as bar:
			for data in row:
				insert_query = create_insert_query(table='table',columns=columns, data=row)
				if insert_query == '':
					break
				cursor.execute(insert_query)
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
