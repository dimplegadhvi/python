import sqlite3

conn=sqlite3.connect("stud.db")
cursor=conn.cursor()
cursor.execute("select * from student")
rs=cursor.fetchall()
for row in rs:
    print(row)
conn.commit()
