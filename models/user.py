#!/usr/bin/python3
"""class user inheriting from Base class """


from .base_model import BaseModel


class User(BaseModel):
    """Class user that imports fro m the BaseClass"""
    email = str ""
    password = str""
    first_name = str""
    last_name = str""
