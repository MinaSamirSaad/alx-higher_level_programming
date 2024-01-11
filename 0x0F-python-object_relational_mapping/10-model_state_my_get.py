#!/usr/bin/python3
"""
prints the State object with the name passed as argument
Arguments:
    username - username to connect the mySQL
    mysql passwd - password to connect the mySQL
    DB name - Name of the database
    state name - name of the state to search
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
    stateObj = session().query(State).filter(State.name == argv[4]).first()
    Base.metadata.create_all(engine)
    if stateObj is None:
        print("Not found")
    else:
        print("{}".format(stateObj.id))
    session().close()
