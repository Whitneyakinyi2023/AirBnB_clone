#!/usr/bin/python3
"""testing the place moduke"""

from models.place import Place
from models.base_model import BaseModel
import unittest


class test_Place(unittest.TestCase):
    """test for the place class"""
    def test_create(self):
        """testing the creation of an instance of Place"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
