#!/usr/bin/python3
"""class user inheriting from Base class"""


from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
