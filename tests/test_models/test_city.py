#!/usr/bin/python3
"""
Unittest for City
"""
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    ''' Test cases for city.py '''
    def setUp(self):
        ''' Set up '''
        self.city = City()

    def tearDown(self):
        ''' Tear down '''
        del self.city


if __name__ == '__main__':
    unittest.main()
