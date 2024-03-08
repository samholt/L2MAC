from uuid import uuid4

class Chat:
	def __init__(self, user):
		self.id = str(uuid4())
		self.users = [user]
		self.messages = []

	def to_dict(self):
		return {
			'id': self.id,
			'users': [user.id for user in self.users],
			'messages': self.messages
		}

	def send_message(self, sender_id, content):
		message = {'sender_id': sender_id, 'content': content}
		self.messages.append(message)
		return message
