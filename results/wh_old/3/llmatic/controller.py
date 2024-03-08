from models import User, Chat, GroupChat, Message, ImageMessage


class Controller:
	def __init__(self):
		self.users = {}

	def create_user(self, username):
		user = User(username)
		self.users[username] = user
		return user

	def create_chat(self, user1, user2):
		chat = Chat([user1, user2])
		self.users[user1].chats.append(chat)
		self.users[user2].chats.append(chat)
		return chat

	def create_group_chat(self, username, users):
		group_chat = self.users[username].create_group_chat(users)
		for user in users:
			self.users[user].chats.append(group_chat)
		return group_chat

	def send_message(self, sender, chat_id, content):
		message = Message(sender, content)
		message.encrypt()
		self.users[sender].send_message(chat_id, message)

	def send_image(self, sender, chat_id, image_content):
		message = ImageMessage(sender, image_content)
		self.users[sender].send_message(chat_id, message)

	def read_messages(self, username, chat_id):
		messages = self.users[username].read_message(chat_id)
		for message in messages:
			message.decrypt()
		return messages

