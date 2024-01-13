#!/usr/bin/pythoni3
''' This module is for the Amenity class that Inherits from BaseModel '''

from models.base_model import BaseModel


class Amenity(BaseModel):
    '''
    Defines an instance of a Amenity

    Public Class Attributes:
        name (str): The name of the amenity
    '''
    name = ""
