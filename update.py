import sqlite3

conn=sqlite3.connect("data.db")
cursor=conn.cursor()
cursor.execute("update base1 set marks=33,name='riya' where rollno=101")
conn.commit()
