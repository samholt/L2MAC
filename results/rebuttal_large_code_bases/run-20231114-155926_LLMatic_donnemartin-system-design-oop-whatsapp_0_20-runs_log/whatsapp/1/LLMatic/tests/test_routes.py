import unittest
from unittest.mock import patch
from flask import url_for, session
from app import app, db
from app.models import User, Message, Group, Status
from werkzeug.security import generate_password_hash


class RoutesTestCase(unittest.TestCase):

	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['DEBUG'] = False
		self.app = app.test_client()
		with app.app_context():
			self.user = User(email='test@test.com', password=generate_password_hash('test', method='sha256'))
			self.user2 = User(email='test2@test.com', password=generate_password_hash('test2', method='sha256'))
			db.session.add(self.user)
			db.session.commit()
			session['user_id'] = self.user.id

	def tearDown(self):
		with app.app_context():
			db.session.remove()
			session.clear()

	@patch('app.routes.User.query')
	def test_signup(self, mock_query):
		mock_query.filter_by.return_value.first.return_value = None
		response = self.app.get('/signup', follow_redirects=True)
		self.assertEqual(response.status_code, 200)

		response = self.app.post('/signup', data=dict(email='test3@test.com', password='test3'), follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		mock_query.filter_by.assert_called_with(email='test3@test.com')

		response = self.app.post('/signup', data=dict(email='', password='test3'), follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		mock_query.filter_by.assert_called_with(email='')

	@patch('app.routes.User.query')
	def test_login(self, mock_query):
		mock_query.filter_by.return_value.first.return_value = self.user
		response = self.app.get('/login', follow_redirects=True)
		self.assertEqual(response.status_code, 200)

		response = self.app.post('/login', data=dict(email='test@test.com', password='test'), follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(session['user_id'], self.user.id)

		response = self.app.post('/login', data=dict(email='wrong@test.com', password='test'), follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		self.assertNotEqual(session.get('user_id'), self.user.id)

		response = self.app.post('/login', data=dict(email='test@test.com', password='wrong'), follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		self.assertNotEqual(session.get('user_id'), self.user.id)

	def test_logout(self):
		response = self.app.get('/logout', follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		self.assertIsNone(session.get('user_id'))

	@patch('app.routes.User.query')
	def test_profile(self, mock_query):
		mock_query.filter_by.return_value.first.return_value = self.user
		response = self.app.get('/profile', follow_redirects=True)
		self.assertEqual(response.status_code, 200)

		response = self.app.post('/profile', data=dict(email='new@test.com', password='new'), follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		mock_query.filter_by.assert_called_with(email='new@test.com')

		response = self.app.post('/profile', data=dict(email='', password='new'), follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		mock_query.filter_by.assert_called_with(email='')

	@patch('app.routes.User.query')
	def test_chat(self, mock_query):
		mock_query.filter_by.return_value.first.return_value = self.user2
		response = self.app.get('/chat', follow_redirects=True)
		self.assertEqual(response.status_code, 200)

		response = self.app.post('/chat', data=dict(receiver_email='test2@test.com', message_content='Hello'), follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		mock_query.filter_by.assert_called_with(email='test2@test.com')

		response = self.app.post('/chat', data=dict(receiver_email='wrong@test.com', message_content='Hello'), follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		mock_query.filter_by.assert_called_with(email='wrong@test.com')

	@patch('app.routes.Group.query')
	def test_group(self, mock_query):
		mock_query.filter_by.return_value.first.return_value = None
		response = self.app.get('/group', follow_redirects=True)
		self.assertEqual(response.status_code, 200)

		response = self.app.post('/group', data=dict(group_name='Test Group'), follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		mock_query.filter_by.assert_called_with(name='Test Group')

		response = self.app.post('/group', data=dict(group_name=''), follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		mock_query.filter_by.assert_called_with(name='')

	@patch('app.routes.Status.query')
	def test_status(self, mock_query):
		mock_query.filter_by.return_value.first.return_value = None
		response = self.app.get('/status', follow_redirects=True)
		self.assertEqual(response.status_code, 200)

		response = self.app.post('/status', data=dict(status_content='Hello, world!', visibility='public'), follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		mock_query.filter_by.assert_called_with(content='Hello, world!')

		response = self.app.post('/status', data=dict(status_content='', visibility='public'), follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		mock_query.filter_by.assert_called_with(content='')

	@patch('app.routes.User.query')
	def test_contacts(self, mock_query):
		mock_query.filter_by.return_value.first.return_value = self.user2
		response = self.app.get('/contacts', follow_redirects=True)
		self.assertEqual(response.status_code, 200)

		response = self.app.post('/contacts', data=dict(contact_email='test2@test.com'), follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		mock_query.filter_by.assert_called_with(email='test2@test.com')

		response = self.app.post('/contacts', data=dict(contact_email='wrong@test.com'), follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		mock_query.filter_by.assert_called_with(email='wrong@test.com')


if __name__ == '__main__':
	unittest.main()

