#!/usr/bin/python3
"""
Tests the Place class.

Unittest classes:
TestPlace
TestDocumentation
TestPlace_1
TestPlace_1_args
TestPlace_1_Public_Attributes
TestPlace_1_created_at
TestPlace_1_updated_at
TestPlace_1_Public_Methods
TestPlace_1_save
"""

import unittest
from models.place import Place
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
from time import sleep
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Tests the Place class."""

    def setUp(self):
        """Does nothing"""
        pass

    def tearDown(self):
        """Resets storage."""

        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_place_type(self):
        """Tests the type of place class."""

        place = Place()
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")

    def test_place_instance(self):
        """Tests if a place object is an instance of Place."""

        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_superclass(self):
        """Tests if place is a subclass of BaseModel."""

        place = Place()
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_place_attributes(self):
        """Tests attributes of Place class."""

        attributes = {
            'city_id': str,
            'user_id': str,
            'name': str,
            'description': str,
            'number_rooms': int,
            'number_bathrooms': int,
            'max_guest': int,
            'price_by_night': int,
            'latitude': float,
            'longitude': float,
            'amenity_ids': list
        }
        place = Place()

        for key, value in attributes.items():
            self.assertTrue(hasattr(place, key))
            self.assertEqual(type(getattr(place, key, None)), value)


class TestDocumentation(unittest.TestCase):
    """Tests for existence of docstrings"""

    def test_documentation(self):
        """Tests if the module, the class,
        and the methods are documented"""

        from models import city

        self.assertIsNotNone(place.__doc__)
        self.assertIsNotNone(Place.__doc__)


class TestPlace_1(unittest.TestCase):
    '''
    Unittests for all cases for the Place class
    '''
    def test_instance(self):
        self.assertTrue(isinstance(Place().id, str))

    def test_type(self):
        self.assertEqual(str, type(Place().id))

    def test_uuid(self):
        place_1 = Place()
        base_model_2 = Place()
        self.assertNotEqual(place_1.id, base_model_2.id)


class TestPlace_1_args(unittest.TestCase):
    '''
    Unittests for the different arguments made to Place
    '''
    def test_init_kwargs(self):
        base_model = Place(name='Plankton', age=32)
        # Test whether the attributes were updated correctly
        self.assertEqual(base_model.name, 'Plankton')
        self.assertEqual(base_model.age, 32)

    def test_none_arg(self):
        place_1 = Place(None)
        self.assertNotIn(None, place_1.__dict__.values())

    def test_kwargs_with_none_as_value(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_args_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        base_model = Place("Sandy", "Spongebob", "Gary", id="123",
                           created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(base_model.id, "123")
        self.assertEqual(base_model.created_at, dt)
        self.assertEqual(base_model.updated_at, dt)


class TestPlace_1_Public_Attributes(unittest.TestCase):
    '''
    Unittests for implementation of the public attributes of Place class
    '''
    def test_created_at_instance(self):
        base_model = Place()
        self.assertIsInstance(base_model.created_at, datetime)

    def test_updated_at_instance(self):
        base_model = Place()
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_str_method_instance(self):
        base_model = Place()
        expected_str = "[Place] ({}) {}".format(base_model.id,
                                                base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)


class TestPlace_1_created_at(unittest.TestCase):
    '''
    Unittests for the additional cases of the created_at attribute
    '''
    def test_created_at_of_two_ids(self):
        place_1 = Place()
        sleep(0.02)
        base_model_2 = Place()
        self.assertNotEqual(place_1.created_at, base_model_2.created_at)


class TestPlace_1_updated_at(unittest.TestCase):
    '''
    Unittests for the additional cases of the updated_at attribute
    '''
    def test_updated_at_of_one_id(self):
        place_1 = Place()
        sleep(0.02)
        place_1 = Place()
        self.assertNotEqual(place_1.created_at, place_1.updated_at)

    def test_updated_at_of_two_ids(self):
        place_1 = Place()
        sleep(0.02)
        base_model_2 = Place()
        self.assertNotEqual(place_1.updated_at, base_model_2.updated_at)


class TestPlace_1_Public_Methods(unittest.TestCase):
    '''
    Unittests for the implementation of the public methods of the Place class
    '''
    def test_save_method(self):
        base_model = Place()
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(base_model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        base_model = Place()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('__class__', base_model_dict)
        self.assertEqual(base_model_dict['__class__'], 'Place')
        self.assertIn('created_at', base_model_dict)
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIn('updated_at', base_model_dict)
        self.assertIsInstance(base_model_dict['updated_at'], str)


class TestPlace_1_save(unittest.TestCase):
    '''
    Unittests for the implementation of the save method in Place
    '''
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_once(self):
        # recieved error when implemented??
        place_1 = Place()
        sleep(0.02)
        first_updated_at = place_1.updated_at
        place_1.save()
        self.assertLess(first_updated_at, place_1.updated_at)

    def test_save_twice(self):
        place_1 = Place()
        sleep(0.02)
        first_updated_at = place_1.updated_at
        place_1.save()
        second_updated_at = place_1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.02)
        place_1.save()
        self.assertLess(second_updated_at, place_1.updated_at)

    def test_save_None(self):
        place_1 = Place()
        with self.assertRaises(TypeError):
            place_1.save(None)


class TestPlace_1_to_dict(unittest.TestCase):
    '''
    Unittests for the implementation of the to_dict method in Place
    '''
    def test_to_dict_type(self):
        base_model = Place()
        self.assertEqual(dict, type(base_model.to_dict()))

    def test_to_dict_keys(self):
        base_model = Place()
        test_d = base_model.to_dict()
        self.assertIn("id", test_d)
        self.assertIn("__class__", test_d)
        self.assertIn("created_at", test_d)
        self.assertIn("updated_at", test_d)

    def test_to_dict_values(self):
        base_model = Place()
        base_model.name = "Mr Crabs"
        base_model.his_number = 45
        self.assertIn("name", base_model.to_dict())
        self.assertIn("his_number", base_model.to_dict())

    def test_to_dict_results(self):
        dt = datetime.today()
        base_model = Place()
        base_model.id = "120964"
        base_model.created_at = base_model.updated_at = dt
        rdict = {
                'id': '120964',
                '__class__': 'Place',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat()
                }
        self.assertDictEqual(base_model.to_dict(), rdict)

    def test_to_dict_None(self):
        base_model = Place()
        with self.assertRaises(TypeError):
            base_model.to_dict(None)


class TestPlace_1_Storage(unittest.TestCase):
    '''
    Unittests related to storing data
    '''
    def test__new_instance_stored(self):
        self.assertIn(Place(), models.storage.all().values())


if __name__ == '__main__':
    unittest.main()
