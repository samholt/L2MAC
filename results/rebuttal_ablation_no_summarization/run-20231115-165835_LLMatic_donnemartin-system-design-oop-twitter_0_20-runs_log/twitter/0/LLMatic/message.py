class Message:
	def __init__(self, sender, receiver):
		self.sender = sender
		self.receiver = receiver
		self.text = ''
		self.timestamp = ''
		self.blocked_users = []
		self.database = {}

	def send_message(self, text, timestamp):
		if self.receiver in self.blocked_users:
			return 'User is blocked'
		self.text = text
		self.timestamp = timestamp
		self.database[timestamp] = {'sender': self.sender, 'receiver': self.receiver, 'text': self.text}
		return 'Message sent'

	def block_user(self, user):
		self.blocked_users.append(user)
		return 'User blocked'
