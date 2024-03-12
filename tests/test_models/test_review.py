#!/usr/bin/python3
"""testing for the review module"""
from models.review import Review
from models.base_model import BaseModel
import unittest


class test_Review(unittest.TestCase):
    """test for the review class"""
    def test_create(self):
        """creation of instance of a review"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)
        self.assertEqual(review.place_id, "")
        self.assertIsInstance(review.place_id, str)
        self.assertEqual(review.user_id, "")
        self.assertIsInstance(review. user_id, str)
        self.assertEqual(review.text, "")
        self.assertIsInstance(review.text, str)


if __name__ == "__main__":
    unittest.main()
