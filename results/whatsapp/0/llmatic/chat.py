from user import User
from message import Message

class Chat:
	def __init__(self, user1: User, user2: User):
		self.user1 = user1
		self.user2 = user2
		self.messages = []

	def send_message(self, sender: User, content: str):
		message = Message(sender, content)
		self.messages.append(message)
		return message

	def receive_message(self):
		if self.messages:
			return self.messages[-1]
		else:
			return None

	def encrypt_message(self, message: Message):
		# This is a placeholder for the encryption logic
		encrypted_content = message.content[::-1]
		return Message(message.sender, encrypted_content)
