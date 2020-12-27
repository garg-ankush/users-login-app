import sqlite3
import yaml


def create_table():
    stream = open('config.yaml', 'r')
    dictionary = yaml.load(stream, Loader=yaml.FullLoader)
    db_name = dictionary['DB_NAME']
    table_name = dictionary['TABLE_NAME']

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    query = '''CREATE TABLE IF NOT EXISTS {} (username varchar, password varchar)'''.format(table_name)

    cur.execute(query)
    conn.commit()


def insert_users(table_name, user_name, password):
    stream = open('config.yaml', 'r')
    dictionary = yaml.load(stream, Loader=yaml.FullLoader)
    db_name = dictionary['DB_NAME']
    table_name = dictionary['TABLE_NAME']

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    query = '''INSERT INTO {}
    VALUES (
    {},
    '{}'
    )'''.format(str(table_name), str(user_name), str(password))

    cur.execute(query)
    conn.commit()
    print("Inserted records successfully.")


def login_users(user_name, password):
    stream = open('config.yaml', 'r')
    dictionary = yaml.load(stream, Loader=yaml.FullLoader)
    db_name = dictionary['DB_NAME']
    table_name = dictionary['TABLE_NAME']

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    query = '''SELECT * FROM '{}'
                WHERE username = '{}'
                 AND password = '{}'''.format(str(table_name), str(user_name), str(password))

    results = cur.execute(query).fetchall()
    print(results)
    return results


def view_users_by_username(user_name):
    user_name = str(user_name)
    stream = open('config.yaml', 'r')
    dictionary = yaml.load(stream, Loader=yaml.FullLoader)
    db_name = dictionary['DB_NAME']
    table_name = dictionary['TABLE_NAME']

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    query = '''SELECT * FROM '{}'
                WHERE username = {}'''.format(str(table_name), user_name)

    results = cur.execute(query).fetchall()
    return results


def view_users():
    stream = open('config.yaml', 'r')
    dictionary = yaml.load(stream, Loader=yaml.FullLoader)
    db_name = dictionary['DB_NAME']
    table_name = dictionary['TABLE_NAME']

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    query = '''SELECT * FROM {}'''.format(str(table_name))

    results = cur.execute(query).fetchall()
    print(results)
    return results


def del_table():
    stream = open('config.yaml', 'r')
    dictionary = yaml.load(stream, Loader=yaml.FullLoader)
    db_name = dictionary['DB_NAME']
    table_name = dictionary['TABLE_NAME']

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    query = """Drop table users"""

    results = cur.execute(query).fetchall()
    return results
