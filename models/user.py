#!/usr/bin/pythoni3
''' This module is for the User class that Inherits from BaseModel '''

from models.base_model import BaseModel


class User(BaseModel):
    '''
    Defines an instance of a user


    Public Class Attributes:
        email (str): The email of the user
        password (str): The password of the user
        first_name (str): The first name of the user
        last_name (str): The surname name of the user
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
