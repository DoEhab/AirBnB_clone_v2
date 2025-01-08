#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """
    represents state table in the DB
    connected to city table
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """get list of cities"""
            city_list = []
            for data in list(models.storage.all(City).values()):
                if data.state_id == self.id:
                    city_list.append(data)
            return city_list
