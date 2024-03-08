import uuid
from datetime import datetime

class Message:
	def __init__(self, sender, content):
		self.id = str(uuid.uuid4())
		self.timestamp = datetime.now()
		self.sender = sender
		self.content = content
		self.read_receipts = []

	def to_dict(self):
		return {
			'id': self.id,
			'timestamp': self.timestamp.isoformat(),
			'sender': self.sender.id,
			'content': self.content,
			'read_receipts': [receipt.to_dict() for receipt in self.read_receipts]
		}
