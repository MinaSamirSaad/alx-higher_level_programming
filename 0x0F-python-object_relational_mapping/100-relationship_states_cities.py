#!/usr/bin/python3
"""
creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
Arguments:
    username - username to connect to MySQL
    mysql passwd - password to connect to MySQL
    DB name - Name of the database
"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from urllib.parse import quote_plus
    from relationship_state import Base, State
    from relationship_city import City

    # Quote the password to handle special characters
    passwd = quote_plus(argv[2])
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.
        format(argv[1], passwd, argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    calif = State(name="California")
    calif.cities = [City(name="San Francisco")]
    session.add(calif)
    session.commit()
    session.close()
