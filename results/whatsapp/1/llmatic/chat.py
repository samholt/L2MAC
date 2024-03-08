from dataclasses import dataclass

@dataclass
class Chat:
	def __init__(self):
		self.messages = []
		self.read_receipts = {}
		self.offline_messages = []

	def send_message(self, sender, recipient, message):
		if recipient.is_online:
			self.messages.append((sender, recipient, message))
			self.read_receipts[(sender.email, recipient.email, message.content)] = False
		else:
			self.offline_messages.append((sender, recipient, message))

	def receive_message(self, sender, recipient, message):
		if (sender.email, recipient.email, message.content) in self.read_receipts:
			self.read_receipts[(sender.email, recipient.email, message.content)] = True
			return message
		return None

	def encrypt_message(self, message):
		# Placeholder for encryption logic
		return message

	def share_image(self, sender, recipient, image):
		if recipient.is_online:
			self.messages.append((sender, recipient, image))
			self.read_receipts[(sender.email, recipient.email, image.content)] = False
		else:
			self.offline_messages.append((sender, recipient, image))

	def restore_connectivity(self, user):
		for offline_message in self.offline_messages:
			if offline_message[1] == user:
				self.messages.append(offline_message)
				self.read_receipts[(offline_message[0].email, offline_message[1].email, offline_message[2].content)] = False
				self.offline_messages.remove(offline_message)

