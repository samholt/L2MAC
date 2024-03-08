from user import User
from chat import Chat
from message import Message

class WebApp:
	def __init__(self):
		self.users = []
		self.chats = []

	def register_user(self, email, password):
		user = User()
		user.register(email, password)
		self.users.append(user)

	def login_user(self, email, password):
		for user in self.users:
			if user.login(email, password):
				return user
		return None

	def send_message(self, sender_email, recipient_email, content, content_type):
		sender = self.get_user_by_email(sender_email)
		recipient = self.get_user_by_email(recipient_email)
		if sender and recipient:
			message = Message(sender, recipient, content, content_type)
			chat = self.get_chat_by_users(sender, recipient)
			if not chat:
				chat = Chat()
				self.chats.append(chat)
			chat.send_message(sender, recipient, message)

	def get_user_by_email(self, email):
		for user in self.users:
			if user.email == email:
				return user
		return None

	def get_chat_by_users(self, user1, user2):
		for chat in self.chats:
			if any(message for message in chat.messages if message[0] == user1 and message[1] == user2):
				return chat
		return None

	def restore_connectivity(self, email):
		user = self.get_user_by_email(email)
		if user:
			user.is_online = True
			for chat in self.chats:
				chat.restore_connectivity(user)

	def display_status(self, email):
		user = self.get_user_by_email(email)
		if user:
			return user.is_online
		return None
