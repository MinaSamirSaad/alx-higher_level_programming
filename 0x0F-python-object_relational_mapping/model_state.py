#!/usr/bin/python3
"""
Class definition of State
&
Declarative base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base
    
    Attributes:
    - id (int): Auto-generated unique integer, primary key.
    - name (str): String of 128 characters, cannot be null.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

