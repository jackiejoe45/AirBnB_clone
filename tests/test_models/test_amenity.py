#!/usr/bin/python3
"""
Unittest for Amenity
"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    ''' Test cases for amenity.py '''

    def setUp(self):
        ''' Set up '''
        self.amenity = Amenity()

    def tearDown(self):
        ''' Tear down '''
        del self.amenity


if __name__ == '__main__':
    unittest.main()
