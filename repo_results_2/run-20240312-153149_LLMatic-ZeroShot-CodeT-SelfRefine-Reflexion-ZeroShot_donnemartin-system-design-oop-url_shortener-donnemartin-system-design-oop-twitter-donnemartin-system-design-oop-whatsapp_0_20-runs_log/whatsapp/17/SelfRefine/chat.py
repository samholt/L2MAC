from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from app import db
import uuid

@dataclass
class Chat(db.Model):
	id: str
	name: str
	users: list
	messages: list

	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String, nullable=False)
	users = db.relationship('User', backref='chat', lazy=True)
	messages = db.relationship('Message', backref='chat', lazy=True)

	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name

	def add_user(self, user_id):
		self.users.append(user_id)

	def send_message(self, user_id, content):
		message = Message(user_id, content)
		self.messages.append(message)
		return message

	def to_dict(self):
		return {'id': self.id, 'name': self.name, 'users': [user.to_dict() for user in self.users], 'messages': [message.to_dict() for message in self.messages]}

@dataclass
class Message(db.Model):
	user_id: str
	content: str

	id = db.Column(db.String, primary_key=True)
	user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
	content = db.Column(db.String, nullable=False)

	def to_dict(self):
		return {'user_id': self.user_id, 'content': self.content}
