#!/usr/bin/python3
''' These Unittests are for the State Class

    Unittest classes:
        TestState_1
        TestState_1_args
        TestState_1_Public_Attributes
        TestState_1_created_at
        TestState_1_updated_at
        TestState_1_Public_Methods
        TestState_1_save
'''
import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.state import State


class TestState_1(unittest.TestCase):
    '''
    Unittests for all cases for the State class
    '''
    def test_instance(self):
        self.assertTrue(isinstance(State().id, str))

    def test_type(self):
        self.assertEqual(str, type(State().id))

    def test_uuid(self):
        state_1 = State()
        state_2 = State()
        self.assertNotEqual(state_1.id, state_2.id)


class TestState_1_args(unittest.TestCase):
    '''
    Unittests for the different arguments made to State
    '''
    def test_init_kwargs(self):
        state = State(name='Plankton', age=32)
        # Test whether the attributes were updated correctly
        self.assertEqual(state.name, 'Plankton')
        self.assertEqual(state.age, 32)

    def test_none_arg(self):
        state_1 = State(None)
        self.assertNotIn(None, state_1.__dict__.values())

    def test_kwargs_with_none_as_value(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_args_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        state = State("Sandy", "Spongebob", "Gary", id="123",
                               created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(state.id, "123")
        self.assertEqual(state.created_at, dt)
        self.assertEqual(state.updated_at, dt)


class TestState_1_Public_Attributes(unittest.TestCase):
    '''
    Unittests for the implementation of the public attributes of the State class
    '''
    def test_created_at_instance(self):
        state = State()
        self.assertIsInstance(state.created_at, datetime)

    def test_updated_at_instance(self):
        state = State()
        self.assertIsInstance(state.updated_at, datetime)

    def test_str_method_instance(self):
        state = State()
        expected_str = "[State] ({}) {}".format(state.id,
                                                    state.__dict__)
        self.assertEqual(str(state), expected_str)


class TestState_1_created_at(unittest.TestCase):
    '''
    Unittests for the additional cases of the created_at attribute
    '''
    def test_created_at_of_two_ids(self):
        state_1 = State()
        sleep(0.02)
        state_2 = State()
        self.assertNotEqual(state_1.created_at, state_2.created_at)


class TestState_1_updated_at(unittest.TestCase):
    '''
    Unittests for the additional cases of the updated_at attribute
    '''
    def test_updated_at_of_one_id(self):
        state_1 = State()
        sleep(0.02)
        state_1 = State()
        self.assertNotEqual(state_1.created_at, state_1.updated_at)

    def test_updated_at_of_two_ids(self):
        state_1 = State()
        sleep(0.02)
        state_2 = State()
        self.assertNotEqual(state_1.updated_at, state_2.updated_at)


class TestState_1_Public_Methods(unittest.TestCase):
    '''
    Unittests for the implementation of the public methods of the State class
    '''
    def test_save_method(self):
        state = State()
        old_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(state.updated_at, old_updated_at)

    def test_to_dict_method(self):
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn('__class__', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIn('created_at', state_dict)
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIn('updated_at', state_dict)
        self.assertIsInstance(state_dict['updated_at'], str)


class TestState_1_save(unittest.TestCase):
    '''
    Unittests for the implementation of the save method in State
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
        state_1 = State()
        sleep(0.02)
        first_updated_at = state_1.updated_at
        state_1.save()
        self.assertLess(first_updated_at, state_1.updated_at)

    def test_save_twice(self):
        state_1 = State()
        sleep(0.02)
        first_updated_at = state_1.updated_at
        state_1.save()
        second_updated_at = state_1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.02)
        state_1.save()
        self.assertLess(second_updated_at, state_1.updated_at)

    def test_save_None(self):
        state_1 = State()
        with self.assertRaises(TypeError):
            state_1.save(None)
        

class TestState_1_to_dict(unittest.TestCase):
    '''
    Unittests for the implementation of the to_dict method in State
    '''
    def test_to_dict_type(self):
        state = State()
        self.assertEqual(dict, type(state.to_dict()))

    def test_to_dict_keys(self):
        state = State()
        test_d = state.to_dict()
        self.assertIn("id", test_d)
        self.assertIn("__class__", test_d)
        self.assertIn("created_at", test_d)
        self.assertIn("updated_at", test_d)

    def test_to_dict_values(self):
        state = State()
        state.name = "Mr Crabs"
        state.his_number = 45
        self.assertIn("name", state.to_dict())
        self.assertIn("his_number", state.to_dict())

    def test_to_dict_results(self):
        dt = datetime.today()
        state = State()
        state.id = "120964"
        state.created_at = state.updated_at = dt
        rdict = {
                'id': '120964',
                '__class__': 'State',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat()
                }
        self.assertDictEqual(state.to_dict(), rdict)

    def test_to_dict_None(self):
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)


class TestState_1_Storage(unittest.TestCase):
    '''
    Unittests related to storing data
    '''
    def test__new_instance_stored(self):
        self.assertIn(State(), models.storage.all().values())


if __name__ == '__main__':
    unittest.main()
