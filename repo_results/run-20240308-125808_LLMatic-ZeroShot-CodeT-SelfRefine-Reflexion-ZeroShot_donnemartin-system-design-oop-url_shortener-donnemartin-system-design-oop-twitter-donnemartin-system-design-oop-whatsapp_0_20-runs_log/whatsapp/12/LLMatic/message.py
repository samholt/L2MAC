class Message:
	def __init__(self, sender, receiver, content, read_status=False, encryption_status=False, image=None):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.read_status = read_status
		self.encryption_status = encryption_status
		self.image = image
		self.emojis_gifs_stickers = []

	def mark_as_read(self):
		self.read_status = True

	def encrypt(self):
		self.encryption_status = True

	def add_image(self, image):
		self.image = image

	def add_emojis_gifs_stickers(self, emojis_gifs_stickers):
		self.emojis_gifs_stickers.append(emojis_gifs_stickers)
