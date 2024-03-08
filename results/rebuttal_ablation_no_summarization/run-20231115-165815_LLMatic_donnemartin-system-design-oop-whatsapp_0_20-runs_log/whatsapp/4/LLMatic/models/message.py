import json

class Message:
	def __init__(self, id, sender, receiver, content, read_receipt, encryption):
		self.id = id
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.read_receipt = read_receipt
		self.encryption = encryption

	def to_dict(self):
		return {
			'id': self.id,
			'sender': self.sender,
			'receiver': self.receiver,
			'content': self.content,
			'read_receipt': self.read_receipt,
			'encryption': self.encryption
		}

	def __repr__(self):
		return str(self.to_dict())

	def __str__(self):
		return str(self.to_dict())
