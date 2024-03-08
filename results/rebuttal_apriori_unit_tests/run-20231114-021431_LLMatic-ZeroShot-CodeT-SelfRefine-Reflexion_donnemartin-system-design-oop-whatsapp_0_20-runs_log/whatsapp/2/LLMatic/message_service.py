import random
import string
from cryptography.fernet import Fernet

# Mock database
messages_db = {}


class MessageService:

	def __init__(self):
		self.key = Fernet.generate_key()
		self.cipher_suite = Fernet(self.key)

	def send_message(self, sender_id, receiver_id, message):
		message_id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
		messages_db[message_id] = {'sender_id': sender_id, 'receiver_id': receiver_id, 'message': message, 'read': False}
		return message_id

	def receive_message(self, receiver_id, message_id):
		if messages_db[message_id]['receiver_id'] == receiver_id:
			return messages_db[message_id]['message']
		return None

	def mark_as_read(self, receiver_id, message_id):
		if messages_db[message_id]['receiver_id'] == receiver_id:
			messages_db[message_id]['read'] = True
			return True
		return False

	def encrypt_message(self, sender_id, message):
		return self.cipher_suite.encrypt(message.encode()).decode()

	def decrypt_message(self, receiver_id, encrypted_message):
		return self.cipher_suite.decrypt(encrypted_message.encode()).decode()

	def send_image(self, sender_id, receiver_id, image_path):
		# For simplicity, we treat image as a special message
		return self.send_message(sender_id, receiver_id, f'Image: {image_path}')

	def receive_image(self, receiver_id, message_id):
		message = self.receive_message(receiver_id, message_id)
		if message and message.startswith('Image: '):
			return message[7:]
		return None

	def send_content(self, sender_id, receiver_id, content):
		# For simplicity, we treat emoji, GIF, and sticker as a special message
		return self.send_message(sender_id, receiver_id, content)

	def receive_content(self, receiver_id, message_id):
		return self.receive_message(receiver_id, message_id)
