#!/usr/bin/python3
<<<<<<< HEAD
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
=======
"""serializes instances to a JSON file and deserializes JSON file to instances"""
import json
from os.path import exists
from models.user import User



class FileStorage:
    """serializes instances to a JSON file & deserializes JSON file"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns __objects"""
        return self.__objects

    def new(self, obj):
        """store objects with key <class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
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
                print('Errrr')
>>>>>>> cb77b257c13c07434eb9cc4b8b447a2fac7902e1
