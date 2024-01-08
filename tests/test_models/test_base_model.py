#!/usr/bin/python3
''' These Unittests are for the BaseModel Class

    Unittest classes:
        TestBaseModel
'''

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''
    Tests all cases for the BaseModel class
    '''
    def test_instantiation(self):
        '''
        Tests instantiation of the instance
        '''
        pass

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
        '''
        Tests the created_at public instance
        '''
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime)

    def test_updated_at(self):
        '''
        Tests the updated_at public instance
        '''
        base_model = BaseModel()
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_str_method(self):
        '''
        Tests the string representation of the object
        '''
        base_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(base_model.id, base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)

    def test_save_method(self):
        '''
        Tests the save() public method
        '''
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(base_model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        '''
        Tests the to_dict() public method
        '''
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('__class__', base_model_dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', base_model_dict)
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIn('updated_at', base_model_dict)
        self.assertIsInstance(base_model_dict['updated_at'], str)

    def test_init_kwargs(self):
        '''
        Tests the kwargs in the constructor (__init__ method)
        '''
        base_model = BaseModel(name='Plankton', age=32)

        # Test whether the attributes were updated correctly
        self.assertEqual(base_model.name, 'Plankton')
        self.assertEqual(base_model.age, 32)

        # Test whether the other attributes remain unchanged
        self.assertEqual(base_model.id, BaseModel().id)
        self.assertEqual(base_model.created_at, BaseModel().created_at)
        self.assertEqual(base_model.updated_at, BaseModel().updated_at)


if __name__ == '__main__':
    unittest.main()
