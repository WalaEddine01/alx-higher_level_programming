#!/usr/bin/python3
"""
This module contains the City class
and apply some operations on it with sqlalchemy module
"""
from sqlalchemy import create_engine, ForeignKey, Column
from sqlalchemy import CHAR, UniqueConstraint, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State

Base = declarative_base()


class State(Base):
    """
    This is the City class
    """
    __tablename__ = "cities"
    id = Column("id", Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, nullable=False, ForeignKey=State.id)


if __name__ == "__main__":
    url = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(url=url, echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()