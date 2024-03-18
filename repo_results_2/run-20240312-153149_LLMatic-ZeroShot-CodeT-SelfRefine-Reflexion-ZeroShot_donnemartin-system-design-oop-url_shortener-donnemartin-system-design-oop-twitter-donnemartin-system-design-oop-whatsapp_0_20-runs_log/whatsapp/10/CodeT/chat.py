from dataclasses import dataclass
import uuid

@dataclass
class Chat:
	id: str
	name: str
	participants: dict
	messages: list

	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name
		self.participants = {}
		self.messages = []

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'participants': {id: participant.to_dict() for id, participant in self.participants.items()},
			'messages': self.messages
		}
