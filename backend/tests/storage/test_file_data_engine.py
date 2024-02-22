"""Test module for database engine."""
import unittest
from model.base_model import User
from storage.file_data_engine import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test for FileStorage."""

    def test_new(self):
        user = User()
        store = FileStorage()
        u = store.new(user)
        store.save()
        self.assertEqual(len(u.id), 36)

    def test_update(self):
        id = "7bd9635e-50b0-423c-ac22-e26479b50b26"
        user = User(id=id)
        attr = {"name": "Yaw", "age": 70}
        store = FileStorage()
        res = store.update(id, **attr)
        store.save()
        self.assertEqual(res.get("name", None), "Yaw")

if __name__ == "__main__":
    unittest.main()