import unittest
from model import Model


class TestModel(unittest.TestCase):

    def setUp(self):
        self.model = Model()

    def test_upload_file(self):
        pass

    def test_store_file(self):
        pass

    def test_retrieve_file(self):
        pass

    def test_share_file(self):
        pass

    def test_delete_file(self):
        pass

    def test_synchronize_files(self):
        pass

    def test_acid_properties(self):
        pass

    def test_permission_tracking(self):
        pass

    def test_collaborative_editing(self):
        pass

    def test_large_file_support(self):
        pass


if __name__ == '__main__':
    unittest.main()