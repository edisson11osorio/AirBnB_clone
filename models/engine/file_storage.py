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
        return self.__objects

    def new(self, obj):
        """  sets in objects the obj with key"""
        key = str(type(obj).__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes the objects list to the JSON file"""
        json_obj = {}        
        for key in self.__objects:            
            json_obj[key] = self.__objects[key].to_dict()        
        with open(self.__file_path, 'w', encoding='UTF-8') as file:            
            json.dump(json_obj, file)

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as my_file:
                dict_file = json.load(my_file)
                for value in dict_file.values():
                    new_object = globals()[value["__class__"]](**value)
                    self.new(new_object)
        except Exception:
            pass