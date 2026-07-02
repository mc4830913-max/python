import sqlite3

DB_file="example.db"
conn=sqlite3.connect(DB_file)
cursor=conn.cursor()

user=[
    (2,"anu",22),
    (3,"rip",12),
    (4,"tip",19)
]

cursor.executemany("insert into users(roll_no,name,age) values(?,?,?)", user)

conn.commit()
print("created succesfully")
conn.close()