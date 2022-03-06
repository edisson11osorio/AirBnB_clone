#!/usr/bin/python3
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
        self.assertTrue(hasattr(inst, "create_at"))
        self.assertIsInstance(inst.created_at, datetime)
        self.assertEqual(inst.created_at, datetime.now())

    def test_updated_at(self):
        """Test the updated_at attribute"""
        inst = BaseModel()
        self.assertTrue(hasattr(inst, "updated_at"))
        self.assertIsInstance(inst.updated_at, datetime)
        inst.save()
        self.assertEqual(inst.updated_at, datetime.now())

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
        """Test the dictionary method"""
        inst = BaseModel()
        self.assertIsInstance(inst.to_dict(), dict)

    def test_save(self):
        """Test to save method"""
        inst = BaseModel()
        before_time = inst.updated_at
        sleep(10)
        inst.id = 784
        inst.save()
        after_time = inst.updated_at
        self.assertTrue(inst.id == 784)
        self.assertNotEqual(before_time, after_time)
        with open("file.json", "r", encoding="utf-8") as f:
            self.assertTrue("\"id\": 784" in f.read())


if __name__ == "__main__":
    unittest.main()
