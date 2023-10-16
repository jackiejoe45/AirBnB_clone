#!/usr/bin/python3
'''
Test for console
'''
import unittest
import os
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
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
            expected_output = "Quit command to exit the program\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_help_EOF(self):
        '''Test help EOF'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_help("EOF")
            expected_output = "EOF command to exit the program\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_help_emptyline(self):
        '''Test help emptyline'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_help("")
            expected_output = ""
            self.assertEqual(f.getvalue(), expected_output)

    def test_help_create(self):
        '''Test help create'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_help("create")
            expected_output = "Creates a new instance of BaseModel\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_help_show(self):
        '''Test help show'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_help("show")
            expected_output = (
                "Prints the string representation of an instance\n"
            )
            self.assertEqual(f.getvalue(), expected_output)

    def test_help_destroy(self):
        '''Test help destroy'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_help("destroy")
            expected_output = (
                "Deletes an instance based on the class name and id\n"
            )
            self.assertEqual(f.getvalue(), expected_output)

    def test_help_all(self):
        '''Test help all'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_help("all")
            expected_output = (
                "Prints all string representation of all instances\n"
            )
            self.assertEqual(f.getvalue(), expected_output)

    def test_help_update(self):
        '''Test help update'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_help("update")
            expected_output = (
                "Updates an instance based on the class name and id "
                "by adding or updating attribute\n"
            )
            self.assertEqual(f.getvalue(), expected_output)

    def test_create(self):
        '''Test create'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_create("")
            expected_output = "** class name missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

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


if __name__ == '__main__':
    unittest.main()
