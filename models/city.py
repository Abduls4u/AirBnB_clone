#!/usr/bin/python3
''' A module that contains the class City that inherits from BaseModel
Usage:
    ./city.py
Author:
    Abdulsalam Abdulsomad .A. - May 24th, 2023.
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''class City'''
    name = ''
    state_id = ''
