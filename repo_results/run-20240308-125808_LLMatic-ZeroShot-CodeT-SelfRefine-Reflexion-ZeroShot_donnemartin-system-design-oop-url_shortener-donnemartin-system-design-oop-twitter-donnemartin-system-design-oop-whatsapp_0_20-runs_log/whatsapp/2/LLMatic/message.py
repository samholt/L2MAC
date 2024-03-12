import datetime
import base64

class Message:
	def __init__(self, sender, receiver, content, message_type='text'):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.timestamp = datetime.datetime.now()
		self.read_receipt = False
		self.encrypted = False
		self.message_type = message_type

	def send_message(self):
		return {'sender': self.sender, 'receiver': self.receiver, 'content': self.content, 'timestamp': self.timestamp, 'read_receipt': self.read_receipt, 'encrypted': self.encrypted, 'message_type': self.message_type}

	def receive_message(self, message):
		self.sender = message['sender']
		self.receiver = message['receiver']
		self.content = message['content']
		self.timestamp = message['timestamp']
		self.read_receipt = message['read_receipt']
		self.encrypted = message['encrypted']
		self.message_type = message['message_type']

	def set_read_receipt(self):
		self.read_receipt = True

	def get_read_receipt(self):
		return self.read_receipt

	def encrypt_message(self):
		self.content = base64.b64encode(self.content.encode()).decode()
		self.encrypted = True

	def decrypt_message(self):
		self.content = base64.b64decode(self.content.encode()).decode()
		self.encrypted = False

	def handle_message_type(self, message_type):
		self.message_type = message_type
