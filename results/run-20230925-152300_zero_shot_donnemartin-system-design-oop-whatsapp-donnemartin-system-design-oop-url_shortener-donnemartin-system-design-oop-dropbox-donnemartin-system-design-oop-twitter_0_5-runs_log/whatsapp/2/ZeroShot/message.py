import uuid
from datetime import datetime

class Message:
	def __init__(self, sender, content):
		self.id = str(uuid.uuid4())
		self.sender = sender
		self.content = content
		self.timestamp = datetime.now()
		self.read_receipts = []

	def to_dict(self):
		return {
			'id': self.id,
			'sender': self.sender.id,
			'content': self.content,
			'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
			'read_receipts': [user.id for user in self.read_receipts]
		}
