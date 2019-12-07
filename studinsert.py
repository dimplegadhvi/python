import sqlite3

conn=sqlite3.connect("stud.db")
cursor=conn.cursor()
cursor.execute("insert into student values (102,'riya',23)")
conn.commit()
