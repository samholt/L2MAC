from user import User
from chat import Chat
from message import Message
from group import Group
from status import Status
from webapp import WebApp

class GlobalChatService:
	def __init__(self):
		self.users = []
		self.chats = []
		self.groups = []
		self.statuses = []
		self.webapp = WebApp()

	def register_user(self, email, password):
		user = User(email, password)
		self.users.append(user)
		return user

	def create_chat(self, user1, user2):
		chat = Chat(user1, user2)
		self.chats.append(chat)
		return chat

	def create_group(self, name, picture, creator):
		group = Group(name, picture, creator)
		self.groups.append(group)
		return group

	def post_status(self, user_id, status_content):
		status = Status(user_id, status_content)
		self.statuses.append(status)
		return status

def test_integration():
	gcs = GlobalChatService()

	# Test user registration
	user1 = gcs.register_user('user1@example.com', 'password1')
	user2 = gcs.register_user('user2@example.com', 'password2')
	assert user1 in gcs.users
	assert user2 in gcs.users

	# Test chat creation
	chat = gcs.create_chat(user1, user2)
	assert chat in gcs.chats

	# Test message sending and receiving
	message = chat.send_message(user1, 'Hello, world!')
	assert message in chat.messages
	assert chat.receive_message() == message

	# Test group creation
	group = gcs.create_group('Group 1', 'picture.jpg', user1)
	assert group in gcs.groups

	# Test status posting
	status = gcs.post_status(user1.email, 'Hello, world!')
	assert status in gcs.statuses

def main():
	gcs = GlobalChatService()

	# Simulate user registration
	user1 = gcs.register_user('user1@example.com', 'password1')
	user2 = gcs.register_user('user2@example.com', 'password2')

	# Simulate chat creation
	chat = gcs.create_chat(user1, user2)

	# Simulate message sending and receiving
	chat.send_message(user1, 'Hello, world!')
	chat.receive_message()

	# Simulate group creation
	gcs.create_group('Group 1', 'picture.jpg', user1)

	# Simulate status posting
	gcs.post_status(user1.email, 'Hello, world!')

def test_main():
	main()

test_integration()
test_main()

if __name__ == "__main__":
	main()
