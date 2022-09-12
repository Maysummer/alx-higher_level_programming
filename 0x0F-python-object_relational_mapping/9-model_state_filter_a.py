#!/usr/bin/python3
'''script that lists all State objects that conatain letter "a"
from the database hbtn_0e_6_usa'''

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    for s in state:
        print('{}: {}'.format(s.id, s.name))