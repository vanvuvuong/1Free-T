from fileinput import filename

import pandas as pd
from datetime import datetime


def log(mes, dt=None):
    """Logging the message depending on the time:
		mes: message you want to assign
		dt: the time you assign. None is by default,
	It will return the current time if time hasn't been typed"""

    dt = dt or datetime.now()
    dt = str(dt)
    message = f"{mes}:{dt}"
    with open("log", "a+") as f:
        f.write(message)
        f.write("\n")


def read_csv_file(file_name=''):
    """Read the csv file"""
    header, line = '', ''
    try:
        file = pd.read_csv(file_name, delimiter=',', encoding='utf-8', lineterminator=None, quotechar='"',
                           doublequote=True, na_values='', keep_default_na=False)
        file.fillna('', inplace=True)
        header = tuple(file.columns)
        line = list()
        for row in file.values:
            line.append(tuple(row))
        line = tuple(line)
    except:
        log(f"Error when reading CSV file")
        exit()
    finally:
        return header, line

def create_db():
    pass


def create_table(database='default', table_name='default', columns=[]):
    """Make the create table query"""
    before_query = f"USE `{database}`; " + f" DROP TABLE IF EXISTS `{table_name}` ;"
    query = f"CREATE TABLE `{table_name}` ( `ID` BIGINT AUTO_INCREMENT PRIMARY KEY, "
    for column in columns:
        if column is columns[-1]:
            query += f" `{column}` text ) ENGINE='MyISAM' COLLATE 'utf8_general_ci';"
            break
        query += f" `{column}` TEXT NULL, "
    return before_query, query


def create_insert_query(table, columns, data, limit=4):
    """Make the insert query for table"""
    query = f"INSERT INTO `{table}` (`{'`,`'.join(columns)}`) VALUES "
    for row in data:
        if row is data[-1]:
            row_insert = '\",\"'.join(str(a).replace('"', '\\"') for a in row)
            query += f" (\"{row_insert}\") ; "
            break
        row_insert = '\",\"'.join(str(a).replace('"', '\\"') for a in row)
        query += f" (\"{row_insert}\"), "
    return query


def limit(function):
    count = limit

    def get_data(row_list=None, *args, **kwargs):
        nonlocal count
        new_row_list = row_list[count:count + 4]
        count += 4
        return function(*args, **kwargs)

    return get_data

if __name__ == "__main__":
    header, lines = read_csv_file('products-backup.csv')
    line = lines[:4]
    table_query = create_table('cartmigration_ver3_test_112', 'xxx', header)
    insert_query = create_insert_query('xxx', header, line)
    a = 1
