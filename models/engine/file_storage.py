#!/usr/bin/python3
"""FileStorage class to serialize/deserialize objects to JSON"""
import json
from os.path import exists

class FileStorage:
    """Serializes instances to a JSON file & deserializes back"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of stored objects"""
        return self.__objects

    def new(self, obj):
        """Add new object with key <class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file"""
        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserialize JSON file to __objects if file exists"""
        if exists(self.__file_path):
            from models.base_model import BaseModel
            classes = {"BaseModel": BaseModel}
            with open(self.__file_path, "r") as f:
                objs = json.load(f)
                for k, v in objs.items():
                    cls = classes[v["__class__"]]
                    self.__objects[k] = cls(**v)
