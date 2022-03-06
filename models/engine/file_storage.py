#!/usr/bin/python3
"""Module Class FileStorage"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Class to save and load the data in a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dicticionary objects """
        return FileStorage.__objects
      
    def new(self, obj):
        """  sets in objects the obj with key"""
        key = str(type(obj).__name__) + "." + str(obj.id)
        """self.__objects[key]"""

    def save(self):
        """Serializes the objects list to the JSON file"""
        string_to_save = json.dumps(self.__objects.__dict__)
        with open(self.__file_path, mode="w", encoding="utf-8") as my_file:
            my_file.write(json.dumps(string_to_save))

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as my_file:
                self.__objects = json.loads(my_file.read())
        except Exception:
            pass