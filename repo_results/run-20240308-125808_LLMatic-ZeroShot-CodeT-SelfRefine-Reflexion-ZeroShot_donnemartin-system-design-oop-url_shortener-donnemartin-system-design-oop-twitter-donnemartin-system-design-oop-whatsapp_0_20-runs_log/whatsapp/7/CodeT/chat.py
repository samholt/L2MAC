from dataclasses import dataclass, field
from typing import List

@dataclass
class Chat:
	id: str
	name: str
	participants: List[str]
	messages: List[dict] = field(default_factory=list)

	def update(self, data):
		self.name = data.get('name', self.name)
		self.participants = data.get('participants', self.participants)

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'participants': self.participants,
			'messages': self.messages
		}
