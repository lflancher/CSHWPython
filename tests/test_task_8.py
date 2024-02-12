import sqlite3
from sqlite3 import Error
from utils.task_8 import make_database, create_table, create_students, create_connection

"""In all honesty I have no idea how to do this using the database system, SQLite
Running tests on the SQLite database that is. This is my best attempt"""

#In the "make_database" function, if the database is created successfully, then 1 is returned


def test_sql():
  assert make_database() == 1