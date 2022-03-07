#!/usr/bin/python3
"""Module that define unittests to models/place.py"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlaceModel(unittest.TestCase):
    """Class to test the Place class"""

    def test_inheritance(self):
        """Test class type"""
        inst_place = Place()
        self.assertIsInstance(inst_place, Place)
        self.assertIsInstance(inst_place, BaseModel)

    def test_attributes(self):
        "Test to verify if has atrributes"
        inst_place = Place()
        self.assertTrue(hasattr(inst_place, "id"))
        self.assertTrue(hasattr(inst_place, "created_at"))
        self.assertTrue(hasattr(inst_place, "updated_at"))

        self.assertFalse(hasattr(inst_place, "city_id"))
        self.assertFalse(hasattr(inst_place, "name"))
        inst_place.city_id = "564"
        inst_place.name = "California"
        self.assertTrue(hasattr(inst_place, "city_id"))
        self.assertTrue(hasattr(inst_place, "name"))


if __name__ == "__main__":
    unittest.main()
