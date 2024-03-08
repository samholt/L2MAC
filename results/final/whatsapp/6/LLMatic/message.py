from connectivity import connectivity, restore_connectivity


class Message:
	def __init__(self, sender, receiver, content, read_receipt=False, encryption=False, attachments=None):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.read_receipt = read_receipt
		self.encryption = encryption
		self.attachments = attachments if attachments else []
		self.queue = []

	def send(self, db):
		if connectivity():
			message_id = len(db) + 1
			self.encrypt()
			db[message_id] = self
			return message_id
		else:
			self.queue.append((self.send, [db]))
			restore_connectivity(self.queue, db)

	@staticmethod
	def receive(db, message_id):
		message = db.get(message_id)
		if message:
			message.decrypt()
			return message
		return None

	def encrypt(self):
		if self.encryption:
			self.content = ''.join(chr(ord(c) + 3) for c in self.content)

	def decrypt(self):
		if self.encryption:
			self.content = ''.join(chr(ord(c) - 3) for c in self.content)

	def attach(self, attachment):
		self.attachments.append(attachment)
