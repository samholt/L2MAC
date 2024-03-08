from dataclasses import dataclass, field
from typing import List
from uuid import uuid4

@dataclass
class Chat:
	id: str = field(default_factory=lambda: str(uuid4()))
	name: str
	messages: List['Message'] = field(default_factory=list)

	def to_dict(self):
		return {'id': self.id, 'name': self.name, 'messages': [message.to_dict() for message in self.messages]}
