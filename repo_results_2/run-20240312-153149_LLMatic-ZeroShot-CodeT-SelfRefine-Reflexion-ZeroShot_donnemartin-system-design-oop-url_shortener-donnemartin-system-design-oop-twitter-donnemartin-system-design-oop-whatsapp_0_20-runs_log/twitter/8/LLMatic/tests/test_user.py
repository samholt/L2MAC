import unittest
from user import User
from post import Post
from message import Message
from notification import Notification


class TestUser(unittest.TestCase):
	def setUp(self):
		self.user1 = User('user1', 'user1@example.com', 'password')
		self.user2 = User('user2', 'user2@example.com', 'password')
		self.user3 = User('user3', 'user3@example.com', 'password')

	def test_authenticate(self):
		self.assertIsNone(self.user1.authenticate('wrongpassword'))
		self.assertIsNotNone(self.user1.authenticate('password'))

	def test_edit_profile(self):
		self.user1.edit_profile(profile_picture='pic.jpg', bio='This is a bio.', website='https://example.com', location='USA')
		self.assertEqual(self.user1.profile_picture, 'pic.jpg')
		self.assertEqual(self.user1.bio, 'This is a bio.')
		self.assertEqual(self.user1.website, 'https://example.com')
		self.assertEqual(self.user1.location, 'USA')

	def test_toggle_privacy(self):
		self.assertFalse(self.user1.is_private)
		self.user1.toggle_privacy()
		self.assertTrue(self.user1.is_private)

	def test_create_post(self):
		self.user1.create_post('This is a post.', ['pic.jpg'])
		self.assertEqual(len(self.user1.posts), 1)

	def test_delete_post(self):
		self.user1.create_post('This is a post.', ['pic.jpg'])
		self.assertEqual(len(self.user1.posts), 1)
		self.user1.delete_post(0)
		self.assertEqual(len(self.user1.posts), 0)

	def test_follow(self):
		self.user1.follow(self.user2)
		self.assertIn(self.user2, self.user1.following)
		self.assertIn(self.user1, self.user2.followers)

	def test_unfollow(self):
		self.user1.follow(self.user2)
		self.user1.unfollow(self.user2)
		self.assertNotIn(self.user2, self.user1.following)
		self.assertNotIn(self.user1, self.user2.followers)

	def test_get_timeline(self):
		self.user1.follow(self.user2)
		self.user2.create_post('This is a post.', ['pic.jpg'])
		self.assertEqual(len(self.user1.get_timeline()), 1)

	def test_send_message(self):
		self.assertTrue(self.user1.send_message(self.user2, 'Hello!'))

	def test_receive_message(self):
		self.assertTrue(self.user1.receive_message(self.user2, 'Hello!'))

	def test_block_user(self):
		self.user1.block_user(self.user2)
		self.assertIn(self.user2, self.user1.blocked_users)

	def test_unblock_user(self):
		self.user1.block_user(self.user2)
		self.user1.unblock_user(self.user2)
		self.assertNotIn(self.user2, self.user1.blocked_users)

	def test_receive_notification(self):
		self.user1.receive_notification('like', self.user2)
		self.assertEqual(len(self.user1.notifications), 1)

	def test_recommend_users(self):
		self.user1.follow(self.user2)
		self.user2.follow(self.user3)
		self.user3.create_post('This is a post.', ['pic.jpg'])
		recommendations = self.user1.recommend_users([self.user3])
		self.assertEqual(len(recommendations), 1)

if __name__ == '__main__':
	unittest.main()

