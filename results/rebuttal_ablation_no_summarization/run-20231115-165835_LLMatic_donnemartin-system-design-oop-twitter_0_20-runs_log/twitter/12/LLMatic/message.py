from user import users_db

messages_db = {}


class Message:
	def __init__(self, sender, receiver, text):
		self.sender = sender
		self.receiver = receiver
		self.text = text

	@staticmethod
	def send_message(sender, receiver, text):
		if sender in users_db and receiver in users_db:
			message = Message(sender, receiver, text)
			messages_db[message] = message
			return True
		return False

	@staticmethod
	def block_user(sender, user_to_block):
		if sender in users_db and user_to_block in users_db:
			users_db[sender].blocked_users.add(user_to_block)
			return True
		return False

	@staticmethod
	def unblock_user(sender, user_to_unblock):
		if sender in users_db and user_to_unblock in users_db:
			if user_to_unblock in users_db[sender].blocked_users:
				users_db[sender].blocked_users.remove(user_to_unblock)
				return True
		return False
