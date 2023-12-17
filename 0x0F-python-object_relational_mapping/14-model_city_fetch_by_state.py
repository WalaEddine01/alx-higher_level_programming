#!/usr/bin/python3
"""
This module contains a script thatprints all City
objects from the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import City, Base

if __name__ == "__main__":
    url = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(url=url, echo=False)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(City).all()
    for r in result:
        print(str(r.id) + ": " + r.name)
