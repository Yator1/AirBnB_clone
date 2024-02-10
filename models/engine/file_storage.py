#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
    __filepath = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__filepath, "w") as j_file:
            Serial_objects = {}
            for key, value in FileStorage.__objects.items():
                Serial_objects[key] = value.to_dict()
            json.dump(Serial_objects, j_file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists pass
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(FileStorage.__filepath, "r") as j_file:
                Unserial_obj = json.load(j_file)
                for key, value in Unserial_obj.items():
                    class_name = value["__class__"]
                    class_name = eval(class_name)
                    obj = class_name(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass
