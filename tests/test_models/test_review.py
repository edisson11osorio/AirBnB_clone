#!/usr/bin/python3
"""Module that define unittests to models/review.py"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReviewModel(unittest.TestCase):
    """Class to test the Review class"""

    def test_inheritance(self):
        """Test class type"""
        inst_rev = Review()
        self.assertIsInstance(inst_rev, Review)
        self.assertIsInstance(inst_rev, BaseModel)

    def test_attributes(self):
        "Test to verify if has atrributes"
        inst_rev = Review()
        self.assertTrue(hasattr(inst_rev, "id"))
        self.assertTrue(hasattr(inst_rev, "created_at"))
        self.assertTrue(hasattr(inst_rev, "updated_at"))

        self.assertFalse(hasattr(inst_rev, "place_id"))
        self.assertFalse(hasattr(inst_rev, "user_id"))
        inst_rev.place_id = "564"
        inst_rev.user_id = "786"
        self.assertTrue(hasattr(inst_rev, "place_id"))
        self.assertTrue(hasattr(inst_rev, "user_id"))


if __name__ == "__main__":
    unittest.main()
