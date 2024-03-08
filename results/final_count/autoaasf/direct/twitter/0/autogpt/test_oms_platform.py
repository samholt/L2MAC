import unittest
from oms_platform import User, Post, OMS


class TestOMSPlatform(unittest.TestCase):
    def setUp(self):
        self.oms = OMS()

    def test_user_registration(self):
        user = self.oms.register_user('testuser', 'password', 'test@example.com')
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testuser')

    def test_user_login(self):
        self.oms.register_user('testuser', 'password', 'test@example.com')
        user = self.oms.login('testuser', 'password')
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testuser')

    def test_following(self):
        user1 = self.oms.register_user('user1', 'password', 'user1@example.com')
        user2 = self.oms.register_user('user2', 'password', 'user2@example.com')
        user1.follow(user2)
        self.assertIn(user2, user1.following)

    def test_unfollowing(self):
        user1 = self.oms.register_user('user1', 'password', 'user1@example.com')
        user2 = self.oms.register_user('user2', 'password', 'user2@example.com')
        user1.follow(user2)
        user1.unfollow(user2)
        self.assertNotIn(user2, user1.following)

    def test_create_post(self):
        user = self.oms.register_user('testuser', 'password', 'test@example.com')
        post = user.create_post('Hello, world!')
        self.assertIsNotNone(post)
        self.assertEqual(post.content, 'Hello, world!')

    def test_like_post(self):
        user1 = self.oms.register_user('user1', 'password', 'user1@example.com')
        user2 = self.oms.register_user('user2', 'password', 'user2@example.com')
        post = user1.create_post('Hello, world!')
        post.like(user2)
        self.assertIn(user2, post.likes)

    def test_unlike_post(self):
        user1 = self.oms.register_user('user1', 'password', 'user1@example.com')
        user2 = self.oms.register_user('user2', 'password', 'user2@example.com')
        post = user1.create_post('Hello, world!')
        post.like(user2)
        post.unlike(user2)
        self.assertNotIn(user2, post.likes)


if __name__ == '__main__':
    unittest.main()