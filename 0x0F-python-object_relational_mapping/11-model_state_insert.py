#!/usr/bin/python3
"""
adds the State object “Louisiana”
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

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    print("{}".format(louisiana.id))

    session.close()
