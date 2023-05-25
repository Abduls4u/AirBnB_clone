#!/usr/bin/python3
''' A module that contains the class Review that inherits from BaseModel
Usage:
    ./review.py
Author:
    Abdulsalam Abdulsomad .A. - May 24th, 2023.
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''class Review'''

    place_id = ''
    user_id = ''
    text = ''
