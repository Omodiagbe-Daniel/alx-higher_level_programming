#!/usr/bin/python3
"""python file that contains the class definition
of a Class and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from model_state import Base, State


class City(Base):
    """Inherits from Base and links to MySQL table states"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = (Integer, ForeignKey(State.id), nullable=False)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
