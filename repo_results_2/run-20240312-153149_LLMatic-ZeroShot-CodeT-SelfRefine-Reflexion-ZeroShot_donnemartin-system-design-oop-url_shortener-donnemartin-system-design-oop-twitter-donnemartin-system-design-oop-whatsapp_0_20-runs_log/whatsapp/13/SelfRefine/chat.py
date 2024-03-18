from dataclasses import dataclass, field
import uuid

@dataclass
class Chat:
	name: str
	picture: str
	admin_id: str
	participants: list = field(default_factory=list)
	id: str = field(default_factory=lambda: str(uuid.uuid4()))

	def __init__(self, name, picture, admin_id):
		self.name = name
		self.picture = picture
		self.admin_id = admin_id

	def add_participant(self, participant_id):
		self.participants.append(participant_id)

	def remove_participant(self, participant_id):
		self.participants.remove(participant_id)

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'picture': self.picture,
			'admin_id': self.admin_id,
			'participants': self.participants
		}
