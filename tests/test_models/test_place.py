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

    def test_city_id(self):
        ''' Test city_id '''
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        ''' Test user_id '''
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        ''' Test name '''
        self.assertEqual(self.place.name, "")

    def test_description(self):
        ''' Test description '''
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        ''' Test number_rooms '''
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        ''' Test number_bathrooms '''
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        ''' Test max_guest '''
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        ''' Test price_by_night '''
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        ''' Test latitude '''
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        ''' Test longitude '''
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        ''' Test amenity_ids '''
        self.assertEqual(self.place.amenity_ids, [])

    def test_created_at(self):
        ''' Test created_at '''
        self.assertEqual(type(self.place.created_at), datetime.datetime)

    def test_updated_at(self):
        ''' Test updated_at '''
        self.assertEqual(type(self.place.updated_at), datetime.datetime)

    def test_id(self):
        ''' Test id '''
        self.assertEqual(type(self.place.id), str)

    def test_str(self):
        ''' Test __str__ '''
        self.assertEqual(type(str(self.place)), str)

    def test_to_dict(self):
        ''' Test to_dict '''
        self.assertEqual(type(self.place.to_dict()), dict)

    def test_save(self):
        ''' Test save '''
        self.place.save()
        self.assertEqual(self.place.updated_at, type(datetime.datetime.now()))


if __name__ == '__main__':
    unittest.main()
