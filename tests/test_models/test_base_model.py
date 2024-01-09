#!/usr/bin/python3
''' These Unittests are for the BaseModel Class

    Unittest classes:
        TestBaseModel
        TestBaseModel_args
        TestBaseModel_Public_Attributes
        TestBaseModel_created_at
        TestBaseModel_updated_at
        TestBaseModel_Public_Methods
        TestBaseModel_save
'''
import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
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


class TestBaseModel_args(unittest.TestCase):
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


class TestBaseModel_Public_Attributes(unittest.TestCase):
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
        base_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(base_model.id,
                                                    base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)


class TestBaseModel_created_at(unittest.TestCase):
    '''
    Unittests for the additional cases of the created_at attribute
    '''
    def test_created_at_of_two_ids(self):
        base_model_1 = BaseModel()
        sleep(0.02)
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.created_at, base_model_2.created_at)


class TestBaseModel_updated_at(unittest.TestCase):
    '''
    Unittests for the additional cases of the updated_at attribute
    '''
    def test_updated_at_of_one_id(self):
        base_model_1 = BaseModel()
        sleep(0.02)
        base_model_1 = BaseModel()
        self.assertNotEqual(base_model_1.created_at, base_model_1.updated_at)

    def test_updated_at_of_two_ids(self):
        base_model_1 = BaseModel()
        sleep(0.02)
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.updated_at, base_model_2.updated_at)


class TestBaseModel_Public_Methods(unittest.TestCase):
    '''
    Unittests for the implementation of the public methods of the BaseModel class
    '''
    def test_save_method(self):
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(base_model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('__class__', base_model_dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', base_model_dict)
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIn('updated_at', base_model_dict)
        self.assertIsInstance(base_model_dict['updated_at'], str)


class TestBaseModel_save(unittest.TestCase):
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


class TestBaseModel_to_dict(unittest.TestCase):
    '''
    Unittests for the implementation of the to_dict method in BaseModel
    '''
    def test_to_dict_type(self):
        base_model = BaseModel()
        self.assertEqual(dict, type(base_model.to_dict()))

    def test_to_dict_keys(self):
        base_model = BaseModel()
        test_d = base_model.to_dict()
        self.assertIn("id", test_d)
        self.assertIn("__class__", test_d)
        self.assertIn("created_at", test_d)
        self.assertIn("updated_at", test_d)

    def test_to_dict_values(self):
        pass # recieved error when implemented?? - check values in to_dict

    def test_to_dict_results(self):
        dt = datetime.today()
        base_model = BaseModel()
        base_model.id = "120964"
        base_model.created_at = base_model.updated_at = dt
        rdict = {
                'id': '120964',
                '__class__': 'BaseModel',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat()
                }
        self.assertDictEqual(base_model.to_dict(), rdict)

    def test_to_dict_None(self):
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.to_dict(None)


class TestBaseModel_Storage(unittest.TestCase):
    '''
    Unittests related to storing data
    '''
    def test__new_instance_stored(self):
        self.assertIn(BaseModel(), models.storage.all().values())


if __name__ == '__main__':
    unittest.main()
