import sqlite3

DB_file="example.db"
conn=sqlite3.connect(DB_file)
cursor=conn.cursor()


cursor.execute("update users set name='anushka' where roll_no=2")

conn.commit()
print("upadtedn succesfully")


cursor.execute("select * from users")
users=cursor.fetchall()

for user in users:
    print(user)

conn.close()