class MessageService:
	def __init__(self):
		self.messages = {}
		self.images = {}
		self.contents = {}

	def send_message(self, sender_id, receiver_id, message):
		if receiver_id not in self.messages:
			self.messages[receiver_id] = []
		self.messages[receiver_id].append((sender_id, message, False))
		return True

	def receive_message(self, receiver_id):
		if receiver_id in self.messages and self.messages[receiver_id]:
			return self.messages[receiver_id].pop(0)
		return None

	def mark_as_read(self, receiver_id, message_id):
		if receiver_id in self.messages and self.messages[receiver_id][message_id][2] == False:
			self.messages[receiver_id][message_id] = (self.messages[receiver_id][message_id][0], self.messages[receiver_id][message_id][1], True)
			return True
		return False

	def encrypt_message(self, sender_id, message):
		return ''.join(chr(ord(c) + 3) for c in message)

	def decrypt_message(self, receiver_id, message):
		return ''.join(chr(ord(c) - 3) for c in message)

	def send_image(self, sender_id, receiver_id, image_path):
		if receiver_id not in self.images:
			self.images[receiver_id] = []
		self.images[receiver_id].append((sender_id, image_path))
		return True

	def receive_image(self, receiver_id):
		if receiver_id in self.images and self.images[receiver_id]:
			return self.images[receiver_id].pop(0)
		return None

	def send_content(self, sender_id, receiver_id, content):
		if receiver_id not in self.contents:
			self.contents[receiver_id] = []
		self.contents[receiver_id].append((sender_id, content))
		return True

	def receive_content(self, receiver_id):
		if receiver_id in self.contents and self.contents[receiver_id]:
			return self.contents[receiver_id].pop(0)
		return None
