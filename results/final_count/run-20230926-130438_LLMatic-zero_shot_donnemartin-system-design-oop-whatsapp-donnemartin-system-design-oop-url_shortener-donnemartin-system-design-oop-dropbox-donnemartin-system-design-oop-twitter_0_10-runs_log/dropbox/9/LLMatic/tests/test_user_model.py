import unittest
from models.user import User

class TestUserModel(unittest.TestCase):
	def test_user_model(self):
		user = User('1', 'Test User', 'test@example.com', 'password', 'profile.jpg', 0)
		self.assertEqual(user.id, '1')
		self.assertEqual(user.name, 'Test User')
		self.assertEqual(user.email, 'test@example.com')
		self.assertEqual(user.password, 'password')
		self.assertEqual(user.profile_picture, 'profile.jpg')
		self.assertEqual(user.storage_used, 0)
