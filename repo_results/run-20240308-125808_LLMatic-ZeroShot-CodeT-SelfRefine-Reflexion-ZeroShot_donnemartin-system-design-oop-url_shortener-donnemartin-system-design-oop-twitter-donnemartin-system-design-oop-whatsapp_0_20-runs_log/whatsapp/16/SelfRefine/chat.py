from dataclasses import dataclass
from db import db
import uuid

@dataclass
class Chat(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String, nullable=False)

	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name

	def to_dict(self):
		return {'id': self.id, 'name': self.name}
