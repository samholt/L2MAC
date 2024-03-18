import datetime

class Message:
	def __init__(self, sender, recipient, content):
		self.sender = sender
		self.recipient = recipient
		self.content = content
		self.time_sent = datetime.datetime.now()

	def send_message(self):
		self.recipient.messages.append(self)

	def receive_message(self):
		self.sender.messages.append(self)
