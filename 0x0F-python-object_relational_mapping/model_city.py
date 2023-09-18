#!/usr/bin/python3
''' model City module '''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    '''Represents a city for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.i
    state_id : foreign key'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, Foreign_key=('states.id'))
