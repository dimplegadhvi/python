import sqlite3

conn=sqlite3.connect("test.db")
cursor=conn.cursor()
cursor.execute("insert into student values (105,'Alay',100)")
conn.commit()
