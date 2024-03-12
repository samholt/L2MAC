import uuid
from dataclasses import dataclass

@dataclass
class Chat:
	id: str
	name: str
	participants: list
	messages: list

	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name
		self.participants = []
		self.messages = []

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'participants': self.participants,
			'messages': self.messages
		}
