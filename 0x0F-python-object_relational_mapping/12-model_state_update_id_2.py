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
    search_state = session.query(State).filter(State.id == 2).first()
    search_state.name = 'New Mexico'
    session.commit()
