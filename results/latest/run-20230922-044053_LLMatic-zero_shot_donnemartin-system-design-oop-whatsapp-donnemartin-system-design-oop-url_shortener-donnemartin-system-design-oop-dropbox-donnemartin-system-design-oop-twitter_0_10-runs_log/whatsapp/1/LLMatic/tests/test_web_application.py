import unittest
from flask import url_for
from app import app, db
from app.models import User


class WebApplicationTestCase(unittest.TestCase):

	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
		self.client = app.test_client()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_home_page(self):
		response = self.client.get(url_for('home'))
		self.assertEqual(response.status_code, 200)

	def test_login_page(self):
		response = self.client.get(url_for('login'))
		self.assertEqual(response.status_code, 200)

	def test_registration_page(self):
		response = self.client.get(url_for('register'))
		self.assertEqual(response.status_code, 200)

	def test_chat_page(self):
		user = User(email='user@example.com')
		user.set_password('password')
		db.session.add(user)
		db.session.commit()
		response = self.client.get(url_for('chat', contact_id=user.id))
		self.assertEqual(response.status_code, 302)

	def test_group_chat_page(self):
		response = self.client.get(url_for('group_chat', group_id=1))
		self.assertEqual(response.status_code, 302)

	def test_status_page(self):
		response = self.client.get(url_for('status'))
		self.assertEqual(response.status_code, 302)
