from dataclasses import dataclass
from typing import List
from PIL import Image
from datetime import datetime


@dataclass
class User:
	id: int
	email: str
	password: str
	profile_picture: str
	status_message: str
	privacy_settings: str
	last_seen: str
	contacts: List[str]
	blocked_contacts: List[str]
	is_online: bool = False

	@classmethod
	def create(cls, id: int, email: str, password: str, profile_picture: str, status_message: str, privacy_settings: str, last_seen: str, contacts: List[str], blocked_contacts: List[str]):
		return cls(id, email, password, profile_picture, status_message, privacy_settings, last_seen, contacts, blocked_contacts)

	def register(self, form):
		self.email = form.email.data
		self.password = form.password.data

	def update_profile(self, form):
		self.profile_picture = form.profile_picture.data
		self.status_message = form.status_message.data

	def update_privacy(self, form):
		self.privacy_settings = form.privacy_settings.data

	def add_contact(self, form):
		self.contacts.append(form.email.data)

	def block_contact(self, form):
		self.blocked_contacts.append(form.email.data)

	def read(self):
		return self.__dict__

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if hasattr(self, key):
				setattr(self, key, value)

	def delete(self):
		del self

@dataclass
class Group:
	name: str
	picture: str
	members: List[str]

	@classmethod
	def create(cls, name: str, picture: str, members: List[str]):
		return cls(name, picture, members)

	def create_group(self, form):
		self.name = form.name.data
		self.picture = form.picture.data
		self.members = form.participants.data.split(', ')

	def read(self):
		return self.__dict__

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if hasattr(self, key):
				setattr(self, key, value)

	def delete(self):
		del self

@dataclass
class Message:
	sender: str
	recipient: str
	content: str
	timestamp: str
	read_receipt: bool
	is_sent: bool = False

	@classmethod
	def create(cls, sender: str, recipient: str, content: str, timestamp: str, read_receipt: bool):
		return cls(sender, recipient, content, timestamp, read_receipt)

	def send_message(self, form):
		self.content = form.content.data
		self.recipient = form.receiver.data

	def read(self):
		return self.__dict__

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if hasattr(self, key):
				setattr(self, key, value)

	def delete(self):
		del self

@dataclass
class Status:
	id: int
	user: str
	content: str
	visibility: str
	expiry_time: datetime

	@classmethod
	def create(cls, id: int, user: str, content: str, visibility: str, expiry_time: datetime):
		return cls(id, user, content, visibility, expiry_time)

	def post_status(self, form):
		self.content = form.image_file.data
		self.visibility = form.visibility.data

	def read(self):
		return self.__dict__

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if hasattr(self, key):
				setattr(self, key, value)

	def delete(self):
		del self
