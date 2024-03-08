from datetime import datetime
import base64
from database import Database


class Message:
	def __init__(self, sender, receiver, content):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.timestamp = None
		self.read_receipt = False
		self.encrypted = False
		self.queued = False

	def send(self, db):
		self.timestamp = datetime.now()
		self.encrypt()
		if not self.receiver.online:
			self.queued = True
		else:
			db.add_message(self)

	def receive(self):
		self.read_receipt = True

	def encrypt(self):
		self.content = base64.b64encode(self.content.encode()).decode()
		self.encrypted = True

	def decrypt(self):
		self.content = base64.b64decode(self.content.encode()).decode()
		self.encrypted = False
