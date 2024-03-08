from abc import ABC, abstractmethod
import uuid
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from base64 import b64encode, b64decode


class User:
	def __init__(self, username):
		self.username = username
		self.chats = []

	def send_message(self, chat_id, message):
		chat = self._get_chat(chat_id)
		if chat:
			chat.add_message(message)
			message.set_delivered()

	def read_message(self, chat_id):
		chat = self._get_chat(chat_id)
		if chat:
			messages = chat.get_unread_messages(self.username)
			for message in messages:
				message.set_read()
			return messages

	def create_group_chat(self, users):
		group_chat = GroupChat([self.username] + users)
		self.chats.append(group_chat)
		return group_chat

	def _get_chat(self, chat_id):
		for chat in self.chats:
			if chat.id == chat_id:
				return chat
		return None

class Message(ABC):
	def __init__(self, sender, content):
		self.id = uuid.uuid4()
		self.sender = sender
		self.content = content
		self.delivered = False
		self.read = False
		self.key = get_random_bytes(16)

	def encrypt(self):
		cipher = AES.new(self.key, AES.MODE_EAX)
		ciphertext, tag = cipher.encrypt_and_digest(self.content.encode())
		self.content = b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')

	def decrypt(self):
		b64 = b64decode(self.content)
		nonce, tag, ciphertext = b64[:16], b64[16:32], b64[32:]
		cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
		self.content = cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8')

	def set_delivered(self):
		self.delivered = True

	def set_read(self):
		self.read = True

class Chat:
	def __init__(self, users):
		self.id = uuid.uuid4()
		self.users = users
		self.messages = []

	def add_message(self, message):
		self.messages.append(message)

	def get_history(self):
		return self.messages

	def get_unread_messages(self, username):
		return [message for message in self.messages if message.sender != username and not message.read]

class GroupChat(Chat):
	def add_user(self, user):
		self.users.append(user)

	def remove_user(self, user):
		self.users.remove(user)


class ImageMessage(Message):
	def __init__(self, sender, image_content):
		super().__init__(sender, image_content)

	def encrypt(self):
		pass

	def decrypt(self):
		pass

	def set_image_content(self, image_content):
		self.content = image_content

	def get_image_content(self):
		return self.content

