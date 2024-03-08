class OfflineService:
	def __init__(self):
		self.user_status = {}
		self.message_queue = {}

	def set_offline(self, user_id):
		self.user_status[user_id] = 'offline'

	def set_online(self, user_id):
		self.user_status[user_id] = 'online'
		if user_id in self.message_queue:
			self.message_queue.pop(user_id)

	def send_message(self, sender_id, receiver_id, message):
		if self.user_status.get(sender_id) == 'offline':
			if sender_id not in self.message_queue:
				self.message_queue[sender_id] = []
			self.message_queue[sender_id].append((receiver_id, message))
			return 'Queued'
		else:
			return 'Sent'

	def check_message_sent(self, sender_id, receiver_id):
		if sender_id in self.message_queue:
			for msg in self.message_queue[sender_id]:
				if msg[0] == receiver_id:
					return False
		return True
