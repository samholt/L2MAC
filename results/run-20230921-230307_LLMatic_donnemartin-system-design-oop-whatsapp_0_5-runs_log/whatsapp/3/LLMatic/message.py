class Message:
	def __init__(self, content, sender, receiver):
		self.content = content
		self.sender = sender
		self.receiver = receiver
		self.read = False

	def send(self):
		# TODO: Implement message sending logic
		pass

	def receive(self):
		# TODO: Implement message receiving logic
		pass

	def handle_text(self, text):
		# Implement text handling logic
		self.content = text

	def handle_image(self, image):
		# Implement image handling logic
		self.content = image

	def handle_emoji(self, emoji):
		# Implement emoji handling logic
		self.content = emoji

	def handle_gif(self, gif):
		# Implement GIF handling logic
		self.content = gif

	def handle_sticker(self, sticker):
		# Implement sticker handling logic
		self.content = sticker
