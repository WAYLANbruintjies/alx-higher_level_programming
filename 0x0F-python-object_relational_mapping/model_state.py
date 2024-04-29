#!/usr/bin/python3
"""Modules to import"""
import SQLAlchemy
import sys

Base = declarative_base()

class State(Base):
    # Class creation that inherits from Base
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
