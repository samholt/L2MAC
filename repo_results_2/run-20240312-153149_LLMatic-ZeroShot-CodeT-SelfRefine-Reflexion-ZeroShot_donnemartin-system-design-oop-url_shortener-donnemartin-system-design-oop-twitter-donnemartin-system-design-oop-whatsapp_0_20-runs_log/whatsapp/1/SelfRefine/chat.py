from dataclasses import dataclass, field
from typing import List
from uuid import uuid4
from app import db

@dataclass
class Chat(db.Model):
	id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
	name = db.Column(db.String, nullable=False)
	messages = db.relationship('Message', backref='chat', lazy=True)

	def update(self, data):
		self.name = data.get('name', self.name)

	def add_message(self, message):
		self.messages.append(message)

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'messages': [message.to_dict() for message in self.messages]
		}
