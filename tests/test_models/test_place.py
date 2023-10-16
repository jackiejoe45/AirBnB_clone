#!/usr/bin/python3
"""
Unittest for Place
"""
import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    ''' Test cases for place.py '''

    def setUp(self):
        ''' Set up '''
        self.place = Place()

    def tearDown(self):
        ''' Tear down '''
        del self.place


if __name__ == '__main__':
    unittest.main()
