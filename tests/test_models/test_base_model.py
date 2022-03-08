#!/usr/bin/python3
"""Module that define unittests to models/base_model.py"""
from datetime import datetime
from time import sleep
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class to test the BaseModel class"""

    def test_id(self):
        """Test the id attribute"""
        inst_one = BaseModel()
        inst_two = BaseModel()
        self.assertIsInstance(inst_one, BaseModel)
        self.assertTrue(hasattr(inst_one, "id"))
        self.assertNotEqual(inst_one.id, inst_two.id)
        self.assertIsInstance(inst_one.id, str)
        inst_one = BaseModel(132)
        self.assertNotEqual(inst_one.id, 132)
        inst_one = BaseModel("Hello")
        self.assertNotEqual(inst_one.id, "Hello")
        inst_one = BaseModel([0, "h", 3])
        self.assertNotEqual(inst_one.id, [0, "h", 3])

    def test_create_at(self):
        """Test the create_at attribute"""
        inst = BaseModel()
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertIsInstance(inst.created_at, datetime)
        self.assertNotEqual(inst.created_at, datetime.now())

    def test_updated_at(self):
        """Test the updated_at attribute"""
        inst = BaseModel()
        self.assertTrue(hasattr(inst, "updated_at"))
        self.assertIsInstance(inst.updated_at, datetime)
        before_time_created = inst.created_at
        before_time_updated = inst.updated_at
        inst.save()
        self.assertNotEqual(before_time_updated, inst.updated_at)
        self.assertEqual(before_time_created, inst.created_at)

    def test_strclasname(self):
        """Test class name"""
        inst = BaseModel()
        self.assertEqual('[BaseModel]' in str(inst), True)

    def test_strint(self):
        """Test __string__"""
        inst = BaseModel()
        result = "[{}] ({}) {}".format(inst.__class__.__name__,
                                       inst.id, inst.__dict__)
        self.assertEqual(result, str(inst))

    def test_to_dict(self):
        """Test the values of dictionary method"""
        inst = BaseModel()
        dict_inst = inst.to_dict()
        self.assertTrue(dict, type(dict_inst))
        self.assertIn("id", dict_inst)
        self.assertIn("created_at", dict_inst)
        self.assertIn("updated_at", dict_inst)
        self.assertIn("__class__", dict_inst)
        self.assertEqual(str, type(dict_inst["created_at"]))
        self.assertEqual(str, type(dict_inst["updated_at"]))

    def test_save(self):
        """Test to save method"""
        inst = BaseModel()
        sleep(0.5)
        date_now = datetime.now()
        inst.save()
        diference = inst.updated_at - date_now
        self.assertTrue(abs(diference.total_seconds()) < 0.01)


if __name__ == "__main__":
    unittest.main()
