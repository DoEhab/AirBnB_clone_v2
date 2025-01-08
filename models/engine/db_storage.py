#!/usr/bin/python3
"""DBstorage class to handle DB functionalities"""
from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """DB initialization"""

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return all items in the DB"""
        result = {}
        if cls:
            queried_objs = self.__session.query(cls).all()
        else:
            my_cls = [User, State, City, Amenity, Place, Review]
            queried_objs = []

            for model_cls in my_cls:
                queried_objs.extend(self.__session.query(model_cls).all())

        for obj in queried_objs:
            key = f"{type(obj).__name__}.{obj.id}"
            result[key] = obj

        return result

    def new(self, obj):
        """create new record in DB"""
        self.__session.add(obj)

    def save(self):
        """Saves data to DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete item from the DB"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload the DB session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
