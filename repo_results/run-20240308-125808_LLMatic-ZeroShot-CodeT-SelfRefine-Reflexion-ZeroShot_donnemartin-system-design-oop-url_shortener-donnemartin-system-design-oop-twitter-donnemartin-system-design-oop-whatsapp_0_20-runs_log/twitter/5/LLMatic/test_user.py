import unittest
from user import User
from post import Post


class TestUser(unittest.TestCase):
	def setUp(self):
		self.user1 = User('email1', 'username1', 'password1')
		self.user2 = User('email2', 'username2', 'password2')
		self.user3 = User('email3', 'username3', 'password3')
		self.post1 = self.user1.create_post('Hello #world!', [])
		self.post2 = self.user2.create_post('Hello #world! #python', [])
		self.post3 = self.user3.create_post('Hello #python!', [])
		self.user1.like(self.post2)
		self.user1.like(self.post3)
		self.user2.like(self.post1)
		self.user3.like(self.post1)
		self.users = [self.user1, self.user2, self.user3]

	def test_recommend_users(self):
		recommended_users = self.user1.recommend_users(self.users)
		self.assertEqual([user.username for user in recommended_users], ['username1', 'username2', 'username3'])
