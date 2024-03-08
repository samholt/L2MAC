class Message:
	def __init__(self):
		self.blocked_users = {}

	def send(self, sender, receiver, message):
		if receiver in self.blocked_users and sender in self.blocked_users[receiver]:
			return 'User is blocked'
		else:
			return 'Message sent'

	def block(self, user, blocked_user):
		if user not in self.blocked_users:
			self.blocked_users[user] = []
		self.blocked_users[user].append(blocked_user)
		return 'User blocked'

	def unblock(self, user, unblocked_user):
		if user in self.blocked_users and unblocked_user in self.blocked_users[user]:
			self.blocked_users[user].remove(unblocked_user)
		return 'User unblocked'
