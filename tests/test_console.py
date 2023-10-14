#!/usr/bin/python3
'''Test for console'''
import unittest
# import pep8
import os
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class TestConsole(unittest.TestCase):
    '''Test for the console'''

    def setUp(self):
        '''Set up for the test'''
        self.consol = HBNBCommand()

    def tearDown(self):
        '''Clean everything up after running setup'''
        pass

    '''
    def test_pep8_console(self):
        Test pep8 style
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8") 
    '''

    def test_docstrings_in_console(self):
        '''Test docstrings'''
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    def test_help_quit(self):
        '''Test help quit'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_help("quit")
            self.assertEqual(f.getvalue(), "Quit command to exit the program\n")

    def test_help_EOF(self):
        '''Test help EOF'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_help("EOF")
            self.assertEqual(f.getvalue(), "EOF command to exit the program\n")

    def test_help_emptyline(self):
        '''Test help emptyline'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_help("")
            self.assertEqual(f.getvalue(), "")

    def test_help_create(self):
        '''Test help create'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_help("create")
            self.assertEqual(f.getvalue(), "Creates a new instance of BaseModel\n")

    def test_help_show(self):
        '''Test help show'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_help("show")
            self.assertEqual(f.getvalue(), "Prints the string representation of an instance\n")

    def test_help_destroy(self):
        '''Test help destroy'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_help("destroy")
            self.assertEqual(f.getvalue(), "Deletes an instance based on the class name and id\n")

    def test_help_all(self):
        '''Test help all'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_help("all")
            self.assertEqual(f.getvalue(), "Prints all string representation of all instances\n")

    def test_help_update(self):
        '''Test help update'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_help("update")
            self.assertEqual(f.getvalue(), "Updates an instance based on the class name and id by adding or updating attribute\n")

    def test_create(self):
        '''Test create'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_create("")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_create_class(self):
        '''Test create class'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_create("BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

    def test_create_class_id(self):
        '''Test create class id'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_create("BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

'''to be continued'''

if __name__ == '__main__':
    unittest.main()
