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

        if __name__ == '__main__':
            unittest.main()
