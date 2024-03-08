from user import User
from message import Message


class Chat:
	def __init__(self, user1, user2):
		self.user1 = user1
		self.user2 = user2
		self.messages = []

	def send_message(self, sender, receiver, content):
		message = Message(content, sender, receiver)
		message.send()
		self.messages.append(message)

	def receive_message(self, message):
		message.receive()

	def encrypt_message(self, message):
		# Simple encryption logic for demonstration
		message.content = ''.join(chr(ord(c) + 1) for c in message.content)

	def decrypt_message(self, message):
		# Simple decryption logic for demonstration
		message.content = ''.join(chr(ord(c) - 1) for c in message.content)

	def handle_read_receipt(self, message):
		message.read = True
