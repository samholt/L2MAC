from datetime import datetime
from user import User


class Message:
	def __init__(self, sender: User, recipient: User, text: str):
		self.sender = sender
		self.recipient = recipient
		self.text = text
		self.timestamp = datetime.now()

	def send_message(self):
		if self.sender in self.recipient.blocked_users:
			return 'Message not sent. You are blocked by the recipient.'
		else:
			self.recipient.inbox.append(self)
			return 'Message sent successfully.'
