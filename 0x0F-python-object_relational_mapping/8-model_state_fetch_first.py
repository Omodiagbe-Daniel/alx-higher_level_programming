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
    query = (session.query(State).order_by(State.id))
    user = query.first()
    if user is None:
        print("Nothing")
    else:
        print(f"{user.id}: {user.name}")
