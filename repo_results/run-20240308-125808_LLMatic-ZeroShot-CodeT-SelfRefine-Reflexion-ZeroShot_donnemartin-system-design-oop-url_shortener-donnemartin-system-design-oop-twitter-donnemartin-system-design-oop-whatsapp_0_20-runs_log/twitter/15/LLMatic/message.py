from datetime import datetime


class Message:
	def __init__(self, sender, receiver, text):
		self.sender = sender
		self.receiver = receiver
		self.text = text
		self.timestamp = datetime.now()

	def send_message(self, db):
		if self.sender in self.receiver.blocked_users:
			return 'You are blocked from sending messages to this user.'
		else:
			db[self.timestamp] = self
			return 'Message sent.'
