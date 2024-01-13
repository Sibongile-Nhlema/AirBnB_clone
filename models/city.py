#!/usr/bin/python3
"""
This module contains the class City that defines a city.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines a city.

    Public Class Attributes:
    - state_id (str): State.id
    - name (str): The name of a city
    """

    state_id = ""
    name = ""
