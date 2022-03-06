#!/usr/bin/python3
"""Module for the Base class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class that defines all common attributes/methods for other classes"""
    def __init__(self):
        """Constructor of the class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """Return the represents of the class objects as a string"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with
            the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
            __dict__ of the instance"""
        serialized = dict(self.__dict__)
        serialized["__class__"] = type(self).__name__
        serialized["created_at"] = serialized["created_at"].isoformat()
        serialized["updated_at"] = serialized["updated_at"].isoformat()