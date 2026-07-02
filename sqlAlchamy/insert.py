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
new_user=user(name="bob",email="bob12@gmail.com")
session.add(new_user)
session.commit()
    

print("inserted succesfully")
session.close()
    
