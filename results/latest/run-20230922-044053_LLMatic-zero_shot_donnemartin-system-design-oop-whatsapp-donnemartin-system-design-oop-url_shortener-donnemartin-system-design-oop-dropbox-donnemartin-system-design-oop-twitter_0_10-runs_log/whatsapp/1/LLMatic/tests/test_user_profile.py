import unittest
import sys
sys.path.insert(0, '..')
from app import app, db
from app.models import User


class UserProfileTestCase(unittest.TestCase):
	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
		self.app = app.test_client()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_profile_picture(self):
		u = User(email='john@example.com')
		u.set_password('cat')
		u.set_profile_picture('john.jpg')
		self.assertEqual(u.get_profile_picture(), 'john.jpg')

	def test_status_message(self):
		u = User(email='john@example.com')
		u.set_password('cat')
		u.set_status_message('Hello, world!')
		self.assertEqual(u.get_status_message(), 'Hello, world!')

	def test_privacy_settings(self):
		u = User(email='john@example.com')
		u.set_password('cat')
		u.update_privacy_settings('Friends only')
		self.assertEqual(u.privacy_settings, 'Friends only')

if __name__ == '__main__':
	unittest.main()
