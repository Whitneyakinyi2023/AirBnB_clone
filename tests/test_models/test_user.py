#!/usr/bin/python3
"""testing the user module"""

from models.user import User
from models.base_model import BaseModel
import unittest


class test_user(unittest.TestCase):
    """test for user class"""
    def test_create(self):
        """creation of an instance of a user"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)
        self.assertEqual(user.email, "")
        self.assertIsInstance(user.email, str)
        self.assertEqual(user.password, "")
        self.assertIsInstance(user.password, str)
        self.assertEqual(user.first_name, "")
        self.assertIsInstance(user.first_name, str)
        self.assertEqual(user.last_name, "")
        self.assertIsInstance(user.last_name, str)


if __name__ == "__main__":
    unittest.main()
