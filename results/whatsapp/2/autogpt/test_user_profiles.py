import unittest
from user_auth import register
from user_profiles import create_user_profile


class TestUserProfiles(unittest.TestCase):
    def test_create_user_profile(self):
        username = 'testuser'
        password = 'testpassword'
        user = register(username, password)
        display_name = 'Test User'
        status = 'Hello, world!'
        user_profile = create_user_profile(user, display_name, status)
        self.assertEqual(user_profile.display_name, display_name)
        self.assertEqual(user_profile.status, status)


if __name__ == '__main__':
    unittest.main()