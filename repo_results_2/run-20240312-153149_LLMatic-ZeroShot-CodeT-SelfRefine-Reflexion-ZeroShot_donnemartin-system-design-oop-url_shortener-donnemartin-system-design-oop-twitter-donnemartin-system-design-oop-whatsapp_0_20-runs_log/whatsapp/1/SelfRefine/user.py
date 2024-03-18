from dataclasses import dataclass, field
from typing import List
from uuid import uuid4
from app import db
from chat import Chat

@dataclass
class User(db.Model):
	id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
	email = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, nullable=False)
	profile_picture = db.Column(db.String)
	status_message = db.Column(db.String)
	contacts = db.relationship('User', backref='user', lazy=True)
	chats = db.relationship('Chat', backref='user', lazy=True)

	def reset_password(self):
		self.password = 'new_password'

	def update_profile(self, data):
		self.profile_picture = data.get('profile_picture', self.profile_picture)
		self.status_message = data.get('status_message', self.status_message)

	def add_contact(self, contact):
		self.contacts.append(contact)

	def remove_contact(self, contact):
		self.contacts.remove(contact)

	def add_chat(self, chat):
		self.chats.append(chat)

	def remove_chat(self, chat):
		self.chats.remove(chat)

	def to_dict(self):
		return {
			'id': self.id,
			'email': self.email,
			'profile_picture': self.profile_picture,
			'status_message': self.status_message,
			'contacts': [contact.id for contact in self.contacts],
			'chats': [chat.id for chat in self.chats]
		}
