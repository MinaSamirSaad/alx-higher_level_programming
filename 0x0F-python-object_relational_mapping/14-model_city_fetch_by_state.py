#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
Arguments:
    mysql username
    mysql password
    database name
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from urllib.parse import quote_plus
    from model_city import City
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Quote the password to handle special characters
    passwd = quote_plus(sys.argv[2])
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], passwd, sys.argv[3]))
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).filter(City.state_id == State.id)
    cities.order_by(City.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
