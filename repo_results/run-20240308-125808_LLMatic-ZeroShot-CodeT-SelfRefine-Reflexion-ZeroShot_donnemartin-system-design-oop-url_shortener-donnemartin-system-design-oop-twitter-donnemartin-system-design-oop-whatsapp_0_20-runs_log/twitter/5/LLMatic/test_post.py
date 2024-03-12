import unittest
from post import Post
from user import User


class TestPost(unittest.TestCase):
	def setUp(self):
		self.user1 = User('email1', 'username1', 'password1')
		self.user2 = User('email2', 'username2', 'password2')
		self.post1 = self.user1.create_post('Hello #world!', [])
		self.post2 = self.user2.create_post('Hello #world! #python', [])
		self.posts = [self.post1, self.post2]

	def test_trending_topics(self):
		self.assertEqual(Post.trending_topics(self.posts), ['#world!', '#python'])
