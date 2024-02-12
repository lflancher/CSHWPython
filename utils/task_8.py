#Full Disclosure I have no idea how to do this without using the database PostgreSQL
#So instead I will demonstrate my ability to work with SQL
#CREATE TABLE students(s_int PRIMARY KEY AUTO_INCREMENT, 
#name VARCHAR(200), age INT NOT NULL);

#INSERT INTO students(name, age) VALUES('Mario', 12),('Hal', 17),('Leo', 8);
#SELECT age FROM students WHERE name = 'Hal';

#So for this whole project I am essentially making a function that makes a connection to the database
#Then there is a function that creates the table "student"
#Then there is a function that inserts the data into the table

import sqlite3
from sqlite3 import Error



def create_connection(db_file):
  conn = None
  try: 
    conn = sqlite3.connect(db_file)
  except Error as e:
      print(e)
  
  return conn


def create_table(conn, create_table_sql):
  try:
    c = conn.cursor()
    c.execute(create_table_sql)
  except Error as e:
    print(e)
    
def create_students(conn, project):
  sql = '''INSERT INTO student(name, age) VALUES('Mario', 12),('Hal', 17),('Leo', 8)'''
  cur = conn.cursor()
  cur.execute(sql, project)
  conn.commit()
  return cur.lastrowid

def make_database():
  database = "student.db"

  sql_create_students_table = """ CREATE TABLE IF NOT EXISTS students (
  s_int INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER
  ); """


  # create a database connection
  conn = create_connection(database)

  # create tables
  if conn is not None:
    # create projects table
    create_table(conn, sql_create_students_table)
    return 1

  else:
    print("Error! cannot create the database connection.")

