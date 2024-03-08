class Messaging:
	def __init__(self):
		self.messages = {}
		self.receipts = {}
		self.group_chats = {}
		self.online_status = {}

	def send_message(self, sender_email, receiver_email, message):
		if receiver_email not in self.messages:
			self.messages[receiver_email] = []
		self.messages[receiver_email].append({'sender': sender_email, 'message': message, 'status': 'unread'})

	def read_message(self, sender_email, receiver_email, message_id):
		if receiver_email in self.messages and len(self.messages[receiver_email]) > message_id:
			self.messages[receiver_email][message_id]['status'] = 'read'
			self.receipts[sender_email] = {'receiver': receiver_email, 'message_id': message_id, 'status': 'read'}

	def get_messages(self, receiver_email):
		return self.messages.get(receiver_email, [])

	def get_receipts(self, sender_email):
		return self.receipts.get(sender_email, [])

	def create_group_chat(self, user_email, group_name, picture, emails):
		self.group_chats[group_name] = {'creator': user_email, 'picture': picture, 'participants': emails, 'messages': []}

	def update_participants(self, user_email, group_name, emails):
		if group_name in self.group_chats and self.group_chats[group_name]['creator'] == user_email:
			self.group_chats[group_name]['participants'] = emails

	def set_online_status(self, user_email, status):
		self.online_status[user_email] = status

	def get_online_status(self, user_email):
		return self.online_status.get(user_email, 'offline')
