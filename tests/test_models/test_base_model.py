#!/usr/bin/python3
''' These Unittests are for the BaseModel Class

    Unittest classes:
        test_uuid
'''

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''
    Tests all cases for the BaseModel class
    '''
    def test_uuid(self):
        '''
        Tests the uniqueness  and format of each id
        '''
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.id, base_model_2.id)

        # Test if the variable is an instance of BaseModel
        self.assertIsInstance(base_model_1, BaseModel)
        self.assertIsInstance(base_model_2, BaseModel)

        # Test if the variable is of type str
        self.assertTrue(isinstance(base_model_1.id, str))
        self.assertTrue(isinstance(base_model_2.id, str))

    def test_created_at(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime)

    def test_updated_at(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_str_method(self):
        base_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(base_model.id, base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)

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


if __name__ == '__main__':
    unittest.main()
