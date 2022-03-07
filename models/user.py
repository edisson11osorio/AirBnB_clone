#!/usr/bin/python3
"""Define a model user"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class to handle a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
