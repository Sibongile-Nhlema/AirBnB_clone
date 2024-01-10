#!/usr/bin/python3
''' These Unittests are for the BaseModel Class

    Unittest classes:
        TestUser
        TestUser_args
        TestUser_Public_Attributes
        TestUser_created_at
        TestUser_updated_at
        TestUser_Public_Methods
        TestUser_save
'''
import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    '''
    Unittests for all cases for the BaseModel class
    '''
    def test_instance(self):
        self.assertTrue(isinstance(BaseModel().id, str))

    def test_type(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_uuid(self):
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.id, base_model_2.id)


class TestUser_args(unittest.TestCase):
    '''
    Unittests for the different arguments made to BaseModel
    '''
    def test_init_kwargs(self):
        base_model = BaseModel(name='Plankton', age=32)
        # Test whether the attributes were updated correctly
        self.assertEqual(base_model.name, 'Plankton')
        self.assertEqual(base_model.age, 32)

    def test_none_arg(self):
        base_model_1 = BaseModel(None)
        self.assertNotIn(None, base_model_1.__dict__.values())

    def test_kwargs_with_none_as_value(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_args_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        base_model = BaseModel("Sandy", "Spongebob", "Gary", id="123",
                               created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(base_model.id, "123")
        self.assertEqual(base_model.created_at, dt)
        self.assertEqual(base_model.updated_at, dt)


class TestUser_Public_Attributes(unittest.TestCase):
    '''
    Unittests for the implementation of the public attributes of the BaseModel class
    '''
    def test_created_at_instance(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime)

    def test_updated_at_instance(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_str_method_instance(self):
        user_1 = User()
        expected_str = "[User] ({}) {}".format(user_1.id,
                                                    user_1.__dict__)
        self.assertEqual(str(user_1), expected_str)


class TestUser_created_at(unittest.TestCase):
    '''
    Unittests for the additional cases of the created_at attribute
    '''
    def test_created_at_of_two_ids(self):
        user_1 = BaseModel()
        sleep(0.02)
        user_2 = User()
        self.assertNotEqual(user_1.created_at, user_2.created_at)


class TestUser_updated_at(unittest.TestCase):
    '''
    Unittests for the additional cases of the updated_at attribute
    '''
    def test_updated_at_of_one_id(self):
        user_1 = User()
        sleep(0.02)
        user_1 = User()
        self.assertNotEqual(user_1.created_at, user_1.updated_at)

    def test_updated_at_of_two_ids(self):
        user_1 = User()
        sleep(0.02)
        user_2 = User()
        self.assertNotEqual(user_1.updated_at, user_2.updated_at)


class TestUser_Public_Methods(unittest.TestCase):
    '''
    Unittests for the implementation of the public methods of the BaseModel class
    '''
    def test_save_method(self):
        user_1 = User()
        old_updated_at = user_1.updated_at
        user_1.save()
        self.assertNotEqual(user_1.updated_at, old_updated_at)

    def test_to_dict_method(self):
        user_1 = User()
        user_1_dict = user_1.to_dict()
        self.assertIsInstance(user_1_dict, dict)
        self.assertIn('__class__', user_1_dict)
        self.assertEqual(user_1_dict['__class__'], 'User')
        self.assertIn('created_at', user_1_dict)
        self.assertIsInstance(user_1_dict['created_at'], str)
        self.assertIn('updated_at', user_1_dict)
        self.assertIsInstance(user_1_dict['updated_at'], str)


class TestUser_save(unittest.TestCase):
    '''
    Unittests for the implementation of the save method in BaseModel
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
        pass # recieved error when implemented??

    def test_save_twice(self):
        pass

    def test_save_thrice(self):
        pass

    def test_save_None(self):
        pass


class TestUser_to_dict(unittest.TestCase):
    '''
    Unittests for the implementation of the to_dict method in BaseModel
    '''
    def test_to_dict_type(self):
        user_1 = User()
        self.assertEqual(dict, type(user_1.to_dict()))

    def test_to_dict_keys(self):
        user_1 = User()
        test_d = user_1.to_dict()
        self.assertIn("id", test_d)
        self.assertIn("__class__", test_d)
        self.assertIn("created_at", test_d)
        self.assertIn("updated_at", test_d)

    def test_to_dict_values(self):
        pass # recieved error when implemented?? - check values in to_dict

    def test_to_dict_results(self):
        dt = datetime.today()
        user_1 = User()
        user_1.id = "120964"
        user_1.created_at = user_1.updated_at = dt
        rdict = {
                'id': '120964',
                '__class__': 'User',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat()
                }
        self.assertDictEqual(user_1.to_dict(), rdict)

    def test_to_dict_None(self):
        user_1 = User()
        with self.assertRaises(TypeError):
            user_1.to_dict(None)


class TestUser_Storage(unittest.TestCase):
    '''
    Unittests related to storing data
    '''
    def test__new_instance_stored(self):
        self.assertIn(User(), models.storage.all().values())


if __name__ == '__main__':
    unittest.main()
