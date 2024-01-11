#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
Arguments:
    username - username to connect the mySQL
    mysql passwd - password to connect the mySQL
    DB name - Name of the database
"""
if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import (create_engine)
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from urllib.parse import quote_plus

    # Quote the password to handle special characters
    passwd = quote_plus(argv[2])
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], passwd, argv[3]))
    session = sessionmaker(bind=engine)
    states_with_a = session().query(State).filter(State.name.like('%a%')).all()
    Base.metadata.create_all(engine)
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))
    session().close()
