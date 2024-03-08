import unittest
from flask import url_for
from flask_login import current_user
from app import create_app, db
from app.models import User


class ProfileTestCase(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		self.client = self.app.test_client()
		db.create_all()
		u = User(email='test@test.com', password='test')
		db.session.add(u)
		db.session.commit()

	def tearDown(self):
		db.session.remove()
		db.drop_all()
		self.app_context.pop()

	def test_view_profile(self):
		with self.client:
			self.client.post(url_for('auth.login'), data=dict(email='test@test.com', password='test'), follow_redirects=True)
			response = self.client.get(url_for('profile.view_profile'))
			self.assertEqual(response.status_code, 200)

	def test_edit_profile(self):
		with self.client:
			self.client.post(url_for('auth.login'), data=dict(email='test@test.com', password='test'), follow_redirects=True)
			response = self.client.post(url_for('profile.edit_profile'), data=dict(name='Test User', profile_picture='test.jpg', status_message='Hello, world!'), follow_redirects=True)
			self.assertEqual(response.status_code, 200)
			self.assertEqual(current_user.name, 'Test User')
			self.assertEqual(current_user.profile_picture, 'test.jpg')
			self.assertEqual(current_user.status_message, 'Hello, world!')

	def test_privacy_settings(self):
		with self.client:
			self.client.post(url_for('auth.login'), data=dict(email='test@test.com', password='test'), follow_redirects=True)
			response = self.client.post(url_for('profile.privacy_settings'), data=dict(private_account=True), follow_redirects=True)
			self.assertEqual(response.status_code, 200)
			self.assertEqual(current_user.private_account, True)
