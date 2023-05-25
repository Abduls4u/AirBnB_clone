#!/usr/bin/python3
''' A module that contains the class Place that inherits from BaseModel
Usage:
    ./state.py
Author:
    Abdulsalam Abdulsomad .A. - May 24th, 2023.
'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''class Place'''
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids  = []
