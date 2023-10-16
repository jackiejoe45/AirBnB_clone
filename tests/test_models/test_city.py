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

    def test_name(self):
        ''' Test name '''
        self.assertEqual(self.city.name, "")

    def test_state_id(self):
        ''' Test state_id '''
        self.assertEqual(self.city.state_id, "")

    def test_created_at(self):
        ''' Test created_at '''
        self.assertEqual(type(self.city.created_at), datetime.datetime)

    def test_updated_at(self):
        ''' Test updated_at '''
        self.assertEqual(type(self.city.updated_at), datetime.datetime)

    def test_id(self):
        ''' Test id '''
        self.assertEqual(type(self.city.id), str)

    def test_str(self):
        ''' Test __str__ '''
        self.assertEqual(type(str(self.city)), str)

    def test_to_dict(self):
        ''' Test to_dict '''
        self.assertEqual(type(self.city.to_dict()), dict)

    def test_save(self):
        ''' Test save '''
        self.city.save()
        self.assertEqual(self.city.updated_at, type(datetime.datetime.now()))


if __name__ == '__main__':
    unittest.main()
