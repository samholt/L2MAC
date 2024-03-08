import unittest
from app import create_app, db
from app.models import User


class ContactsTestCase(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()
		self.app_context.pop()

	def test_block_contact(self):
		u1 = User(username='user1', email='user1@example.com')
		u2 = User(username='user2', email='user2@example.com')
		db.session.add(u1)
		db.session.add(u2)
		db.session.commit()
		with self.app.test_client() as c:
			response = c.post('/contacts/block', json={'user_id': u1.id, 'contact_id': u2.id})
		self.assertEqual(response.status_code, 200)
		self.assertTrue(u2 in u1.blocked_contacts)

	def test_unblock_contact(self):
		u1 = User(username='user1', email='user1@example.com')
		u2 = User(username='user2', email='user2@example.com')
		db.session.add(u1)
		db.session.add(u2)
		u1.block_contact(u2)
		db.session.commit()
		with self.app.test_client() as c:
			response = c.post('/contacts/unblock', json={'user_id': u1.id, 'contact_id': u2.id})
		self.assertEqual(response.status_code, 200)
		self.assertFalse(u2 in u1.blocked_contacts)
