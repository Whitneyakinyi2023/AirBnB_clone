#!/usr/bin/python3
"""test for the city module"""
from models.city import City
from models.base_model import BaseModel
import unittest

class test_City(unittest.TestCase):
    """test for the city class"""
    def test_create(self):
        """testing creation of an instance of a city"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)
        self.assertIsTrue(hasattr(city, "state_id"))
        self.assertIsTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == "__main__":
    unittest.main()
