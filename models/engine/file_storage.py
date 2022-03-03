#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dicticionary objects """
        return FileStorage.__objects
      
    def new(self, obj):
        """  sets in objects the obj with key"""
        key = obj.to_dict().__class__ + "." + obj.__str__.id
        print("In new: {}".format(key))

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
