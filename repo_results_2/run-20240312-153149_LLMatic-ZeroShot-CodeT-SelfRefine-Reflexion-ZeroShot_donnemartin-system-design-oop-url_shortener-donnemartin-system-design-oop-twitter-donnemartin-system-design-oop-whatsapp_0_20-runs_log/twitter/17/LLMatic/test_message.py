import unittest
from message import Message


class TestMessage(unittest.TestCase):
	def setUp(self):
		self.message = Message('User1', 'User2', 'Hello')

	def test_send(self):
		self.assertEqual(self.message.send(), 'Message sent')
		self.message.block('User1')
		self.assertEqual(self.message.send(), 'User is blocked')

	def test_block(self):
		self.assertEqual(self.message.block('User3'), 'User blocked')


if __name__ == '__main__':
	unittest.main()
