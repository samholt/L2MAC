class Message:
	def __init__(self):
		self.messages = {}
		self.blocked_users = {}

	def send_message(self, sender, receiver, message):
		if receiver in self.blocked_users and sender in self.blocked_users[receiver]:
			return 'User is blocked'
		if receiver not in self.messages:
			self.messages[receiver] = []
		self.messages[receiver].append((sender, message))
		return 'Message sent'

	def receive_message(self, receiver):
		if receiver in self.messages:
			return self.messages[receiver]
		return []

	def block_user(self, user, blocked_user):
		if user not in self.blocked_users:
			self.blocked_users[user] = []
		self.blocked_users[user].append(blocked_user)
		return 'User blocked'

	def unblock_user(self, user, unblocked_user):
		if user in self.blocked_users and unblocked_user in self.blocked_users[user]:
			self.blocked_users[user].remove(unblocked_user)
		return 'User unblocked'
