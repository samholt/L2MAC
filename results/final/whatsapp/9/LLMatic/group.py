from user import User
from message import Message

class Group:
	def __init__(self, name: str, picture: str, participants: list, admins: list, messages: list):
		self.name = name
		self.picture = picture
		self.participants = participants
		self.admins = admins
		self.messages = messages

	def add_participant(self, user: User):
		self.participants.append(user)

	def remove_participant(self, user: User):
		self.participants.remove(user)

	def assign_admin(self, user: User):
		self.admins.append(user)

	def remove_admin(self, user: User):
		self.admins.remove(user)

	def send_message(self, message: Message):
		self.messages.append(message)
