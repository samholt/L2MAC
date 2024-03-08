import unittest
from main import app
from models import User, Message

class TestCase(unittest.TestCase):

	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
		self.app = app.test_client()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_send_message(self):
		u1 = User(email='john@example.com')
		u1.set_password('cat')
		u2 = User(email='susan@example.com')
		u2.set_password('dog')
		db.session.add(u1)
		db.session.add(u2)
		db.session.commit()
		u1.send_message(u2, 'Hello, Susan!')
		msg = Message.query.filter_by(text='Hello, Susan!').first()
		self.assertIsNotNone(msg)
		self.assertEqual(msg.author, u1)
		self.assertEqual(msg.recipient, u2)

if __name__ == '__main__':
	unittest.main()
