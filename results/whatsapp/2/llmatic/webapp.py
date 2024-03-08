from user import User
from chat import Chat
from message import Message
from group import Group
from status import Status

class WebApp:
	def __init__(self):
		self.users = []
		self.chats = []
		self.messages = []
		self.groups = []
		self.statuses = []
		self.online_users = []

	def register_user(self, email, password):
		user = User(email, password)
		self.users.append(user)
		return user

	def login_user(self, user):
		if user in self.users:
			self.online_users.append(user)

	def logout_user(self, user):
		if user in self.online_users:
			self.online_users.remove(user)

	def create_chat(self, user1, user2):
		chat = Chat(user1, user2)
		self.chats.append(chat)
		return chat

	def send_message(self, chat, sender, receiver, content):
		message = Message(sender, receiver, content)
		chat.send_message(sender, receiver, content)
		self.messages.append(message)

	def create_group(self, name, picture=None):
		group = Group(name, picture)
		self.groups.append(group)
		return group

	def add_user_to_group(self, user, group):
		group.add_participant(user)

	def create_status(self, user, image, visibility='everyone'):
		status = Status(user, image, visibility)
		self.statuses.append(status)
		return status

	def is_online(self, user):
		return user in self.online_users
