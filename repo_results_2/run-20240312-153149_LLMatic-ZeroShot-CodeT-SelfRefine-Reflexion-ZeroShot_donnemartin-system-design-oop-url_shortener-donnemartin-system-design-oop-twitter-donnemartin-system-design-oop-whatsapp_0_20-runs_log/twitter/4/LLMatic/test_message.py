import unittest
from message import Message


class TestMessage(unittest.TestCase):
	def setUp(self):
		self.message = Message('User1', 'User2', 'Hello')

	def test_send(self):
		self.assertEqual(self.message.send(), 'Message sent')

	def test_block_user(self):
		self.assertEqual(self.message.block_user('User3'), 'User blocked')
		self.assertEqual(self.message.send(), 'Message sent')

	def test_unblock_user(self):
		self.message.block_user('User3')
		self.assertEqual(self.message.unblock_user('User3'), 'User unblocked')
		self.assertEqual(self.message.send(), 'Message sent')


if __name__ == '__main__':
	unittest.main()
