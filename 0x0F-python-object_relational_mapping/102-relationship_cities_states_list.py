#!/usr/bin/python3
"""
Displays all City objects from the database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_new = session.query(State).join(City).order_by(City.id).all()

    for state in states_new:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
