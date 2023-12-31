#!/usr/bin/python3
'''
Module that defines a FileStorage class
'''
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    '''
    FileStorage class to manage serialization and deserialization of objects
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''Sets in __objects the obj with key <obj class name>.id'''
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file (path: __file_path)'''
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        '''
        Deserializes the JSON file to __objects (if the JSON file exists)
        '''
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path,
                      mode="r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj

    def delete(self, obj=None):
        '''Deletes obj from __objects if it’s inside'''
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects.pop(key, None)

    def close(self):
        '''Calls reload() method for deserializing the JSON file to objects'''
        self.reload()

    def get(self, cls, id):
        '''Returns the object based on the class name and its ID'''
        if cls and id:
            key = "{}.{}".format(cls.__name__, id)
            return FileStorage.__objects.get(key)

    def count(self, cls=None):
        '''Returns the number of objects in storage'''
        if cls:
            return sum(1 for key in FileStorage.__objects
                       if cls.__name__ in key)
        else:
            return len(FileStorage.__objects)
