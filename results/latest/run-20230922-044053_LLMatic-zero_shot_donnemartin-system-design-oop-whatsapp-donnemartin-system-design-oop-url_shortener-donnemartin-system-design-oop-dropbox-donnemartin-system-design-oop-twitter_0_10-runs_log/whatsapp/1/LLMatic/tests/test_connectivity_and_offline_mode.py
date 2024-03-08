import unittest
from app import app, db
from app.models import User, QueuedMessage


class ConnectivityAndOfflineModeTestCase(unittest.TestCase):
	def setUp(self):
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_last_seen(self):
		u = User(email='john@example.com')
		db.session.add(u)
		db.session.commit()
		self.assertIsNotNone(u.last_seen)

	def test_queued_messages(self):
		u1 = User(email='john@example.com')
		u2 = User(email='susan@example.com')
		db.session.add(u1)
		db.session.add(u2)
		db.session.commit()
		qm = QueuedMessage(user=u1, recipient=u2, text='Hello, Susan!')
		db.session.add(qm)
		db.session.commit()
		self.assertEqual(u1.queued_messages.count(), 1)
		self.assertEqual(u1.queued_messages.first().text, 'Hello, Susan!')


if __name__ == '__main__':
	unittest.main()
