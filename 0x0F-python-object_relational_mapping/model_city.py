#!/usr/bin/python3
"""
This module contains the City class
and apply some operations on it with sqlalchemy module
"""
from sqlalchemy import create_engine, Column, ForeignKey, String, Integer
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from model_state import State

Base = declarative_base()


class City(Base):
    """
    This is the City class
    """
    __tablename__ = "cities"
    id = Column("id", Integer, primary_key=True,
                nullable=False, unique=True, autoincrement=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id",
                      Integer, ForeignKey('State.id'), nullable=False)
