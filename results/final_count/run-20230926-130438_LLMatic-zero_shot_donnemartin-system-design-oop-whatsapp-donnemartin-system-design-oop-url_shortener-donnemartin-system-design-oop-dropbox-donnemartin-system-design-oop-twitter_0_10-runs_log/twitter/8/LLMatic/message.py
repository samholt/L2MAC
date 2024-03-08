from trending import users_db
class Message:
	def __init__(self, sender, recipient, text):
		self.sender = sender
		self.recipient = recipient
		self.text = text

	def send_message(self):
		if self.recipient in users_db and self.sender not in users_db[self.recipient].get('blocked_users', []):
			return {'sender': self.sender, 'recipient': self.recipient, 'text': self.text}
		else:
			return 'Message not sent. You are blocked by the recipient.'
