from  sqlalchemy import create_engine,Column,Integer,String,UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine=create_engine("sqlite:///datbase.db")
Base=declarative_base()

class user(Base):
    
    __tablename__="users"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=True)
    __table_args__=(UniqueConstraint('email'),)
    
session=sessionmaker(bind=engine)
session=session()

#create new user
users=[user(name="tip",email="tip12@gmail.com"),
       user(name="king",email="patel12@gmail.com"),
       user(name="lsurer",email="manu12@gmail.com"),
       user(name="manu",email="blue2@gmail.com"),
       user(name="patel",email="pavel12@gmail.com")
]
session.add_all(users)
session.commit()
    

print("inserted bulk data succesfully")
session.close()
    
