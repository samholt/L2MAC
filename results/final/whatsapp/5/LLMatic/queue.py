from user import User
from message import Message


class Queue:
	def __init__(self, user: User):
		self.user = user
		self.messages = []

	def enqueue(self, message: Message):
		self.messages.append(message)

	def dequeue(self):
		if self.messages:
			return self.messages.pop(0)

	def send_all(self):
		while self.messages:
			message = self.dequeue()
			message.send()
			print(f'Message sent: {message.content}')
