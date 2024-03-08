class MockDatabase:
	def __init__(self):
		self.users = {}
		self.messages = {}
		self.groups = {}
		self.statuses = {}
		self.offline_message_queues = {}

	# existing methods...

	def insert_message(self, message_id, sender_id, recipient_id, content, read=False):
		self.messages[message_id] = {'sender_id': sender_id, 'recipient_id': recipient_id, 'content': content, 'read': read}
		if recipient_id not in self.users or not self.users[recipient_id]['online']:
			if recipient_id not in self.offline_message_queues:
				self.offline_message_queues[recipient_id] = []
			self.offline_message_queues[recipient_id].append(message_id)

	def get_offline_messages(self, user_id):
		return self.offline_message_queues.get(user_id, [])

	def clear_offline_messages(self, user_id):
		if user_id in self.offline_message_queues:
			self.offline_message_queues[user_id] = []
