import unittest
from gcs_app.connectivity.connectivity import Connectivity


class TestConnectivity(unittest.TestCase):
    def test_is_connected(self):
        result = Connectivity.is_connected()
        self.assertIsInstance(result, bool)


if __name__ == '__main__':
    unittest.main()