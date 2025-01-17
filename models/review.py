#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column, String, ForeignKey

from models.base_model import Base
from models.base_model import BaseModel


class Review(BaseModel, Base):
    """
    Represents review class in the DB
    Review class to store review information
    """

    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
