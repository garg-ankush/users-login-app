import hashlib
from setup_db import insert_users, view_users_by_username, view_users
import yaml

stream = open('config.yaml', 'r')
dictionary = yaml.load(stream, Loader=yaml.FullLoader)
table_name = dictionary['TABLE_NAME']


def _calculate_password_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


def is_valid_password(password):
    return True


def _is_valid_username(username):
    results = view_users_by_username(username)
    if len(results) > 0:
        return False
    return True


def add_user():
    user_name = input("Enter user name here: ")
    if _is_valid_username(user_name):
        password = input("Enter password here: ")
        if is_valid_password(password):
            password = _calculate_password_hash(password)
            insert_users(table_name, user_name, password)
            return
        print("Password not valid. Please enter a valid password.")
        return
    print("User name already taken. Please enter a valid user name.")
    return


def view_all_users():
    view_users()
