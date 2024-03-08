import unittest
from controllers.user_controller import UserController
from models.user import User


class TestUserController(unittest.TestCase):
	def test_create_user(self):
		user = UserController.create_user('John Doe', 'john@example.com', 'password')
		self.assertIsInstance(user, User)

	def test_authenticate(self):
		UserController.create_user('John Doe', 'john@example.com', 'password')
		authenticated_user = UserController.authenticate('john@example.com', 'password')
		self.assertIsInstance(authenticated_user, User)

	def test_link_bank_account(self):
		user = UserController.create_user('John Doe', 'john@example.com', 'password')
		UserController.link_bank_account(user, 'Bank Account 1')
		self.assertIn('Bank Account 1', user.bank_accounts)
