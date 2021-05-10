import csv
import json
import sys

# csv.field_size_limit(sys.maxsize)


def escape(value):
    if value is None or value is False:
        return 'null'
    if value == '':
        return "''"
    if not value:
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        value = value.replace("""\\""", '')
        value = value.replace('"', '\\"')
        value = value.replace("'", "\\'")
    return "'" + to_str(value) + "'"


def to_str(value):
    if isinstance(value, bool):
        return str(value)
    if (isinstance(value, int) or isinstance(value, float)) and value == 0:
        return '0'
    if not value:
        return ''
    if isinstance(value, dict) or isinstance(value, list):
        return json_encode(value)
    try:
        value = str(value)
        return value
    except Exception:
        return ''


def json_encode(data):
    try:
        data = json.dumps(data)
    except Exception:
        data = False
    return data


def create_tbl(tbl_name, csv_file, deli):
    with open(csv_file, encoding='utf-8', errors='ignore') as csvfile:
        fReader = csv.reader(csvfile, delimiter=deli)

        headers = next(fReader)
        list_colume = ''
        for item in headers:
            list_colume += f"`{item}` LONGTEXT NULL, \n"
        mySql_Create_Table_Query = "CREATE TABLE " + tbl_name + """
	    (id int(15) NOT NULL AUTO_INCREMENT,\n""" + list_colume + """
	    PRIMARY KEY (id)) ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;"""
    with open(csv_file, encoding='utf-8', errors='ignore') as f:
        a = [{k: v for k, v in row.items()} for row in csv.DictReader(f, delimiter=deli, skipinitialspace=True)]
    return {'query': mySql_Create_Table_Query, 'data': a}


def create_insert_query(table, data_list):
    a = ''
    try:
        a = f"Insert into {table}({','.join(['`' + key + '`' for key in data_list])})" \
            f" VALUES ({','.join([escape(value) if escape(value) is not None else '' for key, value in data_list.items()])})"
    except:
        pass
    finally:
        return a
