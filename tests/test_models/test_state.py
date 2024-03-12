#!/usr/bin/python3
"""testing the state module"""
from models.state import State
from models.base_model import BaseModel
import unittest


class test_state(unittest.TestCase):
    """test for the state class"""
    def test_create(self):
        """testing creation of an instance of a state"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)
        self.assertEqual(state.name, "")
        self.assertIsInstance(state.name, str)


if __name__ == "__main__":
    unittest.main()
