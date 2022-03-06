#!/usr/bin/python3
"""Module for the Base class"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base Model"""

    # def __init__(self, *args, **kwargs):
    #     """initialize the base model"""
    #     if kwargs:
    def __str__(self):
        """Return the represents of the class objects as a string"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute
         updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
         __dict__ of the instance"""
        return
