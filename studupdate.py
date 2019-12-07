import sqlite3

conn=sqlite3.connect("stud.db")
cursor=conn.cursor()
cursor.execute("update student set marks=88,name='john' where roll=101")
conn.commit()
