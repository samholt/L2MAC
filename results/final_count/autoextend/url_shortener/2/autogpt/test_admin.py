import unittest
from url_shortener import Admin
from analytics import Analytics


class TestAdmin(unittest.TestCase):
    def test_example(self):
        analytics = Analytics()
        admin = Admin(analytics)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()