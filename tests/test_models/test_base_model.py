#!/usr/bin/python3
'''
Unittest for BaseModel class
'''
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''
    Test cases for BaseModel class
    '''

    def setUp(self):
        '''Set up'''
        self.base = BaseModel()

    def tearDown(self):
        '''Tear down'''
        del self.base

    def test_init(self):
        '''Test init'''
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_uuid(self):
        '''Test uuid'''
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertTrue(hasattr(base1, "id"))
        self.assertNotEqual(base1, base2)

    def test_created_at(self):
        '''Test created_at'''
        self.assertTrue(hasattr(self.base, "created_at"))

    def test_updated_at(self):
        '''Test updated_at'''
        self.assertTrue(hasattr(self.base, "updated_at"))

    def test_str(self):
        '''Test __str__'''
        expected_str = "[BaseModel] ({}) {}".format(
            self.base.id, self.base.__dict__
        )
        self.assertEqual(str(self.base), expected_str)

    def test_save(self):
        '''Test save'''
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict(self):
        '''Test to_dict'''
        self.assertEqual(type(self.base.to_dict()), dict)
        self.assertTrue('to_dict' in dir(self.base))

    def test_save(self):
        '''Test save'''
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict(self):
        '''Test to_dict'''
        self.assertEqual(type(self.base.to_dict()), dict)
        self.assertTrue('to_dict' in dir(self.base))


if __name__ == '__main__':
    unittest.main()
