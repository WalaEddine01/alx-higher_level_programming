from sqlalchemy import create_engine, ForeignKey, column
from sqlalchemy import CHAR, UniqueConstraint, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    Base = declarative_base()

    class State(Base):
        __tablename__ == "states"
        id = column(Integer, primary_key=True, nullable=False,
                    unique=True, autoincrement=True)
        name = column(String(128), nullable=False)

    url = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(url=url, echo=True)
    Base.metadata.create_all(engine)
