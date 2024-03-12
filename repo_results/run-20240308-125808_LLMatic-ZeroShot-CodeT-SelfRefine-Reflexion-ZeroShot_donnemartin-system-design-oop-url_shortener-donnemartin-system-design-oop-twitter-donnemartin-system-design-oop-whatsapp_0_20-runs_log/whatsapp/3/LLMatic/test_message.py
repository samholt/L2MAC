import unittest
from message import Message
from user import User

class TestMessage(unittest.TestCase):
	def test_send(self):
		sender = User('sender@test.com', 'password')
		receiver = User('receiver@test.com', 'password')
		message = Message(sender, receiver, 'Hello, World!')
		message.send()
		self.assertEqual(len(receiver.queue), 1)

	def test_receive(self):
		sender = User('sender@test.com', 'password')
		receiver = User('receiver@test.com', 'password')
		message = Message(sender, receiver, 'Hello, World!')
		message.send()
		receiver.go_online()
		message.receive()
		self.assertTrue(message.read)

if __name__ == '__main__':
	unittest.main()
