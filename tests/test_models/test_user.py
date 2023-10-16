#!/usr/bin/python3
"""
Unittest for user.py
"""
import unittest
from models.user import User
import datetime


class UserCase(unittest.TestCase):
    ''' Test cases for user.py '''
    def setUp(self):
        ''' Set up '''
        self.user = User()

    def tearDown(self):
        ''' Tear down '''
        del self.user

    def test_init(self):
        ''' Test init '''
        self.assertTrue(isinstance(self.user, User))

    def test_uuid(self):
        ''' Test uuid '''
        user1 = User()
        user2 = User()
        self.assertTrue(hasattr(user1, "id"))
        self.assertNotEqual(user1, user2)

    def test_created_at(self):
        ''' Test created_at '''
        self.assertTrue(hasattr(self.user, "created_at"))

    def test_updated_at(self):
        ''' Test updated_at '''
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_email(self):
        ''' Test email '''
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "")

    def test_password(self):
        ''' Test password '''
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")

    def test_first_name(self):
        ''' Test first_name '''
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")

    def test_last_name(self):
        ''' Test last_name '''
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")


if __name__ == "__main__":
    unittest.main()
