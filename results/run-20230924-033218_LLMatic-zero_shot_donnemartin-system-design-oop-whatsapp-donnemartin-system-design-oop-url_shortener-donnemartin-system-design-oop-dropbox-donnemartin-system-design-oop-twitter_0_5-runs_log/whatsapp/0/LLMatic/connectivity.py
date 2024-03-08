from datetime import datetime
from user import User
from message import Message


class Connectivity:
	def __init__(self, user: User):
		self.user = user
		self.online = False
		self.last_seen = datetime.now()
		self.message_queue = []

	def go_online(self):
		self.online = True
		self.update_last_seen()

	def go_offline(self):
		self.online = False
		self.update_last_seen()

	def update_last_seen(self):
		self.last_seen = datetime.now()

	def queue_message(self, message: Message):
		self.message_queue.append(message)

	def send_queued_messages(self):
		if self.online:
			for message in self.message_queue:
				message.send()
			self.message_queue = []
