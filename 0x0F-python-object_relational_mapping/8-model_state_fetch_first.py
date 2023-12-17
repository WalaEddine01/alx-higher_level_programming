#!/usr/bin/python3
"""
This module contains a script  prints the first State object from the
database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base

if __name__ == "__main__":
    url = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(url=url, echo=False)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).all()
    print(str(result[0].id) + ": " + result[0].name)
