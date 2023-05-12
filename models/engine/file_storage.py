#!/usr/bin/python3
''' A module that contains a class that creates a simple flow of
serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
Usage:
    ./file_storage.py
Author:
    Abdulsalam Abdulsomad .A. - May 11th, 2023.
'''
import json
import os
import importlib
from models.base_model import BaseModel


class FileStorage:
    '''A class FileStorage that serializes instances to a JSON
file and deserializes JSON file to instances'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return (self.__objects)

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path)'''
        with open(self.__file_path, 'w') as file:
            dict_rep = {}
            for key, value in self.__objects.items():
                dict_rep[key] = value.to_dict()
            json.dump(dict_rep, file)

    def reload(self):
        '''deserializes the JSON file to __objects (only if the JS
ON file (__file_path) exists ; otherwise, do nothing. If the file
doesn’t exist, no exception should be raised)'''
        classes = {
                    'BaseModel': BaseModel
        }
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    self.__objects[key] = classes[value['__class__']](**value)
