#!/usr/bin/python3
""" Test File Storage """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class FileStorageTests(unittest.TestCase):
    """ Suite of File Storage Tests """

    def setUp(self):
        """ Sets up test methods """
        self.storage = FileStorage()

    def tearDown(self):
        """ Tears down test methods """
        os.remove("file.json")

    def test_all(self):
        """ Tests all method """
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        """ Tests new method """
        self.storage.new(BaseModel())
        self.assertEqual(len(self.storage.all()), 1)

    def test_save(self):
        """ Tests save method """
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):

        self.storage.save()
        self.storage.reload()
        self.assertEqual(type(self.storage.all()), dict)

    def test_file_path(self):

        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_file_path_exists(self):

        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))

    def test_objects_exists(self):

        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))

    def test_all(self):

        self.assertEqual(type(self.storage.all()), dict)

    def test_init(self):

        self.assertTrue(isinstance(self.storage, FileStorage))


if __name__ == "__main__":
    unittest.main()
