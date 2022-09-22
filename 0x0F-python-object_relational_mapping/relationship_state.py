#!/usr/bin/python3
"""python file that contains the class definition
of a State and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Inherits from Base and links to MySQL table states"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
