import sqlite3
connection=sqlite3.connect('data.db')
cursor=connection.cursor()
create_table="CREATE TABLE if not exists users(id INTEGER PRIMARY KEY ,username text,password text)"
create_table2="CREATE TABLE if not exists items(id INTEGER PRIMARY KEY ,name text ,price real)"
cursor.execute(create_table2)

cursor.execute(create_table)

connection.commit()
connection.close()