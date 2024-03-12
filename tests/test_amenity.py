#!/usr/bin/python3
"""test for the amenity module"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest

class TestAmenity(unittest.TestCase):
    """test for the amenity class"""
    def test_create_name(self):
        """creation of name in string format"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

if __name__ == "__main__":
    unittest.main()
