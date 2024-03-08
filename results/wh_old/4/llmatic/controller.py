from user import User
from chat import Chat
from group_chat import GroupChat
from message import Message
from image_message import ImageMessage


class Controller:
	def __init__(self):
		self.users = {}
		self.chats = {}

	def create_user(self, id, name):
		user = User(id, name)
		self.users[id] = user
		return user

	def create_chat(self, user_ids):
		for user_id in user_ids:
			if user_id not in self.users:
				raise Exception(f'User with id {user_id} does not exist')
		chat = Chat(str(len(self.chats)), user_ids)
		self.chats[chat.id] = chat
		for user_id in user_ids:
			self.users[user_id].chats[chat.id] = chat
		return chat

	def create_group_chat(self, user_ids):
		for user_id in user_ids:
			if user_id not in self.users:
				raise Exception(f'User with id {user_id} does not exist')
		group_chat = GroupChat(str(len(self.chats)), user_ids)
		self.chats[group_chat.id] = group_chat
		for user_id in user_ids:
			self.users[user_id].chats[group_chat.id] = group_chat
		return group_chat

	def send_message(self, sender_id, receiver_id, chat_id, content):
		message = Message(str(len(self.chats[chat_id].messages)), sender_id, receiver_id, content)
		self.users[sender_id].send_message(chat_id, message)
		self.users[receiver_id].receive_message(chat_id, message)
		return message

	def send_image_message(self, sender_id, receiver_id, chat_id, content, image_data):
		message = ImageMessage(str(len(self.chats[chat_id].messages)), sender_id, receiver_id, content, image_data)
		self.users[sender_id].send_message(chat_id, message)
		self.users[receiver_id].receive_message(chat_id, message)
		return message

	def view_chat_history(self, user_id, chat_id):
		return self.users[user_id].view_chat_history(chat_id)

