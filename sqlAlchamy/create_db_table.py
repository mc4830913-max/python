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
Base.metadata.create_all(engine)    

print("created succesfully")
    
