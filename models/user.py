#!/usr/bin/python3
"""class user"""
from models.base_model import BaseModel

class User(BaseModel):

    email = ""
    password = ""
    firstname = ""
    last_name = ""