import unittest
from url_shortener import User
from analytics import Analytics


class TestUser(unittest.TestCase):
    def test_example(self):
        analytics = Analytics()
        user = User(analytics)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()