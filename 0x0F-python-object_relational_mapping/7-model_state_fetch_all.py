#!/usr/bin/python3
"""Modules to import"""
import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

inpt = sys.argv
if len(inpt) < 4:
    exit(1)
conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
engine = create_engine(conn_str.format(inpt[1], inpt[2], inpt[3]))
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

session = Session()

outpt = session.query(State).order_by(State.id),all()
for state in outpt:
    print("{}: {}".format(state.id, state.name))

session.close()
