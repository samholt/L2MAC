import unittest
from oms_platform import User, Post, OMS


class TestOMSPlatform(unittest.TestCase):
    def setUp(self):
        self.oms = OMS()

    def test_register_user(self):
        user = self.oms.register_user('testuser', 'testpassword', 'test@example.com')
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testuser')

    def test_create_post(self):
        self.oms.register_user('testuser', 'testpassword', 'test@example.com')
        post = self.oms.create_post('testuser', 'Hello, world!')
        self.assertIsNotNone(post)
        self.assertEqual(post.content, 'Hello, world!')

    def test_get_posts(self):
        self.oms.register_user('testuser', 'testpassword', 'test@example.com')
        self.oms.create_post('testuser', 'Hello, world!')
        posts = self.oms.get_posts()
        self.assertEqual(len(posts), 1)

    def test_get_user_posts(self):
        self.oms.register_user('testuser', 'testpassword', 'test@example.com')
        self.oms.create_post('testuser', 'Hello, world!')
        user_posts = self.oms.get_user_posts('testuser')
        self.assertEqual(len(user_posts), 1)


if __name__ == '__main__':
    unittest.main()