class Message:
	def __init__(self, sender, receiver, content):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.read_receipt = False
		self.encrypted = False

	def send_message(self):
		# Simulate sending message
		print(f'Message sent from {self.sender} to {self.receiver}: {self.content}')

	def receive_message(self):
		# Simulate receiving message
		print(f'Message received from {self.sender} to {self.receiver}: {self.content}')
		self.read_receipt = True

	def encrypt_message(self):
		# Simulate encryption
		self.content = ''.join(reversed(self.content))
		self.encrypted = True

	def decrypt_message(self):
		# Simulate decryption
		if self.encrypted:
			self.content = ''.join(reversed(self.content))
			self.encrypted = False

	def is_read(self):
		return self.read_receipt

	def is_encrypted(self):
		return self.encrypted


class ImageMessage(Message):
	def __init__(self, sender, receiver, content, image):
		super().__init__(sender, receiver, content)
		self.image = image

	def send_message(self):
		# Simulate sending message with image
		print(f'Message with image sent from {self.sender} to {self.receiver}: {self.content}, {self.image}')


class EmojiMessage(Message):
	def __init__(self, sender, receiver, content, emoji):
		super().__init__(sender, receiver, content)
		self.emoji = emoji

	def send_message(self):
		# Simulate sending message with emoji
		print(f'Message with emoji sent from {self.sender} to {self.receiver}: {self.content}, {self.emoji}')
