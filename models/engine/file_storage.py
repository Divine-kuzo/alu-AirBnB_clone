#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel  # import any other models you add later

class FileStorage:
    """Serializes instances to a JSON file & deserializes back"""
