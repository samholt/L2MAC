import unittest
from user_auth import register, authenticate


class TestUserAuth(unittest.TestCase):
    def test_register_and_authenticate(self):
        username = 'testuser'
        password = 'testpassword'
        user = register(username, password)
        self.assertTrue(authenticate(user, password))


if __name__ == '__main__':
    unittest.main()