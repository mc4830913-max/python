import sqlite3

DB_file="example.db"
conn=sqlite3.connect(DB_file)
cursor=conn.cursor()


cursor.execute("alter table users add column email varchar(50) default")

conn.commit()
print("altered succesfully")


cursor.execute("select * from users")
users=cursor.fetchall()

for user in users:
    print(user)

conn.close()