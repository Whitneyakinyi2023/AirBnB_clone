#!/usr/bin/python3
"""Public attribute of state that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Representation of a state"""
    name = ""
