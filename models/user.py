#!/usr/bin/python3
"""class user inheriting from Base class """


from .base_model import BaseModel
class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""


    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)

    def save(self):
        """Method saving current instance"""
        super().save()

    def save_to_file(self):
        """Saving instance to file"""
        self.save()
