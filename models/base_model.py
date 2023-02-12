#!/usr/bin/python3
"""
A module that contains the class BaseModel
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    '''A class that defines all common attributes/methods for oth
er classes in this package.'''

    def __init__(self, *args, **kwargs):
        '''Constructs all the necessary attributes for the Basemodel class.
        parameters:
        ___________
             args: positional arguments.
             kwargs: keyworded arguments.
        '''
        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        '''returns the informal representation of Basemodel'''

        model_rep = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return (model_rep)

    def save(self):
        '''updates the public instance attribute updated_at with
the current datetime'''
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance:
        - only instance attributes set will be returned
        - a key __class__ is added with the class name of the object
        - created_at and updated_at must be converted to string object in ISO
        object
        """
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                dict_1[k] = v
        return (dict_1)
