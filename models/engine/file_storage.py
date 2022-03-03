#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:

      __file_path = "file.json"
      __objects = {}

      def all(self):
          """ Return the dicticionary objects """
          return self.__objects
      
      def new(self, obj):
          """  sets in objects the obj with key"""
          key = obj.to_dic 