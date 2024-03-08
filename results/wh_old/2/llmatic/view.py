from controller import Controller


class View:
	def __init__(self):
		self.controller = Controller()

	def create_user(self, id: str, name: str):
		return self.controller.create_user(id, name)

	def send_message(self, sender_id: str, receiver_id: str, content: str):
		self.controller.send_message(sender_id, receiver_id, content)

	def send_image_message(self, sender_id: str, receiver_id: str, image_path: str):
		self.controller.send_image_message(sender_id, receiver_id, image_path)

	def create_group_chat(self, creator_id: str, user_ids: list):
		return self.controller.create_group_chat(creator_id, user_ids)

	def view_chat_history(self, user_id: str, chat_id: str):
		user = self.controller.users.get(user_id)
		if user:
			return user.view_chat_history(chat_id)
		return 'User not found'

	def view_message_status(self, user_id: str, chat_id: str, message_id: str):
		user = self.controller.users.get(user_id)
		if user:
			chat = user.get_chat(chat_id)
			if chat:
				return chat.get_message_status(message_id)
			return 'Chat not found'
		return 'User not found'
