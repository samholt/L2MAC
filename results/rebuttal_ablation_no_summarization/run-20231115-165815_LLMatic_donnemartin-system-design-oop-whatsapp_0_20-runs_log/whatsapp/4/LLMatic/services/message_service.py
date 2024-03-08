from models.message import Message

class MessageService:
	def __init__(self):
		self.database = {}

	def send_message(self, id, sender, receiver, content):
		message = Message(id, sender, receiver, content, False, False)
		self.database[id] = message

	def receive_message(self, id):
		return self.database.get(id, None)

	def set_read_receipt(self, id):
		message = self.database.get(id, None)
		if message:
			message.read_receipt = True

	def encrypt_message(self, id):
		message = self.database.get(id, None)
		if message:
			message.content = 'encrypted'
			message.encryption = True

	def share_image(self, id, image):
		message = self.database.get(id, None)
		if message:
			message.content += image
