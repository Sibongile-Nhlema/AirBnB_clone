#!/usr/bin/pythoni3
''' This module is for the Review class that Inherits from BaseModel '''

from models.base_model import BaseModel


class Review(BaseModel):
    '''
    Defines an instance of a place


    Public Class Attributes:
        place_id (str): The id of the place
        user_id (str): The id of the user
        name (str): The name of the place
    '''
    place_id = ""
    user_id = ""
    text = ""
