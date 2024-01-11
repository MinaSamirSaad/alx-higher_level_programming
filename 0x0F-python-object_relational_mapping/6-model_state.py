#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from urllib.parse import quote_plus

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    # Quote the password to handle special characters
    password = quote_plus(sys.argv[2])
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], password, sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
