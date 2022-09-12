#!/usr/bin/python3
"""script that prints the first State objects
   from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    if session is None:
        print()
    for instance in (session.query(State).
                     filter(State.id == 1).order_by(State.id)):

        print(f"{instance.id}: {instance.name}")
