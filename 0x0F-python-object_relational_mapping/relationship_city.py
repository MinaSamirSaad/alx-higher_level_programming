#!/usr/bin/python3
"""
Class definition of City
&
Declarative base
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class representing the 'cities' table in the database.

    Attributes:
    - id (int): Auto-generated unique integer, primary key.
    - name (str): String of 128 characters, cannot be null.
    - state_id (int): Integer, foreign key to states.id, cannot be null.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
