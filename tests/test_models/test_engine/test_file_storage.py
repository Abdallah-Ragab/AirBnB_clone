from models import storage, BaseModel
import os
import json
import unittest
import copy
class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = copy.deepcopy(storage)  # Make a copy of the storage class
        self.storage = storage
        self.storage.__file_path = self.file_path
        print (self.storage.__file_path)
        self.storage.reload()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        # Test if all() returns the dictionary __objects
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        # Test if new() sets the object in __objects with the correct key
        obj = BaseModel()
        self.storage.new(obj)
        objects = self.storage.all()
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", objects)

    def test_save(self):
        # Test if save() serializes __objects to the JSON file
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.file_path, "r") as file:
            data = json.load(file)
            self.assertIn(f"{obj.__class__.__name__}.{obj.id}", data)

    def test_reload(self):
        # Test if reload() deserializes the JSON file to __objects
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        objects = self.storage.all()
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", objects)

if __name__ == "__main__":
    unittest.main()
