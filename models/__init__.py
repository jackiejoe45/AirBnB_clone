#!/usr/bin/python3
'''Module that defines a unique FileStorage instance'''
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
