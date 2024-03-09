#!/usr/bin/python3
"""serializes instances to a JSON file and deserializes JSON file to instances"""
import json
from os.path import exists



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
                        if class_name in globals():
                            self.__objects[key] = globals()[class_name](**value)
            except (json.decoder.JSONDecodeError, ValueError):
                print('Errrr')
