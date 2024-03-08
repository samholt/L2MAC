from user import User
from chat import Chat
from message import Message
from group import Group
from status import Status


class WebApp:
	def __init__(self):
		self.users = []
		self.chats = []
		self.groups = []
		self.statuses = []

	def display(self):
		print('Users:', self.users)
		print('Chats:', self.chats)
		print('Groups:', self.groups)
		print('Statuses:', self.statuses)

	def handle_user_interaction(self, interaction):
		# Simulate user interaction based on text input
		if interaction == 'display':
			self.display()
		elif interaction.startswith('create user '):
			username, password = interaction.split(' ')[2:]
			self.users.append(User(username, password))
			print('User created:', username)
		elif interaction.startswith('send message '):
			sender, receiver, content = interaction.split(' ')[2:]
			chat = Chat(sender, receiver)
			chat.send_message(sender, receiver, content)
			self.chats.append(chat)
			print('Message sent:', content)
		elif interaction.startswith('create group '):
			name, picture, admin = interaction.split(' ')[2:]
			self.groups.append(Group(name, picture, admin))
			print('Group created:', name)
		elif interaction.startswith('post status '):
			user, image, visibility = interaction.split(' ')[2:]
			status = Status(user, image, visibility)
			status.post()
			self.statuses.append(status)
			print('Status posted:', image)
		else:
			print('Unknown interaction:', interaction)
