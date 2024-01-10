#!/usr/bin/python3
"""
This module is for testing file_storage module.
"""

import unittest
from models.engine import file_storage


class TestFileStorage(unittest.TestCase):
    """Tests FileStorageClass"""

    def test_is_instance(self):
        """Tests instantiation"""

        obj = file_storage.FileStorage()

        self.assertIsInstance(obj, file_storage.FileStorage)

    def test_documentation(self):
        """Tests if the module, the class,
        and the methods are documented"""

        self.assertIsNotNone(file_storage.__doc__)
        self.assertIsNotNone(file_storage.FileStorage.__doc__)
        self.assertIsNotNone(file_storage.FileStorage.all)
        self.assertIsNotNone(file_storage.FileStorage.new)
        self.assertIsNotNone(file_storage.FileStorage.save)
        self.assertIsNotNone(file_storage.FileStorage.reload)


if __name__ == '__main__':
    unittest.main()
