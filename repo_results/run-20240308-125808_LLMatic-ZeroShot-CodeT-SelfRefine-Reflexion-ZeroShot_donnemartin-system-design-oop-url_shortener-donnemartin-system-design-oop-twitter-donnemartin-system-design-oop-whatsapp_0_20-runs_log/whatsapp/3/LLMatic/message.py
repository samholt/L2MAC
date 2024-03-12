from datetime import datetime
import base64

class Message:
	def __init__(self, sender, receiver, content, message_type='text'):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.timestamp = datetime.now()
		self.read = False
		self.encrypted = False
		self.message_type = message_type
		self.queue = []

	def send(self):
		if not self.encrypted:
			self.encrypt()
		if self.receiver.is_online:
			# send message
			self.queue.append(self)
		else:
			self.receiver.queue.append(self)

	def send_queued_messages(self):
		for message in self.queue:
			message.send()
		self.queue = []

	def receive(self):
		if self.encrypted:
			self.decrypt()
		self.read = True
		# receive message

	def encrypt(self):
		self.content = base64.b64encode(self.content.encode()).decode()
		self.encrypted = True

	def decrypt(self):
		self.content = base64.b64decode(self.content.encode()).decode()
		self.encrypted = False

	def read_receipt(self):
		return self.read

	def handle_message_type(self):
		if self.message_type == 'text':
			return self.content
		else:
			return 'This is a placeholder for non-text messages.'
