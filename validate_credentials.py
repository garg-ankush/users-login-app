"""Validate credentials when users are logging in
"""
import json
import hashlib
from setup_db import view_users_by_username


def get_users_record_by_username(user_name):
    try:
        contents = view_users_by_username(user_name)
        for record in contents:
            string_appended_user_name = "'" + record[0] + "'"
            if user_name == string_appended_user_name:
                return record
    except Exception as e:
        print(e)
        print("User name or password does not match our records.")


def is_valid_username(user_name):
    try:
        if view_users_by_username(user_name):
            return True
    except Exception as e:
        print("User name or password does not match our records.")
        return False


def login():
    user_name = input("Enter user name here: ")
    password = input("Enter password here: ")

    hash_password = hashlib.sha256(password.encode()).hexdigest()
    # Check if valid user name
    if is_valid_username(user_name):
        record = get_users_record_by_username(user_name)
        if hash_password == record[1]:
            print("Darkest secret here.......")
        else:
            print("Get lost.")



