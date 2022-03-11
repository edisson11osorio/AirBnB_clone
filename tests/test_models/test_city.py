#!/usr/bin/python3
"""Module that define unittests to models/city.py"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCityModel(unittest.TestCase):
    """Class to test the City class"""

    def test_inheritance(self):
        """Test class type"""
        inst_city = City()
        self.assertIsInstance(inst_city, City)
        self.assertIsInstance(inst_city, BaseModel)

    def test_attributes(self):
        "Test to verify if has atrributes"
        inst_city = City()
        self.assertTrue(hasattr(inst_city, "id"))
        self.assertTrue(hasattr(inst_city, "created_at"))
        self.assertTrue(hasattr(inst_city, "updated_at"))

        self.assertFalse(hasattr(inst_city, "state_id"))
        self.assertFalse(hasattr(inst_city, "name"))
        inst_city.state_id = "675"
        inst_city.name = "California"
        self.assertTrue(hasattr(inst_city, "state_id"))
        self.assertTrue(hasattr(inst_city, "name"))


if __name__ == "__main__":
    unittest.main()
