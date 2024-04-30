#!/usr/bin/python3
"""Modules to import"""
import sys
from sqlalchemy import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    # Create SQLAlchemy engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    # Create session
    Session = sessionmaker(bind=engine)
    # Session object
    session = Session()
    # Do search for state
    found = False
    for state insession.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break

    if found is false:
        print("Not found")
