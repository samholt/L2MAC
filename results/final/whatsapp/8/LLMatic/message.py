from user import User
import hashlib

# Mock database
messages_db = {}


class Message:
	def __init__(self, sender: User, receiver: User, content: str):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.read_receipt = False
		self.encryption = None
		self.attachments = []
		self.queue = []

	def send(self):
		# Encrypt the message
		self.encrypt()
		# Add the message to the database
		messages_db[hash(self)] = self

	def send_offline(self):
		if not self.sender.online:
			self.queue.append(self)
		else:
			self.send()
			self.queue.remove(self)

	def receive(self):
		# Retrieve the message from the database
		return messages_db.get(hash(self))

	def read(self):
		# Update the read receipt
		self.read_receipt = True

	def encrypt(self):
		# Encrypt the content
		self.encryption = hashlib.sha256(self.content.encode()).hexdigest()

	def attach(self, attachment):
		# Add an attachment
		self.attachments.append(attachment)

	def __hash__(self):
		# Hash function for the message
		return hash((self.sender, self.receiver, self.content))
