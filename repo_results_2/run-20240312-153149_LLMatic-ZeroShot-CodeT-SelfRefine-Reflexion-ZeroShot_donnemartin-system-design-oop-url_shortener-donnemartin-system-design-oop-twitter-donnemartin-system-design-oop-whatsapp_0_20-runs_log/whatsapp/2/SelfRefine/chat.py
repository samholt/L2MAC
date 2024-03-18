from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from user import User
import uuid

db = SQLAlchemy()

@dataclass
class Message(db.Model):
	id: str = db.Column(db.String, primary_key=True)
	user_id: str = db.Column(db.String, db.ForeignKey('user.id'))
	content: str = db.Column(db.String, nullable=False)
	user = db.relationship('User', backref=db.backref('messages', lazy=True))

	def __init__(self, user, content):
		self.id = str(uuid.uuid4())
		self.user = user
		self.content = content

	def to_dict(self):
		return {'id': self.id, 'user': self.user.to_dict(), 'content': self.content}

@dataclass
class Chat(db.Model):
	id: str = db.Column(db.String, primary_key=True)
	name: str = db.Column(db.String, nullable=False)
	users = db.relationship('User', secondary='user_chat', backref=db.backref('chats', lazy=True))
	messages = db.relationship('Message', backref='chat', lazy=True)

	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name

	def add_user(self, user):
		self.users.append(user)

	def send_message(self, user, content):
		message = Message(user, content)
		self.messages.append(message)
		return message

	def to_dict(self):
		return {'id': self.id, 'name': self.name, 'users': [user.to_dict() for user in self.users], 'messages': [message.to_dict() for message in self.messages]}
