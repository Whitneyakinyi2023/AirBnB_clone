#!/usr/bin/python3
<<<<<<< HEAD
"""class user inheriting from Base class """


from .base_model import BaseModel


class User(BaseModel):
    """Class user that imports fro m the BaseClass"""
    email = str ""
    password = str""
    first_name = str""
    last_name = str""
=======
"""class, User, that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class, User"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
>>>>>>> cb77b257c13c07434eb9cc4b8b447a2fac7902e1
