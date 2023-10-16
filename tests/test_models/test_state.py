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


if __name__ == '__main__':
    unittest.main()
