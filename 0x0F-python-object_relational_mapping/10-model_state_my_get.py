#!/usr/bin/python3
"""prints the State object with the name passed
   as argument from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = (session.query(State).filter
             (State.name == (argv[4],)).order_by(State.id))
    user = query.first()
    if user is None:
        print("Not found")
    else:
        print(f"{user.id}")
