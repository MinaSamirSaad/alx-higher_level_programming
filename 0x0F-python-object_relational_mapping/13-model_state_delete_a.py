#!/usr/bin/python3
''' model_state_fetch_all '''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    usr = argv[1]
    paswd = argv[2]
    dt = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        usr, paswd, dt, pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State).filter(State.name.like('%a%')).all()
    for row in data:
        session.delete(row)
    session.commit()
