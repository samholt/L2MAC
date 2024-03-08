import unittest
from gcs_app.auth.auth import User, register_user, authenticate_user


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.users = [
            register_user('user1', 'password1', 'user1@example.com'),
            register_user('user2', 'password2', 'user2@example.com')
        ]

    def test_register_user(self):
        user = register_user('user3', 'password3', 'user3@example.com')
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'user3')
        self.assertEqual(user.password, 'password3')
        self.assertEqual(user.email, 'user3@example.com')

    def test_authenticate_user(self):
        auth_result, message = authenticate_user('user1', 'password1', self.users)
        self.assertTrue(auth_result)
        self.assertEqual(message, 'Authenticated')

        auth_result, message = authenticate_user('user1', 'wrong_password', self.users)
        self.assertFalse(auth_result)
        self.assertEqual(message, 'Incorrect password')

        auth_result, message = authenticate_user('nonexistent_user', 'password', self.users)
        self.assertFalse(auth_result)
        self.assertEqual(message, 'User not found')


if __name__ == '__main__':
    unittest.main()