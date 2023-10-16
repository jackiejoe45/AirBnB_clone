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

    def test_kwargs(self):
        '''Test kwargs'''
        base1 = BaseModel()
        base1.name = "Holberton"
        base1.my_number = 89
        base1.save()
        base1_json = base1.to_dict()
        base2 = BaseModel(**base1_json)
        self.assertEqual(base1.id, base2.id)
        self.assertEqual(base1.created_at, base2.created_at)
        self.assertEqual(base1.updated_at, base2.updated_at)
        self.assertEqual(base1.name, base2.name)
        self.assertEqual(base1.my_number, base2.my_number)
        self.assertNotEqual(base1, base2)

    def test_kwargs_empty(self):
        '''Test kwargs empty'''
        base1 = BaseModel()
        base1.name = "Holberton"
        base1.my_number = 89
        base1.save()
        base1_json = base1.to_dict()
        base2 = BaseModel()
        base2.__dict__ = base1_json
        self.assertEqual(base1.id, base2.id)
        self.assertEqual(base1.created_at, base2.created_at)
        self.assertEqual(base1.updated_at, base2.updated_at)
        self.assertEqual(base1.name, base2.name)
        self.assertEqual(base1.my_number, base2.my_number)
        self.assertNotEqual(base1, base2)


if __name__ == '__main__':
    unittest.main()
