import unittest
from flask import current_app
from app import create_app, db

class AuthTestCase(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		self.client = self.app.test_client()
		with self.app.app_context():
			db.create_all()

	def tearDown(self):
		with self.app.app_context():
			db.session.remove()
			db.drop_all()
		self.app_context.pop()

	def test_login(self):
		response = self.client.post('/auth/login', data={'username': 'user1', 'password': 'pass1'})
		self.assertEqual(response.status_code, 200)
		self.assertTrue('Could not login. Please check and try again.' not in response.get_data(as_text=True))

	def test_logout(self):
		response = self.client.get('/auth/logout')
		self.assertEqual(response.status_code, 200)
		self.assertTrue('You are now logged out' in response.get_data(as_text=True))
