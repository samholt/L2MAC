class User:
	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.profile_picture = None
		self.status_message = None
		self.privacy_settings = {'view_profile_picture': 'everyone', 'view_status_message': 'everyone'}
		self.blocked_contacts = set()
		self.online_status = False
		self.queued_messages = []

	def set_profile_picture(self, picture):
		self.profile_picture = picture

	def set_status_message(self, message):
		self.status_message = message

	def manage_privacy_settings(self, setting, value):
		self.privacy_settings[setting] = value

	def block_contact(self, contact):
		self.blocked_contacts.add(contact)

	def unblock_contact(self, contact):
		self.blocked_contacts.remove(contact)

	def set_online_status(self, status):
		self.online_status = status

	def queue_message(self, message):
		self.queued_messages.append(message)

	def receive_message(self, message):
		if message in self.queued_messages:
			self.queued_messages.remove(message)
		return message


class Auth:
	def __init__(self):
		self.users = {}

	def sign_up(self, email, password):
		if email in self.users:
			return 'User already exists'
		else:
			self.users[email] = User(email, password)
			return 'User created successfully'

	def log_in(self, email, password):
		if email in self.users and self.users[email].password == password:
			return 'Logged in successfully'
		else:
			return 'Invalid email or password'

	def recover_password(self, email):
		if email in self.users:
			return self.users[email].password
		else:
			return 'User does not exist'
