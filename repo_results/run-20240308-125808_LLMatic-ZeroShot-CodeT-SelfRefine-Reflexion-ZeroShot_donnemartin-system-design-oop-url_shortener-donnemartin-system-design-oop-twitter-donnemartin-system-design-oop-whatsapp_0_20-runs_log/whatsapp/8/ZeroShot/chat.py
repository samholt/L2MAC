from dataclasses import dataclass, field
import uuid

@dataclass
class Chat:
	id: str = field(default_factory=lambda: str(uuid.uuid4()))
	name: str
	picture: str = None
	participants: list = field(default_factory=list)

	def update_chat(self, data):
		self.name = data.get('name', self.name)
		self.picture = data.get('picture', self.picture)
		self.participants = data.get('participants', self.participants)

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'picture': self.picture,
			'participants': self.participants
		}
