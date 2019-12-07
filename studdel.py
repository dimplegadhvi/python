import sqlite3

conn=sqlite3.connect("stud.db")
cursor=conn.cursor()
cursor.execute("delete from student where roll=101")
conn.commit()
