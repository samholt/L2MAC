class View:
	def __init__(self, controller):
		self.controller = controller

	def display_chat_history(self, chat_id):
		chat = self.controller.get_chat(chat_id)
		if chat:
			for message in chat.get_history():
				print(f'{message.sender}: {message.content}')

	def display_unread_messages(self, username, chat_id):
		messages = self.controller.read_messages(username, chat_id)
		if messages:
			for message in messages:
				print(f'{message.sender}: {message.content}')

	def create_user(self, username):
		self.controller.create_user(username)
		print(f'User {username} created.')

	def create_chat(self, user1, user2):
		self.controller.create_chat(user1, user2)
		print(f'Chat between {user1} and {user2} created.')

	def create_group_chat(self, username, users):
		self.controller.create_group_chat(username, users)
		print(f'Group chat with {username} and {users} created.')

	def send_message(self, sender, chat_id, content):
		self.controller.send_message(sender, chat_id, content)
		print(f'Message sent by {sender}.')

	def send_image(self, sender, chat_id, image_content):
		self.controller.send_image(sender, chat_id, image_content)
		print(f'Image sent by {sender}.')
