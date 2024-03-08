import json
import base64


class Message:
	def __init__(self, sender, receiver, content):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.read_receipt = False
		self.encrypted = False
		self.image = None

	def send_message(self, messages):
		if self.encrypted:
			self.content = self.decrypt_message()
		messages.append(self)
		return messages

	def receive_message(self, messages):
		for message in messages:
			if message.receiver == self.receiver:
				message.read_receipt = True
		return messages

	def set_read_receipt(self):
		self.read_receipt = True

	def encrypt_message(self):
		self.content = base64.b64encode(self.content.encode()).decode()
		self.encrypted = True

	def decrypt_message(self):
		return base64.b64decode(self.content.encode()).decode()

	def share_image(self, image):
		self.image = image

