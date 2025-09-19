#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel  # import any other models you add later

class FileStorage:
    """Serializes instances to a JSON file & deserializes back"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Store object in __objects using <class name>.id as key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, f
            )

    def reload(self):
        """Deserialize JSON file to __objects (if it exists)"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name = value["__class__"]
                    if cls_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**value)
