from datetime import datetime
import base64


class Message:
	def __init__(self, sender, receiver, content, type='text'):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.timestamp = datetime.now()
		self.read_receipt = False
		self.encryption = False
		self.type = type

	def send(self):
		if self.encryption:
			self.content = self.encrypt()
		return {'sender': self.sender, 'receiver': self.receiver, 'content': self.content, 'timestamp': self.timestamp, 'read_receipt': self.read_receipt, 'type': self.type}

	def receive(self):
		if self.encryption:
			self.content = self.decrypt()
		self.read_receipt = True
		return self.content

	def read(self):
		self.read_receipt = True
		return self.content

	def encrypt(self):
		return base64.b64encode(self.content.encode()).decode()

	def decrypt(self):
		return base64.b64decode(self.content.encode()).decode()

	def share_image(self, image_path):
		with open(image_path, 'rb') as image_file:
			self.content = base64.b64encode(image_file.read()).decode()
			self.type = 'image'
		return self.content

	def send_emoji(self, emoji):
		self.content = emoji
		self.type = 'emoji'
		return self.content
