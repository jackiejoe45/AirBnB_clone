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

    def test_name(self):
        ''' Test name '''
        self.assertEqual(self.amenity.name, "")

    def test_created_at(self):
        ''' Test created_at '''
        self.assertEqual(type(self.amenity.created_at), datetime.datetime)

    def test_updated_at(self):
        ''' Test updated_at '''
        self.assertEqual(type(self.amenity.updated_at), datetime.datetime)

    def test_id(self):
        ''' Test id '''
        self.assertEqual(type(self.amenity.id), str)

    def test_str(self):
        ''' Test __str__ '''
        self.assertEqual(type(str(self.amenity)), str)

    def test_to_dict(self):
        ''' Test to_dict '''
        self.assertEqual(type(self.amenity.to_dict()), dict)

    def test_save(self):
        ''' Test save '''
        self.amenity.save()
        self.assertEqual(self.amenity.updated_at,
                         type(datetime.datetime.now()))


if __name__ == '__main__':
    unittest.main()
