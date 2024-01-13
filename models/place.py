#!/usr/bin/python3
"""
This module contains the class Place that defines a place.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Defines a place.

    Public Class Attributes:
    - city_id (str): City.id
    - user_id (str): User.id
    - name (str): The name of a place
    - description (str): The description of a place
    - number_rooms (int): The number of rooms in a place
    - number_bathrooms (int): The number of bathrooms in a place
    - max_guest (int): The maximum number of guests
    - price_by_night (int): The price per night
    - latitude (float): The latitude of the place
    - longitude (float): The longitude of the place
    - amenity_ids (list): A list of Amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
