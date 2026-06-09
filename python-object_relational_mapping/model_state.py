#!/usr/bin/python3

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

Base = declarative_base()

class State(Base):
    
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name= Column(String(128), nullable=False)