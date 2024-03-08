import unittest
from webapp.app import app
from services.auth_service import AuthService

class TestApp(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
		self.user = AuthService.login('test@test.com', 'password')

	def test_home(self):
		response = self.app.get('/')
		self.assertEqual(response.status_code, 200)

	def test_login(self):
		response = self.app.post('/login', data={'email': 'test@test.com', 'password': 'password'})
		self.assertEqual(response.status_code, 302)

	def test_contacts(self):
		response = self.app.get('/contacts')
		self.assertEqual(response.status_code, 200)

	def test_group(self):
		response = self.app.get('/group')
		self.assertEqual(response.status_code, 200)

	def test_message(self):
		response = self.app.get('/message')
		self.assertEqual(response.status_code, 200)

	def test_profile(self):
		response = self.app.get('/profile')
		self.assertEqual(response.status_code, 200)
