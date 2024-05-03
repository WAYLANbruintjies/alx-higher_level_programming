#!/usr/bin/python3
"""
A script that defines a City class to work with MySQLAlchemy
"""
from relationship_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """
    City class that inherits Base
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
