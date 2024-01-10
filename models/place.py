#!/usr/bin/pythoni3
''' This module is for the Place class that Inherits from BaseModel '''

from models.base_model import BaseModel


class Place(BaseModel):
    '''
    Defines an instance of a place

    Public Class Attributes:
        city_id (str): The id of the city
        user_id (str): The id of the user
        name (str): The name of the place
        description (str): Details about the place
        number_rooms (int): Number of rooms in the place
        number_bathrooms (int): Number of bathrooms in the place
        max_guest (int): Maximum number of people allowed in the place
        price_by_night (int): cost of place per night
        latitude (float): Latitude coordinate of the place
        longitude (float): Longitude coordinate of the place
        amenity_ids (list): List of amenity ids associated with the place
    '''
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
