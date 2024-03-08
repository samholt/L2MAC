import unittest
from app import app
from app.models import User, DATABASE

class TestRoutes(unittest.TestCase):
	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['DEBUG'] = False
		self.client = app.test_client()
		self.user = User(id=1, username='test', email='', password='test')
		DATABASE[self.user.id] = self.user

	def test_index(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data, b'Hello, World!')

	def test_signup(self):
		response = self.client.post('/signup', data={'username': 'test2', 'password': 'test2'})
		self.assertEqual(response.status_code, 302)

	def test_login(self):
		response = self.client.post('/login', data={'username': 'test', 'password': 'test'})
		self.assertEqual(response.status_code, 302)

	def test_set_online_status(self):
		response = self.client.post('/set_online_status', data={'user_id': '1', 'online_status': 'True'})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data, b'User(id=1, username=test, email=, password=test, profile_picture=None, status_message=None, privacy_settings=None, last_seen=None, blocked_contacts=[], online=True)')
