from dataclasses import dataclass
import uuid

@dataclass
class Chat:
	id: str
	name: str
	members: dict
	messages: list

	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name
		self.members = {}
		self.messages = []

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'members': self.members,
			'messages': self.messages
		}
