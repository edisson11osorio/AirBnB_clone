#!/usr/bin/python3
"""Module that define unittests to models/base_model.py"""
import json
from os import path
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Class to test the FileStorage class"""

    def test_class(self):
        """Test the File Storage class"""
        storage = FileStorage()
        self.assertTrue(type(storage) == FileStorage)
        self.assertIsInstance(storage, FileStorage)

    def test_private_attr(self):
        """Test the private attribute of File Storage class"""
        storage = FileStorage()
        with self.assertRaises(AttributeError) as er:
            print(storage.__objects)

    def test_attributes(self):
        """Test the attributes of File Storage class"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

    def test_FileStorage_arg(self):
        """Testing file storage with an argument"""
        with self.assertRaises(TypeError):
            FileStorage("AirBnB")
            with self.assertRaises(TypeError):
                FileStorage("107")
                with self.assertRaises(TypeError):
                    FileStorage(None)

    def test_file_path(self):
        """Test the file path is string"""
        self.assertEqual(str, type(FileStorage.__file_path))

    def test_All(self):
        """Test the all method"""
        storage = FileStorage()
        objs_storage = storage.all()
        self.assertIsNotNone(objs_storage)
        self.assertEqual(type(objs_storage), dict)

    def test_reload(self):
        """Tests the reload method"""
        if not path.exists("file.json"):
            new_file = FileStorage()
            new_base = BaseModel(id="123", created_at="2021-02-17T22:46:38.86",
                                 updated_at="2021-02-17T22:46:38.86")
            new_file.new(new_base)
            new_file.save()
            with open("file.json", "r") as f:
                obj = json.load(f)
                self.assertEqual(type(obj), dict)

    def test_reload_with_arg(self):
        """Tests the reload method with argument"""
        storage = FileStorage()
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_save(self):
        """Test save method"""
        storage = FileStorage()
        new_base = BaseModel()
        storage.new(new_base)
        storage.save()
        save_text = ""
        with open("file.json", "r") as file:
            save_text = file.read()
            self.assertIn("BaseModel." + new_base.id, save_text)

if __name__ == "__main__":
    unittest.main()
