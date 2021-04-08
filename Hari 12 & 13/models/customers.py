from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:windioya25@localhost:3306/rentalFilm', echo = True)
Session = sessionmaker(bind=engine)
session = Session()

if session:
    print("Connection Success")



class Customers(Base):
   __tablename__ = 'customers'
   id = Column(Integer, primary_key =  True)
   username = Column(String)
   namaLengkap = Column(String)
   email = Column(String)