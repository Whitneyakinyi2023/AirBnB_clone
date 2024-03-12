#!/usr/bin/python3
"""test for the amenity module"""
from models.amenities import Amenities
from models.base_model import BaseModel
import unittest

class test_Amenity(unittest.TestCase):
    """test for the amenity class"""
    def test_create_name(self):
        """creation of name in string format"""
        amenity = Amenities()
        self.assertIsInstance(amenity, Amenities)
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

if __name__ == "__main__":
    unittest.main()
