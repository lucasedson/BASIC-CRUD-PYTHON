import sqlite3
from query_sql.create_table import query_table_user
database_name = "database.db"


def conect_database():
    global database, cursor
    try:
        database = sqlite3.connect("database/{}".format(database_name))
        cursor = database.cursor()
        return "Successfully Connected"
    except sqlite3.Error as erro:
        return ("Erro: ", erro)

def create_table_user():
    try:
        cursor.execute(query_table_user())
        database.commit()
    except sqlite3.Error as erro:
            return("Error: ", erro)

def insert_user(name, age, email, password):
    try:
        cursor.execute('''
        INSERT INTO user (name, age, email, password)  VALUES('{}','{}', '{}', '{}' )
        '''.format(name, age, email, password))
        database.commit()
    except sqlite3.Error as erro:
        print("Erro: ", erro)

def execute_sql(sql):
    cursor.execute(sql)
    database.commit()
    return cursor.fetchall()