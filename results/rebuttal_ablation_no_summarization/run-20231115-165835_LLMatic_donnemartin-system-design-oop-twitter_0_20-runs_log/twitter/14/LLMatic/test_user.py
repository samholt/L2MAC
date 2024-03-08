import unittest
from user import User
from post import Post

class TestUser(unittest.TestCase):
	def setUp(self):
		self.user1 = User('test1@test.com', 'testuser1', 'testpass1', bio='I love coding')
		self.user2 = User('test2@test.com', 'testuser2', 'testpass2', bio='I love music')
		self.user3 = User('test3@test.com', 'testuser3', 'testpass3', bio='I love coding and music')

	def test_edit_profile(self):
		self.user1.edit_profile(bio='I love music')
		self.assertEqual(self.user1.bio, 'I love music')

	def test_toggle_visibility(self):
		self.user1.toggle_visibility()
		self.assertFalse(self.user1.visible)

	def test_follow(self):
		self.user1.follow(self.user2)
		self.assertIn(self.user2, self.user1.following)
		self.assertIn(self.user1, self.user2.followers)

	def test_unfollow(self):
		self.user1.follow(self.user2)
		self.user1.unfollow(self.user2)
		self.assertNotIn(self.user2, self.user1.following)
		self.assertNotIn(self.user1, self.user2.followers)

	def test_search_users(self):
		users = [self.user1, self.user2, self.user3]
		results = User.search_users(users, 'music')
		self.assertEqual(results, [self.user2, self.user3])

	def test_recommend_users(self):
		users = [self.user1, self.user2, self.user3]
		self.user1.follow(self.user2)
		self.user3.follow(self.user2)
		self.user1.posts.append(Post(self.user1, 'I love coding'))
		self.user2.posts.append(Post(self.user2, 'I love music'))
		self.user3.posts.append(Post(self.user3, 'I love coding and music'))
		self.user3.posts.append(Post(self.user3, 'I love coding and music'))
		recommendations = self.user1.recommend_users(users)
		self.assertEqual(recommendations, [(self.user3, 0, 3, 2), (self.user2, 0, 2, 1)])

if __name__ == '__main__':
	unittest.main()

