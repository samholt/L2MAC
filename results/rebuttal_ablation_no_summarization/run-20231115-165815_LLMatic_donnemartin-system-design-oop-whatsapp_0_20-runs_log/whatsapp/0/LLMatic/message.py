import datetime
import base64


class Message:
	def __init__(self, sender, receiver, text, read=False, image=None, emoji=None):
		self.sender = sender
		self.receiver = receiver
		self.text = text
		self.read = read
		self.image = image
		self.emoji = emoji
		self.timestamp = datetime.datetime.now()

	def send_message(self):
		if self.receiver.get_status() == 'online':
			self.text = self.encrypt_message(self.text)
			return {'sender': self.sender, 'receiver': self.receiver, 'message': self.text, 'timestamp': self.timestamp}
		else:
			self.receiver.add_to_queue(self)

	def receive_message(self, message):
		self.text = self.decrypt_message(message['message'])
		self.read = True
		return self.text

	def update_read(self):
		self.read = True

	def encrypt_message(self, message):
		message_bytes = message.encode('ascii')
		base64_bytes = base64.b64encode(message_bytes)
		base64_message = base64_bytes.decode('ascii')
		return base64_message

	def decrypt_message(self, message):
		base64_bytes = message.encode('ascii')
		message_bytes = base64.b64decode(base64_bytes)
		message = message_bytes.decode('ascii')
		return message

	def handle_image(self, image):
		self.image = image

	def handle_emoji(self, emoji):
		self.emoji = emoji
