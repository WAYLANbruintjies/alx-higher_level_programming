#!/usr/bin/python3
"""Modules to import to create class definition to work with SQLAlchemy ORM"""
from sys import argv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative_base import declarative
from model_state import Base, State


class City(Base):
    """City class"""
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, PrimaryKey=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
