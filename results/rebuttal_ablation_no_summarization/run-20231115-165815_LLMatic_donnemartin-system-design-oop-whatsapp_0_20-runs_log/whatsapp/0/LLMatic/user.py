class User:
	def __init__(self):
		self.users = {}
		self.status = 'offline'
		self.queue = []

	def register(self, email, password):
		if email in self.users:
			return 'User already exists'
		self.users[email] = {'password': password, 'recovery': None, 'profile_picture': None, 'status_message': None, 'privacy_settings': {'details': 'public', 'last_seen': 'public'}, 'blocked_contacts': [], 'groups': []}
		return 'User registered successfully'

	def recover_password(self, email, recovery):
		if email not in self.users:
			return 'User does not exist'
		self.users[email]['recovery'] = recovery
		return 'Password recovery set'

	def set_profile_picture(self, email, picture):
		if email not in self.users:
			return 'User does not exist'
		self.users[email]['profile_picture'] = picture
		return 'Profile picture set'

	def set_status_message(self, email, message):
		if email not in self.users:
			return 'User does not exist'
		self.users[email]['status_message'] = message
		return 'Status message set'

	def update_privacy_settings(self, email, details, last_seen):
		if email not in self.users:
			return 'User does not exist'
		self.users[email]['privacy_settings']['details'] = details
		self.users[email]['privacy_settings']['last_seen'] = last_seen
		return 'Privacy settings updated'

	def block_contact(self, email, contact):
		if email not in self.users:
			return 'User does not exist'
		if contact in self.users[email]['blocked_contacts']:
			return 'Contact already blocked'
		self.users[email]['blocked_contacts'].append(contact)
		return 'Contact blocked successfully'

	def unblock_contact(self, email, contact):
		if email not in self.users:
			return 'User does not exist'
		if contact not in self.users[email]['blocked_contacts']:
			return 'Contact not blocked'
		self.users[email]['blocked_contacts'].remove(contact)
		return 'Contact unblocked successfully'

	def get_user(self, email):
		return self.users.get(email, None)

	def set_status(self, status):
		self.status = status

	def get_status(self):
		return self.status

	def add_to_queue(self, message):
		self.queue.append(message)

	def send_queued_messages(self):
		if self.status == 'online':
			for message in self.queue:
				message.send_message()
			self.queue = []
