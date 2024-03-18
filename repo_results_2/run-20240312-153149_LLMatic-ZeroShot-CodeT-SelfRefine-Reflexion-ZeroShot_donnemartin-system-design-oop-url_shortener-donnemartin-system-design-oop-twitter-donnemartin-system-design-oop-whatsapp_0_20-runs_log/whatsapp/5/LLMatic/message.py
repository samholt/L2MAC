class Message:
	def __init__(self, sender, receiver, content, read_status=False, encryption_status=False):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.read_status = read_status
		self.encryption_status = encryption_status
		self.queue = []

	def send_message(self):
		if self.receiver.is_online:
			return {'sender': self.sender, 'receiver': self.receiver, 'content': self.content}
		else:
			self.queue_message()
			return 'Message queued'

	def receive_message(self, message):
		self.content = message['content']
		self.read_status = True

	def mark_as_read(self):
		self.read_status = True

	def encrypt_message(self):
		if not self.encryption_status:
			self.content = ''.join(chr(ord(c) + 3) if c.isalpha() else c for c in self.content)
			self.encryption_status = True

	def decrypt_message(self):
		if self.encryption_status:
			self.content = ''.join(chr(ord(c) - 3) if c.isalpha() else c for c in self.content)
			self.encryption_status = False

	def share_image(self, image_path):
		with open(image_path, 'rb') as img_file:
			self.content = img_file.read()
			self.encryption_status = False

	def queue_message(self):
		self.queue.append(self.content)
		return 'Message queued'

	def get_queued_messages(self):
		return self.queue
