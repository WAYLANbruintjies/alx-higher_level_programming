#!/usr/bin/python3
"""Modules to import"""
import sys
from sqlalchemy import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    
    """Access database and create SQLAlchemy engine""" 
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))

    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    state = session.query(State).filter(State.name == sys.argv[4]).first()
        if state is not None:
            print("{0}".format(state.id))
        else:
        print("Not found")
