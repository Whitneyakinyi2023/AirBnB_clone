#!/usr/bin/python3
"""Public attribute representing a city"""
from models.base_model import BaseModel


class City(BaseModel):
    """class representation"""
    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
