import uuid

class Chat:
	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name
		self.participants = []
		self.admins = []
		self.messages = []

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'participants': [participant.id for participant in self.participants],
			'admins': [admin.id for admin in self.admins],
			'messages': [message.to_dict() for message in self.messages]
		}
