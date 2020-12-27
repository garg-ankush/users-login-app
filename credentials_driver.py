usage = '''
Expense Tracker CLI.

Usage:
    credentials_driver.py init
    credentials_driver.py add_users
    credentials_driver.py login
    credentials_driver.py view_users

'''

from setup_db import create_table, del_table
from add_user import add_user, view_all_users
from validate_credentials import login
from docopt import docopt

args = docopt(usage)
if args['init']:
    create_table()

if args['create']:
    add_user()

if args['login']:
    login()

