#!/usr/bin/python3
"""
Unittest for review.py
"""
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    ''' Test cases for review.py '''

    def setUp(self):
        ''' Set up '''
        self.review = Review()

    def tearDown(self):
        ''' Tear down '''
        del self.review

    def test_place_id(self):
        ''' Test place_id '''
        self.assertEqual(self.review.place_id, "")

    def test_user_id(self):
        ''' Test user_id '''
        self.assertEqual(self.review.user_id, "")

    def test_text(self):
        ''' Test text '''
        self.assertEqual(self.review.text, "")

    def test_created_at(self):
        ''' Test created_at '''
        self.assertEqual(type(self.review.created_at), datetime.datetime)

    def test_updated_at(self):
        ''' Test updated_at '''
        self.assertEqual(type(self.review.updated_at), datetime.datetime)

    def test_id(self):
        ''' Test id '''
        self.assertEqual(type(self.review.id), str)

    def test_str(self):
        ''' Test __str__ '''
        self.assertEqual(type(str(self.review)), str)

    def test_to_dict(self):
        ''' Test to_dict '''
        self.assertEqual(type(self.review.to_dict()), dict)

    def test_save(self):
        ''' Test save '''
        self.review.save()
        self.assertEqual(self.review.updated_at, type(datetime.datetime.now()))


if __name__ == '__main__':
    unittest.main()
