#!/usr/bin/python3
''' model_state_fetch_all '''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


if __name__ == "__main__":
    usr = argv[1]
    paswd = argv[2]
    dt = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        usr, paswd, dt, pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
