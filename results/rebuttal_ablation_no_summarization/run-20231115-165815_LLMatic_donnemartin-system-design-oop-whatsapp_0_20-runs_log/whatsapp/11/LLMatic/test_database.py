import unittest
from database import MockDatabase

class DatabaseTestCase(unittest.TestCase):
	def setUp(self):
		self.db = MockDatabase()

	# existing tests...

	def test_insert_message(self):
		self.db.insert_message('1', 'user1', 'user2', 'Hello, user2!')
		messages = self.db.get_offline_messages('user2')
		self.assertIn('1', messages)

	def test_clear_offline_messages(self):
		self.db.insert_message('1', 'user1', 'user2', 'Hello, user2!')
		self.db.clear_offline_messages('user2')
		messages = self.db.get_offline_messages('user2')
		self.assertEqual(messages, [])

if __name__ == '__main__':
	unittest.main()
