#!/usr/bin/python3
'''
Unittests for the console

    Test Classes:
        TestHBNBCommand
        TestHBNBCommand_help
        TestHBNBCommand_create
        TestHBNBCommand_update
        TestHBNBCommand_destory
        TestHBNBCommand_exit
        TestHBNBCommand_emptyline
        TestHBNBCommand_prompt
'''


import os
import sys
import unittest
from io import StringIO
from models import storage
from unittest.mock import patch
from console import HBNBCommand
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestHBNBCommand_create(unittest.TestCase):
    ''' Tests the create method '''
    @classmethod
    def setUp(self):
        ''' Initialize necessary objects before each test '''
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        ''' Clean up after each test '''
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        storage.reload()

    def test_create_class_name_missing(self):
        ''' Tests the instance of a missing class '''
        response = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(response, output.getvalue().strip())

    def test_create_class_name_nonexistant(self):
        ''' Tests the instance of a nonexistant class '''
        response = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Townsville"))
            self.assertEqual(response, output.getvalue().strip())


class TestHBNBCommand_update(unittest.TestCase):
    ''' Tests the update method '''
    @classmethod
    def setUp(self):
        ''' Initialize necessary objects before each test '''
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        ''' Clean up after each test '''
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        storage.reload()

    def test_update_class_name_missing(self):
        ''' Tests the instance of a missing class '''
        response = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(response, output.getvalue().strip())

    def test_update_class_name_nonexistant(self):
        ''' Tests the instance of a nonexistant class '''
        response = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Townsville"))
            self.assertEqual(response, output.getvalue().strip())

    def test_update_no_id_(self):
        ''' Tests the instance of a missing id'''
        response = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review"))
            self.assertEqual(response, output.getvalue().strip())

    def test_update_id_not_found(self):
        ''' Tests the instance of no instance found '''
        response = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 1234"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User 1234"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State 1234"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City 1234"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity 1234"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place 1234"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review 1234"))
            self.assertEqual(response, output.getvalue().strip())


class TestHBNBCommand_destroy_updated(unittest.TestCase):
    ''' Tests the dot notation of the destroy method '''
    @classmethod
    def setUp(self):
        ''' Initialize necessary objects before each test '''
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        ''' Clean up after each test '''
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        storage.reload()

    def test_destroy_class_name_missing(self):
        ''' Tests the instance of a missing class '''
        response = "*** Unknown syntax: .destroy()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            self.assertEqual(response, output.getvalue().strip())

    def test_destroy_class_name_nonexistant(self):
        ''' Tests the instance of a nonexistant class '''
        response = "*** Unknown syntax: Townsville.destroy()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Townsville.destroy()"))
            self.assertEqual(response, output.getvalue().strip())

    def test_destroy_no_id_(self):
        ''' Tests the instance of a missing id'''
        response = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy()"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy()"))
            self.assertEqual(response, output.getvalue().strip())

    def test_destroy_id_not_found(self):
        ''' Tests the instance of no instance found '''
        response = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1234)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy(1234)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy(1234)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
             self.assertFalse(HBNBCommand().onecmd("dCity.destroy(1234)"))
             self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy(1234)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy(1234)"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy(1234)"))
            self.assertEqual(response, output.getvalue().strip())


class TestHBNBCommand_destory(unittest.TestCase):
    ''' Tests the destory method '''
    @classmethod
    def setUp(self):
        ''' Initialize necessary objects before each test '''
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        ''' Clean up after each test '''
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        storage.reload()
    
    def test_destroy_class_name_missing(self):
        ''' Tests the instance of a missing class '''
        response = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(response, output.getvalue().strip())

    def test_destroy_class_name_nonexistant(self):
        ''' Tests the instance of a nonexistant class '''
        response = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Townsville"))
            self.assertEqual(response, output.getvalue().strip())

    def test_destroy_no_id_(self):
        ''' Tests the instance of a missing id'''
        response = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(response, output.getvalue().strip())

    def test_destroy_id_not_found(self):
        ''' Tests the instance of no instance found '''
        response = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1234"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User 1234"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State 1234"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City 1234"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity 1234"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place 1234"))
            self.assertEqual(response, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review 1234"))
            self.assertEqual(response, output.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    ''' Tests if the program exits correctly '''

    @classmethod
    def setUp(self):
        ''' Initialize necessary objects before each test '''
        self.console_output = StringIO()

    @classmethod
    def tearDown(self):
        ''' Clean up after each test '''
        self.console_output.close()

    def test_quit(self):
        ''' Tests if the console exits when quit is called '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        self.assertEqual(self.console_output.getvalue(), "")

    def test_eof(self):
        ''' Tests if the console exits when eof is called '''
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        self.assertEqual(self.console_output.getvalue(), "")

    def test_invalid_input(self):
        ''' Tests if the console return an error if input is unknown '''
        with patch("sys.stdout", new=self.console_output):
            HBNBCommand().onecmd("invalid_command")
        self.assertEqual(self.console_output.getvalue(), "*** Unknown syntax: invalid_command\n")



class TestHBNBCommand_emptyline(unittest.TestCase):
    ''' Tests that the emptyline does nothing '''
    def test_emptyline(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())


class TestHBNBCommand_prompt(unittest.TestCase):
    ''' Unittest for the prompt  '''
    def test_prompt(self):
        ''' Tests that the prompt is (hbnb) '''
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


if __name__ == '__main__':
    unittest.main()
