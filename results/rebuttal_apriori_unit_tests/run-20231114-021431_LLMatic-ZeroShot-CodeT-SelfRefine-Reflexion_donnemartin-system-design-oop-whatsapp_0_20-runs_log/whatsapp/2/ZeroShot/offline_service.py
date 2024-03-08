class OfflineService:
	def __init__(self):
		self.users = {}
		self.messages = {}
		self.message_id_counter = 0

	def set_offline(self, user_id):
		self.users[user_id] = {'online': False}

	def set_online(self, user_id):
		self.users[user_id] = {'online': True}

	def send_message(self, sender_id, receiver_id, message):
		if self.users[sender_id]['online']:
			return 'Sent'
		self.message_id_counter += 1
		self.messages[self.message_id_counter] = {'sender': sender_id, 'receiver': receiver_id, 'content': message, 'sent': False}
		return 'Queued'

	def check_message_sent(self, sender_id, receiver_id):
		for message_id, message in self.messages.items():
			if message['sender'] == sender_id and message['receiver'] == receiver_id:
				return message['sent']
		return False
