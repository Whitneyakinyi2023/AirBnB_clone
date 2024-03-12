#!/usr/bin/python3
"""Public instance of amenities"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representation of amenities"""
    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
        self.name = ""
