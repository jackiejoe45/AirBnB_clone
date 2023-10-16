#!/usr/bin/python3
'''
Test for console
'''
import unittest
# import os
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

    def test_all(self):
        '''Test all'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_all("")
            expected_output = "["
            self.assertEqual(f.getvalue(), expected_output)

    def test_count(self):
        '''Test count'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_count("")
            expected_output = "0\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_show(self):
        '''Test show'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_show("")
            expected_output = "** class name missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_destroy(self):
        '''Test destroy'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_destroy("")
            expected_output = "** class name missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_update(self):
        '''Test update'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_update("")
            expected_output = "** class name missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

        
    def test_create_with_class(self):
        '''Test create with class'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_create("BaseModel")
            expected_output = "["
            self.assertEqual(f.getvalue(), expected_output)

    def test_show_with_class_name(self):
        '''Test show with class name'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_show("BaseModel")
            expected_output = "** instance id missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_create_invalid_class(self):
        '''Test create with invalid class name'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_create("InvalidClassName")
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_show_invalid_class(self):
        '''Test show with invalid class name'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_show("InvalidClassName 123")
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_show_missing_id(self):
        '''Test show with missing id'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_show("BaseModel")
            expected_output = "** instance id missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_show_invalid_id(self):
        '''Test show with invalid id'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_show("BaseModel 123")
            expected_output = "** no instance found **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_destroy_invalid_class(self):
        '''Test destroy with invalid class name'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_destroy("InvalidClassName 123")
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_destroy_missing_id(self):
        '''Test destroy with missing id'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_destroy("BaseModel")
            expected_output = "** instance id missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_destroy_invalid_id(self):
        '''Test destroy with invalid id'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_destroy("BaseModel 123")
            expected_output = "** no instance found **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_all_invalid_class(self):
        '''Test all with invalid class name'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_all("InvalidClassName")
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_update_invalid_class(self):
        '''Test update with invalid class name'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_update("InvalidClassName 123")
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_update_missing_id(self):
        '''Test update with missing id'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_update("BaseModel")
            expected_output = "** instance id missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_update_invalid_id(self):
        '''Test update with invalid id'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_update("BaseModel 123")
            expected_output = "** no instance found **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_update_missing_attr_name(self):
        '''Test update with missing attribute name'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_update("BaseModel 123")
            expected_output = "** attribute name missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_update_missing_value(self):
        '''Test update with missing value'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_update("BaseModel 123 attr_name")
            expected_output = "** value missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_create_invalid_class(self):
        '''Test create with invalid class name'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_create("InvalidClass")
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_show_invalid_class(self):
        '''Test show with invalid class name'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_show("InvalidClass 123")
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_show_missing_id(self):
        '''Test show with missing id'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_show("BaseModel")
            expected_output = "** instance id missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_show_invalid_id(self):
        '''Test show with invalid id'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_show("BaseModel 123")
            expected_output = "** no instance found **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_destroy_invalid_class(self):
        '''Test destroy with invalid class name'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_destroy("InvalidClass 123")
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_destroy_missing_id(self):
        '''Test destroy with missing id'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_destroy("BaseModel")
            expected_output = "** instance id missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_destroy_invalid_id(self):
        '''Test destroy with invalid id'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_destroy("BaseModel 123")
            expected_output = "** no instance found **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_all_invalid_class(self):
        '''Test all with invalid class name'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_all("InvalidClass")
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_update_invalid_class(self):
        '''Test update with invalid class name'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_update("InvalidClass 123")
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_update_missing_id(self):
        '''Test update with missing id'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_update("BaseModel")
            expected_output = "** instance id missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_update_invalid_id(self):
        '''Test update with invalid id'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_update("BaseModel 123")
            expected_output = "** no instance found **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_update_missing_attr_name(self):
        '''Test update with missing attribute name'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_update("BaseModel 123")
            expected_output = "** attribute name missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_update_missing_value(self):
        '''Test update with missing value'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.do_update("BaseModel 123 attr_name")
            expected_output = "** value missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

    
if __name__ == '__main__':
    unittest.main()
