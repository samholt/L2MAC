from models.user import User
from models.chat import Chat
from models.group_chat import GroupChat
from models.message import Message
from models.image_message import ImageMessage

class Controller:
	def __init__(self):
		self.users = {}

	def create_user(self, username):
		if username not in self.users:
			self.users[username] = User(username)
		return self.users[username]

	def create_chat(self, usernames):
		users = [self.users[username] for username in usernames if username in self.users]
		chat = Chat(users)
		for user in users:
			user.chats.append(chat)
		return chat

	def create_group_chat(self, username, other_usernames):
		user = self.users[username]
		other_users = [self.users[other_username] for other_username in other_usernames]
		group_chat = user.create_group_chat(other_users)
		return group_chat

	def send_message(self, sender_username, chat, content):
		sender = self.users[sender_username]
		sender.send_message(chat, content)

	def send_image(self, sender_username, chat, image_path):
		sender = self.users[sender_username]
		message = ImageMessage(sender, chat, image_path)
		message.encrypt_content()
		chat.add_message(message)

	def receive_message(self, receiver_username, message):
		receiver = self.users[receiver_username]
		receiver.receive_message(message)
		message.chat.messages.remove(message)

	def view_chat_history(self, username, chat):
		user = self.users[username]
		return [(message.sender.username, message.content, message.status) for message in user.view_chat_history(chat)]

