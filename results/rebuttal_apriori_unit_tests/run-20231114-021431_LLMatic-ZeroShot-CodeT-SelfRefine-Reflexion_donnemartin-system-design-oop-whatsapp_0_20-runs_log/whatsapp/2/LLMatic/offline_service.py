class OfflineService:
	def __init__(self):
		self.users = {}
		self.message_queue = {}

	def set_online(self, user_id):
		self.users[user_id] = 'online'
		if user_id in self.message_queue:
			for message in self.message_queue[user_id]:
				# In a real-world application, we would send the message now.
				# Here, we'll just remove it from the queue.
				del message
			return True
		return False

	def set_offline(self, user_id):
		self.users[user_id] = 'offline'
		return True

	def send_message(self, sender_id, receiver_id, message):
		if receiver_id in self.users and self.users[receiver_id] == 'offline':
			if receiver_id not in self.message_queue:
				self.message_queue[receiver_id] = []
			self.message_queue[receiver_id].append(message)
			return 'Queued'
		# In a real-world application, we would send the message now if the receiver is online.
		# Here, we'll just return True to indicate that the process was successful.
		return True

	def check_message_sent(self, sender_id, receiver_id):
		# In a real-world application, we would check if the message has been sent.
		# Here, we'll just return True to indicate that the process was successful.
		return True
