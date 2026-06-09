#!/usr/bin/python3
"""Script that prints the first State object from the db"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

vroom = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

Session = sessionmaker(bind=vroom)
session = Session()

if not State:
    print("Nothing\n")
else:
    for da_state in session.query(State).\
        filter(State.id == 1):
        print(f"{da_state.id}: {da_state.name}")
