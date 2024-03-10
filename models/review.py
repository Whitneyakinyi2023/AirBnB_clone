#!/usr/bin/python3
"""Public attribute for review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Public class attribute representation of a review"""
    place_id = ""
    user_id = ""
    text = ""
