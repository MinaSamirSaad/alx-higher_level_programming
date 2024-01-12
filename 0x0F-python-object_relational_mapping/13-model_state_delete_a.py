#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
Arguments:
    username - username to connect to MySQL
    mysql passwd - password to connect to MySQL
    DB name - Name of the database
"""
if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from urllib.parse import quote_plus

    # Quote the password to handle special characters
    passwd = quote_plus(argv[2])
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], passwd, argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve all State objects with a name containing 'a'
    states_to_delet = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_to_delet:
        session.delete(state)

    session.commit()

    session.close()
