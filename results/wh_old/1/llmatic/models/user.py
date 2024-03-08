from .message import Message
from .chat import Chat
from .group_chat import GroupChat

class User:
	def __init__(self, username):
		self.username = username
		self.chats = []

	def send_message(self, chat, content):
		message = Message(self, chat, content)
		chat.add_message(message)

	def receive_message(self, message):
		for chat in self.chats:
			if chat == message.chat:
				chat.add_message(message)
				break

	def create_group_chat(self, users):
		group_chat = GroupChat([self] + users)
		self.chats.append(group_chat)
		return group_chat

	def view_chat_history(self, chat):
		for c in self.chats:
			if c == chat:
				return c.messages
		return None

