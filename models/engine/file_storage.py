#!/usr/bin/python3
"""File storage of user"""


import json
from models.base_model import BaseModel

class FileStorage:
    """File storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """All method"""
        return FileStorage.__objects

    def new(self, obj):
        """New method"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Save method"""
        serializable_dict = {}
        for key, value in FileStorage.__objects.items():
            serializable_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serializable_dict, file)

    def reload(self):
        """Reload"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                loaded_dict = json.load(file)
                for key, value in loaded_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_instance = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
