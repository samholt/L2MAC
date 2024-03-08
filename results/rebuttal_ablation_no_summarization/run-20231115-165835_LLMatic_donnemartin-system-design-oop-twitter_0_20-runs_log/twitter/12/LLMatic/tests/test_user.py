import unittest
from user import User, users_db, posts_db
from post import Post


class TestUser(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		users_db.clear()
		User.register('user1', 'user1@example.com', 'password1')
		User.register('user2', 'user2@example.com', 'password2')

	def test_follow(self):
		self.assertTrue(User.follow('user1', 'user2'))
		self.assertIn('user2', users_db['user1'].following)

	def test_unfollow(self):
		User.follow('user1', 'user2')
		self.assertTrue(User.unfollow('user1', 'user2'))
		self.assertNotIn('user2', users_db['user1'].following)

	def test_get_timeline(self):
		User.follow('user1', 'user2')
		posts_db['1'] = Post('user2', 'Hello, world!', [])
		timeline_posts = User.get_timeline('user1')
		self.assertEqual(len(timeline_posts), 1)
		self.assertEqual(timeline_posts[0].username, 'user2')
		self.assertEqual(timeline_posts[0].text, 'Hello, world!')

	def test_recommend_users_to_follow(self):
		User.register('user3', 'user3@example.com', 'password3')
		User.register('user4', 'user4@example.com', 'password4')
		User.register('user5', 'user5@example.com', 'password5')
		User.register('user6', 'user6@example.com', 'password6')
		User.register('user7', 'user7@example.com', 'password7')
		recommended_users = User.recommend_users_to_follow('user1')
		self.assertEqual(len(recommended_users), 5)
		self.assertNotIn('user1', recommended_users)
		self.assertNotIn('user2', recommended_users)

if __name__ == '__main__':
	unittest.main()


