#!/usr/bin/python3
"""Modules to import"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
import sys

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    # Class creation that inherits from Base
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
