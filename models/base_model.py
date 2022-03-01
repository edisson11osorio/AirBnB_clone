#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel:

    def __init__(self):
        """ init__ metho"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """__str__ method"""
        return "[{}] ({}) {}"\

    def save(self):
        """seve method"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """seve to_dict"""
        serialized = dict(self.__dict__)
        serialized["__class__"] = type(self).__name__
        serialized["created_at"] = serialized["created_at"].isoformat()
        serialized["updated_at"] = serialized["updated_at"].isoformat()
        return serialized
        