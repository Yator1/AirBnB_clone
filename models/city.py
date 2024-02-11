#!/usr/bin/python3
"""A class City that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """id for state and the city name"""
    state_id = ""
    name = ""
