class OfflineService:
	def __init__(self):
		self.users = {}
		self.messages = {}

	def set_offline(self, user_id):
		self.users[user_id] = 'offline'
		return True

	def send_message(self, sender_id, receiver_id, message):
		if sender_id in self.users and receiver_id in self.users:
			self.messages[(sender_id, receiver_id)] = message
			return 'Sent'
		return 'Failed'

	def set_online(self, user_id):
		self.users[user_id] = 'online'
		return True

	def check_message_sent(self, sender_id, receiver_id):
		return (sender_id, receiver_id) in self.messages
