class Message:
	def __init__(self, sender, receiver, content):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.read = False
		self.encrypted = False

	def mark_as_read(self):
		self.read = True

	def encrypt_message(self):
		self.content = self.content[::-1]
		self.encrypted = True

	def decrypt_message(self):
		if self.encrypted:
			self.content = self.content[::-1]
			self.encrypted = False

class Messaging:
	def __init__(self):
		self.messages = []

	def send_message(self, sender, receiver, content):
		message = Message(sender, receiver, content)
		self.messages.append(message)
		return True

	def get_unread_messages(self, receiver):
		return [message for message in self.messages if message.receiver == receiver and not message.read]

	def read_message(self, message):
		if message in self.messages:
			message.mark_as_read()

	def encrypt_message(self, message):
		if message in self.messages:
			message.encrypt_message()

	def decrypt_message(self, message):
		if message in self.messages and message.encrypted:
			message.decrypt_message()
