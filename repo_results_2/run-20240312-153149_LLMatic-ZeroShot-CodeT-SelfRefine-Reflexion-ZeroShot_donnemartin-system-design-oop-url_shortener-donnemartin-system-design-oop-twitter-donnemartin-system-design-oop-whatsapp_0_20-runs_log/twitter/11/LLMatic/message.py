class Message:
	def __init__(self):
		self.messages = {}
		self.blocked_users = {}

	def send(self, sender, receiver, message):
		if sender in self.blocked_users and receiver in self.blocked_users[sender]:
			return 'User is blocked'
		if receiver not in self.messages:
			self.messages[receiver] = []
		self.messages[receiver].append((sender, message))
		return 'Message sent'

	def block_user(self, user, blockee):
		if user not in self.blocked_users:
			self.blocked_users[user] = []
		self.blocked_users[user].append(blockee)
		return 'User blocked'

	def unblock_user(self, user, blockee):
		if user in self.blocked_users and blockee in self.blocked_users[user]:
			self.blocked_users[user].remove(blockee)
		return 'User unblocked'
