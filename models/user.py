#!/usr/bin/python3
''' A module that contains the class User that inherits from BaseModel
Usage:
    ./user.py
Author:
    Abdulsalam Abdulsomad .A. - May 24th, 2023.
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''class User'''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
