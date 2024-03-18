import datetime


class Message:
	def __init__(self):
		self.messages = {}
		self.blocked_users = {}

	def send_message(self, sender, receiver, content):
		if receiver in self.blocked_users and sender in self.blocked_users[receiver]:
			return 'User is blocked'
		timestamp = datetime.datetime.now()
		message = {'sender': sender, 'receiver': receiver, 'content': content, 'timestamp': timestamp}
		if receiver not in self.messages:
			self.messages[receiver] = []
		self.messages[receiver].append(message)
		return 'Message sent'

	def block_user(self, user, other_user):
		if user not in self.blocked_users:
			self.blocked_users[user] = []
		self.blocked_users[user].append(other_user)
		return 'User blocked'
