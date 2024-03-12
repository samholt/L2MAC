from datetime import datetime
from user import User


class Message:
	def __init__(self, sender: User, receiver: User, text: str):
		self.sender = sender
		self.receiver = receiver
		self.text = text
		self.timestamp = datetime.now()
		self.id = id(self)

	def send(self, db: dict):
		if self.sender in self.receiver.blocked_users:
			return 'User is blocked'
		else:
			db[self.id] = self
			return 'Message sent'

	def block_user(self, user: User):
		self.receiver.blocked_users.add(user)
		return 'User blocked'

	def unblock_user(self, user: User):
		self.receiver.blocked_users.remove(user)
		return 'User unblocked'
