import datetime


class Message:
	def __init__(self, sender_id, receiver_id, text):
		self.sender_id = sender_id
		self.receiver_id = receiver_id
		self.text = text
		self.timestamp = datetime.datetime.now()
		self.blocked_users = set()

	def send(self, db):
		if self.sender_id in self.blocked_users:
			return 'User is blocked'
		else:
			if 'messages' not in db:
				db['messages'] = []
			db['messages'].append(self)
			return 'Message sent'

	def block(self, user_id):
		self.blocked_users.add(user_id)
