#!/usr/bin/python3
""" A class Review that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Information for the reviews"""
    place_id = ""
    user_id = ""
    text = ""
