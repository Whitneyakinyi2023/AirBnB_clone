#!/usr/bin/env python3
"""BaseModel that defines all common attributes/methods for other classes"""

from datetime import datetime
import uuid


class BaseModel:
    """Public instance attributes"""
    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel class public instances"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        if isinstance(value, str):
                            value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """string representation of the BaseClass"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Public instance method that updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        from models import storage
        if storage:
            storage.new(self)
            storage.save()

    def to_dict(self):
        """Public instance method that  returns a dictionary containing all keys/values of __dict__ of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
