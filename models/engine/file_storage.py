#!/usr/bin/python3
"""File storage handling """


import json
from os.path import exists
from models.user import User

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns __objects"""
        return self.__objects

    def new(self, obj):
        """Stores objects with key <class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as f:
                    serialized_objects = json.load(f)
                    for key, value in serialized_objects.items():
                        class_name, obj_id = key.split('.')
                        if class_name == 'User':
                            self.__objects[key] = User(**value)
                        elif class_name in globals():
                            self.__objects[key] = globals()[class_name](**value)
            except (json.decoder.JSONDecodeError, ValueError):
                print('Error decoding JSON file')
