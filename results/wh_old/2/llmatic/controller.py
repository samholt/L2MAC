from models import User, Message, Chat, GroupChat, ImageMessage


class Controller:
	def __init__(self):
		self.users = {}

	def create_user(self, id: str, name: str):
		user = User(id=id, name=name, chats=[])
		self.users[id] = user
		return user

	def send_message(self, sender_id: str, receiver_id: str, content: str):
		sender = self.users.get(sender_id)
		receiver = self.users.get(receiver_id)
		if sender and receiver:
			message = Message(id=str(len(sender.chats) + 1), content=content, sender=sender, status='sent')
			chat = self.get_chat(sender, receiver)
			if not chat:
				chat = Chat(id=str(len(sender.chats) + 1), users=[sender, receiver], messages=[])
				sender.chats.append(chat)
				receiver.chats.append(chat)
			chat.add_message(message)
			message.set_status('delivered')

	def send_image_message(self, sender_id: str, receiver_id: str, image_path: str):
		sender = self.users.get(sender_id)
		receiver = self.users.get(receiver_id)
		if sender and receiver:
			message = ImageMessage(id=str(len(sender.chats) + 1), content='', sender=sender, status='sent', image_path=image_path)
			chat = self.get_chat(sender, receiver)
			if not chat:
				chat = Chat(id=str(len(sender.chats) + 1), users=[sender, receiver], messages=[])
				sender.chats.append(chat)
				receiver.chats.append(chat)
			chat.add_message(message)
			message.set_status('delivered')

	def create_group_chat(self, creator_id: str, user_ids: list):
		creator = self.users.get(creator_id)
		users = [self.users.get(user_id) for user_id in user_ids if self.users.get(user_id)]
		if creator and users:
			group_chat = creator.create_group_chat(users)
			for user in users:
				user.chats.append(group_chat)
			return group_chat

	def get_chat(self, user1: User, user2: User) -> Chat:
		for chat in user1.chats:
			if user2 in chat.users:
				return chat
		return None

