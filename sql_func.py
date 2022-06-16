import datetime
import mysql.connector
import os

# config = {
#     'user': os.environ['user'],
#     'password': os.environ['password'],
#     'host': os.environ['host'],
#     # 'port': os.environ['port'],
#     'database': os.environ['database'],
#     'auth_plugin': 'mysql_native_password'
# }

# connection = mysql.connector.connect(**config)
# cursor = connection.cursor()
# cursor.execute("CREATE DATABASE IF NOT EXISTS budget_manager;")
# connection.commit()
# cursor.close()
# connection.close()

# To run in local
config = {
    'user': 'sivaram',
    'password': 'password',
    'host': 'localhost',
    'port': '3306',
    'database': 'budget_manager'
}

def init_db():
    global config
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    with open("db.sql", 'r') as file1:
        sql_cmds = file1.read()

    sql_cmds1 = sql_cmds.split(";")

    for i in range(0, len(sql_cmds1)-1):
        query = sql_cmds1[i] + ';'
        cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()

def get_values(table):
    global config
    connection = mysql.connector.connect(**config)

    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table};')

    row_headers = [x[0] for x in cursor.description] 
    result = cursor.fetchall()
    json_data = []

    for res in result:
        res = list(res)
        # converting the datetime value to corresponding string value using datetime
        res[1] = res[1].strftime("%d/%m/%Y")
        json_data.append(dict(zip(row_headers, res)))

    cursor.close()
    connection.close()
    return json_data

def get_categories(table):
    global config
    connection = mysql.connector.connect(**config)

    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table};')

    row_headers = [x[0] for x in cursor.description] 
    result = cursor.fetchall()
    json_data = []

    for res in result:
        res = list(res)
        json_data.append(dict(zip(row_headers, res)))

    cursor.close()
    connection.close()
    return json_data

def insert(date, amt, desc, cat, table):
    global config
    connection = mysql.connector.connect(**config)

    cursor = connection.cursor()

    query = (
        f"INSERT INTO {table} "
        "(expense_id, expense_date, expense_amount, expense_description, expense_category) "
        "VALUES (%s, %s, %s, %s, %s)"
    )

    cursor.execute(query, (0, date, amt, desc, cat))
    connection.commit()
    cursor.close()

    connection.close()

# cursor.close()
# connection.close()