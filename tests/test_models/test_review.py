#!/usr/bin/python3
''' These Unittests are for the Review Class

    Unittest classes:
        TestReview_1
        TestReview_1_args
        TestReview_1_Public_Attributes
        TestReview_1_created_at
        TestReview_1_updated_at
        TestReview_1_Public_Methods
        TestReview_1_save
'''
import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.review import Review


class TestReview_1(unittest.TestCase):
    '''
    Unittests for all cases for the Review class
    '''
    def test_instance(self):
        self.assertTrue(isinstance(Review().id, str))

    def test_type(self):
        self.assertEqual(str, type(Review().id))

    def test_uuid(self):
        review_1 = Review()
        base_model_2 = Review()
        self.assertNotEqual(review_1.id, base_model_2.id)


class TestReview_1_args(unittest.TestCase):
    '''
    Unittests for the different arguments made to Review
    '''
    def test_init_kwargs(self):
        base_model = Review(name='Plankton', age=32)
        # Test whether the attributes were updated correctly
        self.assertEqual(base_model.name, 'Plankton')
        self.assertEqual(base_model.age, 32)

    def test_none_arg(self):
        review_1 = Review(None)
        self.assertNotIn(None, review_1.__dict__.values())

    def test_kwargs_with_none_as_value(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_args_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        base_model = Review("Sandy", "Spongebob", "Gary", id="123",
                               created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(base_model.id, "123")
        self.assertEqual(base_model.created_at, dt)
        self.assertEqual(base_model.updated_at, dt)


class TestReview_1_Public_Attributes(unittest.TestCase):
    '''
    Unittests for the implementation of the public attributes of the Review class
    '''
    def test_created_at_instance(self):
        base_model = Review()
        self.assertIsInstance(base_model.created_at, datetime)

    def test_updated_at_instance(self):
        base_model = Review()
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_str_method_instance(self):
        base_model = Review()
        expected_str = "[Review] ({}) {}".format(base_model.id,
                                                    base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)


class TestReview_1_created_at(unittest.TestCase):
    '''
    Unittests for the additional cases of the created_at attribute
    '''
    def test_created_at_of_two_ids(self):
        review_1 = Review()
        sleep(0.02)
        base_model_2 = Review()
        self.assertNotEqual(review_1.created_at, base_model_2.created_at)


class TestReview_1_updated_at(unittest.TestCase):
    '''
    Unittests for the additional cases of the updated_at attribute
    '''
    def test_updated_at_of_one_id(self):
        review_1 = Review()
        sleep(0.02)
        review_1 = Review()
        self.assertNotEqual(review_1.created_at, review_1.updated_at)

    def test_updated_at_of_two_ids(self):
        review_1 = Review()
        sleep(0.02)
        base_model_2 = Review()
        self.assertNotEqual(review_1.updated_at, base_model_2.updated_at)


class TestReview_1_Public_Methods(unittest.TestCase):
    '''
    Unittests for the implementation of the public methods of the Review class
    '''
    def test_save_method(self):
        base_model = Review()
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(base_model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        base_model = Review()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('__class__', base_model_dict)
        self.assertEqual(base_model_dict['__class__'], 'Review')
        self.assertIn('created_at', base_model_dict)
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIn('updated_at', base_model_dict)
        self.assertIsInstance(base_model_dict['updated_at'], str)


class TestReview_1_save(unittest.TestCase):
    '''
    Unittests for the implementation of the save method in Review
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
        review_1 = Review()
        sleep(0.02)
        first_updated_at = review_1.updated_at
        review_1.save()
        self.assertLess(first_updated_at, review_1.updated_at)

    def test_save_twice(self):
        review_1 = Review()
        sleep(0.02)
        first_updated_at = review_1.updated_at
        review_1.save()
        second_updated_at = review_1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.02)
        review_1.save()
        self.assertLess(second_updated_at, review_1.updated_at)

    def test_save_None(self):
        review_1 = Review()
        with self.assertRaises(TypeError):
            review_1.save(None)
        

class TestReview_1_to_dict(unittest.TestCase):
    '''
    Unittests for the implementation of the to_dict method in Review
    '''
    def test_to_dict_type(self):
        base_model = Review()
        self.assertEqual(dict, type(base_model.to_dict()))

    def test_to_dict_keys(self):
        base_model = Review()
        test_d = base_model.to_dict()
        self.assertIn("id", test_d)
        self.assertIn("__class__", test_d)
        self.assertIn("created_at", test_d)
        self.assertIn("updated_at", test_d)

    def test_to_dict_values(self):
        base_model = Review()
        base_model.name = "Mr Crabs"
        base_model.his_number = 45
        self.assertIn("name", base_model.to_dict())
        self.assertIn("his_number", base_model.to_dict())

    def test_to_dict_results(self):
        dt = datetime.today()
        base_model = Review()
        base_model.id = "120964"
        base_model.created_at = base_model.updated_at = dt
        rdict = {
                'id': '120964',
                '__class__': 'Review',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat()
                }
        self.assertDictEqual(base_model.to_dict(), rdict)

    def test_to_dict_None(self):
        base_model = Review()
        with self.assertRaises(TypeError):
            base_model.to_dict(None)


class TestReview_1_Storage(unittest.TestCase):
    '''
    Unittests related to storing data
    '''
    def test__new_instance_stored(self):
        self.assertIn(Review(), models.storage.all().values())


if __name__ == '__main__':
    unittest.main()
