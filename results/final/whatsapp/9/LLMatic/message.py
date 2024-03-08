class Message:
	def __init__(self, sender, receiver, content='', read_receipt=False, encryption=False, attachments=None):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.read_receipt = read_receipt
		self.encryption = encryption
		self.attachments = attachments if attachments else []
		self.queue = []

	def send_text(self, text):
		if self.receiver.connectivity:
			self.content = text
			# Add to mock database
			mock_db = {}
			mock_db['message'] = self.content
			return 'Text message sent successfully'
		else:
			self.queue.append(text)
			return 'Message queued'

	def send_image(self, image):
		self.attachments.append(image)
		return 'Image sent successfully'

	def send_emoji(self, emoji):
		self.content += emoji
		return 'Emoji sent successfully'

	def send_gif(self, gif):
		self.attachments.append(gif)
		return 'GIF sent successfully'

	def send_sticker(self, sticker):
		self.attachments.append(sticker)
		return 'Sticker sent successfully'

	def send_queued_messages(self):
		if self.receiver.connectivity and self.queue:
			for message in self.queue:
				self.send_text(message)
			self.queue = []
			return 'Queued messages sent successfully'
		return 'No queued messages or receiver is offline'
