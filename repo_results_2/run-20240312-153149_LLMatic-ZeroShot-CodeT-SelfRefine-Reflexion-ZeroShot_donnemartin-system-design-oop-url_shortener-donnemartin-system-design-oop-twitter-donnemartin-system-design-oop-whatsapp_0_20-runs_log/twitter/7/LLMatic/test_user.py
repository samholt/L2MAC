import unittest
from user import User


class TestUser(unittest.TestCase):
	def setUp(self):
		self.user = User('test@test.com', 'testuser', 'password')

	def test_check_password(self):
		self.assertTrue(self.user.check_password('password'))
		self.assertFalse(self.user.check_password('wrongpassword'))

	def test_update_profile(self):
		self.user.update_profile(profile_picture='newpic.jpg', bio='new bio', website_link='newwebsite.com', location='new location')
		self.assertEqual(self.user.profile_picture, 'newpic.jpg')
		self.assertEqual(self.user.bio, 'new bio')
		self.assertEqual(self.user.website_link, 'newwebsite.com')
		self.assertEqual(self.user.location, 'new location')

	def test_follow(self):
		user2 = User('test2@test.com', 'testuser2', 'password')
		self.user.follow(user2)
		self.assertIn(user2, self.user.following)
		self.assertIn(self.user, user2.followers)

	def test_unfollow(self):
		user2 = User('test2@test.com', 'testuser2', 'password')
		self.user.follow(user2)
		self.user.unfollow(user2)
		self.assertNotIn(user2, self.user.following)
		self.assertNotIn(self.user, user2.followers)

	def test_block(self):
		user2 = User('test2@test.com', 'testuser2', 'password')
		self.user.block(user2)
		self.assertIn(user2, self.user.blocked_users)

	def test_unblock(self):
		user2 = User('test2@test.com', 'testuser2', 'password')
		self.user.block(user2)
		self.user.unblock(user2)
		self.assertNotIn(user2, self.user.blocked_users)

	def test_generate_jwt(self):
		token = self.user.generate_jwt()
		self.assertIsNotNone(token)

	def test_validate_jwt(self):
		token = self.user.generate_jwt()
		self.assertTrue(self.user.validate_jwt(token))

		# Test with invalid token
		self.assertFalse(self.user.validate_jwt('invalidtoken'))

if __name__ == '__main__':
	unittest.main()
