class Chat:
	def __init__(self, users):
		self.users = users
		self.messages = []

	def add_message(self, message):
		self.messages.append(message)
		message.set_status('delivered')

	def get_chat_history(self):
		return [(message.sender, message.content) for message in self.messages]

	def get_message_status(self, message):
		if message in self.messages:
			return message.get_status()
		else:
			return 'Message not found in chat'
