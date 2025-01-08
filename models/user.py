#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref

from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """
    defines user table in the DB
    This class defines a user by various attributes
    """

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascasde="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
