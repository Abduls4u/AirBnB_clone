#!/usr/bin/python3
"""
A module that contains the class BaseModel
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    '''A class that defines all common attributes/methods for oth
er classes in this package.'''

    def __init__(self):
        '''Constructs all the necessary attributes for the Basemodel class.
        parameters:
        ___________
             args: positional arguments.
             kwargs: keyworded arguments.
        '''
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''returns the informal representation of Basemodel'''

        model_rep = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return (model_rep)

    def save(self):
        '''updates the public instance attribute updated_at with
the current datetime'''
        self.updated_at = datetime.now()
