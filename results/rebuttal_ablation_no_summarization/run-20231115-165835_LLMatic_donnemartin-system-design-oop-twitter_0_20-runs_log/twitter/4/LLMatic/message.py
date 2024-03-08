class Message:
	def __init__(self, sender, receiver, content):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.blocked_users = []

	def send_message(self, receiver, content):
		if receiver in self.blocked_users:
			return 'User is blocked'
		else:
			new_message = Message(self.sender, receiver, content)
			return new_message

	def block_user(self, user):
		if user not in self.blocked_users:
			self.blocked_users.append(user)

	def unblock_user(self, user):
		if user in self.blocked_users:
			self.blocked_users.remove(user)
