#!/usr/bin/pythoni3
''' This module is for the City class that Inherits from BaseModel '''

from models.base_model import BaseModel


class City(BaseModel):
    '''
    Defines an instance of a City

    Public Class Attributes:
        name (str): The name of the state
        state_id (str): The id of a particular State
    '''
    name = ""
    state_id = ""
