from user import User
from contact import Contact
from queue import Queue


class Message:
	def __init__(self, sender: User, receiver: User or Contact, content: str):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.is_read = False
		self.is_encrypted = False
		self.attachments = []

	def send(self):
		if self.receiver.is_active:
			self.is_read = False
			print(f'Message sent: {self.content}')
		else:
			queue = Queue(self.receiver)
			queue.enqueue(self)
			print(f'Message queued: {self.content}')

	def read(self):
		self.is_read = True

	def encrypt(self):
		self.is_encrypted = True

	def add_attachment(self, file_path: str):
		self.attachments.append(file_path)
