import datetime


class Message:
	def __init__(self):
		self.database = {}
		self.blocked = {}

	def send(self, sender, receiver, text):
		if receiver in self.blocked.get(sender, []):
			return 'User is blocked'
		timestamp = datetime.datetime.now()
		message = {'sender': sender, 'receiver': receiver, 'text': text, 'timestamp': timestamp}
		self.database[timestamp] = message
		return 'Message sent'

	def block(self, user, to_block):
		if user not in self.blocked:
			self.blocked[user] = []
		self.blocked[user].append(to_block)
		return 'User blocked'
