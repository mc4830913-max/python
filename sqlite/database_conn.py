import mysql.connector

Host="localhost"
User="root"
Password="Mona@123"
Database="data1"

conn=mysql.connector.connect(
host=Host,
user=User,
password=Password,
database=Database
)

cursor=conn.cursor()

# cursor.execute(
#     '''
#     drop table if exists default_table
#     '''
    
# )

# conn.commit()

# print("datbase")

# cursor.execute('''
             
#              create table if not exists default_table(
#                  id int not null primary key,
#                  name varchar(50),
#                  age int check(age>18),
#                  phone_number int )  ''')
# conn.commit()

# users=[
#     (1,"sheels",22,927396451),
#     (2,"mona",20,927398751),
#     (3,"meera",21,92776451),
#     (4,"laila",22,927436451),
#     (5,"bobs",20,927326451),
#     (6,"tips",19,9296451),
#     (7,"suraj",23,92726451),
#     (8,"chandan",22,92726451),
#     (9,"aashish",24,92706451),
#     (10,"nimmi",20,92756451)

# ]

# cursor.executemany("insert into default_table(id,name,age,phone_number) values (%s,%s,%s,%s)",users)
# conn.commit()
print("createds succesflly")

cursor.execute('select * from default_table')

default_table=cursor.fetchall()
for i in default_table:
    print(i)


conn.close()
