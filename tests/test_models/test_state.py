#!/usr/bin/python3
"""Module that define unittests to models/state.py"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestStateModel(unittest.TestCase):
    """Class to test the State class"""

    def test_inheritance(self):
        """Test class type"""
        inst_state = State()
        self.assertIsInstance(inst_state, State)
        self.assertIsInstance(inst_state, BaseModel)

    def test_attributes(self):
        "Test to verify if has atrributes of User"
        inst_state = State()
        self.assertTrue(hasattr(inst_state, "id"))
        self.assertTrue(hasattr(inst_state, "created_at"))
        self.assertTrue(hasattr(inst_state, "updated_at"))

        self.assertFalse(hasattr(inst_state, "name"))
        inst_state.name = "California"
        self.assertTrue(hasattr(inst_state, "name"))


if __name__ == "__main__":
    unittest.main()
