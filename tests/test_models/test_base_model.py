#!/usr/bin/python3
"""
This module is for testing base_model module.

Classes:
- TestBaseModel
- TestStr
- TestSave
- TestToDict
"""

from models.base_model import BaseModel
import unittest
from datetime import datetime
from time import sleep
from uuid import uuid4
import re


class TestBaseModel(unittest.TestCase):
    """Tests BaseModel class and its attributes"""

    def test_object_type(self):
        """Tests the type of object"""

        model = BaseModel()

        self.assertEqual(str(type(model)),
                         "<class 'models.base_model.BaseModel'>")

    def test_object_is_subclass(self):
        """Tests if object is a subclass"""

        model = BaseModel()

        self.assertTrue(issubclass(type(model), BaseModel))

    def test_no_args(self):
        """Tests calling BaseModels's __init__ method with no arguments"""

        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()

        self.assertEqual(
            str(e.exception),
            "__init__() missing 1 required positional argument: 'self'"
        )

    def test_id_uniqueness_two_obj(self):
        """Tests if ids of different objects are different"""

        model_one = BaseModel()
        model_two = BaseModel()

        self.assertNotEqual(model_one.id, model_two.id)

    def test_id_uniqueness_many_obj(self):
        """Tests if ids of different objects are different"""

        ids = [BaseModel().id for i in range(5000)]

        self.assertEqual(len(ids), len(set(ids)))

    def test_id_presence(self):
        """Tests if each created object has an id"""

        model = BaseModel()

        self.assertTrue(hasattr(model, 'id'))

    def test_id_format(self):
        """Tests if id is a string"""

        model = BaseModel()

        self.assertIsInstance(model.id, str)

    def test_is_instance(self):
        """Tests if an object is an instance of the class"""

        model = BaseModel()

        self.assertIsInstance(model, BaseModel)

    def test_created_at_type(self):
        """Tests if created_at is an instance of datetime"""

        model = BaseModel()

        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_type(self):
        """Tests if updated_at is an instance of datetime"""

        model = BaseModel()

        self.assertIsInstance(model.updated_at, datetime)

    def test_created_at_init(self):
        """Tests if created_at is initialized with the current time"""

        current_time = datetime.now()
        model = BaseModel()

        time_difference = model.created_at - current_time
        self.assertTrue(abs(time_difference.total_seconds()) < 0.01)

    def test_updated_at_init(self):
        """
        Tests if updated_at is the same
        as created_at after initialization
        """

        model = BaseModel()

        time_difference = model.updated_at - model.created_at
        self.assertTrue(abs(time_difference.total_seconds()) < 0.01)

    def test_kwargs_recreate_obj(self):
        """Tests passing kwargs in instantiation to recreate an object"""

        model_one = BaseModel()
        model_one.first_name = 'Mohamed'
        model_one.last_name = 'Ali'
        model_one_dict = model_one.to_dict()

        model_two = BaseModel(**model_one_dict)

        self.assertEqual(model_one_dict, model_two.to_dict())

    def test_pass_dict_as_kwargs(self):
        """Tests creating an object with an existing dictionary"""

        dict = {
            'id': uuid4(),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'first_name': 'Mohamed',
            'age': 30,
            'height': 173.5,
            '__class__': 'BaseModel'
        }

        model = BaseModel(**dict)

        self.assertEqual(model.to_dict(), dict)


class TestStr(unittest.TestCase):
    """Tests the __str__ method"""

    def test_str(self):
        """Tests the __str__ method"""

        model = BaseModel()
        model_str = str(model)
        regex_match = re.match(r"^\[(.*)\] \((.*)\) (.*)$", model_str)

        self.assertIsNotNone(regex_match)
        self.assertEqual(regex_match.group(1), 'BaseModel')
        self.assertEqual(regex_match.group(2), model.id)


class TestSave(unittest.TestCase):
    """Tests the save method"""

    def test_save(self):
        """Tests if updated_at gets updated when save is called"""

        model = BaseModel()
        sleep(1)
        time_then = datetime.now()
        model.save()
        updated_now = model.updated_at

        time_difference = updated_now - time_then
        self.assertTrue(abs(time_difference.total_seconds()) < 0.01)

    def test_save_without_obj(self):
        """Tests using save without an object"""

        with self.assertRaises(TypeError) as e:
            BaseModel.save()

        self.assertEqual(
            str(e.exception),
            "save() missing 1 required positional argument: 'self'"
        )

    def test_save_excess_args(self):
        """Tests using save with excess arguments"""

        model = BaseModel()

        with self.assertRaises(TypeError) as e:
            model.save('Hi')

        self.assertEqual(
            str(e.exception),
            "save() takes 1 positional argument but 2 were given"
        )


class testToDict(unittest.TestCase):
    """Tests the to_dict method"""

    def test_class_key(self):
        """Tests if the returned dict contains __class__ key"""

        model = BaseModel()
        dict = model.to_dict()

        self.assertTrue(dict['__class__'])

    def test_to_dict(self):
        """Tests if to_dict returns a correct dict"""

        model = BaseModel()
        dict = model.to_dict()

        self.assertEqual(
            dict, {'__class__': 'BaseModel',
                   'updated_at': dict['updated_at'],
                   'id': model.id, 'created_at': dict['created_at']}
                                )

    def test_to_dict_created_at_type(self):
        """Tests if created_at's value in the dict is a string"""

        model = BaseModel()
        dict = model.to_dict()

        self.assertIsInstance(dict['created_at'], str)

    def test_to_dict_updated_at_type(self):
        """Tests if updated_at's value in the dict is a string"""

        model = BaseModel()
        dict = model.to_dict()

        self.assertIsInstance(dict['updated_at'], str)

    def test_to_dict_after_setting_attr(self):
        """Sets attributes and tests if to_dict produces an updated dict"""

        model = BaseModel()
        model.first_name = 'Mohamed'
        model.last_name = 'Ali'
        dict = model.to_dict()

        self.assertEqual(dict['first_name'], model.first_name)
        self.assertEqual(dict['last_name'], model.last_name)
        self.assertEqual(dict["id"], model.id)
        self.assertEqual(dict["__class__"], type(model).__name__)
        self.assertEqual(dict["created_at"], model.created_at.isoformat())
        self.assertEqual(dict["updated_at"], model.updated_at.isoformat())

    def test_to_dict_without_obj(self):
        """Tests using to_dict without an object"""

        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()

        self.assertEqual(
            str(e.exception),
            "to_dict() missing 1 required positional argument: 'self'"
        )

    def test_to_dict_excess_args(self):
        """Tests using to_dict with additional arguments"""

        model = BaseModel()

        with self.assertRaises(TypeError) as e:
            model.to_dict('Hi')

        self.assertEqual(
            str(e.exception),
            "to_dict() takes 1 positional argument but 2 were given"
        )


class TestDocumentation(unittest.TestCase):
    """Tests for existence of docstrings"""

    def test_documentation(self):
        """Tests if the module, the class,
        and the methods are documented"""

        from models import base_model

        self.assertIsNotNone(base_model.__doc__)
        self.assertIsNotNone(base_model.BaseModel.__doc__)
        self.assertIsNotNone(base_model.BaseModel.__init__)
        self.assertIsNotNone(base_model.BaseModel.__str__)
        self.assertIsNotNone(base_model.BaseModel.save)
        self.assertIsNotNone(base_model.BaseModel.to_dict)


if __name__ == '__main__':
    unittest.main()
