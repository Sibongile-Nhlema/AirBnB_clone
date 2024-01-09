#!/usr/bin/pythoni3
''' This module is for the State class that Inherits from BaseModel '''

from models.base_model import BaseModel


class State(BaseModel):
    '''
    Defines an instance of a State

    Public Class Attributes:
        name (str): The name of the state
    '''
    name = ""
