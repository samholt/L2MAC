from dataclasses import dataclass
from typing import List, Optional


@dataclass
class User:
	id: str
	name: str
	chats: List['Chat']

	def send_message(self, chat_id: str, message: 'Message'):
		chat = self.get_chat(chat_id)
		if chat:
			chat.add_message(message)
			message.set_status('delivered')

	def receive_message(self, message: 'Message'):
		message.set_status('read')

	def create_group_chat(self, users: List['User']) -> 'GroupChat':
		group_chat = GroupChat(id=str(len(self.chats) + 1), users=users, messages=[])
		self.chats.append(group_chat)
		return group_chat

	def view_chat_history(self, chat_id: str) -> List['Message']:
		chat = self.get_chat(chat_id)
		if chat:
			return chat.get_history()

	def get_chat(self, chat_id: str) -> Optional['Chat']:
		for chat in self.chats:
			if chat.id == chat_id:
				return chat
		return None


@dataclass
class Message:
	id: str
	content: str
	sender: User
	status: str

	def set_status(self, status: str):
		self.status = status

	def get_status(self) -> str:
		return self.status

	def encrypt_content(self):
		# Placeholder for encryption logic
		pass

	def decrypt_content(self):
		# Placeholder for decryption logic
		pass


@dataclass
class Chat:
	id: str
	users: List[User]
	messages: List[Message]

	def add_message(self, message: Message):
		self.messages.append(message)

	def get_history(self) -> List[Message]:
		return self.messages

	def get_message_status(self, message_id: str) -> str:
		for message in self.messages:
			if message.id == message_id:
				return message.get_status()
		return 'Message not found'


@dataclass
class GroupChat(Chat):
	def add_user(self, user: User):
		self.users.append(user)

	def remove_user(self, user: User):
		self.users.remove(user)


@dataclass
class ImageMessage(Message):
	image_path: str

	def set_image(self, image_path: str):
		self.image_path = image_path

	def get_image(self) -> str:
		return self.image_path
