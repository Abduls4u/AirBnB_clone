#!/usr/bin/python3
''' A module that contains a parent class (called BaseModel) to
take care of the initialization, serialization and deserialization
of future instances.
Usage:
    ./base_model.py
Author:
    Abdulsalam Abdulsomad .A. - May 11th, 2023.
'''
from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''A class BaseModel that defines all common attributes/method
s for other classes'''
    def __init__(self, *args, **kwargs):
        '''class constructor method'''
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key not in ('created_at', 'updated_at'):
                        setattr(self, key, value)
                    else:
                        setattr(self, key, datetime.fromisoformat(value))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''returns unofficial representation of the class'''
        class_name = self.__class__.__name__
        return (f"[{class_name}] ({self.id}) {self.__dict__}")

    def save(self):
        '''updates the public instance attribute updated_at with
the current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of
__dict__ of the instance'''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return (obj_dict)
