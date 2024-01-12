#!/usr/bin/python3
'''
Defines unittests for models/engine/file_storage.py.

Unittest classes:
    - TestFileStorage_Instantiation
    - TestFileStorage_Methods
'''
import os
import json
import models
import unittest
from models.city import City
from models.user import User
from datetime import datetime
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_Instantiation(unittest.TestCase):
    ''' Unittests for testing instantiation of the FileStorage class '''
    def test_file_storage_no_args(self):
        '''Tests the FileStorage class without agruments '''
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_file_storage_arg_given(self):
        ''' Tests the FileStorage class with arguments '''
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_storage_private_str(self):
        ''' Tests the privacy of the __file_path attribute '''
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_file_storage_private_dict(self):
        ''' Tests the privacy of the __objects attribute '''
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        ''' Tests if models.storage is an instance of FileStorage '''
        self.assertEqual(type(models.storage), FileStorage)



class TestFileStorage_Methods(unittest.TestCase):
    ''' Unittests for testing methods of the FileStorage class '''

    @classmethod
    def setUpClass(cls):
        ''' Sets up everything before tests are run '''
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        ''' runs once all tests have been run '''
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        ''' Tests return type of the all method - no args'''
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        ''' Tests  return type of the all method - with args'''
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_reload_with_arg(self):
        ''' Tests  return type of the reload method - with args '''
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_save_with_arg(self):
        ''' Tests  return type of the save method - with args '''
        with self.assertRaises(TypeError):
            models.storage.save(None)
    
    def test_new_instance_id(self):
       ''' Tests if the new instance has an id '''
       base_model = BaseModel()
       user = User()
       state = State()
       place = Place()
       city = City()
       amenity = Amenity()
       review = Review()
       models.storage.new(base_model)
       models.storage.new(user)
       models.storage.new(state)
       models.storage.new(place)
       models.storage.new(city)
       models.storage.new(amenity)
       models.storage.new(review)

       self.assertIn("BaseModel." + base_model.id, models.storage.all().keys())
       self.assertIn(base_model, models.storage.all().values())

       self.assertIn("User." + user.id, models.storage.all().keys())
       self.assertIn(user, models.storage.all().values())

       self.assertIn("State." + state.id, models.storage.all().keys())
       self.assertIn(state, models.storage.all().values())

       self.assertIn("Place." + place.id, models.storage.all().keys())
       self.assertIn(place, models.storage.all().values())

       self.assertIn("City." + city.id, models.storage.all().keys())
       self.assertIn(city, models.storage.all().values())

       self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
       self.assertIn(amenity, models.storage.all().values())

       self.assertIn("Review." + review.id, models.storage.all().keys())
       self.assertIn(review, models.storage.all().values())

    def test_save(self):
        ''' tests the save method of the FileStorage class '''
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)

        models.storage.save()
        saved_text = ""
        with open("file.json", "r") as f:
            saved_text = f.read()
            self.assertIn("BaseModel." + base_model.id, saved_text)
            self.assertIn("User." + user.id, saved_text)
            self.assertIn("State." + state.id, saved_text)
            self.assertIn("Place." + place.id, saved_text)
            self.assertIn("City." + city.id, saved_text)
            self.assertIn("Amenity." + amenity.id, saved_text)
            self.assertIn("Review." + review.id, saved_text)

    def test_reload(self):
        ''' tests the reload method of the FileStorage class '''
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)

        models.storage.save()
        models.storage.reload()

        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_model.id, obj)
        self.assertIn("User." + user.id, obj)
        self.assertIn("State." + state.id, obj)
        self.assertIn("Place." + place.id, obj)
        self.assertIn("City." + city.id, obj)
        self.assertIn("Amenity." + amenity.id, obj)
        self.assertIn("Review." + review.id, obj)
