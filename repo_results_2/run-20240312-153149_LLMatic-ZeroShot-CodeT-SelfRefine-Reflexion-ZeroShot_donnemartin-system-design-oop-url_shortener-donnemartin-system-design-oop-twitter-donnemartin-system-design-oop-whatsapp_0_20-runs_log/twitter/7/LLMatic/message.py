class Message:
	def __init__(self):
		self.messages = {}

	def send_message(self, sender, receiver, message):
		if receiver not in self.messages:
			self.messages[receiver] = []
		self.messages[receiver].append((sender, message))

	def get_messages(self, user):
		return self.messages.get(user, [])
