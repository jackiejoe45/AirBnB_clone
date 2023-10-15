#!/usr/bin/python3
'''Module that defines a User class'''

from models.base_model import BaseModel

class User(BaseModel):
    '''User class that inherits from BaseModel'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
