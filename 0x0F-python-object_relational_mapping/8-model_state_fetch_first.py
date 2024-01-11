#!/usr/bin/python3
"""
Print the first State objects from the DB hbtn_0e_6_usa
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
    Base.metadata.create_all(engine)
    firstState = session().query(State).first()
    if firstState is None:
        print("Nothing")
    else:
        print("{}: {}".format(firstState.id, firstState.name))
    session().close()
