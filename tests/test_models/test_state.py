#!/usr/bin/python3
"""
Unittest for State
"""
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    ''' Test cases for state.py '''
    def setUp(self):
        ''' Set up '''
        self.state = State()

    def tearDown(self):
        ''' Tear down '''
        del self.state

    def test_name(self):
        ''' Test name '''
        self.assertEqual(self.state.name, "")

    def test_created_at(self):
        ''' Test created_at '''
        self.assertEqual(type(self.state.created_at), datetime.datetime)

    def test_updated_at(self):
        ''' Test updated_at '''
        self.assertEqual(type(self.state.updated_at), datetime.datetime)

    def test_id(self):
        ''' Test id '''
        self.assertEqual(type(self.state.id), str)

    def test_str(self):
        ''' Test __str__ '''
        self.assertEqual(type(str(self.state)), str)

    def test_to_dict(self):
        ''' Test to_dict '''
        self.assertEqual(type(self.state.to_dict()), dict)

    def test_save(self):
        ''' Test save '''
        self.state.save()
        self.assertEqual(self.state.updated_at, type(datetime.datetime.now()))


if __name__ == '__main__':
    unittest.main()
