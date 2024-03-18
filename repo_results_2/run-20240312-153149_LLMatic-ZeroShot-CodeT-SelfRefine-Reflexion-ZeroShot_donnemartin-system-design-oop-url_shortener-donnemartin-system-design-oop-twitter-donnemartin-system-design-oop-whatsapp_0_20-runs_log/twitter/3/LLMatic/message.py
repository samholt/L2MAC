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
			self.messages[receiver] = [message]
		else:
			self.messages[receiver].append(message)
		return 'Message sent'

	def block_user(self, user, user_to_block):
		if user not in self.blocked_users:
			self.blocked_users[user] = [user_to_block]
		else:
			self.blocked_users[user].append(user_to_block)
		return 'User blocked'

	def unblock_user(self, user, user_to_unblock):
		if user in self.blocked_users and user_to_unblock in self.blocked_users[user]:
			self.blocked_users[user].remove(user_to_unblock)
			return 'User unblocked'
		return 'User not blocked'
