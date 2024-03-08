import unittest
from oms import User, Post, OMS


class TestOMS(unittest.TestCase):
    def setUp(self):
        self.oms = OMS()

    def test_register_user(self):
        user = self.oms.register_user('testuser', 'password', 'test@example.com')
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.password, 'password')
        self.assertEqual(user.email, 'test@example.com')

    def test_create_post(self):
        self.oms.register_user('testuser', 'password', 'test@example.com')
        post = self.oms.create_post('testuser', 'Hello, world!')
        self.assertIsInstance(post, Post)
        self.assertEqual(post.author.username, 'testuser')
        self.assertEqual(post.content, 'Hello, world!')

    def test_get_timeline(self):
        user1 = self.oms.register_user('user1', 'password', 'user1@example.com')
        user2 = self.oms.register_user('user2', 'password', 'user2@example.com')
        user1.follow(user2)
        post = self.oms.create_post('user2', 'Hello, world!')
        timeline = self.oms.get_timeline('user1')
        self.assertEqual(len(timeline), 1)
        self.assertEqual(timeline[0], post)


if __name__ == '__main__':
    unittest.main()