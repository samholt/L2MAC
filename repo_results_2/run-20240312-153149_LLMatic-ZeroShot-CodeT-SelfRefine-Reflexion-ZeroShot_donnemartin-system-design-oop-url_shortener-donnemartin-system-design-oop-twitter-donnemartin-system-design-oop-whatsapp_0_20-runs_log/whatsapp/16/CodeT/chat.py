import uuid

class Chat:
	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name
		self.messages = []

	def send_message(self, user_id, message):
		self.messages.append({'user_id': user_id, 'message': message})
