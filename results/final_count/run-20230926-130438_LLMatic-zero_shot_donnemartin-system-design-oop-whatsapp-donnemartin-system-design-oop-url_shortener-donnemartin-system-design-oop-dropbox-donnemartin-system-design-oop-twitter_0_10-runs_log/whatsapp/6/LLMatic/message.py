import hashlib

class Message:
	def __init__(self):
		self.messages = {}
		self.read_receipts = {}
		self.images = {}
		self.offline_messages = {}

	def send_message(self, sender_id, receiver_id, message):
		if receiver_id not in self.messages:
			self.messages[receiver_id] = []
		self.messages[receiver_id].append((sender_id, self.encrypt_message(message)))
		return 'Message sent successfully'

	def receive_message(self, receiver_id):
		if receiver_id in self.messages and self.messages[receiver_id]:
			return self.messages[receiver_id].pop()
		return 'No new messages'

	def send_read_receipt(self, sender_id, receiver_id, message_id):
		if receiver_id not in self.read_receipts:
			self.read_receipts[receiver_id] = []
		self.read_receipts[receiver_id].append((sender_id, message_id))
		return 'Read receipt sent successfully'

	def encrypt_message(self, message):
		return hashlib.sha256(message.encode()).hexdigest()

	def share_image(self, sender_id, receiver_id, image_file):
		if receiver_id not in self.images:
			self.images[receiver_id] = []
		self.images[receiver_id].append((sender_id, image_file))
		return 'Image shared successfully'

	def queue_offline_message(self, sender_id, receiver_id, message):
		if receiver_id not in self.offline_messages:
			self.offline_messages[receiver_id] = []
		self.offline_messages[receiver_id].append((sender_id, message))
		return 'Message queued for offline user'

	def get_offline_messages(self, receiver_id):
		return self.offline_messages.get(receiver_id, [])
