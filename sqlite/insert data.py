import sqlite3

DB_file="example.db"
conn=sqlite3.connect(DB_file)
cursor=conn.cursor()

cursor.execute("insert into users(roll_no,name,age) values (1,'mona',18)")

conn.commit()
print("inserted succesfully succesfully")
conn.close()