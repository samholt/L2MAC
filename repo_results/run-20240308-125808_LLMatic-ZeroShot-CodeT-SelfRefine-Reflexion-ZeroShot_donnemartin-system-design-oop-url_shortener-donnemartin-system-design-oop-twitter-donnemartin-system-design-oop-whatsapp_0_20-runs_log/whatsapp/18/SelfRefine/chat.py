from dataclasses import dataclass
import uuid
from app import db

@dataclass
class Chat(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String, nullable=False)
	participants = db.Column(db.PickleType)
	messages = db.Column(db.PickleType)

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
