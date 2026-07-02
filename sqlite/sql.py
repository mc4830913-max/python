import sqlite3

DB_file="example.db"
conn=sqlite3.connect(DB_file)
cursor=conn.cursor()

cursor.execute('''
         create table if not exists users
               (
                   roll_no int not null primary key,
                   name varchar(50),
                   age int)'''
               
)

conn.commit()
print("created succesfully")
conn.close()