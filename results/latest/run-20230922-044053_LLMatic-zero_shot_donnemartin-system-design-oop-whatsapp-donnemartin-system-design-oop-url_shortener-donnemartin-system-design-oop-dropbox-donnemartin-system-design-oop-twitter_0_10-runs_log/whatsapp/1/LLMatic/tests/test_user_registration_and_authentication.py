import unittest
from app import app, db
from app.models import User


class UserRegistrationAndAuthenticationTestCase(unittest.TestCase):

	def setUp(self):
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
		self.app = app.test_client()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_user_registration(self):
		user = User(email='test@example.com')
		user.set_password('testpassword')
		db.session.add(user)
		db.session.commit()
		assert User.query.filter_by(email='test@example.com').first() is not None

	def test_user_authentication(self):
		user = User(email='test@example.com')
		user.set_password('testpassword')
		db.session.add(user)
		db.session.commit()
		assert user.check_password('testpassword')
		assert not user.check_password('wrongpassword')
