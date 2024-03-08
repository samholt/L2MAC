import hashlib
from user import Auth

auth = Auth()

auth.sign_up('sender@test.com', 'password')
auth.sign_up('receiver@test.com', 'password')

class Message:
	def __init__(self, sender, receiver, content):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.read_receipt = False
		self.encrypted_content = self.encrypt_message()

	def send_message(self):
		if auth.users[self.receiver].online_status:
			if auth.users[self.receiver].queued_messages:
				self.send_queued_messages()
			return {'sender': self.sender, 'receiver': self.receiver, 'message': self.encrypted_content}
		else:
			auth.users[self.receiver].queue_message(self.encrypted_content)
			return {'sender': self.sender, 'receiver': self.receiver, 'message': 'Message queued'}

	def send_queued_messages(self):
		if auth.users[self.receiver].online_status:
			for message in auth.users[self.receiver].queued_messages:
				auth.users[self.receiver].receive_message(message)
			auth.users[self.receiver].queued_messages = []
			return {'sender': self.sender, 'receiver': self.receiver, 'message': 'All queued messages sent'}

	def receive_message(self, message):
		self.content = self.decrypt_message(message)
		self.manage_read_receipts()

	def manage_read_receipts(self):
		self.read_receipt = True

	def encrypt_message(self):
		return hashlib.sha256(self.content.encode()).hexdigest()

	def decrypt_message(self, encrypted_message):
		# This is a simple simulation of decryption. In a real-world application, we would use a proper encryption/decryption algorithm.
		return encrypted_message

	def share_image(self, image):
		self.content = image
		self.encrypted_content = self.encrypt_message()

	def support_emojis_gifs_stickers(self, emoji_gif_sticker):
		self.content = emoji_gif_sticker
		self.encrypted_content = self.encrypt_message()
