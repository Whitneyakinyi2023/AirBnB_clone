#!/usr/bin/env python
"""BaseModel that defines all common attributes/methods for other classes"""


class BaseModel:
    """Public instance attributes"""
    def __init__(self):
        """Initialization of BaseModel class public instances"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.current()
        self.updated_at = datetime.current()
        
    def __str__(self):
        """string representation of the BaseClass"""        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """ Public instance method that updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.current()

    def to_dict(self):
        """Public instance method that  returns a dictionary containing all keys/values of __dict__ of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
