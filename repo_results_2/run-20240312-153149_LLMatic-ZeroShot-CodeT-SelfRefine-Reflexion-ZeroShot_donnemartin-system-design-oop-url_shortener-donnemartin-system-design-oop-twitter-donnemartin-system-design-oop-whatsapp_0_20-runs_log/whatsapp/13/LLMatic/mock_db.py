class MockDB:
	def __init__(self):
		self.data = {}
		self.online = True
		self.message_queue = []

	def add(self, key, value):
		self.data[key] = value

	def update(self, key, value):
		if key in self.data:
			self.data[key] = value

	def delete(self, key):
		if key in self.data:
			del self.data[key]

	def retrieve(self, key):
		return self.data.get(key, None)

	def set_online(self, online):
		self.online = online
		if self.online:
			for message in self.message_queue:
				self.add(message['message_id'], {'text': message['text']})
			self.message_queue = []

	def queue_message(self, message):
		self.message_queue.append(message)
